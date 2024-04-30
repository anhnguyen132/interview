# https://leetcode.com/problems/generate-parentheses/description/

from typing import List, Dict


def generateParenthesis(n: int) -> List[str]:
    """
    Backtracking:
    keep left count, right count for # of '(' and ')'
    => valid means left count = right count
    keep a list of strings for result.
    base case: Add to result if length of currStr == 2n

    Loop over several options for “what to do next”:
    • Tentatively “do” one option
    • call recursiveFunction()
    • “undo” that option
    """
    result = []
    # pass curStr by value using str
    generateAllParentesis(n, result, "", 0, 0)
    return result

    # pass curStr by reference using a list (leetcode editorial)
    answer = []

    def backtracking(cur_string, left_count, right_count):
        if len(cur_string) == 2 * n:
            answer.append("".join(cur_string))
            return
        if left_count < n:
            cur_string.append("(")
            backtracking(cur_string, left_count + 1, right_count)
            cur_string.pop()
        if right_count < left_count:
            cur_string.append(")")
            backtracking(cur_string, left_count, right_count + 1)
            cur_string.pop()

    backtracking([], 0, 0)
    return answer

    """
    Divide and conquor, DP
    Can use sol of n-1, n-2, etc. to solve n:
    e.g. sol(n) += sol(n-1) + sol(1)
    sol(n) += sol(n-2) + sol(2)

    Number of valid parentheses for n = The Catalan number = C(n)
    Time: O(C(n)) bc iterate 1 -> n
        => T(n) = Sum{1->n}{C(n)}
        which is asymptotically bounded by O(C(n))
    Space O(C(n)) to store all subsols (memo space T(n) = Sum{1->n}{C(n)})
    """
    # return list(helper(n, {}))


def generateAllParentesis(
    n: int, result: List[str], curStr: str, leftCnt: int, rightCnt: int
) -> None:
    if len(curStr) == 2 * n:
        if leftCnt == rightCnt:
            result.append(curStr)
        return

    if leftCnt >= rightCnt:
        # try adding '('
        generateAllParentesis(n, result, curStr + "(", leftCnt + 1, rightCnt)
        # try adding ')'
        generateAllParentesis(n, result, curStr + ")", leftCnt, rightCnt + 1)


def helper(k: int, memo: Dict[int, str]) -> None:
    if k == 1:
        return set(["()"])

    if k in memo:
        return memo[k]

    result = set()
    for i in range(1, k // 2 + 1):
        subsols1 = helper(k - i, memo)
        subsols2 = helper(i, memo)

        for s1 in subsols1:
            if i == 1:
                result.add(f"({s1})")  # inside ()
                # result.add(f"(){s1}")  # outside before ()
                # result.add(f"{s1}()")  # outside after ()
            for s2 in subsols2:
                result.add(f"{s1}{s2}")
                result.add(f"{s2}{s1}")
    memo[k] = result

    return result


print(generateParenthesis(3))
print(generateParenthesis(2))
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
