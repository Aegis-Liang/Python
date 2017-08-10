"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def Reverse(head):
    node = head
    new_head = None
    
    if node == None:
        return new_head
    
    while node != None:
        new_head = Insert(new_head, node.data)
        node = node.next
     
    return new_head

    
def Insert(head, data):
    new_head = head
    new_node = Node(data)

    node = head

    # No node in list
    if node == None:
        new_head = new_node
    else:
        # Insert to the head
        new_node.next = node
        new_head = new_node
        
        node.prev =  new_node
    return new_head
    

"""
*** One hit to pass! Yeah! ^_^!!! ***
"""









"""
This challenge is part of a tutorial track by MyCodeSchool

You’re given the pointer to the head node of a doubly linked list. Reverse the order of the nodes in the list. The head node might be NULL to indicate that the list is empty.

Input Format 
 You have to complete the Node* Reverse(Node* head) method which takes one argument - the head of the doubly linked list. You should NOT read any input from stdin/console.

Output Format 
 Change the next and prev pointers of all the nodes so that the direction of the list is reversed. Then return the head node of the reversed list. Do NOT print anything to stdout/console.

Sample Input 

NULL 
 NULL <-- 2 <--> 4 <--> 6 --> NULL 

Sample Output
NULL
NULL <-- 6 <--> 4 <--> 2 --> NULL


Explanation 
 1. Empty list, so nothing to do. 
 2. 2,4,6 become 6,4,2 o reversing in the given doubly linked list. 

"""