from collections import defaultdict
import heapq
import math
from typing import List

# def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
#     edges = defaultdict(list)
#     for u,v,w in times:
#         edges[u].append((v,w))
#         
#     minHeap = [(0, k)]
#     visit = set()
#     t = 0
#     
#     while minHeap:
#         w1, n1 = heapq.heappop(minHeap)
#         if n1 in visit:
#             continue
#         visit.add(n1)
#         t = max(t, w1)
#         
#         for n2, w2 in edges[n1]:
#             if n2 not in visit:
#                 heapq.heappush(minHeap, (w1 + w2, n2))
#                 
#     return t if len(visit) == n else -1

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    edges = defaultdict(list)

    for u,v,w in times:
        edges[u].append((v,w))

    queue = [(0, k)]
    visited = set()
    delays = [math.inf] * n
    delays[k - 1] = 0

    while queue:
        node_delay, node = heapq.heappop(queue)
        visited.add(node)

        for neighbour, delay in edges[node]:
            n_delay = node_delay + delay 

            if n_delay < delays[neighbour - 1]:
                heapq.heappush(queue, (n_delay, neighbour))
                delays[neighbour - 1] = n_delay        

    return -1 if len(visited) != n else max(delays)

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

print(networkDelayTime(times, n, k))

