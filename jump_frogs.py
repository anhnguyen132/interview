def maxDist(blocks):
    # Time O(n), Space O(1)
    n = len(blocks)
    l, r = 0, 0
    curMax = 0

    while l <= r and r < n - 1:
        if blocks[r] <= blocks[r + 1]:
            r += 1
        else:  # move l to the first block having same height as blocks[r]
            # set curr max if applies
            curDist = r - l + 1
            if curMax < curDist:
                curMax = curDist
            temp = r
            while blocks[temp - 1] == blocks[temp] and temp > 0:
                temp -= 1
            l = temp
            r += 1

    curDist = r - l + 1
    if curMax < curDist:
        curMax = curDist

    return curMax


print(maxDist([2, 6, 8, 5]) == 3)
print(maxDist([1, 5, 5, 2, 6]) == 4)
print(maxDist([1, 1]) == 2)
print(maxDist([1, 1, 1, 1, 1]) == 5)

# print(maxDist([2, 2, 2, 10, 1, 10, 2, 2, 2]))
print(maxDist([2, 2, 2, 10, 1, 10, 2, 2, 2]) == 4)

print(maxDist([2, 2, 2, 10, 1, 10, 2, 2]) == 4)
