"""
2) Given 2 arrays A, B of same length n where A[i] and B[i] are how much time it costs to assemble a car part on line A, B respectively. X = time it costs to move car assembling on line A to line B for its next part. Y = time it costs to move car assembling on line B to line A for its next part. Find the min time to assemble a car
e.g. 
assemble([1, 6, 2], [3, 2, 5], 2, 1) == 8
bc 1 + (2+2) + (2+1) = 8    
    A     B       A
"""


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
