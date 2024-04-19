
# Fred's sol 
class MyQueue:

  def __init__(self):
    self.main = []
    self.side = []
    
  def peek(self):
    return self.main[0] if self.main else None

  def is_empty(self):
    return not(self.main)

  def enqueue(self, x):
    self.main.append(x)

  def dequeue(self):
    while self.main:
      self.side.append(self.main.pop())

    ret = self.side.pop()

    while self.side:
      self.main.append(self.side.pop())

    return ret

# Anh's sol
class Stack:
  def __init__(self):
    self.stack = []
    
  def push(self, val):
    self.stack.append(val)
    # print("my lst: ", self.stack)
    
  def pop(self):
    if self.is_empty():
      return None
      
    removed = self.stack.pop()
    return removed
    
  def peek(self):
    if self.is_empty():
      return None
      
    return self.stack[-1]
    
  def is_empty(self):
    return len(self.stack) == 0
    
class MyAQueue:

    def __init__(self):
      self.stack_push = Stack()
      self.stack_pop = Stack()  

    def enqueue(self, x: int) -> None:
      # print("queue push: ", x)
      self.stack_push.push(x)

    def dequeue(self) -> int:
      if self.is_empty():
        return None

      while not self.stack_push.is_empty():
        elem = self.stack_push.pop()
        # print("in pop: ", elem)
        self.stack_pop.push(elem)

      removed = self.stack_pop.pop()

      while not self.stack_pop.is_empty():
        elem = self.stack_pop.pop()
        # print("in pop1: ", elem)
        self.stack_push.push(elem)

      return removed

    def peek(self) -> int:
      if self.is_empty():
        return None
        
      while not self.stack_push.is_empty():
        elem = self.stack_push.pop()
        # print("in peek: ", elem)
        self.stack_pop.push(elem)

      first_elem = self.stack_pop.peek()

      while not self.stack_pop.is_empty():
        elem = self.stack_pop.pop()
        # print("in peek1: ", elem)
        self.stack_push.push(elem)

      return first_elem

    def is_empty(self) -> bool:
      return self.stack_push.is_empty()


def main():
  q1 = MyQueue()
  q1.enqueue(1)
  q1.enqueue(2)
  print('Test 1a:', q1.peek() == 1)
  print('Test 1b:', q1.dequeue() == 1)
  print('Test 1c:', q1.is_empty() == False)
  print('Test 1d:', q1.dequeue() == 2)
  print('Test 1e:', q1.is_empty() == True)

  q2 = MyQueue()
  print('Test 2a:', q2.peek() == None)
  print('Test 2b:', q2.is_empty() == True)

  q3 = MyQueue()
  q3.enqueue(1)
  print('Test 3a:', q3.peek() == 1)
  print('Test 3b:', q3.is_empty() == False)
  print('Test 3c:', q3.dequeue() == 1)
  print('Test 3d:', q3.is_empty() == True)

  print("\n========= Testing Anh's ==========")
  q1 = MyAQueue()
  q1.enqueue(1)
  q1.enqueue(2)
  print('Test 1a:', q1.peek() == 1)
  print('Test 1b:', q1.dequeue() == 1)
  print('Test 1c:', q1.is_empty() == False)
  print('Test 1d:', q1.dequeue() == 2)
  print('Test 1e:', q1.is_empty() == True)

  q2 = MyAQueue()
  print('Test 2a:', q2.peek() == None)
  print('Test 2b:', q2.is_empty() == True)

  q3 = MyAQueue()
  q3.enqueue(1)
  print('Test 3a:', q3.peek() == 1)
  print('Test 3b:', q3.is_empty() == False)
  print('Test 3c:', q3.dequeue() == 1)
  print('Test 3d:', q3.is_empty() == True)

main()