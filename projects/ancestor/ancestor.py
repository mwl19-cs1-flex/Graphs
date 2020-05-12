import sys 
sys.path.insert(0, '../graph')
from util import Queue, Stack
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for (parent, child) in ancestors:
        

    
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 1)