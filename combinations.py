# https://leetcode.com/problems/combinations/description/

from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    """
    Backtracking

    Time O(C(n choose k))
    Space O(k)
    """
    result = []
    generateAllCombinations(1, n, k, result, [])
    return result


def generateAllCombinations(
    start: int, n: int, k: int, result: List[List[int]], curComb: List[int]
) -> None:
    if k == 0:
        """
        rmb to append a COPY, not result.append(curComb) 
        since curComb is passed by REF as it is a list
        """
        result.append(curComb[:]) 
        return

    for i in range(start, n + 1):
        # try a number
        curComb.append(i)
        generateAllCombinations(i + 1, n, k - 1, result, curComb)
        # remove this number to try another
        curComb.pop()


# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
print(combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
print(combine(1, 1) == [[1]])
print(combine(4, 3) == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]])
print(combine(4, 1) == [[1], [2], [3], [4]])
print(combine(4, 4) == [[1, 2, 3, 4]])
