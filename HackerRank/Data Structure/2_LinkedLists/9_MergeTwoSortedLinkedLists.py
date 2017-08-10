
"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def MergeLists(headA, headB):
    headC = None
    nodeA = headA
    nodeB = headB

    while True:
        if nodeA == None and nodeB == None:
            break;
        elif nodeA == None:
            headC = Insert(headC, nodeB.data) # Make a new node and found the Insert() function use data -_-!!!
            nodeB = nodeB.next
        elif nodeB == None:
            new_node = Node()
            headC = Insert(headC, nodeA.data)
            nodeA = nodeA.next
        else:
            if nodeA.data <= nodeB.data:
                headC = Insert(headC, nodeA.data)
                nodeA = nodeA.next
            else:
                new_node = Node(nodeB.data)
                headC = Insert(headC, nodeB.data)
                nodeB = nodeB.next
    return headC

def Insert(head, data):  # Insert to tail
    new_node = Node(data)

    if head == None:
        head = new_node
    else:
        node = head    

        while node.next != None:
            node = node.next
        node.next = new_node
    return head


"""
This challenge is part of a tutorial track by MyCodeSchool

You’re given the pointer to the head nodes of two sorted linked lists. The data in both lists will be sorted in ascending order. Change the next pointers to obtain a single, merged linked list which also has data in ascending order. Either head pointer given may be null meaning that the corresponding list is empty.

Input Format 
 You have to complete the Node* MergeLists(Node* headA, Node* headB) method which takes two arguments - the heads of the two sorted linked lists to merge. You should NOT read any input from stdin/console.

Output Format 
 Change the next pointer of individual nodes so that nodes from both lists are merged into a single list. Then return the head of this merged list. Do NOT print anything to stdout/console.

Sample Input 
1 -> 3 -> 5 -> 6 -> NULL
2 -> 4 -> 7 -> NULL

15 -> NULL
12 -> NULL

NULL 
1 -> 2 -> NULL


Sample Output
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> NULL
12 -> 15 -> NULL
1 -> 2 -> NULL


Explanation 
 1. We merge elements in both list in sorted order and output. 
"""