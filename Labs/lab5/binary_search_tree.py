from queue_array import Queue
class TreeNode:
    
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

        
class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

        
    def is_empty(self): # returns True if tree is empty, else False
        return self.root == None

    
    def search(self, key): # returns True if key is in a node of the tree, else False
        if self.is_empty():
            return False
        else:
            return self.search_helper(key, self.root)


    def search_helper(self, key, current_Node):
        if current_Node == None:
            return False
        if current_Node.key == key:
            return True
        elif key < current_Node.key: # search left subtree
            return self.search_helper(key, current_Node.left)
        else: # search right subtree
            return self.search_helper(key, current_Node.right)


    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        if self.is_empty():
            self.root = TreeNode(key, data) # if there is no root node create a TreeNode and set it to be the root node
        else:
            self.insert_helper(key, data, self.root)

            
    def insert_helper(self, key, data, current_Node):
        if key == current_Node.key: # replace data
            current_Node.data = data
        elif key < current_Node.key: # search left subtree
            if current_Node.left:
                self.insert_helper(key, data, current_Node.left)
            else:
                current_Node.left = TreeNode(key, data)
        else: # search right subtree
            if current_Node.right:
                self.insert_helper(key, data, current_Node.right)
            else:
                current_Node.right = TreeNode(key, data)


    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        else:
            return self.find_min_helper(self.root)

        
    def find_min_helper(self, current_Node):
        while current_Node.left != None:
            return self.find_min_helper(current_Node.left)
        return (current_Node.key, current_Node.data)

    
    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        else:
            return self.find_max_helper(self.root)

        
    def find_max_helper(self, current_Node):
        while current_Node.right != None:
            return self.find_max_helper(current_Node.right)
        return (current_Node.key, current_Node.data)

    
    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        # ascending order
        l = []
        if self.is_empty():
            return []
        return self.inorder_list_helper(self.root, l)

    
    def inorder_list_helper(self, current_Node, l):
        if current_Node == None:
            return
        self.inorder_list_helper(current_Node.left, l)
        l.append(current_Node.key)
        self.inorder_list_helper(current_Node.right, l)
        return l


    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        # good for making a copy of the tree
        l = []
        if self.is_empty():
            return []
        return self.preorder_list_helper(self.root, l)

    
    def preorder_list_helper(self, current_Node, l):
        if current_Node == None:
            return
        l.append(current_Node.key)
        self.preorder_list_helper(current_Node.left, l)
        self.preorder_list_helper(current_Node.right, l)
        return l

    
    def postorder(self):  # return Python list of BST keys representing pre-order traversal of BST
        # best for deleting the tree
        l = []
        if self.is_empty():
            return []
        return self.postorder_list_helper(self.root, l)

    
    def postorder_list_helper(self, current_Node, l):
        if current_Node == None:
            return
        self.postorder_list_helper(current_Node.left, l)
        self.postorder_list_helper(current_Node.right, l)
        l.append(current_Node.key)
        return l


    def tree_height(self):  # return the height of the tree
        # returns None if tree is empty
        if self.is_empty():
            return None
        return self.tree_height_helper(self.root) - 1

    
    def tree_height_helper(self, current_Node):
        if current_Node == None:
            return 0
        left_depth = self.tree_height_helper(current_Node.left) + 1
        right_depth = self.tree_height_helper(current_Node.right) + 1
        return max(left_depth, right_depth)


    def delete(self, key): # deletes node containing key
        # Will need to consider all cases 
        # This is the most difficult method - save it for last, so that
        # if you cannot get it to work, you can still get credit for 
        # the other methods
        # Returns True if the item was deleted, False otherwise
        if self.search(key):
            if self.root.left == None and self.root.right == None:
                self.root = None
                return True
            elif key == self.root.key: # delete root
                if self.root.left:
                    self.root.key = self.find_max_node(self.root.left)
                    self.delete_helper(self.root.key, self.root)
                else:
                    self.root.key = self.find_min_node(self.root.right)
                    self.delete_helper(self.root.key, self.root)
                return True
            else:
                self.delete_helper(key, self.root)
                return True
        else:
            return False
        
        
    def delete_helper(self, key, current_Node):
        if key <= current_Node.key and current_Node.left: # search left subtree
            if current_Node.left: # unneeded
                if current_Node.left.key == key:
                    # Then DELETE current_Node.left
                    if current_Node.left.left == None and current_Node.left.right == None: # leaf case
                        current_Node.left = None

                    elif current_Node.left.left and current_Node.left.right: # 2 child case
                        current_Node.left.key = self.find_max_node(self.root.left.left)
                        self.delete_helper(current_Node.left.key, current_Node.left)
                    elif current_Node.left.left and not current_Node.left.right: # single left child case
                        current_Node.left = current_Node.left.left
                    elif not current_Node.left.left and current_Node.left.right: # single right child case
                        current_Node.left = current_Node.left.right
                else:
                    return self.delete_helper(key, current_Node.left)
        else: # search right subtree
            if current_Node.right:
                if current_Node.right.key == key:
                    # delete it
                    if current_Node.right.left == None and current_Node.right.right == None: # leaf case
                        current_Node.right = None
                    elif current_Node.right.left and current_Node.right.right:
                        current_Node.right.key = self.find_max_node(self.root.right.left)
                        self.delete_helper(current_Node.right.key, current_Node.right)
                    elif current_Node.right.left and not current_Node.right.right:  # single left child case
                        current_Node.right = current_Node.right.left
                    elif not current_Node.right.left and current_Node.right.right:  # single right child case
                        current_Node.right = current_Node.right.right
                else:
                    return self.delete_helper(key, current_Node.right)

                
    def find_min_node(self, current_Node): # return min key
        while current_Node.left != None:
            return self.find_min_node(current_Node.left)
        return current_Node.key
    
    
    def find_max_node(self, current_Node): # return max key
        while current_Node.right != None:
            return self.find_max_node(current_Node.right)
        return current_Node.key

'''
tree = BinarySearchTree()
tree.insert('S', 69)
tree.insert('A', 69)
tree.insert('L', 69)
tree.insert('W', 69)
tree.insert('D', 69)
tree.insert('N', 69)
tree.insert('T', 69)
print(tree.search(12))
tree.delete(26)
print(tree.find_min())
print(tree.preorder_list())
'''
