# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

from typing import List


def search(nums: List[int], target: int) -> int:
    """
    nums has distinct values

    Binary search: observation, only 1 side is sorted
    nums[l] < nums[mid]: left side is sorted
    nums[mid] < nums[r]: right side is sorted

    Time O(logn), Space O(1)
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if target == nums[mid]:
            return mid

        # left side is sorted
        if nums[l] <= nums[mid]:
            """
            has to be <= rather than just < bc would fail this case
            print(search([8, 4], 4) == 1)
            would give -1 since l = mid = 0 
            => nums[l] = nums[mid] = 8 => else case
            but target = 4 < 8 = nums[mid] => r = mid - 1 = -1
            => r < l = 0 => return -1
            """
            if target < nums[mid] and target >= nums[l]:
                r = mid - 1  # look in left portion
            else:
                l = mid + 1
        else:  # right side is sorted
            if target > nums[mid] and target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1


# print(search([4, 5, 6, 7, 0, 1, 2], 0) == 4)
# print(search([4, 5, 6, 7, 0, 1, 2], 3) == -1)
# print(search([1], 0) == -1)
# print(search([0, 1, 2, 4, 5, 6, 8], 0) == 0)
# print(search([0, 1, 2, 4, 5, 6, 8], 8) == 6)
# print(search([4, 5, 6, 7, 0, 1, 2], 4) == 0)
# print(search([4, 5, 6, 7, 0, 1, 2], 2) == 6)
# print(search([4, 8], 4) == 0)
# print(search([4, 8], 8) == 1)
# print(search([8, 4], 8) == 0)
# print(search([8, 4], 4))
# print(search([8, 4], -10) == -1)
# print(search([1, 2, 4, 5, 6, 7, 0], 2) == 1)
# print(search([6, 7, 0, 1, 2, 4, 5], 2) == 4)


def searchDups(nums: List[int], target: int) -> int:
    """
    nums can have duplicated values

    Binary search: observation, only 1 side is sorted
    nums[l] < nums[mid]: left side is sorted
    nums[mid] < nums[r]: right side is sorted

    Time O(logn), Space O(1)
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        # print(l, mid, r)
        if target == nums[mid]:
            while target == nums[mid]:
                mid -= 1
            return mid + 1

        # left side is sorted
        if nums[l] <= nums[mid]: 
            if target < nums[mid] and target >= nums[l]:
                r = mid - 1  # look in left portion
            else:
                l = mid + 1
        else:  # right side is sorted
            if target > nums[mid] and target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1

print(searchDups([4, 5, 6, 7, 0, 1, 2], 0) == 4)
print(searchDups([4, 5, 6, 7, 0, 1, 2], 3) == -1)
print(searchDups([1], 0) == -1)
print(searchDups([0, 1, 2, 4, 5, 6, 8, 8, 8], 0) == 0)
print(searchDups([0, 1, 2, 4, 5, 6, 8, 8], 0) == 0)
print(searchDups([0, 1, 2, 4, 5, 6, 8], 8) == 6)
print(searchDups([4, 5, 6, 7, 0, 1, 2], 4) == 0)
print(searchDups([4, 5, 6, 7, 0, 1, 2], 2) == 6)
print(searchDups([4, 8], 4) == 0)
print(searchDups([4, 8], 8) == 1)
print(searchDups([8, 4], 8) == 0)
print(searchDups([8, 4], 4) == 1)
print(searchDups([8, 4], -10) == -1)
print(searchDups([1, 2, 4, 5, 6, 7, 0], 2) == 1)
print(searchDups([6, 7, 0, 1, 2, 4, 5], 2) == 4)

print(searchDups([4, 5, 6, 7, 0, 0, 1, 2], 0) == 4)
print(searchDups([4, 5, 6, 6, 6, 7, 0, 1, 2, 2], 3) == -1)
print(searchDups([1, 1], 0) == -1)
print(searchDups([4, 5, 6, 6, 6, 7, 0, 1, 2, 2], 7) == 5)
print(searchDups([1,2,2,2,2], 2) == 1)
