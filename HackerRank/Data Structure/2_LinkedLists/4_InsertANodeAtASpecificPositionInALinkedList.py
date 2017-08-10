"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    new_node = Node(data)

    if position == 0:
        if head == None:
            head = new_node
        else:
            new_node.next = head
            head = new_node
    else:
        current_position = 0
        node = head
        while current_position < position-1 and node.next != None: # Important: -1, otherwise the order is not right
            node = node.next                                       # and node.next != None : could pass the test case even without it
            current_position += 1
        new_node.next = node.next
        node.next = new_node
    return head


l = None  # Initial with None, the condition ""head == None" is not right if we initial it by l = Node(), head will be a node with data and next are None, but it self is not None.
l = InsertNth(l, 3, 0)
l = InsertNth(l, 5, 1)
l = InsertNth(l, 4, 2)
l = InsertNth(l, 2, 3)
l = InsertNth(l, 10, 1)

def print_list(head):
    node = head
    while node != None:
        print str(node.data)
        node = node.next
        
print_list(l)


"""This challenge is part of a tutorial track by MyCodeSchool and is accompanied by a video lesson.

You’re given the pointer to the head node of a linked list, an integer to add to the list and the position at which the integer must be inserted. Create a new node with the given integer, insert this node at the desired position and return the head node. A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.

Input Format 
    You have to complete the Node* Insert(Node* head, int data, int position) method which takes three arguments - the head of the linked list, the integer to insert and the position at which the integer must be inserted. You should NOT read any input from stdin/console. position will always be between 0 and the number of the elements in the list (inclusive).

Output Format 
    Insert the new node at the desired position and return the head of the updated linked list. Do NOT print anything to stdout/console.

Sample Input 

NULL, data = 3, position = 0 
    3 --> NULL, data = 4, position = 0

Sample Output 
3 --> NULL
4 --> 3 --> NULL


Explanation 
    1. we have an empty list and position 0. 3 becomes head. 
    2. 4 is added to position 0, hence 4 becomes head. 

Note 
    For the purpose of evaluation the list has been initialised with a node with data=2. Ignore it, this is done to avoid printing empty lists while comparing output. 
"""