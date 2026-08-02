# Graph Data Structure: Beginner to Advanced

## 1. Introduction to Graphs

### What is a graph?
A graph is a collection of objects and relationships between them.
- Objects are called **vertices** or **nodes**.
- Relationships are called **edges**.

Think of a graph like a city map: intersections are nodes and roads are edges.

### Core terminology
- **Vertex / Node**: a single point in the graph.
- **Edge**: a connection between two nodes.
- **Degree**: number of edges connected to a node.
- **Indegree / Outdegree**: for directed graphs, indegree counts incoming edges and outdegree counts outgoing edges.
- **Adjacent nodes**: nodes connected directly by an edge.
- **Path**: a sequence of nodes connected by edges.
- **Cycle**: a path that starts and ends on the same node without repeating an edge.
- **Connected component**: a maximal set of nodes where every node is reachable from each other.

### Why graphs are important
Graphs model relationships. They show: 
- connectivity, 
- dependencies, 
- routes, 
- influence, 
- state transitions.

### Real-world examples
- **Social networks**: users as nodes and friendships as edges.
- **Maps / GPS**: locations as nodes and roads as edges.
- **Internet routing**: routers as nodes and links as edges.
- **Recommendation systems**: items and users form a bipartite graph.
- **Dependency graphs**: build systems or package managers.

### Intuition and analogies
- A graph is like a spider web with points and threads.
- A directed graph is like a one-way street map.
- A weighted graph is like a road map with distances or travel times.

---

## 2. Types of Graphs

### Directed Graph
- Definition: edges have a direction.
- Diagram idea: arrows between nodes.
- Real-world use: web links, task dependencies.
- Code: `adj[u].push_back(v)` only.

### Undirected Graph
- Definition: edges are bidirectional.
- Diagram idea: simple lines between nodes.
- Real-world use: friendships, undirected roads.
- Code: add both directions.

### Weighted Graph
- Definition: edges carry a value.
- Diagram idea: edges labeled with cost.
- Real-world use: distances, shipping costs.
- Code: store pairs `(neighbor, weight)`.

### Unweighted Graph
- Definition: edges have equal cost.
- Diagram idea: plain connections.
- Real-world use: connectivity checks.

### Cyclic vs Acyclic
- Cyclic: contains at least one cycle.
- Acyclic: no cycles.
- DAG: directed acyclic graph.

### Connected vs Disconnected
- Connected: every pair of vertices has a path.
- Disconnected: graph has separate components.

### Complete Graph
- Every node connects to every other node.
- Dense, lots of edges.
- Real-world: small networks where every device talks to every other.

### Bipartite Graph
- Vertices split into two sets.
- Edges connect only across sets.
- Real-world: jobs to workers, users to items.

### DAG (Directed Acyclic Graph)
- Definition: directed and no cycles.
- Use case: scheduling, version control commit graphs.

### Tree as a graph
- A tree is a connected acyclic undirected graph.
- A rooted tree is a DAG with a unique path from root to every node.

### Sparse vs Dense graph
- Sparse: edges `E` much smaller than `V^2`.
- Dense: edges close to `V^2`.
- Use adjacency list for sparse, adjacency matrix for dense.

### Comparison table

| Graph type | Directed? | Weighted? | Typical use | Representation |
|---|---|---|---|---|
| Directed | Yes | Either | dependencies | adj list/matrix |
| Undirected | No | Either | social network | adj list/matrix |
| Weighted | Yes/No | Yes | shortest path | weighted adj list |
| DAG | Yes | Either | scheduling | topological order |
| Complete | Yes/No | Either | theoretical | adjacency matrix |
| Bipartite | Yes/No | Either | matching problems | separate partitions |

---

## 3. Graph Representations

### Adjacency Matrix
- Visual: a table with rows and columns for nodes.
- Memory: `O(V^2)`.
- Edge lookup: `O(1)`.
- Iterate neighbors: `O(V)`.
- Best for dense graphs.

C++:
```cpp
vector<vector<int>> adj(V, vector<int>(V, 0));
adj[u][v] = 1; // directed
adj[v][u] = 1; // undirected
```

Java:
```java
int[][] adj = new int[V][V];
adj[u][v] = 1;
adj[v][u] = 1;
```

Python:
```python
adj = [[0]*V for _ in range(V)]
adj[u][v] = 1
adj[v][u] = 1
```

### Adjacency List
- Visual: list of neighbor lists.
- Memory: `O(V + E)`.
- Edge lookup: `O(deg(v))`.
- Iterate neighbors: `O(deg(v))`.
- Best for sparse graphs.

C++:
```cpp
vector<vector<int>> adj(V);
adj[u].push_back(v);
adj[v].push_back(u);
```

Java:
```java
List<List<Integer>> adj = new ArrayList<>();
for(int i=0;i<V;i++) adj.add(new ArrayList<>());
adj.get(u).add(v);
adj.get(v).add(u);
```

Python:
```python
adj = [[] for _ in range(V)]
adj[u].append(v)
adj[v].append(u)
```

