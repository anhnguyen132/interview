# https://en.wikipedia.org/wiki/Cycle_sort

from typing import List


def cycleSort(nums: List[int]) -> int:
    """
    Performs cycle sort on an array
    Return: the number of writes to that array that were needed to sort it

    Given an element x, we can find the index at which it will occur in the sorted list by simply counting the number of elements in the entire list that are smaller than x. Now
        1. If the element is already at the correct position, do nothing.
        2. If it is not, we will write it to its intended position. That position is inhabited by a different element y, which we then have to move to its correct position. This process of displacing elements to their correct positions continues until an element is moved to the original position of x. This completes a cycle.
    Note:
        1. When computing the correct positions, we have to make sure not to double-count the first element of the cycle.
        2. If there are duplicate elements present, when we try to move an element x to its correct position, that position might already be inhabited by an x. Simply swapping these would cause the algorithm to cycle indefinitely. Instead, we have to insert the element after any of its duplicates.

    Time: O(n^2)
    Space: O(n^2)
    """
    n = len(nums)

    def findPos(cycle_start: int, elem: int):
        """
        find the intended position for nums[cycle_start] in sorted nums
        Assume all elems to the left of cycle_start have the correct sorted numbers
        """
        # Find the index to put elem
        pos = cycle_start
        # not nums[pos] <= elem bc want to make sure all elems with same value will result in the sam pos value
        for i in range(cycle_start + 1, n):
            if nums[i] < elem:
                pos += 1

        # if item is already at its intended position, skip the cycle
        # do this before checking duplicates bc want to make sure all elems with same value will result in the sam pos value
        if pos == cycle_start:
            return cycle_start

        # bypass all duplicates that are currently at pos
        while nums[pos] == elem:
            pos += 1

        return pos

    writes = 0
    # dont need to consider the last elem since the array would have been sorted
    for cycle_start in range(0, n - 1):
        # find the intended position for nums[cycle_start] in sorted nums
        pos = findPos(cycle_start, nums[cycle_start])

        # if item is already at its intended position, skip the cycle
        if pos == cycle_start:
            continue

        # update the current elem to find its intended position in sorted nums
        cur_elem = nums[pos]
        nums[pos] = nums[cycle_start]
        writes += 1

        # repeat the cycle until we find the elem in nums where its intended position is cycle_start
        while pos != cycle_start:
            pos = findPos(cycle_start, cur_elem)

            # put cur_elem to its intended position & update the current elem
            nums[pos], cur_elem = cur_elem, nums[pos]
            writes += 1

    return writes


# a = [1, 2, 2, 2, 1, 2, 1]
# print(cycleSort(a))
# print(a)

a = [3, 2, 4, 5, 1]
print(cycleSort(a) == 4)
print(a == [1, 2, 3, 4, 5])

a = [1, 8, 3, 9, 10, 10, 2, 4]
print(cycleSort(a) == 6)
print(a == [1, 2, 3, 4, 8, 9, 10, 10])

a = [1, 1, 1, 2, 2, 2, 2]
print(cycleSort(a) == 0)
print(a == [1, 1, 1, 2, 2, 2, 2])

a = [1, 2, 2, 2, 1, 2, 1]
print(cycleSort(a) == 4)
print(a == [1, 1, 1, 2, 2, 2, 2])

a = [1, 2, -10, 2, 2, 1, 2, 1, -10, -2]
print(cycleSort(a) == 8)
print(a == [-10, -10, -2, 1, 1, 1, 2, 2, 2, 2])

a = []
print(cycleSort(a) == 0)
print(a == [])

a = [100]
print(cycleSort(a) == 0)
print(a == [100])

a = [100, 100]
print(cycleSort(a) == 0)
print(a == [100, 100])

a = [100, -100]
print(cycleSort(a) == 2)
print(a == [-100, 100])

a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(cycleSort(a) == 10)
print(a == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
