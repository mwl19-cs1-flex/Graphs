"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() # A set of edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # If they're both in the graph
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id not in self.vertices:
            raise IndexError("Vertex does not exist in graph!")
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # use two qs because of weird commands
        # qq = Queue()
        # qq.enqueue([starting_vertex])
        
        # # Keep track of visited nodes
        # visited = list()

        # # Repeat until queue is empty
        # while qq.size() > 0:
        #     # Dequeue the first vert
        #     vert = qq.dequeue()
        #     # If it's not visited:
        #     if vert[-1] not in visited:
        #         print(vert)
        #         # Mark as visited
        #         visited.append(vert[-1])
        #         for next_vert in self.get_neighbors(vert[-1]):
        #             new_vert = list(vert)
        #             new_vert.append(next_vert)
        #             qq.enqueue(next_vert)
        
        # return visited
        qq = Queue()
        qq.enqueue([starting_vertex])
        visited = list()
        while qq.size() > 0:
            path = qq.dequeue()
            if path[-1] not in visited:
                visited.append(path[-1]) 
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)
                    
        return visited


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        st = Stack()
        st.push(starting_vertex)

        visited = set()

        while st.size() > 0:
            vert = st.pop()

            if vert not in visited:
                print(vert)
                visited.add(vert)
                for next_vert in self.get_neighbors(vert):
                    st.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        # class work
        # if starting_vertex in visited:
        #     return
        print(starting_vertex)
        visited.add(starting_vertex)
        for next_vert in self.get_neighbors(starting_vertex):
            # school work
            if next_vert not in visited:
                self.dft_recursive(next_vert, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        qq = Queue()
        qq.enqueue(starting_vertex)
        visited = set()
        path = list()
        path.append(starting_vertex)
        while qq.size() > 0:
            vert = qq.dequeue()
            if vert not in visited:
                if vert == destination_vertex:
                    path.append(vert)
                    return path
                visited.add(vert)
                for next_vert in self.get_neighbors(vert):
                    if destination_vertex in self.get_neighbors(next_vert):
                        path.append(vert)
                        qq.enqueue(next_vert)
                    else:
                        qq.enqueue(next_vert)
                            

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        st = Stack()
        st.push(starting_vertex)
        visited = set()
        path = list()
        path.append(starting_vertex)
        while st.size() > 0:
            vert = st.pop()
            if vert not in visited:
                if vert == destination_vertex:
                    path.append(vert)
                    return path
                visited.add(vert)
                for next_vert in self.get_neighbors(vert):
                    if destination_vertex in self.get_neighbors(next_vert):
                        path.append(vert)
                        st.push(next_vert)
                    else:
                        st.push(next_vert)

    # class work
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        print(starting_vertex)
        if visited is None:
            visited = set()
        if path is None:
            path = list()
        visited.add(starting_vertex)
        # We want to make a copy
        path = path + [starting_vertex]
        # You can also do 
        # new_path = path.copy()
        # new_path.append(starting_vertex)
        # or
        # new_path = list(path)
        # Copy a list, that's what we need to do

        # Base case

        if starting_vertex == destination_vertex:
            return path

        for next_vert in self.get_neighbors(starting_vertex):
            if next_vert not in visited:
                answer = self.dfs_recursive(next_vert, destination_vertex, visited, path)
                # if answer:
                # or
                if answer is not None:
                    return answer

        
    # def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.

    #     This should be done using recursion.
    #     """
    #     # checking if starting vertex is the destination
    #     if path is None:
    #         path = list()
    #     if visited is None:
    #         visited = set()
    #     if starting_vertex in visited:
    #         return 
    #     if starting_vertex not in visited:
    #         visited.add(starting_vertex)
    #         path = path + [starting_vertex]
    #         if starting_vertex == destination_vertex:
    #             return path
    #         for next_vert in self.get_neighbors(starting_vertex):
    #             recursion = self.dfs_recursive(next_vert, destination_vertex, path, visited)
    #             if recursion:
    #                 return recursion

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    # print(graph.get_neighbors(1))
    # should raise index error (it does!)
    # print(graph.get_neighbors(8))
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))