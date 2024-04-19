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

def sortStack(stack):
    """
    Write a program to sort a stack such that the smallest items are on top. 
    You can use an additional temporary stack, 
    but you may not copy elements into any other data structure (such as an array).

    Time: O(n^2), Space: O(n)
    """
    temp = Stack()
    
    while not stack.isEmpty():
        num = stack.pop()
        if temp.isEmpty() or temp.peek() <= num:
            temp.push(num)
        else:
            # peel off the layer of number in temp > num and store them in stack
            count = 0
            while not temp.isEmpty() and temp.peek() > num:
                stack.push(temp.pop())
                count += 1

            temp.push(num)

            # put back the peeled off layer to temp
            while count > 0:
                temp.push(stack.pop())
                count -= 1          
    return temp.list()
"""
s = [-1, 1, 2, 1]
t = 0
num = 0
c = 2, tn = 2
"""

def main():
    s  = Stack([])
    print('Test 0:', sortStack(s) == [])

    s  = Stack([1])
    print('Test 1:', sortStack(s) == [1])

    s  = Stack([1, 1, 1, 2, 1])
    print('Test 2:', sortStack(s) == [1, 1, 1, 1, 2])

    s  = Stack([-1, 1, 0, 2, 1])
    print('Test 3:', sortStack(s) == [-1, 0, 1, 1, 2])

    s = Stack([34, 3, 31, 98, 92, 23])
    print('Test 4:', sortStack(s) == [3, 23, 31, 34, 92, 98])

    s = Stack([3, 5, 1, 4, 2, 8])
    print('Test 5:', sortStack(s) == [1, 2, 3, 4, 5, 8])

    s = Stack([1,2,3])
    print('Test 6:', sortStack(s) == [1, 2, 3])

    s = Stack([10,9,3,1])
    print('Test 5:', sortStack(s) == [1, 3,9,10])

main()
