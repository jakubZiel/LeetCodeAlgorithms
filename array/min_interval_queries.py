from typing import List

def min_interval_queries(intervals : List[List[int]], queries : List[int]) -> List[int]:
    
    intervals.sort(key=lambda interval: interval[0])
    queries.sort()



    return intervals, queries



intervals = [[1,4],[2,4],[3,6],[4,4]]
queries = [2,3,4,5]

print(min_interval_queries(intervals, queries))