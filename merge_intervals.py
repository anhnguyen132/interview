# https://leetcode.com/problems/merge-intervals/description/

from typing import List


def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    sort the intervals by the start time
    then iterate thru the sorted array

    Time O(n + nlogn) = O(nlogn)
    Space O(n)
    """
    intervals.sort(key=lambda x: x[0])
    result = []
    for interval in intervals:
        start, end = interval
        if not result or start > result[0][1]:
            result.append(interval)
        else:
            prev_start, prev_end = result[-1]
            merged_interval = [min(prev_start, start), max(prev_end, end)]
            result[-1] = merged_interval

    return result


print(
    mergeIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
)
print(mergeIntervals([[1, 4], [4, 5]]) == [[1, 5]])

print(mergeIntervals([[0, 4], [4, 8], [6, 10]]) == [[0, 10]])
print(mergeIntervals([[0, 4]]) == [[0, 4]])
