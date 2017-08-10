
"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

""" It's wrong because I judge the equality by value not reference, and also because the Reverse() function will copy the list in another place
def FindMergeNode(headA, headB):
    headRevA = Reverse(headA)
    headRevB = Reverse(headB)
    nodeRevA = headRevA
    nodeRevB = headRevB
    
    while True:
        if nodeRevA.next != nodeRevB.next:
            return nodeRevA.data
        else:
            nodeRevA = nodeRevA.next
            nodeRevB = nodeRevB.next


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
  
def FindMergeNode(headA, headB):
    nodeA = headA
    nodeB = headB
    
    while(nodeA != nodeB):
        if nodeA == None:
            nodeA = headB
            nodeB = nodeB.next
        elif nodeB == None:
            nodeB = headA
            nodeA = nodeA.next
        else:
            nodeA = nodeA.next
            nodeB = nodeB.next
    return nodeA.data

"""offical answer:To calculate the merge point, first calculate the difference in the sizes of the linked lists. Move the pointer of the smaller linked list by this difference. Increment both pointers till you reach the merge point."""


"""
A linked list is said to contain a cycle if any node is visited more than once while traversing the list. 

Complete the function provided for you in your editor. It has one parameter: a pointer to a Node object named  that points to the head of a linked list. Your function must return a boolean denoting whether or not there is a cycle in the list. If there is a cycle, return true; otherwise, return false.

Note: If the list is empty,  will be null.



Input Format



Our hidden code checker passes the appropriate argument to your function. You are not responsible for reading any input from stdin.



Constraints


 •



Output Format



If the list contains a cycle, your function must return true. If the list does not contain a cycle, it must return false. The binary integer corresponding to the boolean value returned by your function is printed to stdout by our hidden code checker.



Sample Input



The following linked lists are passed as arguments to your function: 

Sample Inputs



Sample Output


0
1




Explanation


 1.The first list has no cycle, so we return false and the hidden code checker prints  to stdout.
2.The second list has a cycle, so we return true and the hidden code checker prints  to stdout.

"""