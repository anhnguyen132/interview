# https://leetcode.com/problems/ransom-note/description/

from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    create a freq count hash map for magazine
    then iterate thru ransomNote,
        if a char c not in freq -> False
        if its in freq, and freq[c] > 0 -> decrement count
            if freq[c] == 0 -> False
    True

    m = len(magazine), n = len(ransomNote)
    Time O(m + n), Space O(m)
    """
    freq = Counter(magazine)
    for c in ransomNote:
        if c not in freq or freq[c] == 0:
            return False
        freq[c] -= 1

    return True


print(canConstruct("a", "b") == False)
print(canConstruct("aa", "ab") == False)
print(canConstruct("aa", "aab") == True)
print(canConstruct("aabcde", "fecadabmn") == True)
