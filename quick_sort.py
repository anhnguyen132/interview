from typing import List


def swap(a: List, l: int, r: int) -> None:
    a[l], a[r] = a[r], a[l]


def partition(a: List, left: int, right: int, pivotIndex: int) -> None:
    pivot = a[pivotIndex]

    # swap pivot to the end
    swap(a, pivotIndex, right)

    l, r = left, right - 1
    while l <= r:
        # Need to check l <= r first to avoid l getting out of range
        # while a[l] <= pivot and l <= r:
        while l <= r and a[l] <= pivot:
            l += 1

        # while a[r] > pivot and l <= r:
        while l <= r and a[r] > pivot:
            r -= 1

        if l < r:
            swap(a, l, r)
            # l += 1
            # r -= 1

    # swap pivot back
    swap(a, l, right)

    return l


def quickSortHelper(a: List, l: int, r: int) -> None:
    if l >= r:
        return

    # Partition the array to 2 parts where left part contains all numbers <= pivot
    # returns the index splitting these 2 partitions (i.e. the index where the greater partition begins)
    split = partition(a, l, r, l)

    # NOT (a, l, split)!!! Otherwise it'd fail if pivot = max number in a
    quickSortHelper(a, l, split - 1)
    quickSortHelper(a, split + 1, r)


# sort in place
def quickSort(a: List) -> None:
    """
    Divide and Conquer
    Choose the first elem as pivot.
    Swap the pivot with the last elem (=> Can also not swap here, instead do the sorting in a[1:] then swap back pivot with elem at index = right pointer)
    Partition the array to 2 parts where left part contains all numbers <= pivot:
        Have left, right pointers = 0, n - 2 moving inwards, swap a[left] with a[right] if a[left] > pivot and a[right] < pivot
    Keep doing this recursively on the 2 new partitions

    Time:
    Each subarray is on avg half the size of the original arr
    Takes O(n) time to partition each subarray
    Best case = Avg time = O(nlogn)
    Worst case = O(n^2) when repeatedly choosing pivot = min or max number in the array, i.e. when the original array is sorted (asc or desc)

    Space: O(logn) bc of the recursion stack.
        Can do iterative sol but would need a stack => Same space complexity.
        Can't use just a loop bc want to work on BOTH partitions to sort them
        (unlike quick select, only need to look into one partition)
    """
    quickSortHelper(a, 0, len(a) - 1)


# a = [6, 1, 4, 9, 0, 3, 5, 2, 7, 8]
# quickSort(a)
# print(a == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

a = [1, 4, 0, 3, 5, 2]
quickSort(a)
print(a == [0, 1, 2, 3, 4, 5])

a = [6, 1, 4, 9, 0, 3, 5, 2, 7, 8]
quickSort(a)
print(a == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

a = [65, 23, 81, 43, 92, 39, 57, 16, 75, 32]
quickSort(a)
print(a == [16, 23, 32, 39, 43, 57, 65, 75, 81, 92])

a = []
quickSort(a)
print(a == [])

a = [1]
quickSort(a)
print(a == [1])

a = [1, 1, 1, 1]
quickSort(a)
print(a == [1, 1, 1, 1])

a = [2, 2, 2, 4, 1]
quickSort(a)
print(a == [1, 2, 2, 2, 4])

a = [-6, 1, 4, 9, 0, 3, 5, 2, 7, 8, -10, -2, -2, 0, 1]
quickSort(a)
print(a == [-10, -6, -2, -2, 0, 0, 1, 1, 2, 3, 4, 5, 7, 8, 9])
