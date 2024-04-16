from node import Node     

def removeDup(node):
  curr = node
  while curr != None:
    cur_val = curr.data
    temp = curr.next
    if temp == None:
      return
    next_val = temp.data
    if cur_val == next_val:
      curr.next = temp.next
    else:
      curr = temp
  



head = Node(1) # 1
head_head = head
next_node = Node(3)
head.next = next_node # 1->3
head = head.next
next_node = Node(4)
head.next = next_node # 1-> 3->4
head = head.next
next_node = Node(4)
head.next = next_node
head = head.next

print(head_head)
#1->1->2->3->3  
removeDup(head_head)
print(head_head)

# i think we got it