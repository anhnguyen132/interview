# https://brilliant.org/wiki/radix-sort/#:~:text=Radix%20sort%20works%20by%20sorting,digits%20in%20each%20place%20value.

from typing import List


def countingSort(a: List[str], d: int) -> List[int]:
    """
    subroutine for radix sort : implement counting sort, sort based on the d-th digit
    Time: O(n + k)
    Space: O(n + k)
    where k = max(a) - min(a), i.e. the range of elems in a
    """
    n = len(a)
    if n < 2:
        return [int(x) for x in a]

    # get the range of a
    start, end = int(min(a)), int(max(a))
    counts = [0 for _ in range(start, end + 1)]  # NEVER do [0] * (end - start)
    output = [None for _ in range(n)]  # NEVER do [None] * n

    # can get an elem x in a from index i of counts by: x = i + start
    for x in a:
        counts[int(x) - start] += 1

    k = len(counts)
    #### OG Counting sort algo: STABLE ####
    for i in range(1, k):
        counts[i] += counts[i - 1]

    # for x in a: # Need to go right to left to preserve o.g. order of items (stability)
    for x in reversed(a):
        x = int(x)
        i = x - start
        count = counts[i]
        output[count - 1] = x
        counts[i] -= 1

    #### OG Counting sort algo: STABLE ####

    return output


def radixSort(a: List[int]) -> List[int]:
    n = len(a)
    if n < 2:
        return a

    # sort negative and positive numbers separately then combine the outputs
    a_neg = [abs(x) for x in a if x < 0]
    a_pos = [x for x in a if x >= 0]

    a_neg = radixSortHelper(a_neg)
    a_pos = radixSortHelper(a_pos)

    # add back the negative sign and reverse the negative numbers
    a_neg = [-1 * a_neg[i] for i in range(len(a_neg) - 1, -1, -1)]
    """
    This makes it UNSTABLE. How to make it stable?
    https://en.wikipedia.org/wiki/Radix_sort#Stable_MSD_radix_sort_implementations
    """

    return a_neg + a_pos


def radixSortHelper(a: List[int]) -> List[int]:
    n = len(a)
    if n < 2:
        return a

    # get max num of digits
    max_val = max(a)
    d = len(str(max_val))

    # LSD: sort from least significant bit
    output = a
    for i in range(d - 1, -1, -1):
        output_str = [
            str(x) if len(str(x)) == d else f'{"0" * (d - len(str(x)))}{str(x)}'
            for x in output
        ]
        output = countingSort(output_str, i)

    return output


# basic tests
print(radixSort([5, 2, 3, 1]) == [1, 2, 3, 5])
print(radixSort([9, 2, 7, 5, 3, 10, 6, 1, 8, 4]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# larger range
print(
    radixSort([9, 5, 10, 8, 12, 11, 14, 2, 22, 43])
    == [2, 5, 8, 9, 10, 11, 12, 14, 22, 43]
)
print(
    radixSort([65, 23, 81, 43, 92, 39, 57, 16, 75, 32])
    == [16, 23, 32, 39, 43, 57, 65, 75, 81, 92]
)

# already sorted input
print(radixSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])

# reverse sorted
print(radixSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])

# repeated elems
print(radixSort([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5])
print(radixSort([4, 8, 4, 2, 9, 9, 6, 2, 9]) == [2, 2, 4, 4, 6, 8, 9, 9, 9])
print(radixSort([4, 3, 12, 1, 5, 5, 3, 9]) == [1, 3, 3, 4, 5, 5, 9, 12])

# negative nums
print(radixSort([-5, -2, -8, -1, -3]) == [-8, -5, -3, -2, -1])
print(radixSort([-5, 2, 2, -2, -8, 0, 16, -1, -3]) == [-8, -5, -3, -2, -1, 0, 2, 2, 16])

# really large input range
print(
    radixSort([10000, 5000, 20000, 15000, 25000]) == [5000, 10000, 15000, 20000, 25000]
)

# empty array
print(radixSort([]) == [])

# single elem
print(radixSort([1]) == [1])

# all idential elems
print(radixSort([4, 4, 4, 4]) == [4, 4, 4, 4])