### Edge List
- Visual: list of `(u, v)` or `(u, v, w)` pairs.
- Memory: `O(E)`.
- Good for algorithms that process edges directly.
- Useful for Kruskal and Bellman-Ford.

C++:
```cpp
vector<pair<int,int>> edges;
edges.push_back({u, v});
```

Java:
```java
List<int[]> edges = new ArrayList<>();
edges.add(new int[]{u, v});
```

Python:
```python
edges = []
edges.append((u, v))
```

### Summary table

| Representation | Storage | Edge lookup | Iterate neighbors | Best use |
|---|---|---|---|---|
| Matrix | `O(V^2)` | `O(1)` | `O(V)` | dense graph |
| List | `O(V+E)` | `O(deg(v))` | `O(deg(v))` | sparse graph |
| Edge list | `O(E)` | `O(E)` | `O(E)` | edge-centric algorithms |

---

## 4. Graph Traversal Algorithms

### Breadth First Search (BFS)

#### Intuition
BFS explores in rings from the start node.
- First layer: immediate neighbors.
- Second layer: neighbors of neighbors.

This resembles throwing a stone in a pond and watching ripples spread.

#### Queue-based approach
BFS uses a queue to manage the frontier.
- Pop current node.
- Visit each neighbor.
- Push unvisited neighbors into the queue.

#### Level-order traversal
BFS naturally visits nodes by distance in an unweighted graph.
- Great for shortest paths in unweighted graphs.

#### Dry run
Graph:
```
0 -- 1 -- 3
|    |
2 -- 4
```
Start at `0`.
Queue progression: `[0]` -> `[1,2]` -> `[2,3,4]` -> ...
Visit order: `0, 1, 2, 3, 4`.

#### Pseudocode
```
BFS(start):
  queue = [start]
  visited[start] = true
  while queue not empty:
    node = queue.pop()
    for neighbor in adj[node]:
      if not visited[neighbor]:
        visited[neighbor] = true
        queue.push(neighbor)
```

#### Implementations

C++:
```cpp
void bfs(int start, vector<vector<int>>& adj, vector<bool>& visited) {
    queue<int> q;
    q.push(start);
    visited[start] = true;
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node << " ";
        for (int nei : adj[node]) {
            if (!visited[nei]) {
                visited[nei] = true;
                q.push(nei);
            }
        }
    }
}
```

Java:
```java
void bfs(int start, List<List<Integer>> adj, boolean[] visited) {
    Queue<Integer> q = new LinkedList<>();
    q.add(start);
    visited[start] = true;
    while (!q.isEmpty()) {
        int node = q.poll();
        System.out.print(node + " ");
        for (int nei : adj.get(node)) {
            if (!visited[nei]) {
                visited[nei] = true;
                q.add(nei);
            }
        }
    }
}
```

Python:
```python
from collections import deque

def bfs(start, adj, visited):
    q = deque([start])
    visited[start] = True
    while q:
        node = q.popleft()
        print(node, end=' ')
        for nei in adj[node]:
            if not visited[nei]:
                visited[nei] = True
                q.append(nei)
```

#### Complexity
- Time: `O(V + E)`.
- Space: `O(V)` for queue + visited.

#### Common interview questions
- shortest path in unweighted graph
- level order traversal on trees
- flood fill / grid connectivity
- bipartite graph check

#### Common mistakes
- forgetting to mark visited early
- using recursion instead of a queue
- not handling disconnected graphs

### Depth First Search (DFS)

#### Intuition
DFS dives deep into one path before backtracking.
- Like exploring a maze: go straight until you hit a wall, then backtrack.

#### Recursive intuition
Recursion naturally models the stack of unfinished paths.

#### Iterative DFS using stack
Use an explicit stack to simulate recursion.

#### Recursive DFS

C++:
```cpp
void dfs(int node, vector<vector<int>>& adj, vector<bool>& visited) {
    visited[node] = true;
    cout << node << " ";
    for (int nei : adj[node]) {
        if (!visited[nei]) {
            dfs(nei, adj, visited);
        }
    }
}
```

Java:
```java
void dfs(int node, List<List<Integer>> adj, boolean[] visited) {
    visited[node] = true;
    System.out.print(node + " ");
    for (int nei : adj.get(node)) {
        if (!visited[nei]) {
            dfs(nei, adj, visited);
        }
    }
}
```

Python:
```python
def dfs(node, adj, visited):
    visited[node] = True
    print(node, end=' ')
    for nei in adj[node]:
        if not visited[nei]:
            dfs(nei, adj, visited)
```

#### Iterative DFS

C++:
```cpp
void dfs_iterative(int start, vector<vector<int>>& adj, vector<bool>& visited) {
    stack<int> st;
    st.push(start);
    while (!st.empty()) {
        int node = st.top();
        st.pop();
        if (visited[node]) continue;
        visited[node] = true;
        cout << node << " ";
        for (int nei : adj[node]) {
            if (!visited[nei]) st.push(nei);
        }
    }
}
```

