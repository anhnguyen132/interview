# https://leetcode.com/problems/subsets/description

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """
    Backtracking
    Restrict length of subset.
    e.g. find all subsets of length =0, then 1, then 2, etc.

    Time: O(n * 2^n) since there are 2^n subsets (think N-bit bitmask), each subset takes O(n) time to generate and copy to result list
    Space: O(n)
    """
    result = []
    for i in range(len(nums) + 1):
        generateAllSubsets(0, nums, i, result, [])
    return result


def generateAllSubsets(
    start: int, nums: List[int], k: int, result: List[List[int]], curSubset: List[int]
) -> None:
    """
    k = len we want this subset to be
    """
    if len(curSubset) == k:
        result.append(curSubset[:])
        return

    for i in range(start, len(nums)):
        curSubset.append(nums[i])
        generateAllSubsets(i + 1, nums, k, result, curSubset)
        curSubset.pop()


# print(subsets([1, 2, 3]))
print(subsets([1, 2, 3]) == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
print(subsets([0]) == [[], [0]])
print(subsets([0, 4, 2]) == [[], [0], [4], [2], [0, 4], [0, 2], [4, 2], [0, 4, 2]])
print(subsets([0, -4, 2]) == [[], [0], [-4], [2], [0, -4], [0, 2], [-4, 2], [0, -4, 2]])
print(subsets([0, 2]) == [[], [0], [2], [0, 2]])
