"""
Bonus (CodePath intermediate, Week 7, session 2)

Given a string, find the length of the longest substring in it with no more than K distinct characters.

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Input: String="cbbebi", K=3
Output: 5

"""

def longestSubstringKdistinct(string, k):
  low, high, len_longest, num_distinct = 0, 0, 0, 0
  chars = set()
  l = len(string)
  
  for low in range(l):
    high = low
    while num_distinct <= k and high < l:
      if string[high] not in chars:
        if num_distinct == k:
            break
        else:
            chars.add(string[high])
            num_distinct += 1
      high += 1
      
    if high - low > len_longest:
      len_longest = high - low
    #   print(f"high: {high}, low: {low}, num_distinct: {num_distinct}, chars: {chars}")
      
    chars.clear()
    num_distinct = 0
  return len_longest

print(longestSubstringKdistinct("araaci", 2) == 4)
print(longestSubstringKdistinct("araaci", 1) == 2)
print(longestSubstringKdistinct("cbbebi", 3) == 5)






