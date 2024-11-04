def getLongestPalindrome(s: str, i: int) -> tuple[int, int]:
    """
    returns the start and end index for the longest palindromic substring in s having ith index as the middle position
    """
    # move left & right pointers outwards until they dont match. Need to consider odd-length and even-length substrings. 
    # => Length of substring = left - right + 1 - 2 (bc left and right now point at the first mismatched chars) = left - right - 1
    n = len(s)
    start, end = 0, 0 # start and end index of the longest palindromic substr in s having ith index as the middle position

    def expand(l, r): 
        nonlocal end, start           
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        if r - l - 1 > end - start + 1:
            start, end = l + 1, r - 1

    # for odd length
    expand(i - 1, i + 1)
        
    # even length
    expand(i, i + 1)
            
    return start, end

    # for odd length
    # l, r = i - 1, i + 1
    # while l >= 0 and r < n and s[l] == s[r]:
    #     l -= 1
    #     r += 1
    # if r - l - 1 > end - start + 1:
    #     start, end = l + 1, r - 1
    
    # # print(f"after odd len: i = {i}, s = {start}, e = {end}")
            
    # # even length
    # l, r = i, i + 1
    # while l >= 0 and r < n and s[l] == s[r]:
    #     l -= 1
    #     r += 1
    # # print(f"after even len while loop: i = {i}, l = {l}, r = {r}")
    # if r - l - 1 > end - start + 1:
    #     start, end = l + 1, r - 1
    
    # # print(f"after even len: i = {i}, s = {start}, e = {end}")
    
    return start, end


def longestPalindrome(s: str) -> str:
    # starting from the middle method
    # for each position i, check to see what's the longest palidromic substring that can have i as the middle point.  
    start, end = 0, 0 # start and end index of the longest palindromic substr
    n = len(s)
    for i in range(n):
        curr_start, curr_end = getLongestPalindrome(s, i)
        if curr_end - curr_start > end - start:
            start, end = curr_start, curr_end
    
    return s[start : end + 1]
    # time: O(n^2), space: O(1)

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

    