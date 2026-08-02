# Graph Representation using a 2D Adjacency Matrix
class Graph:
    def __init__(self, vertex):
        """
        Initializes a square 2D matrix of size V x V (vertex x vertex).
        Initially filled with 0s, meaning no edges exist between vertices.
        """
        self.mat = [[0] * vertex for i in range(vertex)]
        self.size = vertex  # Keeps track of the total number of vertices (bounds checking)
    
    def add_edge(self, src, dest):
        """
        Adds a bidirectional (undirected) edge between src and dest.
        Sets the matrix connection flag from 0 to 1 at both intersecting points.
        """
        # EDGE CASE: Validate that both vertex indices fall within the allowed range
        if 0 <= src < self.size and 0 <= dest < self.size:
            self.mat[src][dest] = 1  # Connects src -> dest
            self.mat[dest][src] = 1  # Connects dest -> src (Undirected Graph requirement)
        else:
            # Handles out-of-bounds inputs safely without throwing an IndexError
            print("Invalid Edge!")

    def print(self):
        """
        Iterates through the 2D grid matrix and prints it row by row.
        Converts the numerical states into human-readable string patterns.
        """
        for row in self.mat:
            # map(str, row) converts every integer in the row into a string
            # ' '.join(...) merges the strings into a space-separated layout
            print(' '.join(map(str, row)))

# --- Instantiation and Driver Execution ---

# Create a graph with 5 vertices (IDs range from 0 to 4)
g = Graph(5)

# Insert the connection network paths
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(2, 3)

# Print the final symmetric matrix grid
g.print()
