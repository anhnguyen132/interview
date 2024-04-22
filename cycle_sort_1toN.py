# https://www.geeksforgeeks.org/cycle-sort/#

from typing import List


def cycleSort1toN(nums: List[int]) -> None:
    """
    cycle sort for special case where all elements are of value between 1 and n (all distinct values)
    => For an elem x, its index in the sorted array = x - 1
    i.e. index for 1 is 0, index for 2 is 1, etc.
    """
    n = len(nums)
    i = 0
    while i < n:
        cur_elem = nums[i]
        correctIndex = nums[i] - 1
        if correctIndex != i:
            nums[i] = nums[correctIndex]
            nums[correctIndex] = cur_elem
        else:
            i += 1

    # n = len(nums)
    # # writes = 0

    # for cycle_start in range(n - 1):
    #     # find the intended position for nums[cycle_start] in sorted nums
    #     pos = nums[cycle_start] - 1

    #     # if item is already at its intended position, skip the cycle
    #     if pos == cycle_start:
    #         continue

    #     # update the current elem to find its intended position in sorted nums
    #     cur_elem = nums[pos]
    #     nums[pos] = nums[cycle_start]
    #     # writes += 1

    #     # repeat the cycle until we find the elem in nums where its intended position is cycle_start
    #     while pos != cycle_start:
    #         pos = cur_elem - 1

    #         # put cur_elem to its intended position & update the current elem
    #         nums[pos], cur_elem = cur_elem, nums[pos]
    #         # writes += 1

    #     # return writes


a = [3, 2, 4, 5, 1]
cycleSort1toN(a)
print(a == [1, 2, 3, 4, 5])

a = [5, 4, 3, 2, 1]
cycleSort1toN(a)
print(a == [1, 2, 3, 4, 5])

a = [5, 1, 2, 3, 4]
cycleSort1toN(a)
print(a == [1, 2, 3, 4, 5])

# a = [1, 2, 1, 3, 4]
# cycleSort1toN(a)
# print(a == [1, 1, 2, 3, 4])
