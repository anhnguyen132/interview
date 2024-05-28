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
        return str(self.heap)

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
        Each enqueue/dequeue in addNum is O(logn)
        Each findMedian call is O(1)
        => O(nlogn) ??????
    Space: O(n)
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
