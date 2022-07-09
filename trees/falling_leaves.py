from Node import Node
from typing import List, Set


def falling_leaves(root: Node) -> List[List[Node]]:
    
    leaves: Set[Node] = set()

    def get_leaves(node: Node) -> None:
        if node is None:
            return
        left = True
        right = True

        if node.left is None:
            left = False
        else:
            node.left.parent = node
            get_leaves(node.left)

        if node.right is None:
            right = False
        else:
            node.left.parent = node
            get_leaves(node.right)

        if not (left or right):
            leaves.add(node)
    
    get_leaves(root)

    result = []

    while leaves:
        new_leaves: Set[Node] = set()

        for leaf in leaves:
            new_leaves.add(leaf.parent)

        result.append(list(leaves))
        leaves = set()

        for leaf in new_leaves:
            if leaf is not None:
                leaves.add(leaf)

    return result


root = Node(1, 
    Node(2, 
        Node(4, 
            Node(8)),   
        Node(5, 
            Node(9))), 
    Node(3, 
        Node(6, Node(10)), 
        Node(7)))


leaves = falling_leaves(root)
leaves.reverse()

for level in leaves:
    print()
    for leaf in level:
        print(leaf.val, end=" ")

