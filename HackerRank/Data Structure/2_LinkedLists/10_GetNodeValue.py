

"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    headReverse = Reverse(head)
    return GetSpecificNode(headReverse, position).data

def GetSpecificNode(head, position):
    current_position = 0
    current_node = head

    while current_position < position:
        #print str(current_position) + " " + str(position - 1)
        #print str(current_node.data)
        current_node = current_node.next
        current_position += 1   
    return current_node

def Reverse(head):
    node = head
    # if we don't use a new head, the last node in reversed list is pointed to the first node in origin list
    # exp: for an 1->2->3 list, after the first node in reversed list inserted, the list become 1->1->2->3   
    new_head = None #Node()
    while node != None:
        new_head = Insert(new_head, node.data) # Forget to assign the latest value to head
        node = node.next
    return new_head



def Insert(head, data):    # Insert to head
    new_node = Node(data)

    if head == None: # or head.data == None: # if we don't initialize the new_head with Node(), we don't have to check its data
        head = new_node
    else:
        new_node.next = head
        head = new_node
    return head      

"""
This challenge is part of a tutorial track by MyCodeSchool

You’re given the pointer to the head node of a linked list and a specific position. Counting backwards from the tail node of the linked list, get the value of the node at the given position. A position of 0 corresponds to the tail, 1 corresponds to the node before the tail and so on.

Input Format 
 You have to complete the int GetNode(Node* head, int positionFromTail) method which takes two arguments - the head of the linked list and the position of the node from the tail. positionFromTail will be at least 0 and less than the number of nodes in the list. You should NOT read any input from stdin/console. 

Constraints 
 Position will be a valid element in linked list. 

Output Format 
 Find the node at the given position counting backwards from the tail. Then return the data contained in this node. Do NOT print anything to stdout/console.

Sample Input 
1 -> 3 -> 5 -> 6 -> NULL, positionFromTail = 0
1 -> 3 -> 5 -> 6 -> NULL, positionFromTail = 2


Sample Output
6
3
"""