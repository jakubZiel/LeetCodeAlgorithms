from typing import Optional
from Node import Node

def convertBST(root: Optional[Node]) -> Optional[Node]:
    def preprocess(root: Optional[Node]) -> int:
        if root == None:
            return 0

        root.left.parent = root
        root.right.parent = root

        root.left_sum = preprocess(root.left)
        root.right_sum = preprocess(root.right)

        return root.left_sum + root.right_sum + root.val

    def convert(root: Optional[Node]) -> None:
        if root == None:
            return
        
        root.greater_val = root.val + root.right_sum
        
        curr = root
        while curr.parent is not None and curr == curr.parent.left:
            curr = curr.parent

        if curr.parent is not None:
            root.greater_val += curr.parent.val + curr.parent.right.right_sum

        convert(root.left)
        convert(root.right)
        
    def finalize(root: Optional[Node]) -> None:
        if root == None:
            return
        
        root.val = root.greater_val
        finalize(root.left)
        finalize(root.right)
    
    preprocess(root)
    convert(root)
    finalize(root)
    return root


root = Node(4, 
    Node(1, 
        Node(0), 
        Node(2, 
            None, 
            Node(3))
    ), 
    Node(6, 
        Node(5), 
        Node(7, 
            None, 
            Node(8)
        )
    )
)

convertBST(root)