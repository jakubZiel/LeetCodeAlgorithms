from typing import List
import heapq

def car_pooling(trips : List[List[int]], capacity : int) -> bool:
    stops = []
    TRIPS = len(trips)
    trips.sort(key = lambda trip: trip[1])
    curr_pass = 0

    for i in range(0, TRIPS):
        entering_passangers, trip_start, trip_end = trips[i]
        
        while stops and stops[0][0] <= trip_start:
            destination, left = heapq.heappop(stops)
            curr_pass -= left

        curr_pass += entering_passangers
        heapq.heappush(stops, (trip_end, entering_passangers))

        if curr_pass > capacity:
            return False

    return True

trips = [[2,1,5],[3,3,7],[1,2,3]]
capacity = 5

print(car_pooling(trips, capacity))