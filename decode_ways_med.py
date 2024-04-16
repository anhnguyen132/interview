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

    Bottom up approach: iteration
    Go from right to left of string s, 1 char at a time
    store result of
    """
    return numDecodingsHelper(s, {})


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
