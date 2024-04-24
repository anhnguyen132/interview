# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

from typing import List


def tictactoe(moves: List[List[int]]) -> str:
    """
    The last move is the winning move if there is a winner.
    If there is no winner then the length of moves tells if its a Draw or Pending
    Just need to trace back the moves of the last player who played.
    Only Checking moves that involve the same row or col as the last move or diag or antidiag
    For each such move, add 1 to a var row or col or diag or antidiag to keep track of number of moves
    if one of them == n (size of the board), then we have a winner

    m = len of moves, n = size of board
    Time O(m/2) = O(m), Space O(1)
    """
    n = 3  # size of the board
    num_moves = len(moves)
    last_mv_r, last_mv_c = moves[-1]
    row, col, diag, antidiag = 0, 0, 0, 0

    if num_moves % 2 != 0:
        potential_winner = "A"
    else:
        potential_winner = "B"

    for i, move in enumerate(moves):
        r, c = move
        if (potential_winner == "A" and i % 2 == 0) or (
            potential_winner == "B" and i % 2 != 0
        ):
            row += r == last_mv_r
            col += c == last_mv_c
            diag += r == c
            antidiag += (r == c and c == 1) or abs(r - c) == n - 1

            if row == n or col == n or diag == n or antidiag == n:
                return potential_winner

    if num_moves == n**2:
        return "Draw"

    return "Pending"


print(tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]) == "A")
print(tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]) == "B")

print(
    tictactoe([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]])
    == "Draw"
)