Java:
```java
void dfsIterative(int start, List<List<Integer>> adj, boolean[] visited) {
    Stack<Integer> st = new Stack<>();
    st.push(start);
    while (!st.isEmpty()) {
        int node = st.pop();
        if (visited[node]) continue;
        visited[node] = true;
        System.out.print(node + " ");
        for (int nei : adj.get(node)) {
            if (!visited[nei]) st.push(nei);
        }
    }
}
```

Python:
```python
def dfs_iterative(start, adj, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        print(node, end=' ')
        for nei in adj[node]:
            if not visited[nei]:
                stack.append(nei)
```

#### Traversal tree
DFS generates a tree of explored nodes and backtracking edges.

#### Backtracking concept
- Visit neighbor.
- If dead end, return.
- Continue the remaining neighbors.

#### Dry run
Graph:
```
0 -> 1 -> 3
|    |
v    v
2    4
```
DFS order from `0`: `0, 1, 3, 4, 2` (dependent on neighbor order).

#### Complexity
- Time: `O(V + E)`.
- Space: `O(V)` recursion stack or explicit stack.

#### Interview tricks
- DFS is ideal for exploring all possible states.
- Use recursion for simpler code and stack for large inputs.

### BFS vs DFS

| Property | BFS | DFS |
|---|---|---|
| Data structure | queue | stack / recursion |
| Use case | shortest path unweighted | path existence, backtracking |
| Order | level by level | deep-first |
| Space | may be large for wide graphs | may be large for deep graphs |
| Cycle detection | yes with visited | yes with visited and recursion stack |

---

## 5. Connected Components

### What is a connected component?
A set of nodes where every node is reachable from every other node.

### Finding connected components
Use DFS or BFS from unvisited nodes.

#### Algorithm
```
count = 0
for each node:
  if not visited[node]:
    count += 1
    dfs(node)
```

#### Code example

C++:
```cpp
int countComponents(int V, vector<vector<int>>& adj) {
    vector<bool> visited(V, false);
    int count = 0;
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            count++;
            dfs(i, adj, visited);
        }
    }
    return count;
}
```

Java:
```java
int countComponents(int V, List<List<Integer>> adj) {
    boolean[] visited = new boolean[V];
    int count = 0;
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            count++;
            dfs(i, adj, visited);
        }
    }
    return count;
}
```

Python:
```python
def count_components(V, adj):
    visited = [False]*V
    count = 0
    for i in range(V):
        if not visited[i]:
            count += 1
            dfs(i, adj, visited)
    return count
```

### Applications
- network reliability
- clustering
- image segmentation

### Complexity
- Time: `O(V + E)`.
- Space: `O(V)`.

### Practice problems
- count connected components
- largest component size
- number of islands in a grid
- friend circles

---

## 6. Cycle Detection

### Undirected graph cycle detection
Use DFS and track the parent node.

#### Intuition
If a visited neighbor is not the parent, a cycle exists.

#### Code

C++:
```cpp
bool dfs_cycle(int node, int parent, vector<vector<int>>& adj, vector<bool>& visited) {
    visited[node] = true;
    for (int nei : adj[node]) {
        if (!visited[nei]) {
            if (dfs_cycle(nei, node, adj, visited)) return true;
        } else if (nei != parent) {
            return true;
        }
    }
    return false;
}

bool hasCycle(int V, vector<vector<int>>& adj) {
    vector<bool> visited(V, false);
    for (int i = 0; i < V; i++) {
        if (!visited[i] && dfs_cycle(i, -1, adj, visited)) return true;
    }
    return false;
}
```

Java:
```java
boolean dfsCycle(int node, int parent, List<List<Integer>> adj, boolean[] visited) {
    visited[node] = true;
    for (int nei : adj.get(node)) {
        if (!visited[nei]) {
            if (dfsCycle(nei, node, adj, visited)) return true;
        } else if (nei != parent) {
            return true;
        }
    }
    return false;
}

boolean hasCycle(int V, List<List<Integer>> adj) {
    boolean[] visited = new boolean[V];
    for (int i = 0; i < V; i++) {
        if (!visited[i] && dfsCycle(i, -1, adj, visited)) return true;
    }
    return false;
}
```

Python:
```python
def dfs_cycle(node, parent, adj, visited):
    visited[node] = True
    for nei in adj[node]:
        if not visited[nei]:
            if dfs_cycle(nei, node, adj, visited):
                return True
        elif nei != parent:
            return True
    return False


def has_cycle(V, adj):
    visited = [False]*V
    for i in range(V):
        if not visited[i] and dfs_cycle(i, -1, adj, visited):
            return True
    return False
```

### Directed graph cycle detection
Use DFS with recursion stack.

#### Intuition
A back-edge to a node currently in the recursion stack means a cycle.

#### Code

C++:
```cpp
bool dfs_cycle_dir(int node, vector<vector<int>>& adj, vector<int>& state) {
    state[node] = 1; // visiting
    for (int nei : adj[node]) {
        if (state[nei] == 0) {
            if (dfs_cycle_dir(nei, adj, state)) return true;
        } else if (state[nei] == 1) {
            return true;
        }
    }
    state[node] = 2; // visited
    return false;
}

bool hasCycleDirected(int V, vector<vector<int>>& adj) {
    vector<int> state(V, 0);
    for (int i = 0; i < V; i++) {
        if (state[i] == 0 && dfs_cycle_dir(i, adj, state)) return true;
    }
    return false;
}
```

