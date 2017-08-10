
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):
   #Enter you code here.
    node = r
    
    if r == None:    # Forget to handle the r == None case, it's OK to just return new node.
        return Node(val)
    
    while True:
        if val <= node.data:
            if node.left == None:
                node.left = Node(val)
                break
            else:
                node = node.left
        else:
            if node.right == None:
                node.right = Node(val)
                break
            else:
                node = node.right
    return r    # Forget to return r



"""
You are given a pointer to the root of a binary search tree and a value to be inserted into the tree. Insert this value into its appropriate position in the binary search tree and return the root of the updated binary tree. You just have to complete the function.

Input Format

You are given a function,

node * insert (node * root ,int value) {

}
node is defined as :

struct node
{
int data;
node * left;
node * right;
}node;
Constraints

No. of nodes in the tree  500
Output Format

Return the root of the binary search tree after inserting the value into the tree.

Sample Input

        4
       / \
      2   7
     / \
    1   3
The value to be inserted is 6.

Sample Output

         4
       /   \
      2     7
     / \   /
    1   3 6
"""