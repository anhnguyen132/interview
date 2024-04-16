def isPalindrome(s: str) -> bool:
    # time O(n), space O(1)
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        if not s[r].isalnum():
            r -= 1
        if s[l].isalnum() and s[r].isalnum():
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

    return True


# Explanation: "amanaplanacanalpanama" is a palindrome.
print(isPalindrome("A man, a plan, a canal: Panama") == True)
print(isPalindrome("race a car") == False)
print(isPalindrome(" ") == True)
print(isPalindrome("race a car 90asakshugf") == False)
print(isPalindrome("i am a girl am i a girl") == False)
