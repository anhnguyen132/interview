# https://leetcode.com/problems/generate-parentheses/description/

from typing import List, Set


def helper(k: int) -> None:
    if k == 1:
        return set(["()"])

    result = set()
    for i in range(1, k):
        subsols1 = helper(k - i)
        subsols2 = helper(i)

        for s1 in subsols1:
            if i == 1:
                result.add(f"({s1})")  # inside ()
                # result.add(f"(){s1}")  # outside before ()
                # result.add(f"{s1}()")  # outside after ()
            for s2 in subsols2:
                result.add(f"{s1}{s2}")
                result.add(f"{s2}{s1}")

    return result


def generateParenthesis(n: int) -> List[str]:
    """
    Can use sol of n-1, n-2, etc. to solve n:
    e.g. sol(n) += sol(n-1) + sol(1)
    sol(n) += sol(n-2) + sol(2)


    Time: O(n), Space O(n)
    """
    return list(helper(n))


# print(generateParenthesis(3))
print(
    set(generateParenthesis(3))
    == set(["((()))", "(()())", "(())()", "()(())", "()()()"])
)
print(set(generateParenthesis(1)) == set(["()"]))
print(set(generateParenthesis(2)) == set(["(())", "()()"]))
print(
    set(generateParenthesis(4))
    == set(
        [
            "(((())))",
            "((()()))",
            "((())())",
            "((()))()",
            "(()(()))",
            "(()()())",
            "(()())()",
            "(())(())",
            "(())()()",
            "()((()))",
            "()(()())",
            "()(())()",
            "()()(())",
            "()()()()",
        ]
    )
)
