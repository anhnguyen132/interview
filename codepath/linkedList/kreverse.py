"""
    Given a doubly linked list containing n nodes. The problem is to reverse every pod of k nodes in the list.

    Example:

    Input: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8
        k = 3
    Output: 3 <-> 2 <-> 1 <-> 6 <-> 5 <-> 4 <-> 8 <-> 7
"""

class DoublyNode:
    def __init__(self, data=0, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
        
    def __str__(self):
        curr = self
        result = ""
        while curr != None:
            result += str(curr.data) + " "
            curr = curr.next 
        return result 

# recursion
# 1) reverse the first k nodes 
# 2) Link this newly reversed portion with the result of the recursive call to the rest of the list 
# 3) return the head of the newly k-reversed linked list

def kreverse(head, k):
  """
    Time complexity: O(n)
    Space complexity: O(1)
  """
  if head is None or head.next is None:
    return head

  my_iter = head

  # get my_iter to the k-th node
  count = k
  while count > 1 and my_iter.next is not None: 
    my_iter = my_iter.next
    count -= 1

  # cut the list at the k-th node
  rest = my_iter.next
  my_iter.next = None
  if rest: rest.prev = None
    
  # reverse the first k nodes
  first_kreversed_head, first_kreversed_tail = reverse(head, my_iter)

  # make the recursive call to the rest of the list  
  rest_kreversed = kreverse(rest, k)

  # connect the 2 lists
  first_kreversed_tail.next = rest_kreversed
  if rest_kreversed: rest_kreversed.prev = first_kreversed_tail

  return first_kreversed_head
  
# Helper function for kreverse
# Given the head and tail of a doubly linked list, reverses the list  
# Returns the new head and tail
def reverse(head, tail):
  if head is None or head.next is None: 
    return head, tail

  my_iter = tail
  while my_iter is not None:
    temp = my_iter.prev
    if my_iter.next is None:
      my_iter.prev = None
    my_iter.prev = my_iter.next
    my_iter.next = temp
    my_iter = my_iter.next 

  return tail, head


################ TESTING ###################

one = DoublyNode(1)
two = DoublyNode(2)
thr = DoublyNode(3)
four = DoublyNode(4)
five = DoublyNode(5)
one.next = two
two.prev = one
two.next = thr
thr.prev = two
thr.next = four
four.prev = thr
four.next = five
five.prev = four
print("before: ", one)
print(kreverse(one, 3), ", Expected: 3 2 1 5 4\n") 

one = DoublyNode(1)
two = DoublyNode(2)
thr = DoublyNode(3)
four = DoublyNode(4)
five = DoublyNode(5)
six = DoublyNode(6)
seven = DoublyNode(7)
eight = DoublyNode(8)
one.next = two
two.prev = one
two.next = thr
thr.prev = two
thr.next = four
four.prev = thr
four.next = five
five.prev = four
five.next = six
six.prev = five
six.next = seven
six.prev = five
seven.next = eight
eight.prev = seven

print("before: ", one)
print(kreverse(one, 3), ", Expected: 3 2 1 6 5 4 8 7\n") 

one = DoublyNode(1)
two = DoublyNode(2)
one.next = two
two.prev = one
print("before: ", one)
print(kreverse(one, 3), ", Expected: 2 1\n") 

one = DoublyNode(1)
two = DoublyNode(2)
thr = DoublyNode(3)
four = DoublyNode(4)
five = DoublyNode(5)
one.next = two
two.prev = one
two.next = thr
thr.prev = two
thr.next = four
four.prev = thr
four.next = five
five.prev = four
print("before: ", one)
print(kreverse(one, 7), ", Expected: 5 4 3 2 1\n") 

one = DoublyNode(1)
print("before: ", one)
print(kreverse(one, 7), ", Expected: 1\n") 

one = None
print("before: ", one)
print(kreverse(one, 7), ", Expected: None\n") 

one = DoublyNode(1)
two = DoublyNode(2)
thr = DoublyNode(3)
four = DoublyNode(4)
five = DoublyNode(5)
six = DoublyNode(6)
seven = DoublyNode(7)
eight = DoublyNode(8)
one.next = two
two.prev = one
two.next = thr
thr.prev = two
thr.next = four
four.prev = thr
four.next = five
five.prev = four
five.next = six
six.prev = five
six.next = seven
six.prev = five
seven.next = eight
eight.prev = seven

print("before: ", one)
print(kreverse(one, 1), ", Expected: 1 2 3 4 5 6 7 8\n") 

head = DoublyNode(1)
prev_node = head
for i in range(2, 12):
  new_element = DoublyNode(i)
  new_element.prev = prev_node
  prev_node.next = new_element
  prev_node = new_element
print(f'BEFORE: {head}')
k = 3
print(f'Swapping every {k} elements')
result = kreverse(head, k=k)
print(f'AFTER: {result}')




