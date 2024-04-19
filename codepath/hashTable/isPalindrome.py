# start = start of the string s
# end = end of s
# go from 2 ends
# if start and end are alphanumeric:
#     if start == end:
#         start

# // recursive
# def func(s):
#     empty string or 1 letter/numer:
#         return true
#     if leng of s == 2 and these 2 are alphanumeric and s[0] != s[1]:
#         return false
#     start = 0
#     end = length of s - 1
#     if s[start] and s[end] are alphanumeric: 
#         if s[start] == s[end]:
#             return func(s[start+1:end-1])
#         return false
#     if s[start] != alphanumeric:
#         start++
#         return func(s[start:end])
#     if s[end] not alphanumeric:
#         end--
#         return func(s[start:end])

def isPalindrome0(s):
    """
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
    and removing all non-alphanumeric characters, it reads the same forward and backward. 
    Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.
    start = 0
    end = 9
    return isPalindrome("ace a ca")

    start = 0, end = 6, return Palindrome("ce a c")
    start = 0, end = 5, return Palindrome("e a ")
    start = 0, end = 3, return Palindrome("e a")
    start = 0, end = 2, return false

    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
    """
    if len(s) == 0 or (len(s) == 1 and s[0].isalnum()):
        return True
    start = 0
    end = len(s) - 1
    if s[start].isalnum() and s[end].isalnum():
        if s[start].lower() == s[end].lower():
            return isPalindrome0(s[start+1 : end])
        return False
    if not s[start].isalnum():
        return isPalindrome0(s[start+1 : end+1])
    if not s[end].isalnum():
        return isPalindrome0(s[start : end])

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
print(isPalindrome0(s1))
print(isPalindrome0(s2))
print(isPalindrome0("??///"))
print(isPalindrome0("??A///"))
print(isPalindrome0("??AA///"))


def isPalindrome1(s):
    """
    Given a string s, return true if the s can be palindrome after deleting at most one character from it.

    Input: s = "aba"
    Output: true

    Input: s = "abca"
    Output: true
    Explanation: You could delete the character 'c'.

    Input: s = "abc"
    Output: false
    """
    return helper(s, True)
def helper(s, b):
    if len(s) == 0 or (len(s) == 1 and s[0].isalnum()):
        return True
    start = 0
    end = len(s) - 1
    if s[start].isalnum() and s[end].isalnum():
        if s[start].lower() == s[end].lower():
            return helper(s[start+1 : end], b)
        if b == True:
            return helper(s[start+1 : end+1], False) or helper(s[start : end], False)
        else:
            return False
    if not s[start].isalnum():
        return helper(s[start+1 : end+1], b)
    if not s[end].isalnum():
        return helper(s[start : end], b)

print(isPalindrome1("aba"))
print(isPalindrome1("abca"))
print(isPalindrome1("abc"))



