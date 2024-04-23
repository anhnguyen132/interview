# https://leetcode.com/problems/valid-palindrome/description/


def isPalindrome(s: str) -> bool:
    """
    2 pointers meet in the middle

    Time O(n), Space O(1)
    """
    l, r = 0, len(s) - 1
    while l < r:
        lc = s[l].lower()
        rc = s[r].lower()
        if lc.isalnum() and rc.isalnum():
            if lc != rc:
                return False
            l += 1
            r -= 1
        else:
            l += not lc.isalnum()
            r -= not rc.isalnum()

    return True


print(isPalindrome("A man, a plan, a canal: Panama") == True)
print(isPalindrome("race a car") == False)
print(isPalindrome(" ") == True)
print(isPalindrome("a") == True)
print(isPalindrome("9 a ??b$$. a 9") == True)
