class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return not self.left and not self.right


# def bst_to_array(t):
#   l = []

#   if t.right:
#     #l.append(t.right.val)
#     l += bst_to_array(t.right)

#   l.append(t.val)

#   if t.left:
#     #l.append(t.left.val)
#     l += bst_to_array(t.left)

#   return l

def bst_to_array(t):
    if 

def main():
  tests = [
    {
      'input': Node(2),
      'output': [2]
    },
    {
      'input': Node(2, Node(1)),
      'output': [2, 1]
    },
    {
      'input': Node(2, None, Node(3)),
      'output': [3, 2]
    },
    {
      'input': Node(2, Node(1), Node(3)),
      'output': [3, 2, 1]
    },
    {
      'input': Node(2, Node(1), Node(3)),
      'output': [3, 2, 1]
    },
    {
      'input': Node(5, Node(3), Node(9, Node(7), Node(10))),
      'output': [10, 9, 7, 5, 3]
    },
    {
      'input': Node(5, Node(3), Node(9, Node(7), Node(10))),
      'output': [10, 9, 7, 5, 3]
    },
    {
      'input': Node(5, None, Node(9, None, Node(10))),
      'output': [10, 9, 5]
    },
  ]

  for i in range(len(tests)):
    print(f'Test {i+1} Pass:', bst_to_array(tests[i]['input']) == tests[i]['output'])

main()