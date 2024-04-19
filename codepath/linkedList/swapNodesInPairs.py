"""
    Given a linked list, swap every two adjacent nodes and return its head.
    Example:
    Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

from node import Node

def swapNodesInPairs(head):
    if head is None or head.next is None:
        return head

    my_iter = head
    prev_tail = None
    head = head.next

    while my_iter and my_iter.next is not None:
        temp = my_iter.next
        my_iter.next = temp.next
        temp.next = my_iter
        if prev_tail is not None:
            prev_tail.next = temp
        prev_tail = my_iter
        my_iter = my_iter.next
        
    return head