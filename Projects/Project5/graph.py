from stack_array import * #Needed for Depth First Search
from sys import argv
#import time
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.deg = 0
        self.bool = True
        self.color = 'white'


    def add_right_Vert(self, right_id):
        self.adjacent_to.append(right_id)



class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.master_id_dict = {}
        self.num_ids = 0
        self.filename = filename

    def graph_readin(self):
        indices = []
        i = 0
        with open(self.filename, "r", newline="") as file_in:
            for line in file_in:
                indices.append((line.split(' ')))
                indices[i][1] = indices[i][1].rstrip('\n')
                i += 1
        file_in.close()
        return indices



    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        self.num_ids = self.num_ids + 1 # degree
        new_Vert = Vertex(key)
        self.master_id_dict[key] = new_Vert
        return new_Vert


    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.master_id_dict[v1].add_right_Vert(self.master_id_dict[v2])
        self.master_id_dict[v2].deg += 1


        self.master_id_dict[v2].add_right_Vert(self.master_id_dict[v1])
        self.master_id_dict[v1].deg += 1



    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        indices = self.graph_readin()
        for i in indices:
            self.add_vertex(i[0])
            self.add_vertex(i[1])
        for i in range(0, len(indices)):
            self.add_edge(indices[i][0], indices[i][1])

        q = Queue(len(self.master_id_dict))
        path = []
        i = next(iter(self.master_id_dict))
        q.enqueue(self.master_id_dict[i])
        path.append(i)
        counter = 1
        self.master_id_dict[i].color = 'red'
        self.master_id_dict[i].bool = False
        return self.is_bipartite_helper(q, path, counter, i)


    def is_bipartite_helper(self, q, path, counter, i):
        while not q.is_empty():
            for j in self.master_id_dict[i].adjacent_to:
                if self.master_id_dict[i].color == j.color:
                    return False
                if j.bool and j.id not in path:
                    q.enqueue(j)
                    path.append(j.id)
                    counter += 1
                    if self.master_id_dict[i].color == 'red':
                        j.color = 'blue'
                    else:
                        j.color = 'red'

            q.dequeue()
            self.master_id_dict[i].bool = False
            if not q.is_empty():
                i = q.items[q.front].id
            else:
                if counter < len(self.master_id_dict):
                    i = list(self.master_id_dict)[counter]
                    q.enqueue(self.master_id_dict[i])
                    path = []
                    path.append(i)
                    self.master_id_dict[i].color = 'red'
                    self.master_id_dict[i].bool = False
                    counter += 1

        return True



    def conn_components(self):
        '''Returns a list of lists.  For example, if there are three connected components
        then you will return a list of three lists.  Each sub list will contain the
        vertices (in ascending order) in the connected component represented by that list.
        The overall list will also be in ascending order based on the first item of each sublist.
        This method MUST use Depth First Search logic!'''
        indices = self.graph_readin()
        for i in indices:
            self.add_vertex(i[0])
            self.add_vertex(i[1])
        for i in range(0, len(indices)):
            self.add_edge(indices[i][0], indices[i][1])

        stack = Stack(len(self.master_id_dict))
        path = []
        i = next(iter(self.master_id_dict))
        stack.push(self.master_id_dict[i])
        path.append(i)
        master_list = []
        self.master_id_dict[i].bool = False
        r= 0
        return self.conn_components_helper(stack, path, master_list, r)

    def conn_components_helper(self, stack, path, master_list, r):
        while not stack.is_empty():
            node = stack.pop()
            if node.bool:
                node.bool = False
                path.append(node.id)
            for i in self.master_id_dict[node.id].adjacent_to:
                if i.bool:
                    stack.push(i)

            if stack.is_empty():
                r = r + len(path)
                master_list.append(sorted(path))
                if r < len(self.master_id_dict):
                    path = []
                    i = list(self.master_id_dict)[r]
                    stack.push(self.master_id_dict[i])
                    path.append(i)
                    self.master_id_dict[i].bool = False
                    continue
                else:
                    master_list.sort()
                    return master_list

'''
start = time.time()
g = Graph('test5.txt')
print(g.conn_components())
print(g.is_bipartite())
end = time.time()
print(end-start)
'''
