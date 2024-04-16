from typing import List, Optional
from identicalBSTs import identical

"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Examples:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

Output: [3,9,20,null,null,15,7]
       
           3     
          / \
         9   20
            / \
           15  7 
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# preorder: root-left-right
# inorder: left-root-right
def constructBinaryTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: 
    if not preorder or not inorder: 
        return
    
    root = TreeNode(preorder[0])
    for i, node_val in enumerate(inorder):
        if node_val == root.val:
            inorder_left = inorder[: i]
            inorder_right = inorder[i + 1:]
            break
    
    preorder_left = preorder[1:len(inorder_left) + 1]
    preorder_right = preorder[len(inorder_left) + 1:]

    root.left = constructBinaryTree(preorder_left, inorder_left)
    root.right = constructBinaryTree(preorder_right, inorder_right)

    return root

print(constructBinaryTree([], []) == None)

"""
Input: preorder = [3,9,20,15,7]
       inorder = [9,3,15,20,7]

Output:     3
           / \
          9  20
            /  \
           15   7
"""
expected = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(identical(constructBinaryTree([3,9,20,15,7], [9,3,15,20,7]), expected))

print(identical(constructBinaryTree([1], [1]), TreeNode(1)))

