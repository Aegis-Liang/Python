


"""
 Compare two linked list
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


def CompareLists(headA, headB):
    nodeA = headA
    nodeB = headB
    if (nodeA == None) and (nodeB == None):
        return 1
    else:
        while(True): 
            if nodeA == None and nodeB == None: #(nodeA == None and nodeB == None) is paradox with (nodeA != None and nodeB != None) in while loop, never true here
                return 1
            elif nodeA != None and nodeB != None:
                if nodeA.data != nodeB.data:
                    return 0
                else:
                    nodeA = nodeA.next
                    nodeB = nodeB.next                
            else:
                return 0


"""
This challenge is part of a tutorial track by MyCodeSchool

You’re given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to check if they are equal. The lists are equal only if they have the same number of nodes and corresponding nodes contain the same data. Either head pointer given may be null meaning that the corresponding list is empty.

Input Format 
 You have to complete the int CompareLists(Node* headA, Node* headB) method which takes two arguments - the heads of the two linked lists to compare. You should NOT read any input from stdin/console.

Output Format 
 Compare the two linked lists and return 1 if the lists are equal. Otherwise, return 0. Do NOT print anything to stdout/console.

Sample Input 

NULL, 1 --> NULL 
 1 --> 2 --> NULL, 1 --> 2 --> NULL

Sample Output
0
1


Explanation 
 1. We compare an empty list with a list containing 1. They don't match, hence return 0. 
 2. We have 2 similar lists. Hence return 1.
"""


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

print str(CompareLists(node1, node1))