Java:
```java
boolean dfsCycleDir(int node, List<List<Integer>> adj, int[] state) {
    state[node] = 1;
    for (int nei : adj.get(node)) {
        if (state[nei] == 0) {
            if (dfsCycleDir(nei, adj, state)) return true;
        } else if (state[nei] == 1) {
            return true;
        }
    }
    state[node] = 2;
    return false;
}

boolean hasCycleDirected(int V, List<List<Integer>> adj) {
    int[] state = new int[V];
    for (int i = 0; i < V; i++) {
        if (state[i] == 0 && dfsCycleDir(i, adj, state)) return true;
    }
    return false;
}
```

Python:
```python
def dfs_cycle_dir(node, adj, state):
    state[node] = 1
    for nei in adj[node]:
        if state[nei] == 0:
            if dfs_cycle_dir(nei, adj, state):
                return True
        elif state[nei] == 1:
            return True
    state[node] = 2
    return False


def has_cycle_directed(V, adj):
    state = [0]*V
    for i in range(V):
        if state[i] == 0 and dfs_cycle_dir(i, adj, state):
            return True
    return False
```

### Union-Find approach
Use union-find for undirected cycle detection.

#### Intuition
If two nodes of an edge already share the same set, adding the edge creates a cycle.

#### Summary
- track parent for each node
- use union by rank / size
- path compression for efficiency

### Applications
- avoiding redundant connections
- detecting dependency cycles
- verifying DAG structures

---

## 7. Topological Sorting

### What is topological sort?
A linear ordering of nodes such that for every directed edge `u -> v`, `u` comes before `v`.

### Why DAG is required
If a cycle exists, no linear ordering can satisfy all directed edges.

### Applications
- task scheduling
- course prerequisites
- build systems
- dependency resolution

### DFS-based topo sort
- DFS post-order gives reversed topological order.
- Push node to stack after visiting all neighbors.

#### Code

C++:
```cpp
void topoDfs(int node, vector<vector<int>>& adj, vector<bool>& visited, stack<int>& st) {
    visited[node] = true;
    for (int nei : adj[node]) {
        if (!visited[nei]) {
            topoDfs(nei, adj, visited, st);
        }
    }
    st.push(node);
}

vector<int> topoSort(int V, vector<vector<int>>& adj) {
    vector<bool> visited(V, false);
    stack<int> st;
    for (int i = 0; i < V; i++) {
        if (!visited[i]) topoDfs(i, adj, visited, st);
    }
    vector<int> order;
    while (!st.empty()) {
        order.push_back(st.top());
        st.pop();
    }
    return order;
}
```

Java:
```java
void topoDfs(int node, List<List<Integer>> adj, boolean[] visited, Deque<Integer> stack) {
    visited[node] = true;
    for (int nei : adj.get(node)) {
        if (!visited[nei]) topoDfs(nei, adj, visited, stack);
    }
    stack.push(node);
}

List<Integer> topoSort(int V, List<List<Integer>> adj) {
    boolean[] visited = new boolean[V];
    Deque<Integer> stack = new ArrayDeque<>();
    for (int i = 0; i < V; i++) {
        if (!visited[i]) topoDfs(i, adj, visited, stack);
    }
    List<Integer> order = new ArrayList<>();
    while (!stack.isEmpty()) order.add(stack.pop());
    return order;
}
```

Python:
```python
def topo_dfs(node, adj, visited, stack):
    visited[node] = True
    for nei in adj[node]:
        if not visited[nei]:
            topo_dfs(nei, adj, visited, stack)
    stack.append(node)


def topo_sort(V, adj):
    visited = [False]*V
    stack = []
    for i in range(V):
        if not visited[i]:
            topo_dfs(i, adj, visited, stack)
    return stack[::-1]
```

### Kahn's Algorithm
- Maintain indegree for each node.
- Start with nodes of indegree 0.
- Remove edges and update indegree.
- If all nodes are removed, result is a topo order.

#### Code

C++:
```cpp
vector<int> kahnTopo(int V, vector<vector<int>>& adj) {
    vector<int> indeg(V, 0);
    for (int u = 0; u < V; u++) {
        for (int v : adj[u]) indeg[v]++;
    }
    queue<int> q;
    for (int i = 0; i < V; i++) if (indeg[i] == 0) q.push(i);
    vector<int> order;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        order.push_back(u);
        for (int v : adj[u]) {
            indeg[v]--;
            if (indeg[v] == 0) q.push(v);
        }
    }
    return order.size() == V ? order : vector<int>();
}
```

Java:
```java
List<Integer> kahnTopo(int V, List<List<Integer>> adj) {
    int[] indeg = new int[V];
    for (int u = 0; u < V; u++) {
        for (int v : adj.get(u)) indeg[v]++;
    }
    Queue<Integer> q = new LinkedList<>();
    for (int i = 0; i < V; i++) if (indeg[i] == 0) q.add(i);
    List<Integer> order = new ArrayList<>();
    while (!q.isEmpty()) {
        int u = q.poll();
        order.add(u);
        for (int v : adj.get(u)) {
            indeg[v]--;
            if (indeg[v] == 0) q.add(v);
        }
    }
    return order.size() == V ? order : new ArrayList<>();
}
```

