"""
In 3 Way QuickSort, an array arr[l..r] is divided in 3 parts:
a) arr[l..i] elements less than pivot.
b) arr[i+1..j-1] elements equal to pivot.
c) arr[j..r] elements greater than pivot.

https://www.geeksforgeeks.org/3-way-quicksort-dutch-national-flag/

Implementing the 2nd approach here (a more generlization of Dutch National Flag Algo)
"""

from typing import List


def swap(a: List, l: int, r: int) -> None:
    a[l], a[r] = a[r], a[l]


def helper(a: List, l: int, r: int):
    """
    Use 3 pointers: l, cur, r

    Choose a pivot, pivot = a[l]
    After partitioning, a is divided into 3 parts:
    a[start: l] < pivot
    a[l: cur] = pivot
    a[cur : end] > pivot
    where start, end = l, r originally
    i.e. anything to the left of l < pivot, anything to the right of cur > pivot
    """
    if l >= r:
        return

    # save the start, end index
    start, end = l, r
    # print(l, r, a)
    pivot = a[l]
    cur = l

    while cur <= r:
        if a[cur] < pivot:
            swap(a, l, cur)
            l += 1
            cur += 1
            """
            Note: cur only moves right when the current elem <= pivot
            The only time cur will be ahead of l is when it encounters an elem = pivot
             => The section [l:cur] is guaranteed to be elems = pivot
            => Here, we can increment cur without having to examine a[cur] again after the swap since anything cur has iterated thru (i.e. index < cur) is guaranteed to be <= pivot
            """
        elif a[cur] == pivot:
            cur += 1
        else:
            swap(a, cur, r)
            r -= 1

    helper(a, start, l - 1)
    helper(a, cur, end)


def threeWayQuicksort(a: List) -> None:
    """
    In 3 Way QuickSort, an array arr[l..r] is divided in 3 parts:
    a) arr[l..i] elements less than pivot. (inclusive)
    b) arr[i+1..j-1] elements equal to pivot. (inclusive)
    c) arr[j..r] elements greater than pivot. (inclusive)
    """
    helper(a, 0, len(a) - 1)


a = [1, 4, 0, 3, 5, 2]
threeWayQuicksort(a)
print(a == [0, 1, 2, 3, 4, 5])

a = [6, 1, 4, 9, 0, 3, 5, 2, 7, 8]
threeWayQuicksort(a)
print(a == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

a = [65, 23, 81, 43, 92, 39, 57, 16, 75, 32]
threeWayQuicksort(a)
print(a == [16, 23, 32, 39, 43, 57, 65, 75, 81, 92])

a = []
threeWayQuicksort(a)
print(a == [])

a = [1]
threeWayQuicksort(a)
print(a == [1])

a = [1, 1, 1, 1]
threeWayQuicksort(a)
print(a == [1, 1, 1, 1])

a = [2, 2, 2, 4, 1]
threeWayQuicksort(a)
print(a == [1, 2, 2, 2, 4])

a = [-6, 1, 4, 9, 0, 3, 5, 2, 7, 8, -10, -2, -2, 0, 1]
threeWayQuicksort(a)
print(a == [-10, -6, -2, -2, 0, 0, 1, 1, 2, 3, 4, 5, 7, 8, 9])
