def isPalindrome(s: str, i: int, j: int) -> bool:
    l, r = i, j
    
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True
       

def longestPalindrome(s: str) -> str:
    """
    dynamic programing. 2D table of (i, j). For each checks if its palindromic
    Time: O(n^2), Space: O(n^2)
    """
    n = len(s)
    table = [[]] * n 
    for lst in table:
        lst = [0] * n
    
    start, end = 0, 0 # start and end index of the longest palindromic substring in s
    for i in range(n):
        for j in range(n):
            if j - i > end - start and isPalindrome(s, i, j):
                start, end = i, j
    
    return s[start: end + 1]


def main(): 
    print(longestPalindrome("babad") == ('bab' or 'aba'))
    print(longestPalindrome("xcxxbabxxcad") == "cxxbabxxc")
    print(longestPalindrome("xcx16bab61cad") == "16bab61")
    print(longestPalindrome("xcx160bab061cad") == "160bab061")
    print(longestPalindrome("cbbd") == 'bb')
    print(longestPalindrome("aa") == 'aa')
    print(longestPalindrome("a") == 'a')

if __name__ == "__main__":
    main()

    