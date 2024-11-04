def longestPalindromeSubseq(s: str) -> int:
    """
    Dynamic programing
    2D table of size nxn
    lps[i][j] = the longest palindromic subseq in s starting at index i and ending at index j
    if s[i] == s[j]:
        lps[i][j] = 2 + lps[i+1][j-1]
    else:
        lps[i][j] = max(lps[i+1][j], lps[i][j-1])
    
    row i depends on row i+1 => i: n-1 -> 0
    col j depends on col j-1 => j: 0 -> n-1

    returns lps[0][n-1]
    Time: O(n^2). Space: O(n^2)
    Optimization: For each lps[i][j], only need vals from row i+1 and i => only store these 2 rows 
    => Space: O(n)
    """
    n = len(s)
    i_row = [0] * n
    i1_row = [0] * n

    for i in range(n-1, -1, -1):
        for j in range(i, n): # only consider j >= i
            if j == i:
                i_row[j] = 1 # when i == j, 1 char s trings has palindromic subseq len = 1
            elif s[i] == s[j]:
                i_row[j] = 2 + i1_row[j-1]
            else:
                i_row[j] = max(i1_row[j], i_row[j-1])
        
        if i == 0:
            break
  
        i1_row = i_row 
        i_row = [0] * n
    
    return i_row[n-1]



def main():
    print(longestPalindromeSubseq("bbbab") == 4) # bbbb 
    print(longestPalindromeSubseq("cbbd") == 2) # bb

    print(longestPalindromeSubseq("a") == 1)
    print(longestPalindromeSubseq("bqabamctabalb") == 9) # babacabab

if __name__ == '__main__':
    main()