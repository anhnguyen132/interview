def computePrime(s: str) -> int:
    pmap = [2,3,5,7,11,13,17,19,23,29,31,37,41, 43,47,53,59, 61,67,71,73, 79,83, 89,97,101]
    output = 1
    for c in s:
        i = ord(c) - ord('a')
        output *= pmap[i]
    
    return output

def isAnagram(s: str, t: str) -> bool:
    """
    sort: O(nlogn)
    freq count: O(n), space = O(n)
    > prime factor decomposition: O(n), space = O(1)
    """
    if computePrime(s) != computePrime(t):
        return False
    
    return True

print(isAnagram("anagram", "nagaram") == True)
print(isAnagram("rat", "car") == False)
print(isAnagram("a", "a") == True)
print(isAnagram("abc", "cad") == False)
    
        