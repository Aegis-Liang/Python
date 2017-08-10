"""
 Insert Node at the begining of a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Insert(head, data):
    new_node = Node(data)

    if head == None:
        head = new_node
    else:
        new_node.next = head
        head = new_node
    return head

"""
This challenge is part of a tutorial track by MyCodeSchool and is accompanied by a video lesson. 

You’re given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with the given integer, insert this node at the head of the linked list and return the new head node. The head pointer given may be null meaning that the initial list is empty.

Input Format 
 You have to complete the Node* Insert(Node* head, int data) method which takes two arguments - the head of the linked list and the integer to insert. You should NOT read any input from stdin/console.

Output Format 
 Insert the new node at the head and return the head of the updated linked list. Do NOT print anything to stdout/console.

Sample Input

NULL , data = 1 
 1 --> NULL , data = 2

Sample Output 
1 --> NULL
2 --> 1 --> NULL


Explanation 
 1. We have an empty list, on inserting 1, 1 becomes new head. 
 2. We have a list with 1 as head, on inserting 2, 2 becomes the new head. 

"""