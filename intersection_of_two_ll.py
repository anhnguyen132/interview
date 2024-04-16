from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printll(head: ListNode) -> None:
    cur = head
    s = ""
    while cur:
        s += str(cur.val) + " "
        cur = cur.next
    print(s)


def getLength(head: ListNode) -> int:
    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next
    return length


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    Could you write a solution that runs in O(m + n) time and use only O(1) memory?

    Qs: Can there be repeated values in these ll?? Yes

    1. Get the length m, n of each list
    2. do m - n, this is the number of nodes to skip thru b4 we can start comparing node in A w node in B to see if they're the same node
    If we reach the end and no common node => return None

    m, n = 0? No
    Time: O(m+n). Space: O(1)
    """
    # get length of A and B
    m = getLength(headA)
    n = getLength(headB)

    skipLen = m - n
    if skipLen < 0:
        skipHead = headB
        skipLen = abs(skipLen)
        otherHead = headA
    else:
        skipHead = headA
        otherHead = headB

    while skipLen:
        skipHead = skipHead.next
        skipLen -= 1

    while skipHead and otherHead:
        if skipHead is otherHead:
            return skipHead
        skipHead = skipHead.next
        otherHead = otherHead.next


def genIntersect(
    intersectVal: int, listA: List, listB: list, skipA: int, skipB: int
) -> tuple[ListNode, ListNode]:
    headA, headB, intersectNode = None, None, None

    prev = None
    for i, elem in enumerate(listA):
        node = ListNode(elem)
        if i == 0:
            headA = node
        if i == skipA:
            intersectNode = node
        if prev:
            prev.next = node
        prev = node

    prev = None
    for i, elem in enumerate(listB):
        if i < skipB:
            node = ListNode(elem)
        elif i == skipB:
            node = intersectNode

        if i == 0:
            headB = node

        if prev:
            prev.next = node
        prev = node

        if i == skipB:
            break

    return (headA, headB)


# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
headA, headB = genIntersect(
    intersectVal=8, listA=[4, 1, 8, 4, 5], listB=[5, 6, 1, 8, 4, 5], skipA=2, skipB=3
)
intersectNode = getIntersectionNode(headA, headB)
print(intersectNode.val == 8)

# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Intersected at '2'
headA, headB = genIntersect(
    intersectVal=2, listA=[1, 9, 1, 2, 4], listB=[3, 2, 4], skipA=3, skipB=1
)
intersectNode = getIntersectionNode(headA, headB)
print(intersectNode.val == 2)

# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
headA, headB = genIntersect(
    intersectVal=0, listA=[2, 6, 4], listB=[1, 5], skipA=3, skipB=2
)
intersectNode = getIntersectionNode(headA, headB)
print(intersectNode is None)

headA, headB = genIntersect(intersectVal=2, listA=[2], listB=[2], skipA=0, skipB=0)
intersectNode = getIntersectionNode(headA, headB)
print(intersectNode.val == 2)

headA, headB = genIntersect(
    intersectVal=2, listA=[2, 2, 2], listB=[2, 2, 2], skipA=0, skipB=0
)
intersectNode = getIntersectionNode(headA, headB)
print(intersectNode.val == 2)

headA, headB = genIntersect(
    intersectVal=2, listA=[2, 2, 2, 1, 3], listB=[2, 2, 2, 3], skipA=4, skipB=3
)
intersectNode = getIntersectionNode(headA, headB)
print(intersectNode.val == 3)
