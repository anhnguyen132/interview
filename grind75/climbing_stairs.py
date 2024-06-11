# https://leetcode.com/problems/climbing-stairs/description/


def climbStairs(n: int) -> int:
    """
    DP: first step, take 1 or 2 steps
    total = dp(n-1) + dp(n-2)
    """
    ##### Iteration ######
    one_step_back = 0
    two_steps_back = 0
    total = 0

    for i in range(1, n + 1):
        if i == 1:
            one_step_back = 1
            total = 1
        else:
            total = one_step_back + two_steps_back
        two_steps_back = one_step_back
        one_step_back = total

    return total

    ##### Recursion ######
    # # base cases
    # if n < 0:
    #     return 0
    # if n == 0:
    #     return 1

    # return climbStairs(n - 1) + climbStairs(n - 2)


print(climbStairs(2) == 2)
print(climbStairs(3) == 3)
print(climbStairs(1) == 1)

"""
1 1 1 1
1 1 2
1 2 1
2 1 1
2 2
"""
print(climbStairs(4) == 5)
