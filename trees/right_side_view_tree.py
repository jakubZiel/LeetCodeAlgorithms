from collections import deque
from typing import List
from Node import Node

def right_side_view(root : Node) -> List[int]:
    side_view = []
    queue = deque([root])

    while queue:        
        level_len = len(queue)
        level_right_side = None

        for i in range(level_len):
            node = queue.popleft()
            if node:
                level_right_side = node
                queue.append(node.left)
                queue.append(node.right)
        if level_right_side:
            side_view.append(level_right_side.val)
    return  side_view

root = Node(1, Node(2, None, Node(5)), Node(3, None, Node(4)))

print(right_side_view(root))