class Node:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

def identical(root1, root2):
  if not root1 and not root2:
    return True

  if (not root1 and root2) or (not root2 and root1):
    return False

  if root1.val != root2.val:
    return False

  return identical(root1.left, root2.left) and identical(root1.right, root2.right)


if __name__ == "__main__":
    root1p = Node(1, Node(2), Node(3))
    root1q = Node(1, Node(2), Node(3))
    answer1 = True
    print(identical(root1p, root1q) == answer1)

    root2p = Node(1, Node(2))
    root2q = Node(1, None, Node(3))
    answer2 = False
    print(identical(root2p, root2q) == answer2)

    root3p = Node(1, Node(2), Node(1))
    root3q = Node(1, Node(1), Node(2))
    answer3 = False
    print(identical(root3p, root3q) == answer3)

    answer4 = True
    print(identical(None, None) == answer4)

    root5p = Node(1)
    root5q = Node(2)
    answer5 = False
    print(identical(root5p, root5q) == answer5)