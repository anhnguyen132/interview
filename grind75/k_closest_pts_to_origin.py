# https://leetcode.com/problems/k-closest-points-to-origin/description/

from typing import List
import heapq

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:

    def squared_distance(p1: List[int], p2: List[int]) -> float:
        # calculate the Euclidean distance btw 2 points p1, p2
        x1, y1 = p1
        x2, y2 = p2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    origin = [0, 0]

    """
    Use a MAX heap of size k (NEGATE the vals since python only has min heap)

    Keep pushing (distance, point) to this max heap, maintaining size = k
    i.e. if size = k + 1, pop from this heap

    Time: 
        Each push to heap = O(logk). Pushes O(n) times
        Each pop = O(logk). Pop O(n - k) times
        => Total time = O(nlogk)
    Space: O(k) for the heap
    """

    # calculate distance from the origin for each point and store in a max heap 
    distances = [] # format of each node = (dist, [x,y])
    for p in points:
        heapq.heappush(distances, tuple([-1 * squared_distance(p, origin), p]))
        if len(distances) == k + 1:
            heapq.heappop(distances)

    k_closest = [p for _, p in distances] 
    return k_closest[:k]
    




print(kClosest(points=[[1, 3], [-2, 2]], k=1) == [[-2, 2]])
print(kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2) == [[-2, 4],[3, 3]])

# k = # of points
print(kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=3) == [[5, -1], [3, 3], [-2, 4]])

# duplicate points
print(kClosest(points=[[3, 3], [5, -1], [-2, 4], [-2, 4]], k=3) == [[-2, 4], [-2, 4], [3, 3]])

print(kClosest(points=[[3, 3], [5, -1], [-2, 4], [-2, 4]], k=2) == [[-2, 4], [3, 3]])

# points has only dups
print(kClosest(points=[[2, 2], [2, 2], [2, 2], [2, 2]], k=2) == [[2, 2], [2, 2]])

# n = 1
print(kClosest(points=[[1, 3]], k=1) == [[1, 3]])

# points include the origin
print(kClosest(points=[[3, 3], [5, -1], [-2, 4], [0, 0]], k=2) == [[3, 3], [0, 0]])

# lots of points
print(kClosest(points=[[2, 3],[5, -1],[-2, 4],[1, -10],[12, -1],[-8, 4],[20, -20],[0, 0]],k=4) 
      == [[5, -1], [2, 3], [-2, 4], [0, 0]])

print(kClosest(points = [[3, 3], [5, -1], [-2, 4], [0, 0], [1, 1]], k = 3) == [[3, 3], [1, 1], [0, 0]])

# points on the axes
print(kClosest(points = [[1, 0], [0, 1], [0, -2], [-2, 0]], k = 2) == [[0, 1], [1, 0]])

# high x,y val
print(kClosest(points = [[100, 100], [200, 200], [300, 300], [400, 400]],k = 3) == [[300, 300], [100, 100], [200, 200]])