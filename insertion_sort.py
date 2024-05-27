from typing import List


def insertionSort(a: List[int]) -> None:
    """
    sort in-place

    iterate thru list, keep shifting right elems that are > curr elem

    Time:
        Best case: O(n) (already sorted)
        Worst case: O(n^2) (sorted in DEC order)
        Avg case: O(n^2)
    Space: O(1)
    """
    n = len(a)
    for i in range(1, n):
        cur_elem = a[i]

        #### shift and insert ####
        # check elems to the left of i, shift them right 1 by 1 if they're > cur_elem
        j = i
        while j > 0 and a[j - 1] > cur_elem:
            a[j] = a[j - 1]
            j -= 1

        # insert cur_elem to its correct position (among all elems seen so far)
        a[j] = cur_elem
        #### shift and insert ####


a = [1, 4, 0, 3, 5, 2]
insertionSort(a)
print(a == [0, 1, 2, 3, 4, 5])

a = [6, 1, 4, 9, 0, 3, 5, 2, 7, 8]
insertionSort(a)
print(a == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

a = [65, 23, 81, 43, 92, 39, 57, 16, 75, 32]
insertionSort(a)
print(a == [16, 23, 32, 39, 43, 57, 65, 75, 81, 92])

a = []
insertionSort(a)
print(a == [])

a = [1]
insertionSort(a)
print(a == [1])

a = [1, 1, 1, 1]
insertionSort(a)
print(a == [1, 1, 1, 1])

a = [2, 2, 2, 4, 1]
insertionSort(a)
print(a == [1, 2, 2, 2, 4])

a = [-6, 1, 4, 9, 0, 3, 5, 2, 7, 8, -10, -2, -2, 0, 1]
insertionSort(a)
print(a == [-10, -6, -2, -2, 0, 0, 1, 1, 2, 3, 4, 5, 7, 8, 9])
