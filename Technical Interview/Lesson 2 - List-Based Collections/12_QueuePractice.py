"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.insert(0, new_element)
        #new_element.next = self.head
        #self.head = new_element

    def peek(self):
        #return self.head 
        return self.storage[len(self.storage)-1]

    def dequeue(self):
        #current = self.head
        #while current != None:
            #current = current.next
        #return current
        return self.storage.pop(len(self.storage)-1)
    
    def enqueue_Offical_Answer(self, new_element):
        self.storage.append(new_element)

    def peek_Offical_Answer(self):
        return self.storage[0]

    def dequeue_Offical_Answer(self):
        return self.storage.pop(0)    
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print q.peek()

# Test dequeue
# Should be 1
print q.dequeue()

# Test enqueue
q.enqueue(4)
# Should be 2
print q.dequeue()
# Should be 3
print q.dequeue()
# Should be 4
print q.dequeue()
q.enqueue(5)
# Should be 5
print q.peek()