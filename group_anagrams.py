from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    https://leetcode.com/problems/group-anagrams/editorial/

    lower case English letters only => 26 letters
    use a hash map with key = tuple of size 26 where if a word has 2 letters 'a' then the first elem of the tuple = 2
    return list(d.values)

    Time O(n), Space O(n)
    """
    d = {}
    for s in strs:
        key = [0] * 26
        for c in s:
            key[ord(c) - ord("a")] += 1
        key = tuple(key)
        if key in d:
            d[key].append(s)
        else:
            d[key] = [s]

    return list(d.values())


"""
prime product factor decomposition sol
"""
# def computeProduct(s: str):
#         # map each char in string s to a prime number and compute the product of them
#         prime_map = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
#         prod = 1
#         for ch in s:
#             prod *= prime_map[ord(ch) - ord('a')]
#         return prod

# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     """
#     Uses prime factor decomposition
#     Each char is mapped to a prime number.
#     For each word, take the product of these number. 2 words are anagram is their products equal.
#     Uses a hash map where key = product, val = list of anagram words having that same product

#     Time: O(n), Space: O(n)
#     """
#     product_map = {}
#     for s in strs:
#         s_prod = computeProduct(s)
#         if s_prod in product_map:
#             product_map[s_prod].append(s)
#         else:
#             product_map[s_prod] = [s]

#     return list(product_map.values())

print(
    groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
)
print(groupAnagrams([""]) == [[""]])
print(groupAnagrams(["a"]) == [["a"]])
print(groupAnagrams(["", "a"]) == [[""], ["a"]])
