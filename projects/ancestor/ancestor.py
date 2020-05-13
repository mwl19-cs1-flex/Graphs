import sys 
sys.path.insert(0, '../graph')
from util import Queue, Stack
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for (parent, child) in ancestors:
        if parent in g.vertices and child not in g.vertices:
            g.add_vertex(child)
        elif child in g.vertices and parent not in g.vertices:
            g.add_vertex(parent)
        elif parent in g.vertices and child in g.vertices:
            pass
        else:
            g.add_vertex(parent)
            g.add_vertex(child)

    for (parent, child) in ancestors:
        g.add_edge(child, parent)
    
    ancestors = g.bft(starting_node)
    latest = ancestors[-1]
    if latest == starting_node:
        return -1
    else:
        return latest
        


    
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 1)