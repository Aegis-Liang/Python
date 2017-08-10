
class Node:
    def __init__(self,data): 
        self.data = data  
        self.left = None  
        self.right = None 

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def topView(root):
    #Write your code here
    
    # We have to use stack to do the left traversal, otherwise the order is not correct
    node = root
    left_stack = []
    while (node.left != None):
        left_stack.append(node.left.data)
        node = node.left
    while (len(left_stack)>0):
        print left_stack[len(left_stack)-1],
        left_stack.pop()
        
    node = root
    if node != None:
        print node.data,
    
    node = root
    while (node.right != None):
        print node.right.data,
        node = node.right



"""
You are given a pointer to the root of a binary tree. Print the top view of the binary tree. 
You only have to complete the function. 
For example :

   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
Top View : 1 -> 2 -> 5 -> 6

Input Format

You are given a function,

void topView(node * root) {

}
Constraints

1 Nodes in the tree  500

Output Format

Print the values on a single line separated by space.

Sample Input

   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
Sample Output

1 2 5 6

Explanation

   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
From the top only nodes 1,2,5,6 will be visible.
"""

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)

Node1.left = Node2
Node2.left = Node3
Node1.right = Node4
Node4.right = Node5

topView(Node1)