Python:
```python
def kahn_topo(V, adj):
    indeg = [0]*V
    for u in range(V):
        for v in adj[u]:
            indeg[v] += 1
    q = deque([i for i in range(V) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == V else []
```

### Visualization
- DFS topo: reverse post-order.
- Kahn: gradually peel off layers of nodes with 0 indegree.

### Interview insight
- Kahn's algorithm also detects cycles when result size < V.
- Use topological sort for schedule planning and dependency resolution.

---

## 8. Shortest Path Algorithms

### BFS shortest path
Use BFS when all edges have equal weight.

#### Use case
- unweighted graph
- grid shortest path

#### Implementation

C++:
```cpp
vector<int> shortestPathUnweighted(int V, vector<vector<int>>& adj, int src) {
    vector<int> dist(V, INT_MAX);
    queue<int> q;
    dist[src] = 0;
    q.push(src);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) {
            if (dist[v] == INT_MAX) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return dist;
}
```

Java:
```java
int[] shortestPathUnweighted(int V, List<List<Integer>> adj, int src) {
    int[] dist = new int[V];
    Arrays.fill(dist, Integer.MAX_VALUE);
    Queue<Integer> q = new LinkedList<>();
    dist[src] = 0;
    q.add(src);
    while (!q.isEmpty()) {
        int u = q.poll();
        for (int v : adj.get(u)) {
            if (dist[v] == Integer.MAX_VALUE) {
                dist[v] = dist[u] + 1;
                q.add(v);
            }
        }
    }
    return dist;
}
```

Python:
```python
def shortest_path_unweighted(V, adj, src):
    dist = [float('inf')]*V
    q = deque([src])
    dist[src] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == float('inf'):
                dist[v] = dist[u] + 1
                q.append(v)
    return dist
```

### Dijkstra Algorithm

#### Intuition
- always expand the closest unvisited node.
- uses a min-priority queue.
- works for non-negative weights.

#### Steps
1. initialize distance to source = 0, others = infinity.
2. push source into min-heap.
3. relax edges when a shorter path is found.
4. repeat until heap empty.

#### C++ implementation
```cpp
vector<int> dijkstra(int V, vector<vector<pair<int,int>>>& adj, int src) {
    vector<int> dist(V, INT_MAX);
    dist[src] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, src});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}
```

Java implementation
```java
int[] dijkstra(int V, List<List<int[]>> adj, int src) {
    int[] dist = new int[V];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[src] = 0;
    PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
    pq.add(new int[]{0, src});
    while (!pq.isEmpty()) {
        int[] top = pq.poll();
        int d = top[0], u = top[1];
        if (d > dist[u]) continue;
        for (int[] edge : adj.get(u)) {
            int v = edge[0], w = edge[1];
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.add(new int[]{dist[v], v});
            }
        }
    }
    return dist;
}
```

Python implementation
```python
def dijkstra(V, adj, src):
    dist = [float('inf')] * V
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist
```

#### Complexity
- Time: `O((V + E) log V)`.
- Space: `O(V)`.

#### Limitations
- negative weights break correctness.
- not ideal for dense graphs when using adjacency lists and binary heap.

### Bellman-Ford

#### Intuition
Relax all edges repeatedly.
- works with negative weights.
- detects negative cycles.

#### Steps
1. set source distance = 0.
2. relax each edge `V-1` times.
3. check for negative cycle in one more pass.

#### Code

C++:
```cpp
vector<int> bellmanFord(int V, vector<tuple<int,int,int>>& edges, int src) {
    vector<int> dist(V, INT_MAX);
    dist[src] = 0;
    for (int i = 1; i < V; i++) {
        for (auto [u, v, w] : edges) {
            if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }
    for (auto [u, v, w] : edges) {
        if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
            // negative cycle exists
        }
    }
    return dist;
}
```

Java:
```java
int[] bellmanFord(int V, List<int[]> edges, int src) {
    int[] dist = new int[V];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[src] = 0;
    for (int i = 1; i < V; i++) {
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            if (dist[u] != Integer.MAX_VALUE && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }
    return dist;
}
```

Python:
```python
def bellman_ford(V, edges, src):
    dist = [float('inf')] * V
    dist[src] = 0
    for _ in range(V-1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist
```

#### Complexity
- Time: `O(V * E)`.
- Space: `O(V)`.

#### Use cases
- negative edge weights
- currency exchange arbitrage
- network routing with penalties

### Floyd-Warshall

#### Intuition
Compute all-pairs shortest paths by considering each node as an intermediate.

#### Code

C++:
```cpp
vector<vector<int>> floydWarshall(int V, vector<vector<int>>& dist) {
    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][k] < INT_MAX && dist[k][j] < INT_MAX) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
    return dist;
}
```

