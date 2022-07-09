from typing import List


def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    def merge_intervals(curr_index: int, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        beg = curr_index
        end = curr_index

        while curr_index < len(intervals):    
            curr_interval = intervals[curr_index]
            
            if new_interval[1] < curr_interval[0] or new_interval[0] > curr_interval[1]:
                break
            new_interval = [min(new_interval[0], curr_interval[0]), max(new_interval[1], curr_interval[1])]

            end = curr_index

            curr_index += 1

        return intervals[0:beg] + [new_interval] + intervals[end+1:len(intervals)]
    
    if not intervals:
        return new_interval

    for index in range(len(intervals)):
        curr_interval = intervals[index]

        if new_interval[1] < curr_interval[0]:
            if index == 0:
                intervals.insert(0, new_interval)
            else:
                intervals.insert(index, new_interval)
            return intervals

        elif new_interval[0] > curr_interval[1]:
            if index == len(intervals) - 1:
                intervals.append(new_interval)
                return intervals
        else:
            return merge_intervals(index, intervals, new_interval)
            


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_interval = [4,8]

# intervals = [[0,1],[4,5],[8,9],[12,13],[16,20]]
# new_interval = [9, 14]


print("new interval : " + str(new_interval))
print("interals : " + str(intervals))
print("merged   : " + str(insert_interval(intervals, new_interval)))