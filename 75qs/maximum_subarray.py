# https://leetcode.com/problems/maximum-subarray/description/

from typing import List


def maxSubarray(nums: List[int]) -> int:
    """
    start w 2 pointers: sliding window
    l, r = 0, 0
    if nums[r] + cur_sum < nums[r]:
        l = r
        cur_sum = nums[r]
    => but l isnt really needed => use only r

    Time O(n), Space O(1)
    """
    max_sum = float("-inf")
    cur_sum = 0

    for x in nums:
        cur_sum += x
        if x > cur_sum:
            cur_sum = x
        max_sum = max(max_sum, cur_sum)

    return max_sum


print(maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)  # [4,-1,2,1]
print(maxSubarray([1]) == 1)
print(maxSubarray([5, 4, -1, 7, 8]) == 23)  # [5,4,-1,7,8]
print(maxSubarray([5, 4, -1]) == 9)
print(maxSubarray([5, 4, -10, 100]) == 100)
print(maxSubarray([-10, -10, -1]) == -1)
print(maxSubarray([-10, 0, -10, -1, 0]) == 0)
