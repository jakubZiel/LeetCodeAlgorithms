import heapq
from typing import List


def min_cost_spanning_tree(points : List[List[int]]) -> int:
    connected = set()
    frontier = [(0, 0)]
    span_cost = 0

    while frontier:
        cost, node = heapq.heappop(frontier)

        if node in connected:
            continue

        span_cost += cost
        connected.add(node)

        for i in range(len(points)):
            if i not in connected:
                distance = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])    
                heapq.heappush(frontier, (distance, i))
            
    return span_cost

points = [
    [0,0], [2,2], [3,10], [5,2], [7,0]
]
print(min_cost_spanning_tree(points))