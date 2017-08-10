"""
 Reverse a linked list
 head could be None as well for empty list
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

def print_list(head):
    node = head
    while node != None:
        print str(node.data)
        node = node.next
        

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
print_list(node1)
print_list(Reverse(node1))








