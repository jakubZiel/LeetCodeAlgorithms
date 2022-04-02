class Node():
    def __init__(self, val : int, left = None, right = None) -> None:
        self.left : Node = left
        self.right : Node = right
        self.val = val