"""
Given an array of integers A sorted in non-decreasing order, return a new array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

def sorted_squares(a):
  if not a:
    return a


  #Brute Force method
  #Time: O(n)
  for i in range(len(a)):
    a[i] = a[i]**2
    
  #Time: O(nlogn)
  a.sort()
  return a

def new_sorted_squares(a):
  """
  1. Divide a into 2 parts: negative numbers & positive numbers
  2. square them
  3. reverse the negative array
  4. merge 2 sorted arrays
  """
  if not a:
    return a

  return_list = []

  #Find negative number seperation: O(n)
  right_ptr = len(a)
  for index, val in enumerate(a):
    if val >= 0:
      right_ptr = index
      break
  left_ptr = right_ptr-1

  #while it is within bounds of array-square and add: O(n)
  while left_ptr > -1 or right_ptr < len(a):
    if left_ptr <= -1 and right_ptr < len(a): #if left ptr out of bounds
      return_list.append(a[right_ptr]**2)
      right_ptr += 1
    elif left_ptr > -1 and right_ptr >= len(a): #if right ptr out of bounds
      return_list.append(a[left_ptr]**2)
      left_ptr -= 1
    else: #if both in bounds
      if abs(a[left_ptr]) > a[right_ptr]:
        return_list.append(a[right_ptr]**2)
        right_ptr += 1
      else:
        return_list.append(a[left_ptr]**2)
        left_ptr -= 1 
  return return_list

  #so you find the smallest positive number in the array.
  #set it to pos
  #the number to the left, if any, will be negative; set it to neg
# now we do some kind of window sliding, where we increament both sides (neg(will be decresed - as in -1) and pos(increased as in +1))
#before we do the increamentation every time, we check for the smallest number (disregard the signs) and compute its square into the array. Then we increament it in the rightful order if neg or pos.
  #we do this till there's nothing left on both sides to check(that is if neg is < 0 and pos > len(array) - 1) 

#The time complexity for this will be 0(n) where n is the number of elem



    
  #[-4,-1,0,3,10]
  #0
  #left ptr < right ptr => append smaller, increment smaller ptr
  #abs(-1) compare 3 => 0, 1
  #abs(-4) compare 3 => 0, 1, 9
  #abs(-4) compare 10 => 0, 1, 9, 16

  #[-4,-1,[0],3,10]
  #[-4,[-1,0],3,10]
  #[-4,[-1,0,3],10]
  #[[-4,-1,0,3],10]

def main():
 
  squares_tests = [
    {
      'input': [],
      'output': []
    },
    {
      'input': [1],
      'output': [1]
    },
    {
      'input': [0,1,2],
      'output': [0,1,4]
    },
    {
      'input': [0,1,2,3,4],
      'output': [0,1,4,9,16]
    },
    {
      'input': [-2,-1,0],
      'output': [0,1,4]
    },
    {
      'input': [-4,-3,-2,-1,0],
      'output': [0,1,4,9,16]
    },
    {
      'input': [-1,0,1],
      'output': [0,1,1]
    },
    {
      'input': [-2,-1,0,1,2],
      'output': [0,1,1,4,4]
    },
    {
      'input': [-4,-1,0,3,10],
      'output': [0,1,9,16,100]
    },
    {
      'input': [-7,-3,2,3,11],
      'output': [4,9,9,49,121]
    },
  ]

  print()
  print()
  print()
  print("Sorted Squares:")
  for i in range(len(squares_tests)):
    print(f'Test {i+1} Pass:', new_sorted_squares(squares_tests[i]['input']) == squares_tests[i]['output'])

main()
