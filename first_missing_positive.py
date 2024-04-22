# https://leetcode.com/problems/first-missing-positive/description/
from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    """
    index as hash key (i.e. Array as a hash map with hash key = index)
    Iterate thru the list, marking any number <= 0 as 1, keeping a bool has_one to indicate if the array contains 1
    If not has_one, return 1
    else iterate thru the array again, if an elem 0 < x < n, mark nums[x] = -1. if x == n, mark nums[0] = -1
    Iterate thru the array again. Using the array as a hashmap with index as key, value < 0 at index i is < 0 if there is value in in array. Iterate from i = 2 to n-1, if nums[i] > 0, return i. If nums[0] > 0, return n

    Time Iterate thru the  array 3 times => O(3n) = O(n)
    Space O(1)
    """
    n = len(nums)
    has_one = False
    for i, x in enumerate(nums):
        if x <= 0:
            nums[i] = 1
        if x == 1:
            has_one = True

    if not has_one:
        return 1

    for i, x in enumerate(nums):
        # must do abs(x) since x could've been changed to negative by previous elems
        x = abs(x)
        if x > 0 and x < n:
            # do abs not using an idicator  like a negative num (e.g. nums[x] = -1) bc if we did so, we'd lose the information about value at nums[x]
            # would fail this case [4, 5, -1, 1, 2]
            # will return 2 instead of 3
            nums[x] = -abs(nums[x])
        if x == n:
            nums[0] = -1

    for i in range(2, n):
        if nums[i] > 0:
            return i

    if nums[0] > 0:
        return n

    return n + 1

    """
    index as hash key (i.e. Array as a hash map with hash key = index)
    Iterate thru the list, marking any number <= 0 as 1, keeping a bool has_one to indicate if the array contains 1
    If not has_one, return 1
    else iterate thru the array again, if an elem 0 < x < n, mark nums[x] = -1. if x == n, mark nums[0] = -1
    Iterate thru the array again. Using the array as a hashmap with index as key, value < 0 at index i is < 0 if there is value in in array. Iterate from i = 2 to n-1, if nums[i] > 0, return i. If nums[0] > 0, return n

    Time Iterate thru the  array 3 times => O(n)
    Space O(1)
    """


print(firstMissingPositive([1, 2, 0]) == 3)
print(firstMissingPositive([4, 5, -1, 1, 2]) == 3)
print(firstMissingPositive([3, 4, -1, 1]) == 2)
print(firstMissingPositive([3, 4, -1, 1, 3, 4]) == 2)
print(firstMissingPositive([3, 4, -1, 1, -1, -2, -2]) == 2)
print(firstMissingPositive([7, 8, 9, 11, 12]) == 1)
print(firstMissingPositive([1]) == 2)
