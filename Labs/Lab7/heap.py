class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.cap = capacity
        self.heap_List = [None] * (self.cap + 1)
        self.size = 0

    def enqueue(self, item):
        """inserts "item" into the heap, returns true if successful, false if there is no room in the heap"""
        if self.size < self.cap:
            self.heap_List.insert(self.size + 1, item)
            self.size = self.size + 1
            self.perc_up(self.size)
            return True
        else:
            return False


    def peek(self):
        """returns max without changing the heap, returns None if the heap is empty"""
        return self.heap_List[1]


    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty"""
        if self.size == 0:
            return None
        else:
            hold_max = self.heap_List[1]
            self.heap_List[1] = self.heap_List[self.size]
            self.size = self.size - 1
            self.heap_List.pop()
            self.perc_down(1)
            return hold_max

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        return self.heap_List[1:self.size + 1]


    def build_heap(self, alist):
        """Builds a heap from the items in alist and builds a heap using the bottom up method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased"""
        if self.cap < len(alist):
            self.cap = len(alist)
            self.size = 0
        if alist == []:
            self.heap_List = [None] * self.cap
            self.size = 0
        elif len(alist) == 1:
            self.heap_List = [None] * self.cap
            self.heap_List[1] = alist[0]
            self.size = 1
        else:
            self.size = len(alist)
            i = len(alist) // 2
            #p = (len(alist)) // 2
            self.heap_List = [None] + alist[:]

            while (i > 0):
                self.perc_down(i)
                i += -1
            '''
            if p % 2 == 0:
                for i in range(p, p + 2):
                    self.perc_down(i)
            else:
                for i in range(p, p - 2, -1):
                    self.perc_down(i)
            '''
    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        #return self.heap_List[1] == None
        return self.size == 0

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        return self.size == self.cap
        
    def capacity(self):
        """this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return self.cap
    
    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.size

    '''
    ##stopped##
    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while (i * 2) <= self.size: # while it is not a leaf, i.e., has a left child at least
            #if i == 0:
            if i == 1:
                #break
                #if self.size > 3:
                    #i = 2
                #else:
                    #break
                break
            if (i * 2) + 1 <= self.size:
                max_child = max(self.heap_List[i * 2], self.heap_List[(i * 2) + 1])
            else:
                max_child = self.heap_List[i * 2]
            if max_child > self.heap_List[i]:
                if max_child == self.heap_List[i * 2]:
                    self.heap_List[i], self.heap_List[i * 2] = self.heap_List[i * 2], self.heap_List[i]
                    if i * 4 <= self.size:
                        i = i * 2
                    else:
                        i -= 1
                    #if i * 2 < self.size:
                        #i = i * 2
                    #else:
                        #i = i // 2
        
                else:
                    self.heap_List[i], self.heap_List[(i * 2) + 1] = self.heap_List[(i * 2) + 1], self.heap_List[i]
                    #i = (i * 2) + 1
                    #if i % 2 != 0:
                    #if (i * 2) + 1 < self.size:
                        #i = (i * 2) + 1
                    #else:
                        #i = i // 2
                    if i * 4 <= self.size:
                        i = i * 2
                    else:
                        i -= 1

            else:
                #if i % 2 == 0:
                    #i = i // 2
                #else:
                    #return
                if i * 4 <= self.size:
                    i = i * 2
                else:
                    i -= 1
        '''

    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        if (i * 2) + 1 <= self.size:
            max_child = max(self.heap_List[i * 2], self.heap_List[(i * 2) + 1])
        elif i * 2 <= self.size:
            max_child = self.heap_List[i * 2]
        else:
            return
        if max_child > self.heap_List[i]:
            if max_child == self.heap_List[i * 2]:
                self.heap_List[i], self.heap_List[i * 2] = self.heap_List[i * 2], self.heap_List[i]
                if i == 1:
                    self.perc_down(i * 2)
                if i * 4 <= self.size:
                    i = i * 2
                    self.perc_down(i)
            else:
                self.heap_List[i], self.heap_List[(i * 2) + 1] = self.heap_List[(i * 2) + 1], self.heap_List[i]
                if i == 1:
                    self.perc_down((i * 2) + 1)
                if i * 4 <= self.size:
                    i = (i * 2) + 1
                    self.perc_down(i)
        else:
            i -= 1





    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        if i <= 1:
            return
        if self.size >= 2:
            while self.heap_List[i] > self.heap_List[i // 2]:
                self.heap_List[i], self.heap_List[i // 2] = self.heap_List[i // 2], self.heap_List[i]
                i = i // 2
                if i == 1:
                    break


    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order"""
        self.heap_List = [None] * self.cap
        self.build_heap(alist)
        alist.sort()
        return alist


'''
heap = MaxHeap(20)
#15, 10, 8, 6, 7, 5, 3, 1, 2, 4
heap.build_heap([4,2,3,5,6,8,7,10,15,1])
print(heap.contents())
#[7,7,7,7,7,7,7,1]
'''

heap = MaxHeap(20)
#heap.build_heap([10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2])
heap.build_heap([50, 44, 47, 43, 41, 39, 36, 35, 38])
heap.enqueue(42)
print(heap.contents())
#[7,7,7,7,7,7,7,1]