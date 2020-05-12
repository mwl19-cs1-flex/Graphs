# Day One

## What is a graph?
A graph is just a collection of vertices and edges

Its edges are usually depicted as arrows, if it moves in that direction. If it moves in both directions, there are (usually) no arrows.

A completely connected graph is where every node is connected to each other.

## Type of graphs

### Cyclic

A graph that has a cycle in it

Ex:
-Doubly Linked List

### Acyclic

A graph that has no cycles in it

Ex:
-Linked List
-Binary Search Tree

### Directed

Can only go one way when traversing vertices and edges

### Undirected

Can go wherever when traversing vertices and edges

## Dense and Sparse

### Dense
Lots of edges and vertices. Each node is connected to a lot of nodes. A completed graph is an ultra dense graph.

### Sparse
Not a lot of edges and vertices. Each node is only connected to a few others.

## Graph Weights

Weight can represent many different things, distance, cost, time, etc.

### Weighted

Different weights on the edges, could be used to determine the cost of a path.

### Unweighted

All of the edges have the same weight to them. You can optimize paths this way.

## Graph Representation

How do we represent a graph? There are a couple ways to do it via code or otherwise non-traditionally (such as, a graph with the vertices drawn and connected)

```
class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = [] # Adjacency List
```

### Adjacency Matrix

Better for denser graphs because of memory usage!

A two dimensional grid that stores the node on the X and Y axis. Looking between each X and Y node on this graph can show us if it is connected.

A zero shows that it is not connected, anything else shows a connection. If it is a 1, it can be either a weight or an indicator that the node is connected to another node.

Ex:
* (Our example does not show a vertex connecting back to itself, but it is possible to do so!) 
```
class Graph:
    def __init__(self):
        self.edges = [
            # This list has A, B, C, D vertices, following the index order in the list
            [0, 1, 1, 0], # A's edges to B and C
            [1, 0, 1, 1], # B's edges to A, C and D, this is cyclic and undirected
            [1, 1, 0, 1], # C's edges to A, B and D
            [0, 1, 1, 0] # D's edges to B and C
        ]
```

### Adjacency List

Better for sparser graphs because of memory usage! 

A Graph that stores a list of vertices, and for each vertex, a list of each vertex to which its connected. Can have weights.

Ex:
```
class Graph:
    def __init__(self):
        self.vertices = {
            "A": {"B": 1, "C": 3} # Has a hash of vertices with edge weights, shows that this is a weighted graph
            "B": {"D": 3}
            "C": {"D": 2} # Shows that it is connected to D, but not to A, so this is a directed graph
            "D": {} # Has no connections, shows that this is a acyclic graph
        }
```

## Traversals 

### Depth First Traversal
* This can be recursive!

**This uses a Stack**

> Go the deepest you can, then back up the minimum amount, and travel through the graph that way

```
Add starting node to a stack

While the stack isn't empty:
    Pop the first vert
    If that vert isn't visited:
        Mark as visited
        Push all its unvisited neighbors to the stack
```

### Breadth First Traversal
* This can NOT be recursive!

**This uses a Queue**

```
Add starting node to a queue

While the queue isn't empty:
    Dequeue the first vertex
    If that vert isn't visited:
        Mark as visited
        Add its unvisited neighbors to the queue
```



# Day Two

## Breadth First and Depth First Searching

- Breadth first finds the _shortest_ route
- Depth first finds 

## How to solve a Graph problem

1. Translate the problem into graph terminology

2. Build the graph

3. Traverse it

### Word Ladders Problem

How can you transfer one word into another word?

Rules:
-Changing one letter at a time
-Each word must be an actual word

Ex:
```
begin_word: hit
end_word: cog

hit -> hot -> cot -> cog

begin_word: sail
end_word: boat

sail -> bail -> bait -> 
```