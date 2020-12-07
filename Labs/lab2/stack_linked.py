class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # Link; Points to the next node object in the list


class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Linked List'''
    def __init__(self, capacity):
        '''Creates an empty stack with a capacity'''
        self.capacity = capacity
        self.head = None # starting Node
        self.num_items = 0
        self.previous = None

    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == 0

    def is_full(self):
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == self.capacity

    # The head attribute holds/links the entire list by storing the data attribute from each Node
    def push(self, item):
        '''If stack is not full, pushes item on stack.
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''
        if not self.is_full():
            self.num_items = self.num_items + 1
            next_Node = Node(item) # Every time push is called we instantiate a new Node object
            if (self.head):
                self.head = next_Node # Move head to top, i.e set to latest node
                self.head.next = self.previous # populates next node
                self.previous = next_Node
            else:
                self.previous = next_Node
                self.head = next_Node
        else:
            raise IndexError


    def pop(self): 
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''
        if not self.is_empty():
            self.num_items = self.num_items - 1
            save = self.previous.data
            self.previous = self.head.next
            self.head = self.head.next
            return save
        else:
            raise IndexError

    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if not self.is_empty():
            return self.head.data
        else:
            raise IndexError

    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        return self.num_items

#stack = Stack(5)
#stack.push(0)
#stack.push(1)
#stack.push(2)
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())

#'''
#stack = Stack(5)
#stack.push(0)
#stack.push(1)
#stack.push(2)
#stack.push(3)
#print(stack.peek())
#print(stack.pop())
#print(stack.pop())
#print(stack.is_full())
#'''