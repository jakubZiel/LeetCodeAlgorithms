from collections import deque
from typing import List, Dict

def connected_components(graph : Dict[int, List[int]]) -> int:

    components = 0
    visited = set()
    
    for node in graph.keys():
        if node not in visited:
            components += 1

        queue = deque([node])

        while queue:
            curr = queue.pop()

            if curr in visited:
                continue
            
            visited.add(curr)

            for neighbour in graph[curr]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return components

graph = {
    3 : [],
    4 : [6],
    6 : [4, 5, 7, 8],
    8 : [6],
    7 : [6],
    5 : [6],
    1 : [2],
    2 : [1]
}

print(connected_components(graph))