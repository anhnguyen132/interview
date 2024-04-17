# https://leetcode.com/problems/decode-ways/description/


def numDecodingsHelper(s: str, mem: dict) -> int:
    # base case
    if not s:
        return 1
    if int(s[0]) == 0:
        return 0
    if len(s) == 1:
        return 1
    if s in mem:
        return mem[s]

    num_decode = numDecodingsHelper(s[1:], mem)
    if len(s) > 1 and int(s[:2]) <= 26:
        num_decode += numDecodingsHelper(s[2:], mem)

    mem[s] = num_decode
    return num_decode


def numDecodings(s: str) -> int:
    """
    Dynamic programming:

    Topdown w memoization:
    take first 1 or 2 letters (given that the first letter != 0)
    numDecodings(s) =  numDecoding(s[1:]) + (int(s[:2]) <= 26) * numDecoding(s[2:])
    Use memoization to reduce number of recursive calls

    Time O(n) Space O(n)
    """
    # return numDecodingsHelper(s, {})

    """
    Bottom up approach: iteration
    Go from left to right of string s, 1 char at a time
    store result of prev and 2 prev chars
    At each char, examine if it be decoded either
    1) as a single digit
    2) or be added to the previous char to make a 2-digit number <= 26
    """
    if s[0] == "0":
        return 0

    if len(s) == 1:
        return 1

    one_back = None
    two_back = None
    for i, c in enumerate(s):
        cur = 0
        if i == 0:
            cur = 1

        if i > 0:
            if c != "0":
                cur += one_back

            two_digit = int(s[i - 1] + s[i])
            if two_digit <= 26 and two_digit >= 10:
                if two_back != None:
                    cur += two_back
                else:
                    cur += 1
        if i == len(s) - 1:
            return cur

        two_back = one_back
        one_back = cur


# Example 1:
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
# print(numDecodings("12"))
print(numDecodings("12") == 2)

# Example 2:
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
print(numDecodings("226") == 3)

# Example 3:
# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
print(numDecodings("06") == 0)

print(numDecodings("1006") == 0)
print(numDecodings("2206") == 1)
print(numDecodings("2611") == 4)
print(numDecodings("22611") == 6)
print(numDecodings("10011") == 0)
