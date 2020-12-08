class Node:
    
    def __init__(self,item):
        self.item = item
        self.next = None  # Link; Points to the next node object in the list

        
class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.head = None # starting Node
        self.num_items = 0
        self.previous = None


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        
        return self.num_items == 0

    
    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        
        return self.num_items == self.capacity

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        
        if not self.is_full():
            self.num_items = self.num_items + 1
            next_Node = Node(item)  # Every time enqueue is called we instantiate a new Node object
            if (self.head): # first time we enqueue head is None
                # temp is a node object
                temp = self.previous # disappears when new call to enqueue
                temp.next = next_Node # This 'appends' to head. The bottom rung on head is temp.
                self.previous = next_Node # after the second enqueue previous will only hold 1 (the previous) node
            else: # Come here on first enqueue
                self.head = next_Node
                self.previous = next_Node
        else:
            raise IndexError


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        
        if not self.is_empty():
            self.num_items = self.num_items - 1
            save = self.head.item
            self.head = self.head.next # 'shrinks' head
            return save
        else:
            raise IndexError


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        
        return self.num_items

'''
q = Queue(5)
q.enqueue(0)
q.enqueue(1)
print(q.dequeue())
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())
'''
