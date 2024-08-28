from typing import List

class Node:
    def __init__(self, data=-1):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self, data=None):
        if not data:
            self.root = None
        else:
            self.root = Node(data)

    def insert(self, data):
        cur = self.root
        parent = cur
        while cur:
            parent = cur
            if data < cur.data:
                cur = cur.left
            else:
                cur = cur.right

        if data < parent.data:
            parent.left = Node(data)
        else:
            parent.right = Node(data)
        
    def traverse_preorder(self):
        def preorder(node):
            if not node:
                return
            
            print(node)
            preorder(node.left)
            preorder(node.right)
        
        preorder(self.root)

    ##################################
    ##  Tree Traversal Iteratively  ##
    ##################################
    def traverse_preorder_i(self):
        def preorder(node):
            if not node:
                return
            
            stack = []
            stack.append(node)
            while len(stack) > 0:
                cur = stack.pop()
                print(cur)
                if cur.right: stack.append(cur.right)
                if cur.left: stack.append(cur.left)

        preorder(self.root)
    
    def traverse_inorder_i(self):
        def inorder(node):
            if not node:
                return
            
            stack = []
            stack.append(node)
            seen = set()
            while len(stack) > 0:
                cur = stack.pop()

                # an internal node that has been traversed thru or a leaf node
                if cur.data in seen or (not cur.left and not cur.right):
                    print(cur)
                    continue

                seen.add(cur.data)
                # add nodes to stack in order right - mid - left so that when popped, 
                # things are in order left - mid - right
                if cur.right: stack.append(cur.right)
                stack.append(cur)
                if cur.left: stack.append(cur.left)
        
        inorder(self.root)

    def traverse_postorder_i(self):
        def postorder(node):
            if not node:
                return
            stack = []
            seen = set()
            stack.append(node)

            while len(stack) > 0:
                cur = stack[-1] # only pop if we've already printed it n hence dont need it again

                # an internal node that has been traversed thru or a leaf node
                if cur.data in seen or (not cur.left and not cur.right):
                    print(cur)
                    stack.pop()
                    continue
                
                seen.add(cur.data)
                if cur.right: stack.append(cur.right)
                if cur.left: stack.append(cur.left)

        postorder(self.root)

def constructBST(lst: List) -> BST:
    if not lst:
        return
    
    bst = BST(lst[0])
    i = 1
    while i < len(lst):
        bst.insert(lst[i])
        i += 1
    
    return bst

if __name__ == "__main__":
    lst = [22, 9, 34, 18, 3]
    bst = constructBST(lst)
    if bst:
        bst.traverse_inorder_i() # 3,9,18,22,34
        # bst.traverse_postorder_i() # 3,18,9,34,22

    lst = [6,8,2,4,1,3,9]
    bst = constructBST(lst)
    if bst:
        bst.traverse_inorder_i() # 1,2,3,4,6,8,9
        # bst.traverse_postorder_i() # 1,3,4,2,9,8,6