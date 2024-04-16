"""
Convert 1D Array to 2D
"""
def convert1Dto2D(arr, m, n):
  if m*n != len(arr): #if invalid size
    return
  if arr == None:
    return
  result = []
  
  for i in range(m):
    result.append(arr[i*n: i*n + n ])
  # for i in range(0, len(arr), n):
  #   result.append(arr[i: i + n])

  return result

def print2dArray(arr):
    for row in arr:
        print(row)



test_1 = [1, 1, 1, 1, 1, 0, 1, 0, 1]
print2dArray(convert1Dto2D(test_1, 3, 3))

test_1 = [1, 1, 1, 1, 1, 0]
print2dArray(convert1Dto2D(test_1, 2, 3))

test_1 = [1, 1, 1, 1, 1, 0]
print2dArray(convert1Dto2D(test_1, 3, 2))