from collections import defaultdict, deque
from typing import List
from xml.dom import NOT_FOUND_ERR


class Node():
    def __init__(self, val, neighbors = None):
        self.val = val
        self.neighbors : List[Node] = neighbors if neighbors is not None else []

def clone_graph(node : Node) -> Node:
    if node == None:
        return []

    visited = set()
    queue = deque([node])
    n_nodes = {node.val : Node(node.val)}

    n_current : Node = None
    
    while queue:
        current = queue.popleft()

        if current.val in visited:
            continue
        
        n_current = n_nodes[current.val]
        visited.add(current.val)

        for neighbor in current.neighbors:
            if neighbor.val not in visited:
                queue.append(neighbor)
                if neighbor.val not in n_nodes:
                    n_nodes[neighbor.val] = Node(neighbor.val)

            n_current.neighbors.append(n_nodes[neighbor.val])

    return n_nodes[node.val]

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n3]
n2.neighbors = [n1, n4]
n3.neighbors = [n1, n4]
n4.neighbors = [n2, n3]

clone = clone_graph(n1)