"""
Given an input string, write a function that returns the run-length encoded string for the input string.*

Example:

Input: "wwwwaaadexxxxxx"
Output: "w4a3d1e1x6"
"""
def Encoding(string):

    """ (Deric's code)
  if len(string) == 0:
    return ""
  
  
  prev = string[0]
  count = 0
  return_string = ""
  for character in string: #iterate through string
    #check if character is different
    if(character != prev): #if new character append prev charcter and count
      return_string += prev + str(count) #append character and count to return
      print(return_string)
      prev = character #updates prev character < currently
      count = 1
    else: #if not new character update count
      count += 1
      
  return_string += prev + str(count)
  print(return_string)
  return return_string
"""



print(Encoding("wwwwaaadexxxxxx") == "w4a3d1e1x6")
print(Encoding("") == "")
print(Encoding("wwwwaaadexxxxxxww") == "w4a3d1e1x6w2")
print(Encoding("wwwwaaadexxxxxxwwWw") == "w4a3d1e1x6w2W1w1")
print(Encoding("0000111dexxx5xx") == "0413d1e1x351x2")


##### Fred Ngo's sol #####
def rle(s):
  l = len(s)

  result = ''

  i = 0
  while i < l:
    char = s[i]
    result += char

    count = 1

    while i + count < l and s[i + count] == char:
      count += 1
    
    result += str(count)

    i += count

  return result

def main():
  tests = [
    { 'input': '',                'output': '' },
    { 'input': 'a',               'output': 'a1' },
    { 'input': 'abc',             'output': 'a1b1c1' },
    { 'input': 'aa',              'output': 'a2' },
    { 'input': 'aab',             'output': 'a2b1' },
    { 'input': 'aabbcc',          'output': 'a2b2c2' },
    { 'input': 'aabaccccdexdx',   'output': 'a2b1a1c4d1e1x1d1x1' },
    { 'input': 'wwwwaaadexxxxxx', 'output': 'w4a3d1e1x6' },
  ]

  for i in range(len(tests)):
    print(f'Test {i+1}:', rle(tests[i]['input']) == tests[i]['output'])

main()


