# https://en.wikipedia.org/wiki/Quickselect

# Find the smallest k-th elements in an array

from typing import List


def quickSelect(a: List[int], k: int) -> int:
    """
    Similar to quicksort
    Quick select = Select + Partition

    Partition around k-th element.

    Partition function = exactly the same as in Quick sort
    Select function (can be implemented recursively or iteratively w a while loop)
        1) Choose a pivot
        2) After calling Partition on pivot, the array becomes:
            [Unsorted partition <= pivot] — pivot — [Unsorted partition > pivot]
            If pivot == k: done. Else recurse in the appropriate partition

    Time:
        Avg: O(n) bc only recurse in one of the partitions (vs O(nlogn) quicksort) => O(n + n/2 + n/4 +…+ 1) = O(n)
        Worst case: O(n^2)
    Space: O(logn) recursive, O(1) iterative
    """
    n = len(a)
    if n == 1:
        return a[0]

    # return quickSelectRecursive(a, k, 0, n - 1)

    return quickSelectIterative(a, k, 0, n - 1)


def quickSelectIterative(a: List[int], k: int, left: int, right: int) -> int:
    while left <= right:
        pivotIndex = left
        split = partition(a, left, right, pivotIndex)
        if k - 1 == split:
            return a[split]

        if k - 1 < split:
            right = split - 1
        else:
            left = split + 1


def quickSelectRecursive(a: List[int], k: int, left: int, right: int) -> int:
    pivotIndex = left
    split = partition(a, left, right, pivotIndex)

    if k - 1 == split:
        return a[split]

    if k - 1 < split:
        return quickSelectRecursive(a, k, left, split - 1)
    else:
        return quickSelectRecursive(a, k, split + 1, right)


def swap(a: List[int], l: int, r: int) -> None:
    if l < r:
        a[l], a[r] = a[r], a[l]


def partition(a: List, left: int, right: int, pivotIndex: int) -> int:
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


print(quickSelect([10, 4, 5, 8, 6, 11, 26], 3) == 6)
print(quickSelect([7, 10, 4, 3, 20, 15], 3) == 7)
print(quickSelect([7, 10, 4, 3, 20, 15], 4) == 10)
print(quickSelect([3, 1, 4, 2, 5], 2) == 2)
print(quickSelect([12, 32, 14, 56, 23, 5, 8, 29, 10], 1) == 5)

# negative nums
print(quickSelect([50, 0, -12, 30, 20, 10, -100, 40], 3) == 0)
print(quickSelect([50, 0, -12, 30, 20, 10, -100, 40], 8) == 50)

# edge cases
print(quickSelect([1], 1) == 1)
print(quickSelect([4, 4, 4, 4], 2) == 4)
print(quickSelect([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 1) == 1)
print(quickSelect([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 10)

# performance tests
print(quickSelect([i for i in range(10000)], 500) == 499)
print(quickSelect([10000 - i for i in range(10000)], 500) == 500)
print(quickSelect([i for i in range(100000)], 5000) == 4999)
print(quickSelect([100000 - i for i in range(1000000)], 5000) == 5000)