Java:
```java
int[][] floydWarshall(int V, int[][] dist) {
    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][k] < Integer.MAX_VALUE && dist[k][j] < Integer.MAX_VALUE) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
    return dist;
}
```

Python:
```python
def floyd_warshall(V, dist):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
```

#### Complexity
- Time: `O(V^3)`.
- Space: `O(V^2)`.

### A* Overview
- Use heuristic to guide search.
- Best for pathfinding in grids or maps.
- Advanced topic not required for most interviews.

### Comparison chart

| Algorithm | Graph type | Weights | Complexity | Good for |
|---|---|---|---|---|
| BFS | unweighted | no | `O(V+E)` | shortest path unweighted |
| Dijkstra | non-negative | yes | `O((V+E) log V)` | weighted positive edges |
| Bellman-Ford | negative allowed | yes | `O(VE)` | negative weights, cycle detection |
| Floyd-Warshall | any weights | yes | `O(V^3)` | all pairs shortest path |
| A* | heuristic available | usually non-negative | depends | pathfinding in grids |

---

## 9. Minimum Spanning Tree (MST)

### Concept
MST is a subset of edges connecting all nodes with minimum total weight.

### Applications
- network design
- road system planning
- clustering

### Prim’s Algorithm
- greedy pick the cheapest edge that expands the tree.
- uses priority queue.

#### C++ implementation
```cpp
int prim(int V, vector<vector<pair<int,int>>>& adj) {
    vector<int> dist(V, INT_MAX);
    vector<bool> used(V, false);
    dist[0] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, 0});
    int total = 0;
    while (!pq.empty()) {
        auto [w, u] = pq.top(); pq.pop();
        if (used[u]) continue;
        used[u] = true;
        total += w;
        for (auto [v, wt] : adj[u]) {
            if (!used[v] && wt < dist[v]) {
                dist[v] = wt;
                pq.push({wt, v});
            }
        }
    }
    return total;
}
```

Java implementation
```java
int prim(int V, List<List<int[]>> adj) {
    int[] dist = new int[V];
    boolean[] used = new boolean[V];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[0] = 0;
    PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
    pq.add(new int[]{0, 0});
    int total = 0;
    while (!pq.isEmpty()) {
        int[] cur = pq.poll();
        int w = cur[0], u = cur[1];
        if (used[u]) continue;
        used[u] = true;
        total += w;
        for (int[] edge : adj.get(u)) {
            int v = edge[0], wt = edge[1];
            if (!used[v] && wt < dist[v]) {
                dist[v] = wt;
                pq.add(new int[]{wt, v});
            }
        }
    }
    return total;
}
```

Python implementation
```python
def prim(V, adj):
    dist = [float('inf')] * V
    used = [False] * V
    dist[0] = 0
    pq = [(0, 0)]
    total = 0
    while pq:
        w, u = heapq.heappop(pq)
        if used[u]:
            continue
        used[u] = True
        total += w
        for v, wt in adj[u]:
            if not used[v] and wt < dist[v]:
                dist[v] = wt
                heapq.heappush(pq, (wt, v))
    return total
```

### Kruskal’s Algorithm
- sort edges by weight.
- add edges if they do not form a cycle.
- use union-find.

#### C++ implementation
```cpp
struct Edge { int u, v, w; };
int kruskal(int V, vector<Edge>& edges) {
    sort(edges.begin(), edges.end(), [](Edge &a, Edge &b){ return a.w < b.w; });
    DSU dsu(V);
    int total = 0;
    for (auto &e : edges) {
        if (dsu.find(e.u) != dsu.find(e.v)) {
            dsu.unite(e.u, e.v);
            total += e.w;
        }
    }
    return total;
}
```

Java implementation
```java
class Edge { int u, v, w; }
int kruskal(int V, List<Edge> edges) {
    edges.sort(Comparator.comparingInt(e -> e.w));
    DSU dsu = new DSU(V);
    int total = 0;
    for (Edge e : edges) {
        if (dsu.find(e.u) != dsu.find(e.v)) {
            dsu.union(e.u, e.v);
            total += e.w;
        }
    }
    return total;
}
```

Python implementation
```python
def kruskal(V, edges):
    edges.sort(key=lambda e: e[2])
    dsu = DSU(V)
    total = 0
    for u, v, w in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            total += w
    return total
```

---

## 10. Disjoint Set Union (Union Find)

### What is DSU?
A structure to maintain partitioned sets.
- `find(x)`: returns representative.
- `union(a, b)`: merges sets.

### Path compression
Attach nodes directly to root during `find`.

### Union by rank/size
Attach smaller tree under larger tree.

### Amortized complexity
Almost constant: `O(α(N))` where `α` is inverse Ackermann.

### Implementation templates

C++:
```cpp
struct DSU {
    vector<int> parent, rank;
    DSU(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    bool unite(int a, int b) {
        a = find(a); b = find(b);
        if (a == b) return false;
        if (rank[a] < rank[b]) swap(a, b);
        parent[b] = a;
        if (rank[a] == rank[b]) rank[a]++;
        return true;
    }
};
```

