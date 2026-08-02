# Graph Representation and Iterative Depth-First Search (DFS)
class Graph:
    def __init__(self, vertex):
        """Initializes a square V x V matrix filled with 0s to track connections"""
        self.mat = [[0] * vertex for x in range(vertex)]
        self.size = vertex

    def add_edge(self, src, dest):
        """Adds a bidirectional edge between src and dest"""
        if 0 <= src < self.size and 0 <= dest < self.size:
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else:
            print("Invalid!!")

    def print(self):
        """Prints the adjacency matrix layout row by row"""
        for row in self.mat:
            print(' '.join(map(str, row)))

    def dfs(self, src):
        """
        Traverses the graph deeper along each branch using an iterative stack.
        
        ⚠️ IMPLEMENTATION NOTE ON TRAVERSAL DIRECTION:
        Because a stack follows LIFO (Last-In, First-Out) logic:
        - Scanning neighbors from 0 to self.size pushes smaller indices first.
        - Consequently, larger indices end up at the top of the stack.
        - This causes the algorithm to pop and visit larger neighbors first.
        
        This behavior is 100% correct for standard DFS. If your application 
        specifically requires visiting smaller neighbors first, change the neighbor 
        loop to scan backwards: for i in range(self.size - 1, -1, -1):
        """
        # EDGE CASE: Validate if the starting vertex is within bounds
        if not (0 <= src < self.size):
            print("Invalid starting source vertex!")
            return

        # TRACKING ARRAY: Keeps track of visited nodes to avoid infinite cycles/loops
        visited = [False] * self.size
        
        # CORE CONTAINER: Initialize stack with the source node to track traversal path
        stack = [src]

        print("DFS Traversal Path: ", end="")
        while stack:
            # LIFO ACTION: Pop the top element from the stack (favors last appended element)
            v = stack.pop()

            # Process the vertex only if it hasn't been visited yet
            if visited[v] == False:
                print(v, end=" -> " if stack or any(self.mat[v][i] == 1 and not visited[i] for i in range(self.size)) else "\n")
                # Mark the current node as visited immediately
                visited[v] = True

            # NEIGHBOR LOOKUP: Scan the matrix row of the current vertex
            # NOTE: Forward range means higher indices sit on top of the stack
            for i in range(self.size):
                # If a connection exists (1) and the target node is unvisited (False)
                if self.mat[v][i] == 1 and visited[i] == False:
                    stack.append(i)

# --- Instantiation and Driver Execution ---
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

# Run Depth-First Search starting from node 0
g.dfs(0)
