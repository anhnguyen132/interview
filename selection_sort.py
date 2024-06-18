# https://en.wikipedia.org/wiki/Selection_sort

from typing import List

def selectionSort(a: List[int]) -> None:
    """
    Find the smallest item in the list, and exchange it with the left- most unsorted element.

    Repeat the process from the first unsorted element.
    
    [----sorted---- cur ----unsorted----]
                    i  |-->             | 

    cur: the index separating the sorted (left side of it) and unsorted part of the array (cur is part of unsorted)
    i: iterate (cur -> n) to find the min elem in the unsorted part

    Time:
        Worst, Best, Avg: O(n^2) 
        bc always iterate thru entire unsorted part to find min elem
    Space: O(1)
    """
    n = len(a)
    cur = 0 
    while cur < n:
        # find min elem in the unsorted part
        min_elem_i = cur
        for i in range(cur, n):
            if a[i] < a[min_elem_i]:
                min_elem_i = i
        
        # swap this min elem with cur
        a[cur], a[min_elem_i] = a[min_elem_i], a[cur]
        cur += 1


a = [1, 4, 0, 3, 5, 2]
selectionSort(a)
print(a == [0, 1, 2, 3, 4, 5])

a = [6, 1, 4, 9, 0, 3, 5, 2, 7, 8]
selectionSort(a)
print(a == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

a = [65, 23, 81, 43, 92, 39, 57, 16, 75, 32]
selectionSort(a)
print(a == [16, 23, 32, 39, 43, 57, 65, 75, 81, 92])

a = []
selectionSort(a)
print(a == [])

a = [1]
selectionSort(a)
print(a == [1])

a = [1, 1, 1, 1]
selectionSort(a)
print(a == [1, 1, 1, 1])

a = [2, 2, 2, 4, 1]
selectionSort(a)
print(a == [1, 2, 2, 2, 4])

a = [-6, 1, 4, 9, 0, 3, 5, 2, 7, 8, -10, -2, -2, 0, 1]
selectionSort(a)
print(a == [-10, -6, -2, -2, 0, 0, 1, 1, 2, 3, 4, 5, 7, 8, 9])
