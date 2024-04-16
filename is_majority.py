"""
Write a function to find if a given integer x appears more than n/2 times in a sorted array of n integers.

Examples:

Input:  [1, 2, 3, 3, 3, 3, 10], x = 3
Output: True (x appears more than n/2 times in the given array)

Input:  [1, 1, 2, 4, 4, 4, 6, 6], x = 4
Output: False (x doesn't appear more than n/2 times in the given array)

Input:  [1, 1, 1, 2, 2], x = 1
Output: True (x appears more than n/2 times in the given array)
"""

def majority(a, x):
  l = len(a)
  target = l/2
  count = 0

  #Brute Force
  #Time: O(n)
  for val in a:
    if val == x:
      count += 1
  return count > target

def new_majority(a, x):
  if not a:
    return False
    
  if len(a) == 1:
    return a[0] == x
    
  if len(a) % 2 != 0:
    i = len(a) // 2
    mid = a[i]
    if mid != x:
      return False
    return new_majority(a[:i], x) or new_majority(a[i+1:], x)
  else:
    print(a)
    i = len(a) // 2
    print(i)
    mid1 = a[i-1]
    mid2 = a[i]
    
    if mid1 != x or mid2 != x:
      return False
    return new_majority(a[:i], x) or new_majority(a[i:], x)
  

    
def main():
  tests = [
    {
      'input': {
        'a': [1],
        'x': 1
      },
      'output': True
    },
    {
      'input': {
        'a': [1, 1],
        'x': 1
      },
      'output': True
    },
    {
      'input': {
        'a': [1, 1, 2],
        'x': 1
      },
      'output': True
    },
    {
      'input': {
        'a': [1, 1, 2, 2],
        'x': 1
      },
      'output': False
    },
    {
      'input': {
        'a': [1, 1, 1, 2, 2],
        'x': 1
      },
      'output': True
    },
    {
      'input': {
        'a': [1, 1, 2, 2, 2],
        'x': 1
      },
      'output': False
    },
    {
      'input': {
        'a': [0, 1, 1, 1, 2],
        'x': 1
      },
      'output': True
    },
    {
      'input': {
        'a': [0, 0, 1, 1, 2],
        'x': 1
      },
      'output': False
    },
    {
      'input': {
        'a': [0, 1, 1, 2, 2],
        'x': 1
      },
      'output': False
    },
    {
      'input': {
        'a': [0, 1, 1, 1, 2],
        'x': 2
      },
      'output': False
    },

    {
      'input': {
        'a': [0, 0, 1, 1, 1, 2],
        'x': 1
      },
      'output': False
    },
    {
      'input': {
        'a': [0, 1, 1, 1, 1, 2],
        'x': 1
      },
      'output': True
    },
    {
      'input': {
        'a': [1, 1, 1, 1, 2, 2],
        'x': 1
      },
      'output': True
    },
    {
      'input': {
        'a': [1, 1, 1, 2, 2, 2],
        'x': 1
      },
      'output': False
    },
    {
      'input': {
        'a': [1, 1, 1, 1, 1, 1],
        'x': 1
      },
      'output': True
    },
    {
      'input': {
        'a': [1, 2, 3, 3, 3, 3, 10],
        'x': 3
      },
      'output': True
    },
    {
      'input': {
        'a': [1, 1, 2, 4, 4, 4, 6, 6],
        'x': 4
      },
      'output': False
    },
    {
      'input': {
        'a': [1, 1, 1, 2, 2],
        'x': 1
      },
      'output': True
    },
  ]

  # for i in range(len(tests)):
  #   print(f'Test {i+1} Pass:', new_majority(tests[i]['input']['a'], tests[i]['input']['x']) == tests[i]['output'])

  i = 6
  print(f'Test {i+1} Pass:', new_majority(tests[i]['input']['a'], tests[i]['input']['x']) == tests[i]['output'])

main()