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

    # # time O(n), space O(1)
    # l, r = 0, len(s) - 1
    # while l < r:
    #     if not s[l].isalnum():
    #         l += 1
    #     if not s[r].isalnum():
    #         r -= 1
    #     if s[l].isalnum() and s[r].isalnum():
    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l += 1
    #         r -= 1

    # return True


# Explanation: "amanaplanacanalpanama" is a palindrome.
print(isPalindrome("A man, a plan, a canal: Panama") == True)
print(isPalindrome("race a car") == False)
print(isPalindrome(" ") == True)
print(isPalindrome("race a car 90asakshugf") == False)
print(isPalindrome("i am a girl am i a girl") == False)
print(isPalindrome("a") == True)
print(isPalindrome("9 a ??b$$. a 9") == True)
