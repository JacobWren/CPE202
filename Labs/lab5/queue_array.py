class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None]*capacity
        self.front = 0
        self.rear = 0
        self.num = 0


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        return self.rear == self.front


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        #return self.rear - self.front == self.capacity or (self.front - self.rear == 1 and self.rear != 0)
        return self.rear == self.capacity

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue
           If Queue is full when enqueue is attempted, raises IndexError'''
        if not self.is_full():
                self.num = self.num + 1
                self.items[self.rear] = item
                if self.num == self.capacity: # adding last item in capacity. THERE ARE NO open spaces
                    #self.rear = self.rear + 1
                    self.rear = self.capacity
                else:
                    if (self.rear + 1) % self.capacity == self.front: # we are full when rear is behind front
                        self.rear = self.capacity
                    else:
                        self.rear = (self.rear + 1) % self.capacity
                #self.rear = (self.rear + 1) % self.capacity
        else:
            raise IndexError


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if not self.is_empty():
            self.num = self.num - 1
            save = self.items[self.front]
            self.front = (self.front + 1) % self.capacity # move front index up 1
            if self.rear == self.capacity: # 'Loops' around array
                #self.rear = 0
                self.rear = self.front - 1
            return save
        else:
            raise IndexError


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num

'''
q = Queue(5)
q.enqueue(0)
q.enqueue(1)
q.dequeue()
q.dequeue()
print(q.size())
'''