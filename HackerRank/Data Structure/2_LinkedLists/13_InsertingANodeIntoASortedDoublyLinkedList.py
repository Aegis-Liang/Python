"""
Given a reference to the head of a doubly-linked list and an integer, , create a new Node object having data value  and insert it into a sorted linked list.

Complete the Node* SortedInsert(Node* head, int data) method in the editor below. It has two parameters:
1.: A reference to the head of a doubly-linked list of Node objects.
2.: An integer denoting the value of the  field for the Node you must insert into the list.

The method must insert a new Node into the sorted (in ascending order) doubly-linked list whose data value is  without breaking any of the list's double links or causing it to become unsorted.

Note: Recall that an empty list (i.e., where ) and a list with one element are sorted lists. 



Input Format



Do not read any input from stdin. Hidden stub code reads in the following sequence of inputs and passes  and  to the method:

The first line contains an integer, , denoting the number of lists that will be checked. The  subsequent lines describe the elements to insert into each list over two lines:
1.The first line contains an integer, , denoting the number of elements that will be inserted into the list.
2.The second line contains  space-separated integers describing the respective data values that your code must insert into the list during each call to the method.



Output Format



Do not print anything to stdout. Your method must return a reference to the  of the same list that was passed to it as a parameter. The custom checker for this challenge checks the list to ensure it hasn't been modified other than to properly insert the new Node in the correct location.



Sample Input


1
3
2 5 4




Sample Output


2 4 5




Explanation


 1.We start out with an empty list. We insert a node with . The list becomes . We return .
2.The head of the previously modified list is passed to our method as an argument. We insert a node with . The list becomes . We return .
3.The head of the previously modified list is passed to our method as an argument. We insert a node with . The list becomes . We return .

Hidden stub code then prints the final list as a single line of space-separated integers.

"""


"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    new_head = head
    new_node = Node(data)

    node = head

    # No node in list
    if node == None: # node.prev == None and node.next == None, it's better use node == None, otherwise will occurs an error
        new_head = new_node
    else:
        # Insert to the head
        if node.prev == None and new_node.data <= node.data: # Why I used node.next.data?
            new_node.next = node
            new_head = new_node
        else:
            # Insert to non-head
            while(node != None):
                # Insert to tail
                if (node.next == None):
                    node.next = new_node
                    break
                # Get right place
                elif node.data < new_node.data and new_node.data <= node.next.data:
                    # No set prev could pass the test cases
                    new_node.next = node.next
                    node.next = new_node
                    break
                # Compare next
                else:
                    node = node.next
            return new_head

