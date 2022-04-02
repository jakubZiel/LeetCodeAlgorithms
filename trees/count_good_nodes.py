import math
from Node import Node

def count_good_nodes(root : Node) -> int:
    
    def good_nodes(root : Node, max_val : int) -> int:
        if not root:
            return  0
        good = 1 if root.val >= max_val else 0     
        max_in_path = max(max_val,  root.val)

        return good + good_nodes(root.left, max_in_path) + good_nodes(root.right, max_in_path)
    
    return good_nodes(root, -math.inf)

root = Node(3, Node(1, Node(3), None), Node(4, Node(1), Node(5)))

print(count_good_nodes(root))