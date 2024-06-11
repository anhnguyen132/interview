# https://leetcode.com/problems/word-search/description/

from typing import List, Set, Tuple


def exist(board: List[List[str]], word: str) -> bool:
    """
    Backtracking

    1) Instead of using a visited set to stored coordinates of cells we've explored in the current backtracking call, simply mark the cell as a non-alphanumeric char. After the backtrack call returns, revert the change to leave the board in a clean state.

    2) To prune the tree for a faster sol, can save the (result of) visited cells (which would be all False)

    Time
    let L = len(word)
    DFS tre traversal of 3-aray tree (fan out is at most 3 since at each position, there are 4 directions we can take next but we won't go back to where we came from).
    The max height of this tree = k
    At each node, we split the word which takes O(L) time
    We iterate through each cell in the board to find the starting position
    => Time = O(m * n) * Time for each backtracking invocation in exist
            = O(m * n) * O(L) * Number of nodes
            = O(m * n * L * (3^L - 1))
            = O(mnL3^L)

    Space = height of tree + visisted size
        = O(L + m * n) = O(mn)
    """
    m, n = len(board), len(board[0])

    def backtrack(curWord: str, r: int, c: int) -> bool:
        if not curWord:
            return True

        # try going up, right, down, left
        options = [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]

        for step in options:
            i, j = step

            if i < m and i >= 0 and j < n and j >= 0 and board[i][j] == curWord[0]:
                board[i][j] = "#"

                if backtrack(curWord[1:], i, j):
                    # return the board to O.G. state before returning
                    board[i][j] = curWord[0]
                    return True

                board[i][j] = curWord[0]

        return False

    # find the starting position
    for r in range(m):
        for c in range(n):
            if board[r][c] == word[0]:
                board[r][c] = "#"
                if backtrack(word[1:], r, c):
                    board[r][c] = word[0]
                    return True
                board[r][c] = word[0]

    return False


"""
A B C E
S F C S
A D E E
"""
print(
    exist(
        [
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "B"],
            ["A", "A", "A", "A", "B", "A"],
        ],
        "AAAAAAAAAAAAABB",
    )
    == False
)
print(
    exist(
        [
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "B"],
            ["A", "A", "A", "A", "B", "A"],
        ],
        "AAAAAAAAAAAAABAB",
    )
    == True
)
print(
    exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
    == True
)
print(
    exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
    == True
)
print(
    exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")
    == False
)
print(
    exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ECCFDE")
    == True
)
print(
    exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCcED")
    == False
)
print(
    exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "CED")
    == True
)
print(exist([["a", "a"]], "aaa") == False)
print(exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB") == True)
