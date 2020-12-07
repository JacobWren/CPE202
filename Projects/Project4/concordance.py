from hash_quad import *
import string
import time

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTable(191)
        block_words = []
        try:
            with open(filename, "r", newline="") as file_object:
                for line in file_object:
                    block_words.append((line.split(' ')[0]).rstrip('\n'))
        except:
            raise FileNotFoundError
        file_object.close()
        for i in block_words:
            self.stop_table.insert(i, 0) # 0 is a default



    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.concordance_table = HashTable(191)
        l = []
        try:
            start = time.time()
            stop_list = self.stop_table
            st = stop_list.get_all_keys()
            with open(filename, "r", newline="") as file_object:
                for line in file_object:
                    no_digits = str.maketrans('', '', string.digits)
                    line = line.replace("-", " ")
                    line = line.translate(no_digits)

                    line = line.translate(str.maketrans('', '', string.punctuation))
                    line = line.lower()
                    line = line.rstrip('\n')

                    line = line.split()
                    line = list(set(line))

                    #stop_list = self.stop_table
                    #line = list(set(line) - set(stop_list.get_all_keys()))
                    line = list(set(line) - set(st))



                    l.append(line)
            stop = time.time()
            #print("cleaning process", stop - start)
        except:
            raise FileNotFoundError
        #stop_list = self.stop_table
        #l = list(set(l) - set(stop_list.get_all_keys()))


        #print(l)
        file_object.close()
        start2 = time.time()
        for i in range(len(l)):
            for j in l[i]:
                if j != []:
                    self.concordance_table.insert(j, i+1)
        stop2 = time.time()
        #print("mini for", stop2-start2)

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        #print(self.concordance_table.get_num_items())
        write_to = open(filename, "w", newline="")
        l = []
        pr = self.concordance_table.get_all_keys()
        jb = self.concordance_table.get_value
        start3 = time.time()
        for i in range(self.concordance_table.get_num_items()):
            #print(self.concordance_table.get_value(self.concordance_table.get_all_keys()[i]))
            l.append(pr[i] + ":" + " " + str((jb(pr[i]))).replace("]", "").replace("[", "").replace(",", ""))
        l.sort()
        stop3 = time.time()
        #print('write', stop3-start3)
        for j in range(len(l)):
            if j == len(l) - 1:
                write_to.write(l[j])
            else:
                write_to.write(l[j] + "\n")
        write_to.close()




'''
start4 = time.time()
conc = Concordance()
conc.load_stop_table("stop_words.txt")

conc.load_concordance_table("war.txt")
conc.write_concordance("war_con.txt")
stop4 = time.time()
print('tot', stop4-start4)
'''

