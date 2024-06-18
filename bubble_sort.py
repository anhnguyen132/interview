# https://en.wikipedia.org/wiki/Bubble_sort#Optimizing_bubble_sort

from typing import List

def bubbleSort(a: List[int]) -> None:
    """
    Time: 
        Worst, Avg, Best: O(n^2)
    Space: O(1)
    """
    n = len(a)
    
    # the n-th pass finds the n-th largest element and puts it into its final place. So, the inner loop can avoid looking at the last n − 1 items when running for the n-th time
    unsorted_len = n

    while True:
        # stop once we reach a state where there is no swap happened bc the array has been sorted
        swapped = False
        
        for i in range(unsorted_len - 1):
            if a[i] > a[i + 1]:
                swap(a, i, i + 1)
                swapped = True
        unsorted_len -= 1

        if swapped == False:
            break


def swap(a: List[int], i: int, j: int) -> None:
    n = len(a)
    if i in range(n) and j in range(n):
        a[i], a[j] = a[j], a[i]

a = [1, 4, 0, 3, 5, 2]
bubbleSort(a)
print(a == [0, 1, 2, 3, 4, 5])

a = [6, 1, 4, 9, 0, 3, 5, 2, 7, 8]
bubbleSort(a)
print(a == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

a = [65, 23, 81, 43, 92, 39, 57, 16, 75, 32]
bubbleSort(a)
print(a == [16, 23, 32, 39, 43, 57, 65, 75, 81, 92])

a = []
bubbleSort(a)
print(a == [])

a = [1]
bubbleSort(a)
print(a == [1])

a = [1, 1, 1, 1]
bubbleSort(a)
print(a == [1, 1, 1, 1])

a = [2, 2, 2, 4, 1]
bubbleSort(a)
print(a == [1, 2, 2, 2, 4])

a = [-6, 1, 4, 9, 0, 3, 5, 2, 7, 8, -10, -2, -2, 0, 1]
bubbleSort(a)
print(a == [-10, -6, -2, -2, 0, 0, 1, 1, 2, 3, 4, 5, 7, 8, 9])
