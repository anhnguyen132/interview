from typing import Optional


def binarySearchHelper(nums: int, key: int, l: int, r: int) -> Optional[int]:
    if l > r:
        return None

    #### NOTE: NOT (r - l) // 2. Must add l ####
    mid = l + (r - l) // 2

    if key == nums[mid]:
        # find the smallest index where nums[i] == key
        while mid >= 0 and nums[mid] == key:
            mid -= 1
        return mid + 1

    if key < nums[mid]:
        # recurse on left portion
        return binarySearchHelper(nums, key, l, mid - 1)

    # key > nums[mid]: recurse on right portion
    return binarySearchHelper(nums, key, mid + 1, r)


def binarySearch(nums: int, key: int) -> Optional[int]:
    """
    nums is sorted in ascending order
    return the first index at which key is at in nums
    return None if key is not in nums
    """
    ########## Recursion ##########
    # Time: O(logN), Space: O(logN) bc of recursion stacks
    # return binarySearchHelper(nums, key, 0, len(nums) - 1)
    ########## Recursion ##########

    ########## Iteration ##########
    # Time: O(logN), Space: O(1)
    l, r = 0, len(nums) - 1
    while l <= r:
        # if use (l+r) / 2 can cause an overflow bug if use Java or C
        mid = l + (r - l) // 2 

        if key == nums[mid]:
            while mid >= 0 and nums[mid] == key:
                mid -= 1
            return mid + 1

        if key < nums[mid]:
            # another ver to support l and r meeting at termination: r = mid (also while loop cond. is while l < r). Prob: First Bad Version
            r = mid - 1

        if key > nums[mid]:
            l = mid + 1

    ########## Iteration ##########


print(binarySearch([2, 3, 4, 10, 40], 10) == 3)

print(binarySearch([3, 4, 5, 6, 7, 8, 9], 4) == 1)

print(binarySearch([2, 7, 8, 13, 25, 29, 33, 51, 89, 90, 95], 90) == 9)

# key = last num
print(binarySearch([2, 3, 4, 10, 40], 40) == 4)
print(binarySearch([2, 7, 8, 13, 25, 29, 33, 51, 89, 90, 95], 95) == 10)
# key = first num
print(binarySearch([2, 7, 8, 13, 25, 29, 33, 51, 89, 90, 95], 2) == 0)

# duplicate elems
print(binarySearch([-10, 2, 3, 3, 4, 10, 10, 10, 40], 2) == 1)
# duplicate elems, key = 1 of the dup elems
print(binarySearch([-10, 2, 3, 3, 4, 10, 10, 10, 40], 10) == 5)
print(binarySearch([2, 3, 4, 4, 10, 40], 4) == 2)
print(binarySearch([2, 3, 4, 4, 10, 40, 40], 40) == 5)
print(binarySearch([2, 3, 4, 4, 4, 10, 40, 40], 4) == 2)
print(binarySearch([2, 3, 4, 4, 4, 10, 40, 40, 40], 40) == 6)
print(binarySearch([2, 3, 4, 4, 10, 40, 40, 40], 40) == 5)

# empty nums
print(binarySearch([], 10) == None)

# negative numbers
print(binarySearch([-10, -4, -3, -2, 0, 1, 2, 4, 8], -2) == 3)

# key not in nums
print(binarySearch([-10, -4, -3, -2, 0, 1, 2, 4, 8], 10) == None)
