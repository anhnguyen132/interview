# https://en.wikipedia.org/wiki/Counting_sort
"""
Must be Stable - preserves order of repeated elements
i.e. if two elements share the same key, their relative order in the output array and their relative order in the input array should match
"""

from typing import List


def countingSort(a: List[int]) -> List[int]:
    """
    Time: O(n + k)
    Space: O(n + k)
    where k = max(a) - min(a), i.e. the range of elems in a
    """
    n = len(a)
    if n < 2:
        return a

    # get the range of a
    start, end = min(a), max(a)
    counts = [0 for _ in range(start, end + 1)]  # NEVER do [0] * (end - start)
    output = [None for _ in range(n)]  # NEVER do [None] * n

    # get counts of the elems in a, 
    # can get an elem x in a from index i of counts by: x = i + start
    for x in a:
        counts[x - start] += 1

    k = len(counts)

    #### Anh's variant from the OG algo: NOT STABLE ####
    # """
    # iterate thru counts, for each index j in counts, if its val > 0, write to output the val (x = j + start) counts[j] times
    # """
    # i = 0
    # for j in range(k):
    #     x = j + start
    #     while counts[j] > 0 and i < n:
    #         output[i] = x
    #         counts[j] -= 1
    #         i += 1
    #### Anh's variant from the OG algo: NOT STABLE ####

    #### OG Counting sort algo: STABLE ####
    # add counts of prev elems
    for i in range(1, k):
        counts[i] += counts[i - 1]

    # for x in a: # Need to go right to left to preserve o.g. order of items (stability)
    for x in reversed(a):
        i = x - start
        count = counts[i]
        output[count - 1] = x
        counts[i] -= 1

    #### OG Counting sort algo: STABLE ####

    return output


# basic tests
print(countingSort([5, 2, 3, 1]) == [1, 2, 3, 5])
print(countingSort([9, 2, 7, 5, 3, 10, 6, 1, 8, 4]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# larger range
print(
    countingSort([9, 5, 10, 8, 12, 11, 14, 2, 22, 43])
    == [2, 5, 8, 9, 10, 11, 12, 14, 22, 43]
)
print(
    countingSort([65, 23, 81, 43, 92, 39, 57, 16, 75, 32])
    == [16, 23, 32, 39, 43, 57, 65, 75, 81, 92]
)

# already sorted input
print(countingSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])

# reverse sorted
print(countingSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])

# repeated elems
print(countingSort([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5])
print(countingSort([4, 8, 4, 2, 9, 9, 6, 2, 9]) == [2, 2, 4, 4, 6, 8, 9, 9, 9])
print(countingSort([4, 3, 12, 1, 5, 5, 3, 9]) == [1, 3, 3, 4, 5, 5, 9, 12])

# negative nums
print(countingSort([-5, -2, -8, -1, -3]) == [-8, -5, -3, -2, -1])
print(
    countingSort([-5, 2, 2, -2, -8, 0, 16, -1, -3]) == [-8, -5, -3, -2, -1, 0, 2, 2, 16]
)

# really large input range
print(
    countingSort([10000, 5000, 20000, 15000, 25000])
    == [5000, 10000, 15000, 20000, 25000]
)

# empty array
print(countingSort([]) == [])

# single elem
print(countingSort([1]) == [1])

# all idential elems
print(countingSort([4, 4, 4, 4]) == [4, 4, 4, 4])
