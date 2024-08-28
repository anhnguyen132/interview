from typing import List, Optional

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
        if not self.root:
            self.root = Node(data)

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
        
    # get node w min val
    def get_min(self) -> Optional[Node]:
        cur = self.root
        min_node = cur
        while cur:
            min_node = cur
            cur = cur.left
        return min_node
    
    # get node w max val 
    def get_max(self) -> Optional[Node]:
        cur = self.root
        max_node = cur
        while cur:
            max_node = cur
            cur = cur.right
        return max_node

    # returns node containing data and its parent node (parent is None if data is in the root node)
    # if there is no node containing such data, returns None
    def search(self, data) -> tuple[Node, Node] | None:
        cur = self.root
        parent = None
        while cur:
            if cur.data == data:
                return (parent, cur)
            
            parent = cur
            if data < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        return (None, None)

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

    def shift_node(self, parent: Node, v: Node) -> None:
        pass
    def delete(self, data):
        """
        Delete node with value = data from BST
        Do nothing if data isn't in the tree
        """
        parent, u = self.search(data)
        if not u: # data isnt in the tree
            return
        
        # if u only has 1 child (i.e. only left or right subtree), then just shift that subtree up
        # if not u.left:

    
    


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
        print(bst.get_min().data == 3) # 3
        print(bst.get_max().data == 34) # 34

        par, u = bst.search(9)
        print(f'{par.data == 22}, {u.data == 9}')

        par, u = bst.search(22) # root
        print(f'{par == None}, {u.data == 22}')

        par, u = bst.search(34)
        print(f'{par.data == 22}, {u.data == 34}')

        par, u = bst.search(18)
        print(f'{par.data == 9}, {u.data == 18}')

        # bst.traverse_inorder_i() # 3,9,18,22,34
        # bst.traverse_postorder_i() # 3,18,9,34,22

    lst = [6,8,2,4,1,3,9]
    bst = constructBST(lst)
    if bst:
        print(bst.get_min().data == 1) # 1
        print(bst.get_max().data == 9) # 9

        par, u = bst.search(9)
        print(f'{par.data == 8}, {u.data == 9}')

        par, u = bst.search(1)
        print(f'{par.data == 2}, {u.data == 1}')

        par, u = bst.search(3)
        print(f'{par.data == 4}, {u.data == 3}')

        # bst.traverse_inorder_i() # 1,2,3,4,6,8,9
        # bst.traverse_postorder_i() # 1,3,4,2,9,8,6

    lst = [20,8,4,12,10,14] # root only has left child
    bst = constructBST(lst)
    if bst:
        print(bst.get_min().data == 4) # 4
        print(bst.get_max().data == 20) # 20

        par, u = bst.search(12)
        print(f'{par.data == 8}, {u.data == 12}')

        par, u = bst.search(20) # data in root
        print(f'{par == None}, {u.data == 20}')

    lst = [16] # root only 
    bst = constructBST(lst)
    if bst:
        print(bst.get_min().data == 16) # 16
        print(bst.get_max().data == 16) # 16

        par, u = bst.search(9) # not in tree
        print(f'{par == None}, {u == None}')

        par, u = bst.search(16)
        print(f'{par == None}, {u.data == 16}')