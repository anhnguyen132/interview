class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self._next = next 

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node
    
    def __str__(self):
        curr = self
        result = ""
        while curr != None:
            result += str(curr.data) + " "
            curr = curr.next 
        return result 