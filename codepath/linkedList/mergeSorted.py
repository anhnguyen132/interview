from node import Node 

def mergeSorted(lst1, lst2):
    """
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
    """
    head = Node()
    iter1 = lst1
    iter2 = lst2
    iter3 = head

    while iter1 and iter2:
        if iter1.data <= iter2.data:
            iter3.next = iter1
            iter1 = iter1.next
        else:
            iter3.next = iter2
            iter2 = iter2.next
        iter3 = iter3.next
    
    if iter1:
        iter3.next = iter1
    
    if iter2:
        iter3.next = iter2
    
    return head.next


one = Node(1)
two = Node(2)
fr = Node(4)
one.next = two
two.next = fr
lst1 = one
print(lst1)

one = Node(1)
thr = Node(3)
fr = Node(4)
one.next = thr
thr.next = fr
lst2 = one
print(lst2)
lst2 

print(mergeSorted(lst1, lst2))
        
