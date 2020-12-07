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

    for i in graph.master_id_dict:
        if graph.master_id_dict[i].deg == 0:
            stack.push(i)

    while s < fixed:
        if not stack.is_empty():
            off = stack.pop()
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

#print(tsort(['blue', 'black', 'red', 'blue', 'red', 'green', 'green', 'blue', 'green', 'purple', 'purple', 'blue']))
#start = time.time()
#print(tsort(['v1','v2','v1','v3','v2','v4','v2','v5','v1','v4','v3','v6','v5','v4','v4','v3','v4','v6','v7','v6','v4','v7','v5','v7']))
#end = time.time()
#print(end - start)

'''
j = []
for i in range(0, 50000):
    j.append(str(i))
start = time.time()
print(tsort(j))
tsort(j)
end = time.time()
print('Total time is: ', end - start)
'''
