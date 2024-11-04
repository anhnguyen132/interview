def lengthOfLongestSubstring(s: str) -> int:
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

    left and right pointer, both starting at index 0
    expand right until there's a repeated char in the substring in s[l:r+1]. 
    Shrink this substring using left pointer until all chars are unique
    Update length of longest substr w/o repeated chars along the way
    Use a set to store chars seen in curr substr 
    Each check in set = O(logn)
        --> Can we use a hash map? key = char, val = count
        --> optimize: key = char, val = index of char in s
        --> Time O(n). Space O(n)
    """
    n = len(s)
    l, r = 0, 0
    length = 0
    chars = {}

    while r < n and l <= r:
        c = s[r]

        # check if we can add this character c to our substring 
        if c in chars: 
            i = chars[c]
            if i >= l and i < r:
                # shrink left side until there's no repeat
                l = i + 1

        length = max(length, r - l + 1)

        # expand right side
        chars[c] = r
        r += 1

    return length

print(lengthOfLongestSubstring("abcabcbb") == 3)
print(lengthOfLongestSubstring("bbbbb") == 1)
print(lengthOfLongestSubstring("pwwkew") == 3)
print(lengthOfLongestSubstring(" ") == 1)
print(lengthOfLongestSubstring("biidygcc") == 5)
# print(lengthOfLongestSubstring("abba"))
print(lengthOfLongestSubstring("abba") == 2)

# n = len(s)
# if not n:
#     return 0

# l, r = 0, 0
# chars = {s[0]: 1}
# length = 1

# while l < n and r < n - 1:
#     r += 1
#     c = s[r]

#     while l < r and c in chars:
#         del chars[s[l]]
#         l += 1
    
#     chars[c] = 1
#     length = max(length, len(chars))

# return length