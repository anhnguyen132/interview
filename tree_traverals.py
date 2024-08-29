from typing import List, Optional

class Node:
    def __init__(self, data=-1):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
    def __rep__(self):
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
        
    # get node w min val and its parent (useful for del method)
    def get_min(self, u = None) -> tuple[Node, Node] | None:
        if not u:
            u = self.root

        if not u:
            return (None, None)    
        
        min_node = None
        parent = None
        while u:
            parent = min_node
            min_node = u
            u = u.left
        return (parent, min_node)
    
    # get node w max val and its parent (useful for del method)
    def get_max(self, u = None) -> tuple[Node, Node] | None:
        if not u:
            u = self.root
        if not u:
            return (None, None) 
        
        max_node = None
        parent = None
        while u:
            parent = max_node
            max_node = u
            u = u.right
        return (parent, max_node)

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

    def get_height(self) -> int:
        """
        height of a tree = length of the longest path from root to a leaf node
        For example:
            A tree that has only 1 node has height = 0
        """
        def height(u: Optional[Node]) -> int:
            # if u is None or is a leaf node
            if not u or (not u.left and not u.right):
                return 0
            return 1 + max(height(u.left), height(u.right))
        
        return height(self.root)
    ##################################
    ##  Tree Traversal Recursively  ##
    ##################################
    def traverse_preorder(self):
        def preorder(node):
            if not node:
                return ""
            return str(node.data) + " " + preorder(node.left) + preorder(node.right)
            
        return preorder(self.root)[:-1]

    def traverse_inorder(self):
        def inorder(node):
            if not node:
                return ""
            return inorder(node.left) + str(node.data) + " " + inorder(node.right)
            
        return inorder(self.root)[:-1]

    def traverse_postorder(self):
        def postorder(node):
            if not node:
                return ""
            return postorder(node.left) + postorder(node.right) + str(node.data) + " "
        
        return postorder(self.root)[:-1]

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
                s += str(cur.data) + " "
                if cur.right: stack.append(cur.right)
                if cur.left: stack.append(cur.left)
            return s[:-1]
        return preorder(self.root)
    
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

    def shift_node(self, parent: Optional[Node], old: Node, v: Node) -> None:
        """
        Make v the child of PARENT replacing the place of OLD node which is currently a child of PARENT
        If PARENT is None, then OLD is the root node. Set root to v.
        """
        if not parent: # old is root
            self.root = v
            return
        
        if old is parent.left:
            parent.left = v
        else: 
            parent.right = v

    def delete(self, data):
        """
        Delete node with value = data from BST
        Do nothing if data isn't in the tree
        """
        parent, u = self.search(data)
        if not u: # data isnt in the tree
            return
        
        # if u only has 1 child (i.e. only left or right subtree), then just shift that subtree up
        if not u.left:
            self.shift_node(parent, u, u.right)
        elif not u.right:
            self.shift_node(parent, u, u.left)
        else: # u has 2 children
            # v will be replacement for u
            # can also get max left subtree
            par, v = self.get_min(u.right) 

            # attach v to u's parent
            self.shift_node(parent, u, v)

            # move u's left subtree
            v.left = u.left # v must not have had a left child since its the min node in u's right subtree
            u.left = None

            # reattach u's right subtree if v is not u's right child
            if v != u.right: 
                par.left = v.right # v is par.left bc v is the min node in the subtree
                v.right = u.right
                u.right = None


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
    print("TEST 1")
    lst = [22, 9, 34, 18, 3]
    bst = constructBST(lst)
    if bst:
        print(bst.traverse_preorder() == "22 9 3 18 34")
        print(bst.traverse_inorder() == "3 9 18 22 34")
        print(bst.traverse_postorder() == "3 18 9 34 22")

        par, u = bst.get_min()
        print(f'{par.data == 9, u.data == 3}')
        par, u = bst.get_max()
        print(f'{par.data == 22, u.data == 34}')

        par, u = bst.search(9)
        print(f'{par.data == 22}, {u.data == 9}')

        par, u = bst.search(22) # root
        print(f'{par == None}, {u.data == 22}')

        par, u = bst.search(34)
        print(f'{par.data == 22}, {u.data == 34}')

        par, u = bst.search(18)
        print(f'{par.data == 9}, {u.data == 18}')

        print(bst.get_height() == 2)

        """
        delete test cases:
        0. data isn't in tree
        1. u has no children
        2. u has 1 child: left or right (2 cases)
        3. u has 2 children
            3.1 v is u's right child
            3.2 v isnt right child and has no right child
            3.3 v isnt right child and has a right child
        4. u is the root: 
            4.1 no children,
            4.2 1 child, 
            4.3 2 children:
                4.3.1 v is u's right child
                4.3.2 v isnt right child and has no right child
                4.3.3 v isnt right child and has a right child 
        """
        print("DELETE tests")
        # 0. data isn't in tree
        bst.delete(-1)
        print(bst.traverse_preorder() == "22 9 3 18 34")
        print(bst.traverse_inorder() == "3 9 18 22 34")
        print(bst.traverse_postorder() == "3 18 9 34 22")

        # 1. leaf node
        bst.delete(18)
        print(bst.traverse_preorder() == "22 9 3 34")
        print(bst.traverse_inorder() == "3 9 22 34")

        # 2. u has 1 child: left
        bst.delete(9)
        print(bst.traverse_preorder() == "22 3 34")
        print(bst.traverse_inorder() == "3 22 34")
        print(bst.get_height() == 1)

        # 4.3.1 u is the root w 2 children: v is u's right child
        bst.delete(22)
        print(bst.traverse_preorder() == "34 3")
        print(bst.traverse_inorder() == "3 34")

    print("TEST 2")
    lst = [6,8,2,4,1,3,9]
    bst = constructBST(lst)
    if bst:
        print(bst.traverse_preorder() == "6 2 1 4 3 8 9")
        print(bst.traverse_inorder() == "1 2 3 4 6 8 9")
        print(bst.traverse_postorder() == "1 3 4 2 9 8 6")

        par, u = bst.get_min()
        print(f'{par.data == 2, u.data == 1}')
        par, u = bst.get_max()
        print(f'{par.data == 8, u.data == 9}')

        par, u = bst.search(9)
        print(f'{par.data == 8}, {u.data == 9}')

        par, u = bst.search(1)
        print(f'{par.data == 2}, {u.data == 1}')

        par, u = bst.search(3)
        print(f'{par.data == 4}, {u.data == 3}')

        print(bst.get_height() == 3)
        
        print("DELETE tests")
        # 2. u has 1 child: right
        bst.delete(8)
        print(bst.traverse_preorder() == "6 2 1 4 3 9")
        print(bst.traverse_inorder() == "1 2 3 4 6 9")

        # 3.2 u has 2 children, v isnt u's right child and has no right child
        bst.delete(2)
        print(bst.traverse_preorder() == "6 3 1 4 9")
        print(bst.traverse_inorder() == "1 3 4 6 9")
        print(bst.traverse_postorder() == "1 4 3 9 6")

        # 3.1 u has 2 children, v is u's right child
        bst.delete(3)
        print(bst.traverse_preorder() == "6 4 1 9")
        print(bst.traverse_inorder() == "1 4 6 9")
        print(bst.traverse_postorder() == "1 4 9 6")

    print("TEST 3: root has only left branch")
    lst = [20,8,4,12,10,14] # root only has left child
    bst = constructBST(lst)
    if bst:
        print(bst.traverse_preorder() == "20 8 4 12 10 14")
        print(bst.traverse_inorder() == "4 8 10 12 14 20")
        print(bst.traverse_postorder() == "4 10 14 12 8 20")

        par, u = bst.get_min()
        print(f'{par.data == 8, u.data == 4}')
        par, u = bst.get_max() # u is root
        print(f'{par == None, u.data == 20}')

        par, u = bst.search(12)
        print(f'{par.data == 8}, {u.data == 12}')

        par, u = bst.search(20) # data in root
        print(f'{par == None}, {u.data == 20}')

        print(bst.get_height() == 3)

        print("DELETE tests")
        # 4.2 u is the root w 1 child: left
        bst.delete(20)
        print(bst.traverse_preorder() == "8 4 12 10 14")
        print(bst.traverse_inorder() == "4 8 10 12 14")
        print(bst.traverse_postorder() == "4 10 14 12 8")

        # 4.3.3 u is the root w 2 children, v isnt right child and has a right child
        bst.insert(11)
        bst.delete(8)
        print(bst.traverse_preorder() == "10 4 12 11 14")
        print(bst.traverse_inorder() == "4 10 11 12 14")
        print(bst.traverse_postorder() == "4 11 14 12 10")

        # 3.3 u has 2 children, v isnt right child and has a right child
        bst.insert(8)
        bst.insert(6)
        bst.insert(7)
        bst.insert(2)
        bst.delete(4)
        print(bst.traverse_preorder() == "10 6 2 8 7 12 11 14")
        print(bst.traverse_inorder() == "2 6 7 8 10 11 12 14")
        print(bst.traverse_postorder() == "2 7 8 6 11 14 12 10")
       

    print("TEST 4: tree has root only")
    lst = [16] # root only 
    bst = constructBST(lst)
    if bst:
        print(bst.traverse_preorder() == "16")
        print(bst.traverse_inorder() == "16")
        print(bst.traverse_postorder() == "16")

        par, u = bst.get_min()
        print(f'{par == None, u.data == 16}')
        par, u = bst.get_max()
        print(f'{par == None, u.data == 16}')

        par, u = bst.search(9) # not in tree
        print(f'{par == None}, {u == None}')

        par, u = bst.search(16)
        print(f'{par == None}, {u.data == 16}')

        print(bst.get_height() == 0)

        print("DELETE tests")
        bst.delete(16)
        print(bst.traverse_preorder() == "")
        print(bst.traverse_inorder() == "")
        print(bst.traverse_postorder() == "")