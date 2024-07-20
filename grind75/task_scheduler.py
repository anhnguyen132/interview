# https://leetcode.com/problems/task-scheduler/description/

from typing import List
from collections import Counter, deque
import heapq

def leastInterval(tasks: List[str], n: int) -> int:
    """
    All approaches use GREEDY. 
    Proof of optimality for greedy: https://leetcode.com/problems/task-scheduler/editorial/comments/2466264
        (also see pdf sol for this Q)
    """
    k = len(tasks)

    """
    Max heap + queue
    (Name of task doesnt matter here, so can ignore it and just store the frequencies)
    Use a max heap to keep track of the highest freq
    Use a queue to store tasks that need to be in idle 
    Construct a freq map of tasks. O(k)
    While max heap and queue not empty: O(k)
        time++ 
        0. If queue.peek()[1] == cur_time (i.e. the time of the 1st elem in queue), dequeue this and add freq to max heap
        1. pop from max heap & subtract 1 from the the max freq
        2. if max_freq - 1 > 0 enqueue a tuple (max_freq - 1, time interval this task will be avail again). The 2nd term = cur_time + n + 1

    Time: O(k * n) (e.g. case where only 1 type of task "A": 3, n=2)
    Space: O(1)
        Max heap: O(26) = O(1) bc tasks are uppercase English letters
        Queue: O(26) = O(1)

    Vid sol: NeetCode https://www.youtube.com/watch?v=s8p8ukTyA2I&ab_channel=NeetCode

    TODO: Proof of optimality for this
    """
    freqs = Counter(tasks) # can use an array of size 26 to minimize memory since there are only 26 possible tasks
    max_heap = [-f for f in freqs.values()]
    heapq.heapify(max_heap)
    q = deque()
    time = 0

    while max_heap or q:
        if q and q[0][1] == time:
            heapq.heappush(max_heap, -1 * q.popleft()[0]) # add freq to max heap
        
        if max_heap:
            max_freq = abs(heapq.heappop(max_heap)) - 1
            if max_freq > 0:
                q.append((max_freq, time + n + 1))

        time += 1
    
    return time

    """
    Greedy approach

    Time: O(k)
    Space: O(1)
    """

    """
    Math formula

    Time: O(k)
    Space: O(1)
    """

# basics
print(leastInterval(tasks = ["A","A","A","B","B","B"], n = 2) == 8)
print(leastInterval(tasks = ["A","C","A","B","D","B"], n = 1) == 6)
print(leastInterval(tasks = ["A","A","A", "B","B","B"], n = 3) == 10)

# only 1 type of task
print(leastInterval(tasks = ["A","A","A"], n = 2) == 7)
print(leastInterval(tasks = ["A","A","A"], n = 0) == 3)

# > 1 task w max freq
print(leastInterval(tasks = ["A","A","A", "B","B","B", "C","C","C", "D", "D", "E"], n = 2) == 12)
print(leastInterval(tasks = ["A","A","A", "B","B","B", "C","C","C"], n = 2) == 9)
print(leastInterval(tasks = ["A","A","A", "B","B","B", "C","C", "D", "D", "E"], n = 2) == 11)

