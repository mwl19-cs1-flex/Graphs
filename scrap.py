# This is a space for scrap work for Graphs week
import string

listicle = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

def smallest_calculator(lists):
    total = 0
    for small_list in lists:
        smallest_item = small_list[0]
        for item in small_list:
            if item < smallest_item:
                smallest_item = item
        print(smallest_item)
        total += smallest_item 
    return f"Total:{total}"

# print(smallest_calculator(listicle))

def f(n):
    if n > 997:
        error = "Too large!"
        return error
    else:
        if n == 0:
            return 3490
        
        return f(n-1)

# Lesson here: Recursion will only go to 1000

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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


    # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    # 'n', ]


    def get_neighbors(self, word):
        # THIS BUILDS THE GRAPH ON THE FLY
        
        # Reads all of the words and puts it into a list:
        with open('words.txt') as f:
            words = f.read().split()

        word_set = set()

        for w in words:
            word_set.add(w.lower())

        # Making a list of letters (have to import string!)
        letters = list(string.ascii_lowercase)

        # What we return
        neighbors = []

        string_word = list(word) # turns 'word' into ['w', 'o', 'r', 'd']

        # for each letter
        for i in range(len(string_word)):
            for letter in letters:
                temp_word = list(string_word)
                temp_word[i] = letter

                ww = "".join(temp_word)

                # Only adds if a word is valid and is not the original word
                if ww in word_set and ww != word:
                    neighbors.append(ww)

        return neighbors

    def find_ladders(self, begin_word, end_word):
        visited = set()
        qt = Queue()

        qt.enqueue([begin_word])

        while qt.size() > 0:

            path = qt.dequeue()

            word = path[-1]

            if word not in visited:

                visited.add(word)
                
                # Did we reach the end word?
                if word == end_word:
                    return path
                
                for neighbor in self.get_neighbors(word):
                    path_copy = list(path)
                    path_copy.append(neighbor)

                    qt.enqueue(path_copy)
