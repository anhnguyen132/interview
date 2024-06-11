# https://leetcode.com/problems/insert-interval/description/

from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    iterate thru intervals, check if newInterval overlaps. If yes, merge.
    Add this interval to the result list

    Time O(n), Space O(1) not counting space to store the output
    """
    result = []
    new_start, new_end = newInterval
    merging = False

    for i, interval in enumerate(intervals):
        start, end = interval
        if merging:  # in the process of merging newInterval
            prev_start, prev_end = result[-1]
            if prev_end < start:
                result.append(interval)
                merging = False
            else:
                merged = [min(start, prev_start), max(end, prev_end)]
                result[-1] = merged
        elif new_start != None and new_end != None:  # havent merged new interval
            if end < new_start:  # no overlap
                result.append(interval)
                merging = False
            # new interval has no overlap with any of the current intervals
            elif new_end < start:
                result.append(newInterval)
                new_start = new_end = None  # newInterval has been added to result
                result.extend(intervals[i:])
                break
            else:
                merged = [min(start, new_start), max(end, new_end)]
                if not merging:
                    result.append(merged)
                    merging = True
                else:
                    result[-1] = merged
                new_start = new_end = None
        else:  # merging of newInterval is complete
            result.append(interval)

    if new_start != None and new_end != None:
        result.append(newInterval)

    return result


print(insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]) == [[1, 5], [6, 9]])

print(
    insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8])
    == [[1, 2], [3, 10], [12, 16]]
)
print(insert(intervals=[], newInterval=[4, 8]) == [[4, 8]])
print(
    insert(intervals=[[1, 2], [3, 3], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8])
    == [[1, 2], [3, 3], [4, 10], [12, 16]]
)
print(insert(intervals=[[0, 1]], newInterval=[1, 4]) == [[0, 4]])
print(insert(intervals=[[0, 1], [2, 6]], newInterval=[1, 4]) == [[0, 6]])
print(insert(intervals=[[1, 5]], newInterval=[6, 8]) == [[1, 5], [6, 8]])
print(insert(intervals=[[1, 5]], newInterval=[0, 3]) == [[0, 5]])
print(insert(intervals=[[1, 5]], newInterval=[0, 0]) == [[0, 0], [1, 5]])
print(
    insert(intervals=[[4, 5], [6, 8]], newInterval=[1, 3]) == [[1, 3], [4, 5], [6, 8]]
)
print(
    insert(intervals=[[1, 3], [6, 8]], newInterval=[4, 5]) == [[1, 3], [4, 5], [6, 8]]
)
