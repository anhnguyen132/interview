# https://leetcode.com/problems/combination-sum/description/

from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Backtracking

    Let
    N = len(candidates)
    T = target
    M = the minimal value among the candidates

    Time:
    > This is DFS tree traversal in a n-ary tree (the fan-out of each node would be bounded to N)
    > The maximal depth of the tree, would be T/M where we keep on adding the smallest element to the combination
    > At each node, it takes a constant time to process, except the leaf nodes which could take a linear time to make a copy of combination
    > # leaf nodes is bounded by O(N^{T/M})
    > # non-leaf nodes is bounded by
        O(N^0 + N^1 + ... + N^{T/M - 1}) = O(N^{T/M} - 1)
    => Time: O(N^{T/M} - 1) + O(N * N^{T/M})
            = O(N * N^{T/M})
            = O(N^{T/M + 1})

    Space: O(T/M)
    """
    result = []
    n = len(candidates)

    def generateCombs(start: int, remaining: int, curComb: List[int]) -> None:
        if remaining < 0:
            return
        if remaining == 0:
            result.append(curComb[:])
            return

        for i in range(start, n):
            x = candidates[i]
            curComb.append(x)
            generateCombs(i, remaining - x, curComb)
            curComb.pop()

    generateCombs(0, target, [])
    return result


print(combinationSum(candidates=[2, 3, 6, 7], target=7) == [[2, 2, 3], [7]])
print(
    combinationSum(candidates=[2, 3, 5], target=8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
)
print(combinationSum(candidates=[2], target=8) == [[2, 2, 2, 2]])
print(combinationSum(candidates=[2], target=9) == [])
print(
    combinationSum(candidates=[2, 3, 5], target=9)
    == [[2, 2, 2, 3], [2, 2, 5], [3, 3, 3]]
)
print(combinationSum(candidates=[2], target=1) == [])
print(combinationSum(candidates=[2, 4, 6], target=1) == [])
