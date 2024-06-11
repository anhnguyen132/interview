# https://leetcode.com/problems/find-median-from-data-stream/description/

import heapq


class BinaryHeap:
    """
    Wrapper class for Python implementation of binary heap to add support for max heap since Python only implements min heap
    Only support int type elements
    """

    def __init__(self, type: str) -> None:
        self.heap = []
        if type == "min":
            self.multiplier = 1
        else:  # max heap
            self.multiplier = -1

    def isEmpty(self) -> bool:
        return len(self.heap) == 0

    def size(self) -> int:
        return len(self.heap)

    def __str__(self) -> str:
        return str([x * self.multiplier for x in self.heap])

    def push(self, num: int) -> None:
        heapq.heappush(self.heap, self.multiplier * num)

    def pop(self) -> int:
        return self.multiplier * heapq.heappop(self.heap)

    def peek(self) -> int:
        return self.multiplier * self.heap[0]


class MedianFinder:
    """
    Maintain 2 heaps:
        a Max heap to store the lowest half elems
        a Min heap to store the top half elems

    We will balance the size of these 2 heaps s.t. their sizes are roughly enough
    => To find the median:
    >> If the heap sizes are equal => current stream has even number of elems => median = Sum of head of these 2 heaps / 2
    >> else: return the head of the heap that has more elem (the larger heap)

    For this sol to work, every add needs to maintain 2 properties:
    1. All elems in Max heap <= All elems in Min heap (i.e. head of Max heap <= head of Min heap)
    2. These 2 heaps size are roughly equal

    Time:
        In addNum: each number addition takes at most 2 pushes & 1 pop
         => O(3logn) = O(logn)
        In findMedian: each call is O(1)
        Total = O(logn) + O(1) = O(logn)
    Space: O(n)

    Follow up Qs:
    1. If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    - we maintain HashMap<number,frequency> (keys are in range [0, 100])
    - we also maintain total number of elements, so that median is just total-nums/2 th element from sorted array.
    => For each addNum, update map & total number of elems => O(1)
    - then we go over Map from 1-100 and count element, when we hit total-nums/2 th element , that is our median
    => For each findMedian() call, need to go over at most 100 numbers
    => O(100) = O(1)
        Total time = O(1) + O(1) = O(1)
        Space: O(100) for map + O(n) for elems = O(n)

    2. If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    Does this mean that at any time findMedian is called, 99% of the current integers are in the range [0, 100]? Or is it not guaranteed (e.g. all nums outside of this range is given first, then findMedian is called)?

    Assume that the 99% property is guaranteed whenever findMedian is called.
        - Similar to sol to 1), just need to keep an extra bucket for numbers < 0 in the HashMap of freq (don't care about numbers > 100 since by definition of the median, it's at the 50 percentile meaning it has to be in range [0, 100]).
        - For every call to addNum: update freq map and total num elems
        - For each findMedian call: need to go over at most 101 buckets
        => Total time = O(1) + O(1) = O(1)
            Space: O(101) for map + O(n) for elems = O(n)

    """

    def __init__(self) -> None:
        self.maxHeap = BinaryHeap("max")
        self.minHeap = BinaryHeap("min")

    def addNum(self, num: int) -> None:
        # to ensure All elems in Max heap <= All elems in Min heap
        if self.maxHeap.isEmpty() or self.maxHeap.peek() >= num:
            self.maxHeap.push(num)
        else:
            self.minHeap.push(num)

        # make sure heap sizes are balanced
        if self.maxHeap.size() - self.minHeap.size() > 1:
            val = self.maxHeap.pop()
            self.minHeap.push(val)

        if self.minHeap.size() - self.maxHeap.size() > 1:
            val = self.minHeap.pop()
            self.maxHeap.push(val)

    def findMedian(self) -> float:
        if self.maxHeap.size() > self.minHeap.size():
            return self.maxHeap.peek()

        if self.minHeap.size() > self.maxHeap.size():
            return self.minHeap.peek()

        # sizes are equal, meaning num elems is even
        return (self.maxHeap.peek() + self.minHeap.peek()) / 2


if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)  # arr = [1]
    medianFinder.addNum(2)  # arr = [1, 2]
    print(medianFinder.findMedian() == 1.5)  # return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3)  # arr[1, 2, 3]
    print(medianFinder.findMedian() == 2.0)  # return 2.0

    medianFinder = MedianFinder()
    medianFinder.addNum(3)  # arr = [3]
    medianFinder.addNum(2)  # arr = [2, 3]
    print(medianFinder.findMedian() == 2.5)  # return 2.5 (i.e., (3 + 2) / 2)
    medianFinder.addNum(7)  # arr[2, 3, 7]
    print(medianFinder.findMedian() == 3.0)  # return 3.0
    medianFinder.addNum(4)  # arr[2, 3, 4, 7]
    print(medianFinder.findMedian() == 3.5)

    # negative numbers
    medianFinder = MedianFinder()
    medianFinder.addNum(-3)  # arr = [-3]
    medianFinder.addNum(-2)  # arr = [-3, -2]
    print(medianFinder.findMedian() == -2.5)  # return -2.5 (i.e., (-3 + -2) / 2)
    medianFinder.addNum(-7)  # arr[-7, -3, -2]
    print(medianFinder.findMedian() == -3.0)
    medianFinder.addNum(-4)  # arr[-7, -4, -3, -2]
    print(medianFinder.findMedian() == -3.5)

    # mixed neg & pos nums
    medianFinder = MedianFinder()
    medianFinder.addNum(-3)  # arr = [-3]
    medianFinder.addNum(2)  # arr = [-3, 2]
    print(medianFinder.findMedian() == -0.5)
    medianFinder.addNum(-7)  # arr[-7, -3, 2]
    print(medianFinder.findMedian() == -3.0)
    medianFinder.addNum(4)  # arr[-7, -3, 2, 4]
    print(medianFinder.findMedian() == -0.5)
