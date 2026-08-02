# Graph Representation and Breadth-First Search (BFS) Traversal
from collections import deque

class Graph:
    def __init__(self, vertex):
        """Initializes a square V x V matrix filled with 0s to track connections"""
        self.mat = [[0] * vertex for x in range(vertex)]
        self.size = vertex

    def add_edge(self, src, dst):
        """Adds a bidirectional (undirected) edge between src and dst"""
        if 0 <= src < self.size and 0 <= dst < self.size:
            self.mat[src][dst] = 1
            self.mat[dst][src] = 1
        else:
            print("Invalid!!")

    def print(self):
        """Prints the adjacency matrix layout row by row"""
        for row in self.mat:
            print(' '.join(map(str, row)))

    def bfs(self, src):
        """
        Traverses the graph layer by layer (level-order) using a Queue.
        
        📝 IMPLEMENTATION NOTE ON TRAVERSAL DIRECTION:
        Because a Queue follows FIFO (First-In, First-Out) logic:
        - Scanning neighbors from 0 to self.size discovers smaller indices first.
        - Smaller indices are appended first, meaning they are popped first.
        - This naturally results in a left-to-right (ascending index) exploration.
        """
        # EDGE CASE: Validate if the starting vertex is within bounds
        if not (0 <= src < self.size):
            print("Invalid starting source vertex!")
            return

        # TRACKING ARRAY: Prevents nodes from being processed multiple times
        visited = [False] * self.size
        
        # CORE CONTAINER: Initialize FIFO Queue using a double-ended queue (deque)
        queue = deque([src])
        
        # CRITICAL STEP: Mark the source node as visited immediately upon queuing
        visited[src] = True

        print("BFS Traversal Path: ", end="")
        while queue:
            # FIFO ACTION: Remove and retrieve the front element of the queue
            v = queue.popleft()
            print(v, end=" ")

            # NEIGHBOR LOOKUP: Scan the matrix row of the current vertex
            for i in range(self.size):
                # If a connection exists (1) and the target node is unvisited (False)
                if self.mat[v][i] == 1 and visited[i] == False:
                    # Mark as visited right now so no other path queues it again
                    visited[i] = True
                    # Append to the back of the queue
                    queue.append(i)
        print() # Newline for clean output formatting

# --- Instantiation and Driver Execution ---
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

# Run Breadth-First Search starting from node 0
g.bfs(0)
