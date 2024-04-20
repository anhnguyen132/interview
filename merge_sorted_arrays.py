# https://leetcode.com/problems/merge-sorted-array/description/

from typing import List


def mergeSortedArrays(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    merge backwards. Going from right to left in nums1. Sort the arrays desc
    """
    # start from the end of 2 arrays
    cur1, cur2 = m - 1, n - 1

    # iterate thru nums1 backward
    for i in range(m + n - 1, -1, -1):
        # print(i, cur1, cur2, nums1)
        if cur1 >= 0 and cur2 >= 0:
            if nums1[cur1] <= nums2[cur2]:
                nums1[i] = nums2[cur2]
                cur2 -= 1
            else:
                nums1[i] = nums1[cur1]
                cur1 -= 1
        elif cur1 < 0:
            nums1[: i + 1] = nums2[: cur2 + 1]
            return


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
mergeSortedArrays(nums1, 3, nums2, 3)
print(nums1 == [1, 2, 2, 3, 5, 6])

nums1 = [1]
nums2 = []
mergeSortedArrays(nums1, 1, nums2, 0)
print(nums1 == [1])

nums1 = [0]
nums2 = [1]
mergeSortedArrays(nums1, 0, nums2, 1)
print(nums1 == [1])

nums1 = [1, 2, 4, 0, 0, 0, 0, 0]
nums2 = [3, 7, 8, 10, 12]
mergeSortedArrays(nums1, 3, nums2, 5)
print(nums1 == [1, 2, 3, 4, 7, 8, 10, 12])

nums1 = [0, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0]
nums2 = [0, 0, 3, 7, 8, 10, 12]
mergeSortedArrays(nums1, 4, nums2, 7)
print(nums1 == [0, 0, 0, 1, 2, 3, 4, 7, 8, 10, 12])

nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nums2 = [1, 1, 4, 4, 8, 8, 10, 12]
mergeSortedArrays(nums1, 2, nums2, 8)
print(nums1 == [0, 0, 1, 1, 4, 4, 8, 8, 10, 12])
