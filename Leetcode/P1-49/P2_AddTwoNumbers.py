"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        moveNode = ListNode(None)
        l3 = moveNode
        
        add1 = False
        while True:
            if l1 != None and l2 != None:
                node = ListNode(self.addInABit(l1.val, l2.val, add1))
                moveNode.next = node
                moveNode = moveNode.next
                
                add1 = (True if l1.val + l2.val + (1 if add1 else 0) >= 10 else False)    # miss "(1 if add1 else 0)"
                l1 = l1.next
                l2 = l2.next
            elif l1 != None and l2 == None:
                node = ListNode(self.addInABit(l1.val, 0, add1))
                moveNode.next = node
                moveNode = moveNode.next
            
                add1 = (True if l1.val + (1 if add1 else 0) >= 10 else False)     # miss this line
                l1 = l1.next            
            elif l1 == None and l2 != None:
                node = ListNode(self.addInABit(0, l2.val, add1))
                moveNode.next = node
                moveNode = moveNode.next
            
                add1 = (True if (1 if add1 else 0) + l2.val >= 10 else False)     # miss this line
                l2 = l2.next
            else:
                if add1:
                    node = ListNode(1)
                    moveNode.next = node
                    moveNode = moveNode.next      
                break
        l3 = l3.next    # Because the first node is None in initialzation, I have to move this node one step forward, cannot come up with a better way.
        return l3
                
        
    def addInABit(self, a, b, add1=False):
        if add1:
            return (a + b + 1) % 10    # forget to mod 10 so that sometimes a 10 value is in a bit
        else:
            return (a + b) % 10        # forget to mod 10 so that sometimes a 10 value is in a bit
        
        
    """ other's java solution:
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummyHead = new ListNode(0);
    ListNode p = l1, q = l2, curr = dummyHead;
    int carry = 0;
    while (p != null || q != null) {
        int x = (p != null) ? p.val : 0;           # more clean than my switch solution, I have thought about it, but don't know why I have given up,
        int y = (q != null) ? q.val : 0;           # actually it's not only clean, but also have a cool manipulation.
        int sum = carry + x + y;
        carry = sum / 10;                          # it's called carry, not add1 ^_^!!!
        curr.next = new ListNode(sum % 10);
        curr = curr.next;
        if (p != null) p = p.next;
        if (q != null) q = q.next;
    }
    if (carry > 0) {
        curr.next = new ListNode(carry);
    }
    return dummyHead.next;                          # same as my solution here
}
    """
  
if __name__ == "__main__":      
    ln1 = ListNode(3)
    ln2 = ListNode(7)
    #ln3 = ListNode(2)
    
    ln1.next = ln2
    #ln2.next = ln3
    
    l1 = ln1
    
    
    ln4 = ListNode(9)
    ln5 = ListNode(2)
    #ln6 = ListNode(5)
    
    ln4.next = ln5
    #ln5.next = ln6
    
    l2 = ln4
    
    print Solution().addTwoNumbers(l1, l2).val

        

        
