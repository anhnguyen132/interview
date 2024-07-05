# https://leetcode.com/problems/h-index/description/

from typing import List

def hIndex(citations: List[int]) -> int:
    n = len(citations)

    #### Approach 2: Use counting sort O(n) ####
    """
    Can replace any paper w > n citations by n since h <= n
    In the cumulative count step of counting sort, can go in reverse. For each val x, count # of elems in array having values >= x. Call this count c. 
    h index is the largest x where c >= x

    Time: O(n)
    Space: O(n) for the count array
    """
    count = [0 for _ in range(n + 1)]

    # count freq of elems in citations. If an elem x > n, add freq count to n
    for x in citations:
        if x > n:
            x = n
        count[x] += 1
    
    # compute cumulative count in desc
    for x in range(n, -1, -1):
        if x < n:
            count[x] += count[x + 1] 
        if count[x] >= x:
            return x
        
    return 0

    #### Approach 1: Sort the array first O(nlogn) ####
    """
    1. Sort the list of citations O(nlogn)
    2. Iterate thru the list, for each elem x, check if x >= n - i O(n)
    3. If this is True, return n - i

    Time: O(nlogn)
    Space: If sort in place O(1), otherwise O(n)
    """
    # sorted_citations = sorted(citations)
    # for i, x in enumerate(sorted_citations):
    #     if x >= n - i:
    #         return n - i
    # return 0
    

print(hIndex([3,0,6,1,5]) == 3)
print(hIndex([1,3,1]) == 1)
print(hIndex([1]) == 1)
print(hIndex([0]) == 0)
print(hIndex([2,2,2,2]) == 2)
print(hIndex([4,4,4,4]) == 4)
print(hIndex([8,6,4,10]) == 4)
print(hIndex([1000,2,4,10]) == 3)
print(hIndex([0,0,0,10000,0,0,0,0,0,0]) == 1)
