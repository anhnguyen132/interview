from typing import List


# sort an array
# Time: O(nlogn)
# Space: O(n) (to store the sorted array when merge 2 sorted arrays)
def mergeSort(a: List[int]) -> None:
    n = len(a)
    if n < 2:
        return a

    return merge(mergeSort(a[0 : n // 2]), mergeSort(a[n // 2 :]))


def merge(l1: List[int], l2: List[int]) -> List[int]:
    """
    merge 2 sorted arrays in-place
    """
    if not l1 or not l2:
        return l1 or l2

    #### Iteration ####
    p1, p2 = 0, 0
    result = []
    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] <= l2[p2]:
            result.append(l1[p1])
            p1 += 1
        else:
            result.append(l2[p2])
            p2 += 1

    if p1 < len(l1):
        result.extend(l1[p1:])

    if p2 < len(l2):
        result.extend(l2[p2:])

    return result

    #### Recursion ####
    # if l1[0] <= l2[0]:
    #     return [l1[0]] + merge(l1[1:], l2)
    # return [l2[0]] + merge(l1, l2[1:])


print(mergeSort([5, 2, 3, 1]) == [1, 2, 3, 5])
print(mergeSort([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5])
print(mergeSort([]) == [])
print(mergeSort([0]) == [0])
print(mergeSort([-8, 5, 1, 1, 2, 0, 0, -4]) == [-8, -4, 0, 0, 1, 1, 2, 5])
