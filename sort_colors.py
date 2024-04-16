from typing import List


def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.

    Use a hash map
    Time: O(n), Space: O(n)

    Want space O(1)
    3 pointers: l, cur, r = 0, 0, n-1
    swap elem if nums[l] would become 0 and nums[r] would become [2]

    Time: O(n), Space O(1)
    """
    n = len(nums)
    l, cur, r = 0, 0, n - 1
    # move l and r towards middle s.t. anything to left of l = 0 and anything to right of r = 2. Aything btw them = 1 (inclusive)

    while cur < n and r >= cur:
        if nums[l] == 2 and (nums[r] == 0 or nums[r] == 1):
            nums[l] = nums[r]
            nums[r] = 2

        if nums[cur] == 0:
            if nums[l] == 1:
                nums[l], nums[cur] = 0, 1
                cur += 1
        elif nums[cur] == 1:
            cur += 1
        elif nums[cur] == 2:
            if nums[r] == 0 or nums[r] == 1:
                nums[cur] = nums[r]
                nums[r] = 2

        if nums[l] == 0:
            l += 1
            if cur < l:
                cur = l
        if nums[r] == 2:
            r -= 1


nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums == [0, 0, 1, 1, 2, 2])

nums = [2, 0, 1]
sortColors(nums)
print(nums == [0, 1, 2])

nums = [0, 1]
sortColors(nums)
print(nums == [0, 1])

nums = [2, 0]
sortColors(nums)
print(nums == [0, 2])

nums = [2, 1]
sortColors(nums)
print(nums == [1, 2])

nums = [2, 2]
sortColors(nums)
print(nums == [2, 2])

nums = [1]
sortColors(nums)
print(nums == [1])
