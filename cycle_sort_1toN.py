# https://www.geeksforgeeks.org/cycle-sort/#

from typing import List


def cycleSort1toN(nums: List[int]) -> None:
    """
    cycle sort for special case where all elements are of value between 1 and n (all distinct values)
    """
    n = len(nums)
    # writes = 0

    def findPos(cycle_start: int, elem: int) -> int:
        pos = elem - 1

        if pos == cycle_start:
            return pos

        while nums[pos] == elem:
            pos += 1

        return pos

    for cycle_start in range(n - 1):
        # find the intended position for nums[cycle_start] in sorted nums
        pos = findPos(cycle_start, nums[cycle_start])

        # if item is already at its intended position, skip the cycle
        if pos == cycle_start:
            continue

        # update the current elem to find its intended position in sorted nums
        cur_elem = nums[pos]
        nums[pos] = nums[cycle_start]
        # writes += 1

        # repeat the cycle until we find the elem in nums where its intended position is cycle_start
        while pos != cycle_start:
            pos = findPos(cycle_start, cur_elem)
            # print(nums, cycle_start, pos)

            # put cur_elem to its intended position & update the current elem
            nums[pos], cur_elem = cur_elem, nums[pos]
            # writes += 1

        # return writes


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
