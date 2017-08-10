
class Node:
    def __init__(self,info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    return inOrder(root, -1, 0)

def inOrder(root, currentHeight, maxHeight):
    #Write your code here
    if root != None:
        currentHeight += 1
        maxHeightLeft = inOrder(root.left, currentHeight, max(maxHeight, currentHeight))
        #print root.data,
        maxHeightRight = inOrder(root.right, currentHeight, max(maxHeight, currentHeight))
        return max(maxHeightLeft, maxHeightRight)
    else:
        return maxHeight    

"""
*** Maybe it's not perefect, but one hit to pass! Yeah! ^_^!!! ***
"""    
    
    
tree = BinarySearchTree()
t = int(raw_input())

for _ in xrange(t):
    x = int(raw_input())
    tree.create(x)

print height(tree.root)




"""
The height of a binary tree is the number of edges between the tree's root and its furthest leaf. This means that a tree containing a single node has a height of .

Complete the getHeight function provided in your editor so that it returns the height of a binary tree. This function has a parameter, , which is a pointer to the root node of a binary tree.

Input Format

You do not need to read any input from stdin. Our grader will pass the root node of a binary tree to your getHeight function.

Output Format

Your function should return a single integer denoting the height of the binary tree.

Sample Input

BST.png

Note: A binary search tree is a binary tree in which the value of each parent node's left child is less than the value the parent node, and the value of the parent node is less than the value of its right child.

Sample Output

3
Explanation

The longest root-to-leaf path is shown below:

Longest RTL.png

There are  nodes in this path that are connected by  edges, meaning our binary tree's . Thus, we print  as our answer.
"""