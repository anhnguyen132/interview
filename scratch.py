from collections import deque
class Stack:
    def __init__(self, l=[]):
        self.stack = deque(l)
    
    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0
    
    def list(self):
        return list(self.stack)

    def __str__(self):
        return f'{self.stack}'

class MyQueue:

    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()
        self.front = None

    def push(self, x: int) -> None:
        if self.empty():
            self.front = x
        self.push_stack.push(x)

    def pop(self) -> int:
        if self.empty(): 
            return None

        while not self.push_stack.isEmpty():
            self.pop_stack.push(self.push_stack.pop())
        
        result = self.pop_stack.pop()
        if self.pop_stack.isEmpty():
            self.front = None
        else:
            self.front = self.pop_stack.peek()

        """
        dont need to put back elems to push_stack since next push can keep pushing 
        to that stack and next pop and keep popping from pop_stack
        """
        # while not self.pop_stack.isEmpty():
        #     self.push_stack.push(self.pop_stack.pop())

        return result

    def peek(self) -> int:
        if self.empty(): 
            return None
        return self.front

    def empty(self) -> bool:
        return self.push_stack.isEmpty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()