Java:
```java
class DSU {
    int[] parent, rank;
    DSU(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    boolean union(int a, int b) {
        a = find(a); b = find(b);
        if (a == b) return false;
        if (rank[a] < rank[b]) {
            int tmp = a; a = b; b = tmp;
        }
        parent[b] = a;
        if (rank[a] == rank[b]) rank[a]++;
        return true;
    }
}
```

Python:
```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True
```

### Applications
- Kruskal MST
- cycle detection
- dynamic connectivity
- offline query processing

---

## 11. Advanced Graph Algorithms

### Strongly Connected Components (SCC)

#### Kosaraju
1. run DFS on original graph and record finish times.
2. reverse graph.
3. run DFS in finish time order.
4. each DFS tree in reversed graph is an SCC.

#### Tarjan
- single DFS pass.
- uses discovery time and low link values.
- maintains a stack of active nodes.

### Bridges and Articulation Points
- **bridge**: edge whose removal increases components.
- **articulation point**: vertex whose removal increases components.
- use DFS with discovery time and low values.

### Euler Path / Circuit
- Euler path uses every edge exactly once.
- Euler circuit is an Euler path that starts and ends at same node.
- Conditions depend on degree parity.

### Hamiltonian Path
- visits every vertex exactly once.
- NP-complete in general.
- use backtracking or dynamic programming in special cases.

### Network Flow
- **Ford-Fulkerson**: augment along any path in residual graph.
- **Edmonds-Karp**: use BFS to find shortest augmenting paths.
- applications: bipartite matching, max flow/min cut.

### Bipartite Graph Checking
- Use BFS/DFS to 2-color the graph.
- If a conflict occurs, graph is not bipartite.

### Graph Coloring
- assign colors to nodes so adjacent nodes differ.
- NP-hard for general graphs.
- greedy heuristics work for scheduling.

### Trie + Graph combinations
- model prefix relationships as a tree-like graph.
- useful for word search and auto-completion.

### DSU on Trees (overview)
- use DSU merging technique for subtree queries.
- optimize by merging smaller child maps into larger child maps.

### Heavy Light Decomposition (overview)
- decompose tree into heavy and light chains.
- reduce path queries to segment tree intervals.
- useful for tree path updates and queries.

---

## 12. Graph Patterns for Coding Interviews

### Multi-source BFS
- start BFS from multiple nodes simultaneously.
- useful for nearest distance to a set of sources.
- example: multi-source fire spread, multi-source distance.

### Grid as graph
- treat each cell as a node.
- neighbors are up/down/left/right.
- apply BFS/DFS with bounds checks.

### Shortest path patterns
- use BFS for equal cost edges.
- Dijkstra for weighted positive edges.
- state includes node and extra dimension when needed.

### State graph problems
- nodes represent a state, not physical positions.
- transitions are edges between states.
- common in dynamic programming and puzzles.

### Topological sort patterns
- use when tasks have dependencies.
- detect cycles to ensure feasibility.
- when multiple valid orders exist, Kahn’s algorithm can generate one.

### Implicit graph problems
- graph is defined by rules, not explicit adjacency.
- generate neighbors on the fly.
- example: word ladder, knight moves, BFS on state space.

### Pattern recognition tips
- if the problem mentions "minimum steps", think BFS.
- if it mentions "constraints or dependencies", think DAG/topo sort.
- if it involves all pairs or dense paths, consider Floyd-Warshall.
- if it asks for groups or components, think DFS/BFS.

---

## 13. Competitive Programming Graph Tricks

### Fast input tips
- use fast IO in C++ (`ios::sync_with_stdio(false); cin.tie(NULL);`).
- use buffered input in Java.
- avoid repeated string parsing.

### Adjacency optimization
- reserve vector size in advance.
- reuse adjacency lists across test cases carefully.

### Iterative DFS to avoid recursion limits
- use stack manually.
- avoid deep recursion for large graphs.

### Bitmask + graph ideas
- represent small sets of nodes as bitmasks.
- use DP over subsets in traveling salesman or state graphs.

### Shortest path optimizations
- use adjacency list for sparse graphs.
- use 0-1 BFS for edge weights `0` and `1`.
- use monotonic queue or dial's algorithm when edge weights are small integers.

### Sparse graph tricks
- use `vector<vector<int>>` and avoid matrix.
- compress node labels if nodes are large numbers.
- use adjacency lists or edge lists depending on algorithm.

---

## 14. Real-World Engineering Applications

### Google Maps
- intersections and roads are nodes and edges.
- Dijkstra/A* for routing.
- graph search with heuristics for navigation.

### Social media
- follow graph and friendship graph.
- community detection, influence, recommendation.

### Recommendation systems
- items and users as a bipartite graph.
- graph embeddings and similarity search.

### Compilers
- dependency graphs for compilation order.
- topological sorting for build systems.

### Kubernetes / dependency management
- service dependency graphs.
- DAG-based orchestration.

### AI knowledge graphs
- entities and relationships.
- graph traversal for inference.

### Networking
- packet routing as graph shortest path.
- connectivity and cut analysis.

### Blockchain
- transaction DAGs or blockchains.
- dependency tracking in ledger structures.

