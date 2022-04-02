from collections import defaultdict
from typing import List

def graph_valid_tree(edges : List[List[int]], n : int) -> bool:

    adjacency_matrix = defaultdict(set)
    
    for edge in edges:
        adjacency_matrix[edge[0]].add(edge[1])
        adjacency_matrix[edge[1]].add(edge[0])

    visited = set()
    stack = [(0, None)]

    while stack:
        curr, prev = stack.pop()

        if visited.__contains__(curr):
            return False

        visited.add(curr)
        
        for neighbour_i in adjacency_matrix[curr]: 
            if neighbour_i != prev:
                stack.append((neighbour_i, curr))
        
    return len(visited) == n


edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
n = 5

print(graph_valid_tree(edges, n))