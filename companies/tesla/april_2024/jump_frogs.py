"""
1) Given an array of post nums, find the max dist s.t. having 2 pointers l, r starting at a position, l can only go left and r and only go right and both can only move if next num >= current num. 
E.g. 
print(maxDist([2, 6, 8, 5]) == 3)
print(maxDist([1, 5, 5, 2, 6]) == 4)print(maxDist([1, 1]) == 2)
print(maxDist([1, 1, 1, 1, 1]) == 5)
print(maxDist([2, 2, 2, 10, 1, 10, 2, 2, 2]) == 4)
print(maxDist([2, 2, 2, 10, 1, 10, 2, 2]) == 4)
print(maxDist([2, 10, 8, 4, 2, 1, 9, 10, 2]) == 7)
"""


def maxDist(blocks):
    # Time O(n), Space O(1)
    n = len(blocks)
    l, r = 0, 0
    r_dir = "neutral"
    curMax = 0

    while l <= r and r < n - 1:
        # print(l, r)
        if (
            r_dir == "neutral"
            or blocks[r] == blocks[r + 1]
            or (r_dir == "up" and blocks[r] < blocks[r + 1])
            or r_dir == "down"
        ):
            if blocks[r] < blocks[r + 1]:
                r_dir = "up"

            r += 1

        elif r_dir == "up" and blocks[r] > blocks[r + 1]:
            # print(l, r)
            curMax = max(curMax, r - l + 1)

            # reset l
            # reset l to the first block having same height as current r block
            temp = r
            while blocks[temp - 1] == blocks[temp] and temp > 0:
                temp -= 1
            l = temp
            r_dir = "down"
    curMax = max(curMax, r - l + 1)

    return curMax


print(maxDist([2, 6, 8, 5]) == 3)
print(maxDist([1, 5, 5, 2, 6]) == 4)
print(maxDist([1, 1]) == 2)
print(maxDist([1, 1, 1, 1, 1]) == 5)
print(maxDist([2, 2, 2, 10, 1, 10, 2, 2, 2]) == 4)
print(maxDist([2, 2, 2, 10, 1, 10, 2, 2]) == 4)
print(maxDist([2, 10, 8, 4, 2, 1, 9, 10, 2]) == 7)
