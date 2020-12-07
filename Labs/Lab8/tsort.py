from sys import argv
from stack_array2 import *
import time

def tsort(indices):
    """
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of idices where each pair of idices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one idex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - idices is emtpy with the message "input contains no edges"
    *   - idices has an odd number of idices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message
    *     "input contains a cycle """
    if indices == []:
        raise ValueError("input contains no edges")
    elif len(indices) % 2 != 0:
        raise ValueError("input contains an odd number of tokens")
    graph = Graph()
    stack = Stack(len(indices))
    for i in indices:
        if i not in graph.master_id_dict:
            graph.add_Vert(i)
    for i in range(0, len(indices)-1, 2):
        graph.add_Edge(indices[i], indices[i + 1], 0)
    string = ""
    s = 0
    fixed = len(graph.master_id_dict)
    '''
    while s < fixed:
        for i in graph.master_id_dict:
                #if graph.master_id_dict[i].deg == 0 and i not in string and i not in stack.items: # degree 0!
                if graph.master_id_dict[i].deg == 0 and i not in stack.items:
                    stack.push(i)
        if not stack.is_empty():
            off = stack.pop()
            #adjacents = list(graph.master_id_dict[off].adj_dict.keys())
            #adjacents = graph.master_id_dict[off].adj_dict
            string = string + off + "\n"
            for j in graph.master_id_dict[off].adj_dict:
                j.deg -= 1
            del graph.master_id_dict[off]
            s += 1
        else:
            raise ValueError("input contains a cycle")
    return string
    '''
    #'''
    for i in graph.master_id_dict:
        if graph.master_id_dict[i].deg == 0:
            stack.push(i)
    #'''
    #'''
    while s < fixed:
        if not stack.is_empty():
            off = stack.pop()
            #adjacents = list(graph.master_id_dict[off].adj_dict.keys())
            #adjacents = graph.master_id_dict[off].adj_dict
            string = string + off + "\n"
            for j in graph.master_id_dict[off].adj_dict:
                j.deg -= 1
            for i in graph.master_id_dict[off].adj_dict:
                if graph.master_id_dict[i.id].deg == 0:
                    stack.push(i.id)
            del graph.master_id_dict[off]
            s += 1
        else:
            raise ValueError("input contains a cycle")
    return string

    #'''



class Vertex:
    def __init__(self, key):
        self.id = key
        self.adj_dict = {}
        self.deg = 0

    def add_right_Vert(self, right_id, null = 0):
        self.adj_dict[right_id] = null


class Graph:
    def __init__(self):
        self.master_id_dict = {}
        self.num_ids = 0

    def add_Vert(self,key):
        self.num_ids = self.num_ids + 1 # degree
        new_Vert = Vertex(key)
        self.master_id_dict[key] = new_Vert
        return new_Vert

    def add_Edge(self,adj_1,adj_2,null=0):
        if adj_1 == adj_2:
            raise ValueError("input contains a cycle")
        self.master_id_dict[adj_1].add_right_Vert(self.master_id_dict[adj_2], null)
        self.master_id_dict[adj_2].deg += 1

print(tsort(['blue', 'black', 'red', 'blue', 'red', 'green', 'green', 'blue', 'green', 'purple', 'purple', 'blue']))
#print(tsort(['101', '102', '102', '103', '103', '315', '225', '315', '103', '357', '315', '357', '141', '102', '102', '225']))
#print(tsort(['a','b','b','c','c','a','b','d']))
#print(tsort(['a','b','b','c','c','c']))
#start = time.time()
#print(tsort(['v1','v2','v1','v3','v2','v4','v2','v5','v1','v4','v3','v6','v5','v4','v4','v3','v4','v6','v7','v6','v4','v7','v5','v7']))
#end = time.time()
#print(end - start)
'''
j = []
for i in range(0, 50000):
    j.append(str(i))
start = time.time()
#print(tsort(j))
tsort(j)
end = time.time()
print('whole thing', end - start)
'''

#print(tsort(['blue', 'black', 'red', 'blue', 'red', 'green', 'green', 'blue', 'green', 'purple', 'purple', 'blue']))
#print(tsort(['1', '2', '1', '9', '1', '8', '9', '8', '9', '10', '8', '11', '10', '11', '2', '3', '3', '11', '3', '4', '4', '7', '4', '5', '7', '5', '7', '13', '7', '6', '6', '14', '6', '12']))
#"1\n9\n10\n8\n2\n3\n4\n7\n6\n12\n14\n13\n5\n11"
'''
g = Graph()

g.add_Vert('V1')
g.add_Vert('V2')
g.add_Vert('V3')
g.add_Vert('V4')
g.add_Vert('V5')
g.add_Vert('V0')

g.add_Edge('V0','V1',5)
g.add_Edge('V0','V5',2)
g.add_Edge('V1','V2',4)
g.add_Edge('V2','V3',9)
g.add_Edge('V3','V4',7)
g.add_Edge('V3','V5',3)
g.add_Edge('V4','V0',1)
g.add_Edge('V5','V4',8)
g.add_Edge('V5','V2',1)

#print("hold")
#print(g.master_id_dict['V0'].deg)
'''


'''
def main():

    # Entry point for the tsort utility allowing the user to specify
      # a file containing the edge of the DAG
       
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()
    
    idices = []
    for line in f:
        idices += line.split()
       
    try:
        result = tsort(idices)
        print(result)
    except Exception as e:
        print(e)
    
if __name__ == '__main__': 
    main()
'''
