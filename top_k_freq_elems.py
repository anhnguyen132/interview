# https://leetcode.com/problems/top-k-frequent-elements/description/

from typing import List, Tuple, Dict
from collections import Counter


def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    #### Naive ####
    1. Construct a hash map mapping elem : freq
    2. Construct an array of tuples (freq: elem). Sort this array by freq
    3. Get the first k tuples

    Assume worst case all elems in nums are unique (N = len(nums) = # unique elems)
    Time:  O(N) hash map + O(N) array construction + O(NlogN) sort
        = O(NlogN)
    Space: O(N)

    #### Heap ####
    1. Construct a hash map mapping elem : freq
    2. For each (elem, freq) pair in this map, add it to a min heap with key = freq, val = elem.
        If heap size = k + 1, pop the top (the elem w min freq)
    3. Pop all k nodes from the heap to return the top k freq elems

    Time:
    1. O(N)
    2. For first k pairs: O(klogk) worst case
        For the next N - k pairs, each has O(logk) pop time => (N-k)O(logk)
        => Total = O(Nlogk)
    3. O(klogk)
    => Total time: O(N + Nlogk + klogk) = O(Nlogk)

    Space: O(N) map + O(k) heap = O(N + k) = O(N)

    #### Bucket sort ####
    1. Construct a hash map mapping elem : freq
    2. # buckets = len(nums) (Optz: # buckets = max(map.values()))
    3. for elem, freq in map.items(): buckets[freq].append(elem) => O(N)
    4. Flatten buckets: [elem for bucket in buckets for elem in bucket] => O(N)
    5. flatten[-k:]
    Time: O(N)
    Space: O(N)

    #### Quick Selection ####
    Select + Partition

    Time: Avg O(n), worst case O(n^2)
    Space: O(n)
    """
    # return sorted(topKFrequentHeap(nums, k))
    # return sorted(topKFrequentBucketSort(nums, k))
    return topKFrequentQuickSelect(nums, k)


def topKFrequentQuickSelect(nums: List[int], k: int) -> List[int]:
    """
    Uses quick select to find the top K freqs

    Time: Avg O(n), Worst O(n^2)
    Space: O(n)
    """
    n = len(nums)
    if n < 2:
        return nums

    freq_map = Counter(nums)
    elems = list(freq_map.keys())  # unique elements in nums
    m = len(elems)  # number of unique elements in nums

    left, right = 0, m - 1
    while left <= right:
        split1, split2 = partition3Ways(elems, freq_map, left, right, left)
        if m - k < split1:
            right = split1 - 1
        elif m - k >= split2:
            left = split2
        else:
            # m - k >= split1 and m - k < split2
            return sorted(elems[m - k :])


def partition3Ways(
    nums: List[int], freq_map: Dict[int, int], left: int, right: int, pivotIndex: int
) -> Tuple[int, int]:
    """
    Split nums into 3 parts using 3 pointers set initially to
    l, cur, r = left, left, right

    After partitioning:
    nums[:l] = all elems having freq < pivot's freq (inclusive -> non-inclusive)
    nums[l: cur] = elems having freq == pivot's freq
    nums[cur: r] = elems having freq > pivot's freq

    Return l, cur
    """
    pivot = nums[pivotIndex]
    piv_freq = freq_map[pivot]

    l, cur, r = left, left, right
    while cur <= r:
        cur_num = nums[cur]
        cur_freq = freq_map[cur_num]
        if cur_freq == piv_freq:
            cur += 1
        elif cur_freq < piv_freq:
            swap(nums, l, cur)
            l += 1
            cur += 1
        elif cur_freq > piv_freq:
            swap(nums, cur, r)
            r -= 1

    return (l, cur)


def swap(nums: List[int], l: int, r: int) -> None:
    if l < r:
        nums[l], nums[r] = nums[r], nums[l]


def topKFrequentBucketSort(nums: List[int], k: int) -> List[int]:
    """
    Use an array as buckets of possible frequencies
    len of arr = # buckets = len(nums)

    Time O(n), Space O(n)
    """
    freq_map = Counter(nums)
    n = len(nums)

    """
    Note:
    1) not n since freq can be n
    2) Use [[]] instead of [None] so that we won't overwrite elems having same freq count
    3) DO NOT use [[]] * (n+1) since that'd make a copy of a single object
        => buckets[1] = 10 would result in [[10], [10], ...[10]]
    """
    buckets = [[] for _ in range(n + 1)]

    for x, freq in freq_map.items():
        buckets[freq].append(x)

    # print(buckets)
    # [[], [10, 6, 2, -2], [4, -4], [], [], [], [], [], []]
    flatten = [x for bucket in buckets for x in bucket]
    # print(flatten)
    # [10, 6, 2, -2, 4, -4]

    return flatten[-k:]

    ##### this could result in result arr having > k elems!!!! ####
    # result = []
    # for x in reversed(buckets):
    #     if x:
    #         result.extend(x)
    #         k -= len(x)
    #         if k <= 0:
    #             break
    ##### this could result in result arr having > k elems!!!! ####


import heapq


def topKFrequentHeap(nums: List[int], k: int) -> List[int]:
    """
    Time: O(nlogk), Space: O(k)
    """
    freq_map = Counter(nums)

    # To get top k frequencies, push to a min heap, maintaining heap size = k
    h = []
    for x, freq in freq_map.items():
        """
        Must push BEFORE pop bc if not, the final iteration will leave the heap having k + 1 nodes
        """
        heapq.heappush(h, (freq, x))
        if len(h) > k:
            heapq.heappop(h)

    # pop from heap to get the result
    return [x for _, x in h]


# print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))

print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2])
print(topKFrequent(nums=[1], k=1) == [1])
print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=3) == [1, 2, 3])
print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=1) == [1])
print(topKFrequent(nums=[10, 4, -4, 6, 2, 4, -2, -4], k=2) == [-4, 4])
print(topKFrequent(nums=[10, 4, -4, 6, 2, 4, -2, 10, -4], k=3) == [-4, 4, 10])
print(topKFrequent(nums=[8, 6, 4, 2, 0, 2, 4, 6, 8], k=4) == [2, 4, 6, 8])
print(topKFrequent(nums=[8, 6, 4, 2, 0], k=5) == [0, 2, 4, 6, 8])
