# https://leetcode.com/problems/merge-k-sorted-lists/description/


from typing import List, Optional
import functools

@functools.total_ordering
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other: object) -> bool:
        return self.val < other.val
    
    def __eq__(self, other: object) -> bool:
        return self.val == other.val

def generate_ll(l: List[int]):
    # generate a linked list and returns the head node
    dummy = ListNode()
    cur = dummy

    for x in l:
        node = ListNode(val=x)
        cur.next = node
        cur = node

    return dummy.next

def print_ll(head: ListNode):
    ll_rep = ""
    while head:
        ll_rep += str(head.val)
        if head.next:
            ll_rep += "->"
        head = head.next
    print(ll_rep)
    return ll_rep

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Approach 1: Add one by one + Use a min HEAP to get the min val among all heads for each add

    Time:
        k = number of ll, 
        n = total number of nodes across all ll in lists
        (=> n >= k)
        For first add, push to heap takes O(log1 + log2 +...+logk) which is bounded by O(logk + logk +...+logk) = O(klogk)
        For each subsequent add: 1 pop from the heap to get the min val + 1 push to heap = O(logk)
        There are n adds  
        => Total time = O(klog(k) + (n-1)logk) 
                      = O(nlogk)
    Space:
        O(k) auxillary space for the heap
    """
    import heapq
    min_heap = []
    dummy = ListNode()
    cur = dummy

    # for ll in lists:
    for i, ll in enumerate(lists):
        if ll:
            heapq.heappush(min_heap, ll)

            # use this if ListNode has no __lt__ method defined
            # heapq.heappush(min_heap, (ll.val, i))
    
    while min_heap:
        min_head = heapq.heappop(min_heap)
        # _, i = heapq.heappop(min_heap)
        # min_head = lists[i]
        # lists[i] = min_head.next
        if min_head.next:
            heapq.heappush(min_heap, min_head.next)
            # heapq.heappush(min_heap, (min_head.next.val, i))
        cur.next = min_head
        cur = min_head
    
    return dummy.next




    """
    Approach 2: Divide and Conquer
    """

# basic tests
lsts = [[1,4,5],[1,3,4],[2,6]]
lists = []
for l in lsts:
    head = generate_ll(l)
    lists.append(head)
merged = mergeKLists(lists)
print(print_ll(merged) == "1->1->2->3->4->4->5->6")

lsts = [[1,20,24],[-16,-8,-4, 0, 4, 8],[-100,6], [10]]
lists = []
for l in lsts:
    head = generate_ll(l)
    lists.append(head)
merged = mergeKLists(lists)
print(print_ll(merged) == "-100->-16->-8->-4->0->1->4->6->8->10->20->24")

# empty lists
merged = mergeKLists([])
print(print_ll(merged) == "")

# lists having one ll which has len = 1
lists = [ListNode(val=16)]
merged = mergeKLists(lists)
print(print_ll(merged) == "16")

# lists having one ll which is empty
merged = mergeKLists([None])
print(print_ll(merged) == "")

# lists having one ll
head = generate_ll([-8, 16, 32, 64])
lists = [head]
merged = mergeKLists(lists)
print(print_ll(merged) == "-8->16->32->64")

# lists has a None node 
lsts = [[1,4,5],[1,3,4],[2,6]]
lists = []
for l in lsts:
    head = generate_ll(l)
    lists.append(head)
lists.append(None)
merged = mergeKLists(lists)
print(print_ll(merged) == "1->1->2->3->4->4->5->6")