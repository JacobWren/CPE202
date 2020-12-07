import copy
class Node:
    '''Node for use with doubly-linked list'''
    
    def __init__(self, item):
        self.item = item
        self.next = None # link to next node
        self.prev = None # link to previous node

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           Do not have an attribute to keep track of size'''
        
        self.sentinel = Node(None) # dummy node that plays the role of both the head and the tail!
        # It does not contain data
        self.sentinel.next = self.sentinel # The sentinel points to itself as the list is a loop
        self.sentinel.prev = self.sentinel

        
    def is_empty(self):
        '''Returns back True if OrderedList is empty
            MUST have O(1) performance'''
        return self.sentinel.next == self.sentinel

    
    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list)
           If the item is already in the list, do not add it again 
           MUST have O(n) average-case performance'''
        
        new_node = Node(item)
        if self.is_empty(): # adds first node
            new_node.prev = self.sentinel
            new_node.next = self.sentinel

            self.sentinel.next = new_node
            new_node.next.prev = new_node
        else:
            # fix new node links before you fix sentinel node links or you will loose information!
            # Add new node to start
            if self.sentinel.next.item > new_node.item:
                new_node.prev = self.sentinel
                new_node.next = self.sentinel.next # 'self.sentinel.next' was pointing to first node
                self.sentinel.next = new_node # 'self.sentinel.next' points to first node
                new_node.next.prev = new_node # fix 'previous link' of previous first node to point to new node
            else:
                current_node = self.sentinel.next
                while current_node.next != self.sentinel:
                    if current_node.item == new_node.item:
                        return
                    if current_node.next.item > new_node.item: # Then insert after current node!
                        new_node.prev = current_node
                        new_node.next = current_node.next

                        current_node.next = new_node
                        new_node.next.prev = new_node
                        return # don't want to run any of the code below if this if statement is executed!
                    current_node = current_node.next

                # Place new node at the end of the list. New node is the max node.
                if current_node.item == new_node.item:
                    return
                last_node = self.sentinel.prev
                # new node links
                new_node.prev = last_node
                new_node.next = last_node.next
                last_node.next = new_node
                new_node.next.prev = new_node


    def remove(self, item):
        '''Removes an item from OrderedList. If item is removed (was in the list) returns True
           If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        
        current_node = self.sentinel.next
        if self.is_empty():
            return False

        # for list with 1 node!
        if current_node.next == self.sentinel and current_node.prev == self.sentinel and current_node.item == item:
            self.sentinel.next = self.sentinel # back to 'base case' (empty list/default)
            self.sentinel.prev = self.sentinel
            return True
        if current_node.next == self.sentinel and current_node.prev == self.sentinel and current_node.item != item:
            return False
        # for list with more than 1 node
        while current_node.next != self.sentinel:
            if current_node.item == item: # Then remove current node
                # skips links over current node
                current_node.next.prev = current_node.prev
                current_node.prev.next = current_node.next
                return True
            current_node = current_node.next
        # for last node in list with more then 1 node
        if current_node.next == self.sentinel and current_node.item == item:
            current_node.next.prev = current_node.prev
            current_node.prev.next = current_node.next
            return True
        return False


    def index(self, item):
        '''Returns index of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        
        if self.is_empty():
            return None

        current_node = self.sentinel.next
        # if first node contains item
        if current_node.item == item:
            return 0
        # if list has 1 node
        if current_node.next == self.sentinel and current_node.prev == self.sentinel and current_node.item != item:
            return None

        # for list with more than 1 node
        index = 1
        while current_node.next != self.sentinel:
            if current_node.next.item == item:
                return index
            current_node = current_node.next
            index = index + 1
        return None


    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        
        if index < 0:
            raise IndexError
        if self.is_empty():
            raise IndexError
        current_node = self.sentinel.next
        # for list with 1 node!
        if current_node.next == self.sentinel and current_node.prev == self.sentinel and index == 0:
            self.sentinel.next = self.sentinel # back to 'base case' (empty list/default)
            self.sentinel.prev = self.sentinel
            return current_node.item
        # if list has 1 node
        if current_node.next == self.sentinel and current_node.prev == self.sentinel and index != 0:
            raise IndexError

        # for list with more than 1 node
        # Loop through a set (index) number of times
        my_index = 0
        while my_index < index:
            current_node = current_node.next
            if current_node == self.sentinel:
                raise IndexError
            my_index = my_index + 1

        current_node.next.prev = current_node.prev
        current_node.prev.next = current_node.next
        return current_node.item


    def search_helper(self, item, node):
        '''recursive helper function to search.'''
        
        if node == self.sentinel:
            return False
        if node.item == item:
            return True
        return self.search_helper(item, node.next)


    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        
        return self.search_helper(item, self.sentinel.next)


    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        
        current_node = self.sentinel.next
        if self.is_empty():
            return []
        if current_node.next == self.sentinel and current_node.prev == self.sentinel:
            return [current_node.item]
        save = [current_node.item]
        while current_node.next != self.sentinel:
            save.append(current_node.next.item)
            current_node = current_node.next
        return save

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        
        return self.python_list_reversed_helper(self.sentinel.next)


    def python_list_reversed_helper(self, node):
        '''recursive helper function to python_list_reversed.'''
        
        if node == self.sentinel:
            return []
        else:
            return self.python_list_reversed_helper(node.next) + [node.item]


    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        
        return self.size_helper(self.sentinel.next)

    def size_helper(self, node):
        '''recursive helper function to python_list_reversed.'''
        
        if node == self.sentinel:
            return 0
        else:
            return self.size_helper(node.next) + 1


'''
OL = OrderedList()
OL.add(2)
OL.add(3)
OL.add(1)
OL.add(4)
print(OL.search(1))

OL = OrderedList()
OL.add(2)

OL.add(3)
OL.add(1)
OL.add(4)
print(OL.remove(5))
'''
