
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def lca(node , v1 , v2):
    if node == None:   # It's neccesary!!!
        return node
    
    current_node = node
    while (current_node.data > v1 and current_node.data > v2) or (current_node.data < v2 and current_node.data < v1): # Use > < not >= <=
        if (current_node.data > v1 and current_node.data > v2):
            current_node = current_node.left
        if (current_node.data < v1 and current_node.data < v2):
            current_node = current_node.right
    return current_node

# geeksforgeeks solution:
# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def lca_geeksforgeeks(root, n1, n2):

    # Base Case
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right 
    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)

        
        
class Node:
    def __init__(self,data): 
        self.data = data  
        self.left = None  
        self.right = None 
        

#class LinkListNode(object):
    #def __init__(self, data=None, next_node=None):
        #self.data = data
        #self.next = next_node
    
#def lca(root , v1 , v2):
    ##Enter your code here
    #trace_v1 = trace(root, v1)
    #trace_v2 = trace(root, v2)
    
    #node_v1 = trace_v1
    #node_v2 = trace_v2
    
    #if node_v1 != None and node_v2 != None:
        #while node_v1.next.data == node_v2.next.data: 
            #node_v1 = node_v1.next
            #node_v2 = node_v2.next
        ## return node_v1    # return the pointer as the problem said, finally found this is a new pointer, not the root of the tree anymore

    #node = root
    
    #if node.data == node_v1.data:
        #return node
    #else:
        #while node != None:
            #if node_v1.data == node.data:
                #return node
            #elif node_v1.data < node.data:
                #node = node.left
            #else:
                #node = node.right
        #return None

#def trace(root, data):    # Has a defect that if we cannot find the node, we still have a trace
    #current_node = root
    #new_head = None
    
    #if root == None:
        #return new_head
    
    #while current_node != None:
        #new_head = LinkListInsert(new_head, current_node.data)  # mistake: use data not current_node.data
        
        #if current_node.data == data:
            #return new_head
        #elif data < current_node.data:    # should be "data < current_node.data" not "current_node.data < data"
            #current_node = current_node.left
        #else:
            #current_node = current_node.right
    
    #return new_head

#def LinkListInsert(head, data):
    #new_node = LinkListNode(data)    # Insert is Linked List function

    #if head == None:
        #head = new_node
    #else:
        #node = head    

        #while node.next != None:
            #node = node.next
        #node.next = new_node
    #return head


#def print_list(head):
    #node = head
    #while node != None:
        #print str(node.data)
        #node = node.next
        
        
#Node1 = Node(1)
#Node2 = Node(2)
#Node3 = Node(3)
#Node4 = Node(4)
#Node6 = Node(6)
#Node7 = Node(7)

#Node4.left = Node2
#Node2.left = Node1
#Node2.right = Node3
#Node4.right = Node7
#Node7.left = Node6

# 8 4 9 1 2 3 6 5

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
Node6 = Node(6)
Node8 = Node(8)
Node9 = Node(9)

Node8.left = Node4
Node8.right = Node9

Node4.left = Node1
Node4.right = Node6

Node1.right = Node2

Node2.right = Node3

Node6.left = Node5






#print_list(trace(Node3, 1))
#print_list(trace(Node3, 5))
print(lca(Node8, 1, 2).data)
        

# Even pass, but the code is not good!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        



"""
You are given pointer to the root of the binary search tree and two values  and . You need to return the lowest common ancestor (LCA) of  and  in the binary search tree. You only need to complete the function.

Input Format

You are given a function,

node * lca (node * root ,int v1,int v2) {

}
It is guaranteed that v1 and v2 are present in the tree.

Node is defined as :

struct node
{
int data;
node * left;
node * right;
}node;
Output Format

Return the LCA of  and .

Sample Input

         4
       /   \
      2     7
     / \   /
    1   3 6
 and .

Sample Output

LCA of  and  is  (which is the root). 
Return a pointer to the root in this case."""