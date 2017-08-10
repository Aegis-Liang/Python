class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert_my_answer(self, new_val):
        node = self.root
        while True:
            if new_val <= node.value:
                if node.left == None:
                    node_new = Node(new_val)
                    node.left = node_new
                    break
                else:
                    node = node.left
                    continue
            else:
                if node.right == None:
                    node_new = Node(new_val)
                    node.right = node_new
                    break
                else:
                    node = node.right
                    continue                    
                

    def search_my_answer(self, find_val):
        node = self.root
        while True:
            if node.value == find_val:
                return True
            elif node.value < find_val:
                if node.left == None:
                    return False
                node = node.left
                continue
            else:
                if node.right == None:
                    return False
                node = node.right
                continue

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False    

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)