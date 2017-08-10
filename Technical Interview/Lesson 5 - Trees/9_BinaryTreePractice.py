class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        str = self.preorder_print(self.root, "")
        return str[:len(str)-1]

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start.value == find_val:
            return True
        
        if start.left != None:
            result_left = self.preorder_search(start.left, find_val)
        else:
            result_left = False
            
        if start.right != None:
            result_right = self.preorder_search(start.right, find_val)
        else:
            result_right = False        
        
        return result_left or result_right
            

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        str_left = ""
        str_right = ""
        
        str_current = str(start.value)
        if start.left != None:
            str_left = self.preorder_print(start.left, "") 
        if start.right != None:
            str_right = self.preorder_print(start.right, "")
            
        
        traversal = str_current + "-" + str_left + str_right
        return traversal 
    
    def search_offical_answer(self, find_val):
        return self.preorder_search(tree.root, find_val)

    def print_tree_offical_answer(self):
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search_offical_answer(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print_offical_answer(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal    


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()