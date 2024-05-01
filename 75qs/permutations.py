# https://leetcode.com/problems/permutations/description/

from typing import List, Set


def permute(nums: List[int]) -> List[List[int]]:
    """
    Backtracking. Keep track of a set used = set of all indices used so far to construct the current permutation

    Time: O(n!)
    Space: O(n)
    """
    result = []
    n = len(nums)

    def generatePermutations(used: Set[int], curPer: List[int]) -> None:
        if len(curPer) == n:
            result.append(curPer[:])
            return

        for i in range(n):
            if i not in used:
                curPer.append(nums[i])
                used.add(i)
                generatePermutations(used, curPer)
                curPer.pop()
                used.remove(i)

    generatePermutations(set(), [])
    return result


print(
    permute([1, 2, 3])
    == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
)
print(permute([0, 1]) == [[0, 1], [1, 0]])
print(permute([1]) == [[1]])
print(
    permute([-2, 2, 4])
    == [[-2, 2, 4], [-2, 4, 2], [2, -2, 4], [2, 4, -2], [4, -2, 2], [4, 2, -2]]
)
