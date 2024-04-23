# https://leetcode.com/problems/longest-palindrome/description/

from collections import Counter


def longestPalindrome(s: str) -> int:
    """
    create a freq count hash map on s
    for each char c, if count is even, add to length
    else:
        if count == 1, add 1 if 1 hasnt been added to length
        add count - 1 to length

    Time O(n), Space O(52) = O(1)
    """
    freq = Counter(s)
    max_len = 0
    odd_char = None

    for c, cnt in freq.items():
        if cnt % 2 == 0:
            max_len += cnt
        elif cnt == 1 and max_len % 2 == 0:
            max_len += 1
        else:
            odd_char = c
            max_len += cnt - 1

    if max_len % 2 == 0 and odd_char:
        max_len += 1

    return max_len


print(longestPalindrome("abccccdd") == 7)
print(longestPalindrome("a") == 1)
print(longestPalindrome("AabcccAcdd") == 9)
print(longestPalindrome("Aa") == 1)
print(longestPalindrome("AabB") == 1)
print(longestPalindrome("ACaCbB") == 3)
print(longestPalindrome("ccc") == 3)
print(longestPalindrome("cccA") == 3)
print(longestPalindrome("cccAA") == 5)
