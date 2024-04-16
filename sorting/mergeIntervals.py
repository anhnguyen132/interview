"""
    Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

    Examples:

    Intervals: [[1,4], [2,5], [7,9]]
    Output: [[1,5], [7,9]]
    Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5]

    Intervals: [[6,7], [2,4], [5,9]]
    Output: [[2,4], [5,9]]
    Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

    Intervals: [[1,4], [2,6], [3,5]]
    Output: [[1,6]]
    Explanation: Since all the given intervals overlap, we merged them into one.

    HAPPY CASE
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]

    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]

    EDGE CASE (Single Case)
    Input: [[1, 4]]
    Output: [[1, 4]]
"""

"""
[[6,7], [2,4], [5,9]]
[[2,4], [5,9], [6,7]] => 4 < 5, so move to next pair
[[2,4], [5,9], [6,7]] => 9 > 6, so take larger of right side [9]
[[2,4], [5,9]]
"""

def Merge2(int1, int2):
  # if int1[2] > int2[1]: #compare 9 with 6 
  if int1[1] > int2[1]: #if 9 > 7
    larger = int1[1] #larger = 9
  else:
    larger = int2[1] #larger = 7
  return [int1[0], larger] #[5, 9]
  #return #return nothing if doesnt overlap

def mergeIntervals(intervals):
  if len(intervals) == 0:
    return []
    
  if len(intervals) == 1:
    return intervals
    
  intervals.sort(key=lambda x: x[0])
  result = []
  i = 0

  while i < len(intervals) - 1:
    a, b = intervals[i], intervals[i + 1]
      
    if a[len(a) - 1] > b[0]:
      merged = Merge2(a, b)
      result.append(merged)
      i+= 2
    elif a[len(a) - 1] == b[0]:
      result.append([a[0], b[1]])
      i += 2
    else:
      result.append(a)
      i += 1
      

  if i == len(intervals) - 1: # merge last interval
    last_interval = intervals[len(intervals) - 1]
    if len(result) > 0:
      last_result_interval = result[len(result) - 1]
      
    if last_interval[0] > last_result_interval[1]:
      result.append(last_interval)
    elif last_interval[0] == last_result_interval[1]:
      result.pop()
      result.append([last_result_interval[0], last_interval[1]])
    else:
      merged = Merge2(last_result_interval, last_interval)
      result.pop()
      result.append(merged)
    
  return result

print(mergeIntervals([[1,4], [2,5], [7,9]]) == [[1,5], [7,9]])

print(mergeIntervals([[6,7], [2,4], [5,9]]) == [[2,4], [5,9]])

print(mergeIntervals([[1,4], [2,6], [3,5]]) == [[1,6]])
print(mergeIntervals([[1,4]]) == [[1,4]])



