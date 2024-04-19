class Node:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

# Anh's sol
# Time: O(n)
# Space: O(n + 2^logn) = O(n)
def level_order(root):
    if not root:
        return []

    result = []
    result.append([root])
    temp = []

    while True:
        last_level = result[len(result) - 1]
        
        for i, node in enumerate(last_level):       
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            last_level[i] = node.val
        
        if not temp:
            return result
        result.append(temp[:])
        temp.clear()
        
    return result

# Fred's sol
# def level_order(root):

#     def recurse_tree(root, current_level = 0):
#         if not root: return

#         if len(levels) == current_level:
#             levels.append([])
        
#         levels[current_level].append(root.val)
#         recurse_tree(root.left, current_level + 1)
#         recurse_tree(root.right, current_level + 1)
    
#     levels = []
#     recurse_tree(root)
#     return levels

def main():
  tests = [
    {
      'input': None,
      'output': []
    },
    {
      'input': Node(1),
      'output': [[1]]
    },
    {
      'input': Node(2, Node(1)),
      'output': [[2],[1]]
    },
    {
      'input': Node(2, None, Node(1)),
      'output': [[2],[1]]
    },
    {
      'input': Node(2, Node(1), Node(3)),
      'output': [[2],[1,3]]
    },
    {
      'input': Node(3, Node(2, Node(1))),
      'output': [[3],[2],[1]]
    },
    {
      'input': Node(1, None, Node(2, None, Node(3))),
      'output': [[1],[2],[3]]
    },
    {
      'input': Node(3, Node(2), Node(4, Node(5), Node(6))),
      'output': [[3], [2,4], [5,6]]
    },
    {
      'input': Node(3, Node(5, Node(4), Node(9)), Node(1, None, Node(2))),
      'output': [[3], [5,1], [4,9,2]]
    },
    {
      'input': Node(3, Node(9), Node(20, Node(15), Node(7))),
      'output': [[3], [9,20], [15,7]]
    },
    {
      'input': Node(2, Node(1), Node(4, Node(9))),
      'output': [[2], [1,4], [9]]
    },
    {
      'input': Node(2, Node(1, None, Node(9, Node(3, Node(6))))),
      'output': [[2], [1], [9], [3], [6]]
    },
  ]

  for i in range(len(tests)):
    print(f'Test {i+1} Pass:', level_order(tests[i]['input']) == tests[i]['output'])

main()