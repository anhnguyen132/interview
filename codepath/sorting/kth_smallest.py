from quickSort import quicksort

"""
    Given an array and a number k where k is less than size of array, we need to find the 
    k-th smallest element in the given array. It is given that all array elements are distinct.

    Examples:

    Input: [7, 10, 4, 3, 20, 15]
        k = 3
    Output: 7

    Input: [7, 10, 4, 3, 20, 15]
        k = 4
    Output: 10

    HAPPY CASE
    Input: [7, 10, 4, 3, 20, 15], K = 3
    Output: 7

    Input: [7, 10, 4, 3, 20, 15], K = 4
    Output: 10

    EDGE CASE (Single element)
    Input: [7], K = 1
    Output: 7
"""
def kth_smallest(array, k):
  if not (k <= len(array) and k > 0):
    return
  quicksort(array)
  return array[k-1]

test_1 = [1,2,3,7,5]
quicksort(test_1)
print(test_1 == [1,2,3,5,7])


test_2 = [1,2,3,4,5,6]
quicksort(test_2)
print(test_2 == [1,2,3,4,5,6])

test_3 = []
quicksort(test_3)
print(test_3 == [])

test_4 = [1]
quicksort(test_4)
print(test_4 == [1])

print("Testing k-th smallest")

print(kth_smallest([7, 10, 4, 3, 20, 15], k = 4) == 10)
print(kth_smallest([7], 1) == 7)

"""
Sample Approach #2: Min Heap of size K O(N logK)

1) Create a Max Heap
2) Put the first k elements in the heap
3) Iterate through the rest of the array
    a) If the element is smaller than the largest element in the heap:
        i) Push the element in
        ii) Pop the largest element out
            - This will maintain K elements in the heap
4) Return the largest element in the heap at the end of the iteration

Time Complexity: O((N-K) log(K))
Space Complexity: O(K) [Heap of size K]

>>>>> Sample Implementation #2 (Python)

    import heapq
    def kth_smallest(arr: list, k: int) -> int:
        arr = [-1 * x for x in arr]
        h = []
        for i in range(k):
            heapq.heappush(h, arr[i])
        for i in range(k, len(arr)):
            heapq.heappushpop(h, arr[i])
        return -1 * heapq.heappop(h)

#####################################
Sample Approach #3: Quick Select O(N)

1) Create two variables, a start index and end, both initialized to 0 and 
    len(arr) - 1
2) While True
    a) Generate a random value between start and end variables
    b) Partition the subarray between start and end with the randomly 
        selected value
    c) If the randomly selected value belongs in overall index K - 1
        i) We found the Kth smallest element, return it
    d) If the randomly selected value has index less than K - 1
        i) Update start variable to the randomly selected variable + 1
        ii) Repeat
    e) Else, the randomly selected value has index greater than K - 1
        i) Update end variable to the randomly selected variable - 1
        ii) Repeat

>>>>>>>>> Sample Implementation #3 (Python)

    def kthSmallest(arr, l, r, k):
    
        # If k is smaller than number of
        # elements in array
        if (k > 0 and k <= r - l + 1):
        
            # Partition the array around last
            # element and get position of pivot
            # element in sorted array
            pos = partition(arr, l, r)
    
            # If position is same as k
            if (pos - l == k - 1):
                return arr[pos]
            if (pos - l > k - 1): # If position is more,
                                # recur for left subarray
                return kthSmallest(arr, l, pos - 1, k)
    
            # Else recur for right subarray
            return kthSmallest(arr, pos + 1, r,
                                k - pos + l - 1)
    
        # If k is more than number of
        # elements in array
        return sys.maxsize
    
    # Standard partition process of QuickSort().
    # It considers the last element as pivot and
    # moves all smaller element to left of it
    # and greater elements to right
    def partition(arr, l, r):
    
        x = arr[r]
        i = l
        for j in range(l, r):
            if (arr[j] <= x):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i

"""