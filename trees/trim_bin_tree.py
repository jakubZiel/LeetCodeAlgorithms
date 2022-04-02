from Node import Node

def trim_bin_tree(root : Node, low : int, high : int) -> Node:
    if root == None:
        return None
    
    if root.val < low:
        return trim_bin_tree(root.right, low, high)
    elif root.val > high:
        return trim_bin_tree(root.left, low, high)
    else:
        if root.val < low:
            root.left = None
        else:
            root.left = trim_bin_tree(root.left, low, high)

        if root.val > high:
            root.right = None
        else :
            root.right = trim_bin_tree(root.right, low, high)
        return root

root = Node(3, Node(0, None, Node(2, Node(1), None)), Node(4))
trim_bin_tree(root, 1, 3)
