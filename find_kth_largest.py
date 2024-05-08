# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List, Tuple


def findKthLargest(nums: List[int], k: int) -> int:
    """
    Use quick select

    Time:
        Avg: O(n)
        Worst: O(n^2)
    Space: O(1)

    """
    n = len(nums)
    if n == 1:
        return nums[0]

    return quickSelectIterative(nums, k, 0, n - 1)


def quickSelectIterative(a: List[int], k: int, left: int, right: int) -> int:
    n = len(a)
    while left <= right:
        split1, split2 = partition3Ways(a, left, right, left)
        if n - k in range(split1, split2):
            return a[split1]

        if n - k < split1:
            right = split1 - 1
        elif n - k >= split2:
            left = split2
        # split = partition(a, left, right, left)
        # if n - k == split:
        #     return a[split]

        # if n - k < split:
        #     right = split - 1
        # else:
        #     left = split + 1


def swap(a: List[int], l: int, r: int) -> None:
    if l < r:
        a[l], a[r] = a[r], a[l]


def partition3Ways(
    a: List[int], left: int, right: int, pivotIndex: int
) -> Tuple[int, int]:
    """
    After partitioning, a is divided into 3 parts:
    a[start: l] < pivot
    a[l: cur] = pivot
    a[cur : end] > pivot
    where start, end = l, r originally
    i.e. anything to the left of l < pivot, anything to the right of cur > pivot

    Returns l and cur
    """
    pivot = a[pivotIndex]
    cur = left
    l, r = left, right

    while cur <= r:
        if a[cur] == pivot:
            cur += 1
        elif a[cur] < pivot:
            swap(a, l, cur)
            l += 1
            cur += 1
        else:
            swap(a, cur, r)
            r -= 1

    return (l, cur)


def partition(a: List[int], left: int, right: int, pivotIndex: int) -> int:
    # Returns the index of a[pivotIndex] in the sorted array
    pivot = a[pivotIndex]

    # swap pivot w the last elem
    swap(a, pivotIndex, right)

    l, r = left, right - 1
    while l <= r:
        while l <= r and a[l] <= pivot:
            l += 1
        while l <= r and a[r] > pivot:
            r -= 1

        if l < r:
            swap(a, l, r)

    # swap pivot back
    swap(a, l, right)

    return l


# print(findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
"""
k = 2
0 1 2 3 4 5
2 1 3 6 4 5
1 2 3 4 5 6
"""
print(findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2) == 5)
print(findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4)

print(findKthLargest([10, 4, 5, 8, 6, 11, 26], 3) == 10)
print(findKthLargest([7, 10, 4, 3, 20, 15], 3) == 10)
print(findKthLargest([7, 10, 4, 3, 20, 15], 4) == 7)
print(findKthLargest([3, 1, 4, 2, 5], 2) == 4)
print(findKthLargest([12, 32, 14, 56, 23, 5, 8, 29, 10], 1) == 56)

# negative nums
print(findKthLargest([50, 0, -12, 30, 20, 10, -100, 40], 3) == 30)
print(findKthLargest([50, 0, -12, 30, 20, 10, -100, 40], 8) == -100)

# edge cases
print(findKthLargest([1], 1) == 1)
print(findKthLargest([4, 4, 4, 4], 2) == 4)
print(findKthLargest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 1) == 10)
print(findKthLargest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 1)

# performance tests
print(findKthLargest([i for i in range(10000)], 500) == 9500)
print(findKthLargest([10000 - i for i in range(10000)], 500) == 9501)
print(findKthLargest([i for i in range(100000)], 5000) == 95000)
print(findKthLargest([100000 - i for i in range(100000)], 5000) == 95001)
