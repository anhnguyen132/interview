# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def helper(A, B, X, Y, cur):
    if not A or not B:
        return 0

    total = 0
    if cur == "A":
        # stay or not stay on A
        total = min(
            A[0] + helper(A[1:], B[1:], X, Y, "A"),
            B[0] + X + helper(A[1:], B[1:], X, Y, "B"),
        )
    else:
        total = min(
            B[0] + helper(A[1:], B[1:], X, Y, "B"),
            A[0] + Y + helper(A[1:], B[1:], X, Y, "A"),
        )
    # print(len(A), cur, total)
    return total


def solution(A, B, X, Y):
    # Implement your solution here
    # DP

    # start at A or B
    startA = A[0] + helper(A[1:], B[1:], X, Y, "A")
    startB = B[0] + helper(A[1:], B[1:], X, Y, "B")
    # print(startA, startB)
    total = min(
        A[0] + helper(A[1:], B[1:], X, Y, "A"), B[0] + helper(A[1:], B[1:], X, Y, "B")
    )
    return total


print(solution([1, 6, 2], [3, 2, 5], 2, 1) == 8)
