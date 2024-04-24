from typing import Optional


def binarySearchHelper(nums: int, key: int, l: int, r: int) -> Optional[int]:
    if l > r:
        return None
    if l == r:
        if key == nums[l]:
            return l
        return None

    # print(l, r)
    mid = l + (r - l) // 2
    if key == nums[mid]:
        # find the smallest index where nums[i] == key
        i = mid
        while i >= 0 and nums[i] == key:
            i -= 1

        return i + 1
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
    return binarySearchHelper(nums, key, 0, len(nums) - 1)
    ########## Recursion ##########

    ########## Iteration ##########
    # TODO: implement iterative sol
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
