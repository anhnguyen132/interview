"""
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Examples:

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted

Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
"""

def shortestUnsortedSub(arr):
    if len(arr) == 0 or len(arr) == 1:
        return 0

    # Scan from left to right and find first element that’s out of order 
    prev = None
    sub_arr_start_index = 0
    for i, elem in enumerate(arr):
        if prev == None:
            prev = elem
        else:
            # print(f"sub_arr_start_index: {sub_arr_start_index}, prev: {prev}, elem: {elem}")
            if prev >= elem:
                sub_arr_start_index = i - 1
                break
            prev = elem

    # Scan from right to left and find first element that’s out of order
    right_elem = None
    sub_arr_end_index = 0
    i = len(arr) - 1
    while i >=0 :
        if right_elem == None:
            right_elem = arr[i]
        else:
            # print(f"right_elem: {right_elem}, arr[i]: {arr[i]}", )
            if right_elem <= arr[i]:
                sub_arr_end_index = i + 1
                break
            right_elem = arr[i]
            # print("right_elem here: ", right_elem)
        
        i -= 1

    if sub_arr_start_index == sub_arr_end_index:
        return 0

    # Find the local minimum and local maximum in that sub-array
    # print(sub_arr_start_index, sub_arr_end_index)
    sub_arr = arr[sub_arr_start_index : sub_arr_end_index + 1]
    local_min = min(sub_arr)
    local_max = max(sub_arr)

    # Extend subarray on both ends to include any number bigger than the local minimum and smaller than the local maximum
    for i in range(sub_arr_start_index):
        if arr[i] > local_min:
            sub_arr_start_index = i
            break

    for i in range(len(arr) - 1, sub_arr_end_index, -1):
        if arr[i] < local_max:
            sub_arr_end_index = i
            break
    
    print(arr[sub_arr_start_index : sub_arr_end_index + 1])
    return sub_arr_end_index - sub_arr_start_index + 1


print("===== Anh's tests ====\n")
print(shortestUnsortedSub([3, 2, 1]) == 3)
print(shortestUnsortedSub([1, 2, 5, 3, 7, 10, 9, 12]) == 5)
print(shortestUnsortedSub([1, 3, 2, 0, -1, 7, 10]) == 5)
print(shortestUnsortedSub([1, 2, 3]) == 0)
print(shortestUnsortedSub([1]) == 0)

# Fred's sol
def sort(arr):
  # Edge case: Empty and single length arrays are already sorted
    if len(arr) <= 1: return 0

    left = 0
    right = len(arr) - 1

    while left < right and arr[left] <= arr[left+1]:
        left += 1

    if left == right:
        return 0

    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1

    unsorted = arr[left:right+1]
    #print(unsorted)

    min_unsorted = min(unsorted)
    while left > 0 and arr[left - 1] > min_unsorted:
        left -= 1

    max_unsorted = max(unsorted)
    while right < len(arr) - 1 and arr[right + 1] < max_unsorted:
        right += 1
        
    #print(left, right)
    len_longest_unsorted = right - left + 1
    return len_longest_unsorted
  

def main():
    print("\n===== Fred's tests ====\n")

    tests = [
        { 'input': [5],                 'output': 0 },
        { 'input': [1,2,3],             'output': 0 },
        { 'input': [3,2,1],             'output': 3 },
        { 'input': [1,2,3,2],           'output': 2 }, # 3,2
        { 'input': [1,2,5,3,7,10,9,12], 'output': 5 }, # 5,3,7,10,9
        { 'input': [1,2,3,0,8,9,10],    'output': 4 }, # 1,2,3,0
        { 'input': [1,2,3,11,8,9,10],   'output': 4 }, # 11,8,9,10
        { 'input': [1,2,3,0,11,8,9,10], 'output': 8 }, # 1,2,3,0,11,8,9,10
        { 'input': [1,2,3,2,1],         'output': 4 }, # 2,3,2,1
    ]

    for i in range(len(tests)):
        print(f'Test {i+1}:', shortestUnsortedSub(tests[i]['input']) == tests[i]['output'])

main()