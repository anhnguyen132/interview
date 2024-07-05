# https://www.geeksforgeeks.org/cycle-sort/#

from typing import List


def cycleSort1toN(nums: List[int]) -> None:
    """
    cycle sort for special case where all elements are of value between 1 and n (all DISTINCT values and array has all values in this range (no missing val))
    => For an elem x, its index in the sorted array = x - 1
    i.e. index for 1 is 0, index for 2 is 1, etc.

    Time: O(n)
    Space: O(1)
    """
    # a = [3, 2, 4, 5, 1]
    n = len(nums)
    i = 0
    """
    Using nums[i] instead of cur_elem will increase #writes, but it will result in dups elem being at the indexes that are not x - 1
    => useful for finding dups problems. (e.g. 442. Find All Duplicates in an Array)
    """
    # cur_elem = nums[i]
    while i < n:
        # correctIndex = cur_elem - 1
        correctIndex = nums[i] - 1
        # not correctIndex != i since it'd stuck in the loop if there are duplicates. Also i is for the start of cycle, wouldnt change in the whole cycle
        # if nums[correctIndex] != cur_elem:
        if nums[correctIndex] != nums[i]:
            # write cur_elem to its correct index
            # but "save" the number currently occupies this index first
            # nums[correctIndex], cur_elem = cur_elem, nums[correctIndex]
            nums[correctIndex], nums[i] = nums[i], nums[correctIndex]
        else:
            i += 1
            # if i < n:
            #     cur_elem = nums[i]


# a = [10,2,5,10,9,1,1,4,3,7]
# cycleSort1toN(a)
# print(a)

# a = [4,3,2,7,8,2,3,1]
# cycleSort1toN(a)
# print(a)

a = [3, 2, 4, 5, 1]
cycleSort1toN(a)
print(a == [1, 2, 3, 4, 5])

a = [5, 4, 3, 2, 1]
cycleSort1toN(a)
print(a == [1, 2, 3, 4, 5])

a = [5, 1, 2, 3, 4]
cycleSort1toN(a)
print(a == [1, 2, 3, 4, 5])

a = [1, 2, 5, 3, 4]
cycleSort1toN(a)
print(a == [1,2,3,4,5])
