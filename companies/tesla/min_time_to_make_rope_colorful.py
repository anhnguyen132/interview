# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

from typing import List


def minCost(colors: str, neededTime: List[int]) -> int:
    """
    Iterate thru the array, keep track of any stretch of repeated colors encountered
    use 2 pointers start and end to keep track of this
    For each stretch, remove every balloon except for the one with the highest cost

    Time O(n), Space O(1)
    """
    start, end = 0, 0  # start and end index of a stretch of repeated colors (inclusive)
    totalCost = 0

    def removeCost(start: int, end: int) -> int:
        # get the cost of removing all balloons except for the one with highest cost starting from index start and ending at index end
        cost = 0
        maxCost = 0
        for i in range(start, end + 1):
            curCost = neededTime[i]
            maxCost = max(maxCost, curCost)
            cost += curCost
        return cost - maxCost

    prev = None
    for i, color in enumerate(colors):
        if color == prev:
            end += 1
        else:
            prev = color
            if start < end:
                totalCost += removeCost(start, end)

            start, end = i, i

    if start < end:
        totalCost += removeCost(start, end)
    return totalCost


print(minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]) == 3)
print(minCost(colors="abc", neededTime=[1, 2, 3]) == 0)
print(minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]) == 2)
print(minCost(colors="bbbaaa", neededTime=[4, 9, 3, 8, 8, 9]) == 23)