---

## 15. Complexity Cheat Sheet

| Algorithm | Best | Average | Worst | Space | Notes |
|---|---|---|---|---|---|
| BFS | `O(V+E)` | `O(V+E)` | `O(V+E)` | `O(V)` | unweighted shortest path |
| DFS | `O(V+E)` | `O(V+E)` | `O(V+E)` | `O(V)` | traversal/backtracking |
| Dijkstra | `O((V+E) log V)` | same | same | `O(V)` | positive weights |
| Bellman-Ford | `O(VE)` | `O(VE)` | `O(VE)` | `O(V)` | negative weights |
| Floyd-Warshall | `O(V^3)` | `O(V^3)` | `O(V^3)` | `O(V^2)` | all pairs |
| Prim | `O((V+E) log V)` | `O((V+E) log V)` | same | `O(V)` | MST |
| Kruskal | `O(E log E)` | same | same | `O(V)` | MST |
| Union-Find | `O(α(N))` | `O(α(N))` | `O(α(N))` | `O(N)` | connectivity |

---

## 16. Interview Preparation Section

### Most asked graph problems
- Graph traversal: `Number of Islands`, `Clone Graph`, `Course Schedule`.
- Shortest path: `Network Delay Time`, `Cheapest Flights Within K Stops`.
- Cycle detection: `Course Schedule II`, `Redundant Connection`.
- MST: `Minimum Spanning Tree`, `Connecting Cities With Minimum Cost`.
- SCC: `Minimum Number of Vertices to Reach All Nodes`.

### Beginner problems
- basic BFS/DFS
- connected components
- bipartite check
- cycle detection

### Intermediate problems
- topological sort
- Dijkstra
- Bellman-Ford
- MST

### Advanced problems
- SCC and bridges
- max flow / min cut
- Hamiltonian path heuristics
- graph state search with multiple variables

### FAANG-style questions
- `Course Schedule`, `Alien Dictionary`, `Network Delay Time`, `Minimum Height Trees`, `Critical Connections`.

### Progression roadmap
1. understand graph basics and representations.
2. master BFS/DFS and connectivity.
3. learn cycle detection and topological sort.
4. tackle shortest path and MST.
5. study DSU and advanced algorithms.
6. solve real interview problems from LeetCode and Codeforces.

### Platforms
- **LeetCode**: structured list of common graph questions.
- **Codeforces**: practice problems with time pressure.
- **AtCoder**: clean graph problems and contests.
- **CSES**: classical graph tasks and patterns.

---

## 17. Practice Section

### Easy problems
- concept: BFS/DFS, connectivity.
  - `Number of Islands` (grid graph)
  - `Find Circle Num` (connected components)
- hint: use visited markers.
- optimal approach: BFS/DFS.

### Medium problems
- concept: topological sort, Dijkstra.
  - `Course Schedule`, `Network Delay Time`.
- hint: model dependencies as DAG.
- optimal approach: Kahn / Dijkstra.

### Hard problems
- concept: SCC, max flow.
  - `Critical Connections`, `Maximum Flow`.
- hint: use advanced graph structures.
- optimal approach: Tarjan / Edmonds-Karp.

---

## 18. Common Mistakes and Debugging

### Visited array mistakes
- forgetting to mark visited before push/recursion.
- reusing visited array across test cases.

### Recursion depth issues
- stack overflow for very deep DFS.
- fix with iterative DFS or increased recursion limit.

### Disconnected graph bugs
- only traversing from one source.
- fix by looping over all nodes.

### Indexing errors
- mixing 0-based and 1-based nodes.
- use consistent indexing and variable names.

### Directed vs undirected confusion
- add edges both ways for undirected graphs.
- treat edge direction carefully in cycle detection.

---

## 19. Revision Notes

### Quick summary
- Graph = vertices + edges.
- Adjacency list best for sparse.
- BFS for unweighted shortest path.
- DFS for deep exploration.
- Topological sort for DAG ordering.
- Dijkstra for positive weights.
- Bellman-Ford for negative weights.
- Kruskal and Prim for MST.
- DSU for connectivity and cycles.

### Key templates
- BFS
- DFS
- Topological sort
- Dijkstra
- DSU

### Core formulas
- `O(V + E)` for traversal.
- `O((V+E) log V)` for Dijkstra.
- `O(VE)` for Bellman-Ford.
- `O(V^3)` for Floyd-Warshall.
- `O(E log E)` for Kruskal.

### Memory tricks
- graph = web, nodes = intersections, edges = roads.
- BFS = waves, DFS = drill.
- topological sort = order tasks by prerequisites.
- union-find = groups with leaders.

---

## Final roadmap
1. Master graph definitions and representations.
2. Build BFS/DFS intuition with examples.
3. Solve connectivity, cycle, and topological sort problems.
4. Learn shortest path and MST algorithms deeply.
5. Add DSU and advanced graph techniques.
6. Practice on interview platforms with a gradual problem set.

**Graphs are one of the most versatile structures in algorithms.** With practice, visual thinking, and code templates, you can handle both standard interview questions and real-world engineering challenges.
