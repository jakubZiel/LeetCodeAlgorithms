class Node():
    def __init__(self, val : int, left = None, right = None, parent = None) -> None:
        self.left : Node = left
        self.right : Node = right
        self.parent : Node = parent
        self.val = val