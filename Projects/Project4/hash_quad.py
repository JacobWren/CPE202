class HashTable:

    def __init__(self, table_size = 191): # can add additional attributes
        self.table_size = table_size # initial table size
        self.num_items = 0 # empty hash table
        self.load_factor = 0
        self.hash_table = [None] * table_size

        
    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        
        The key is a string (a word) to be entered, and value is the line number that the word appears on. 
        If the key is not already in the table, then the key is inserted, and the value is used as the first 
        line number in the list of line numbers. If the key is in the table, then the value is appended to that 
        key’s list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table),
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        
        hash_value = self.horner_hash(key)
        if self.hash_table[hash_value] == None: # Then insert it!
            self.hash_table[hash_value] = (key,[])
            self.hash_table[hash_value][1].append(value)
            self.num_items += 1
            self.load_factor = self.num_items / self.table_size
            if self.load_factor > .5:
                self.num_items = 0
                temp_hash_table = []
                temp_hash_table = list(filter(None, self.hash_table))
                self.table_size = (self.table_size * 2) + 1
                self.hash_table = [None] * self.table_size
                for i in range(len(temp_hash_table)):
                    for j in temp_hash_table[i][1]:
                        self.insert(temp_hash_table[i][0], j)
        elif self.hash_table[hash_value][0] == key and value in self.hash_table[hash_value][1]:
            return
        else:
            if self.hash_table[hash_value][0] == key:
                self.hash_table[hash_value][1].append(value)
            else:
                i = 0
                quad_slot = hash_value
                og_hash = hash_value
                while self.hash_table[quad_slot] != None and self.hash_table[quad_slot][0] != key:
                    i += 1
                    quad_slot = self.rehash(og_hash, i)

                if self.hash_table[quad_slot] == None:  # Then insert it!
                    self.hash_table[quad_slot] = (key, [])
                    self.hash_table[quad_slot][1].append(value)
                    self.num_items += 1
                    self.load_factor = self.num_items / self.table_size
                    if self.load_factor > .5:
                        self.num_items = 0
                        temp_hash_table = []
                        for j in self.hash_table:
                            if j != None:
                                temp_hash_table.append(j)
                        self.table_size = (self.table_size * 2) + 1
                        self.hash_table = [None] * self.table_size
                        for i in range(len(temp_hash_table)):
                            for j in temp_hash_table[i][1]:
                                self.insert(temp_hash_table[i][0], j)
                elif self.hash_table[quad_slot][0] == key and value in self.hash_table[quad_slot][1]:
                    return
                else:
                    self.hash_table[quad_slot][1].append(value)


    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        
        char_list = list(key)
        n = min(8, len(char_list))
        cum_sum = 0
        for i in range(n):
            cum_sum = cum_sum + (ord(char_list[i]) * 31**(n-1-i))
        return cum_sum % self.table_size


    def rehash(self, old_hash, i):
        """ Compute and return new hash value"""
        
        return (old_hash + i**2) % self.table_size

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        
        if all(i is None for i in self.hash_table):
            return False
        hash_value = self.horner_hash(key)
        if self.hash_table[hash_value] == None:
            return False
        elif self.hash_table[hash_value][0] == key:
            return True
        else:
            i = 0
            og_hash = hash_value
            while self.hash_table[hash_value] != None and self.hash_table[hash_value][0] != key:
                i += 1
                hash_value = self.rehash(og_hash, i)
            else:
                if self.hash_table[hash_value] == None:
                    return False
                else:
                    return True


    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""
        
        hash_value = self.horner_hash(key)
        if self.hash_table[hash_value] == None:
            return None
        elif self.hash_table[hash_value][0] == key:
            return hash_value
        else:
            i = 0
            og_hash = hash_value
            while self.hash_table[hash_value] != None:
                if self.hash_table[hash_value][0] == key:
                    return hash_value
                else:
                    i += 1
                    hash_value = self.rehash(og_hash, i)
            if self.hash_table[hash_value] == None:
                return None

            
    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        return [i[0] for i in self.hash_table if i]

    
    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""
        
        if all(i is None for i in self.hash_table):
            return None
        hash_value = self.horner_hash(key)
        if self.hash_table[hash_value] == None:
            return None
        elif self.hash_table[hash_value][0] == key:
            return self.hash_table[hash_value][1]
        else:
            i = 0
            og_hash = hash_value
            while self.hash_table[hash_value] != None:
                if self.hash_table[hash_value][0] == key:
                    return self.hash_table[hash_value][1]
                else:
                    i += 1
                    hash_value = self.rehash(og_hash, i)
            if self.hash_table[hash_value] == None:
                return None


    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        
        return (self.num_items / self.table_size)

'''
ht = HashTable(9)
ht.insert("cbQ", 6)
ht.insert("cap", 7)
ht.insert("m", 6)
ht.insert("cbQ", 6)
ht.insert("cap", 7)
ht.insert("m", 6)
ht.get_value("capo")
'''
