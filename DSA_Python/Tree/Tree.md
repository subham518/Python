# Tree Data Structures in Python: A Technical Guide

## 1. Basics & Terminology

A **Tree** is a hierarchical, non-linear data structure consisting of nodes connected by edges. Key terms:

- **Root**: The topmost node; no parent.
- **Edge**: The connection between two nodes (parent → child).
- **Leaf**: A node with no children.
- **Subtree**: A tree formed by a node and all its descendants.
- **Height**: Maximum distance from a node to its leaf.
- **Depth**: Distance from root to a node.
- **Degree**: Number of children a node has.

---

## 2. Node Implementation

```python
class Node:
    """Basic tree node structure."""
    def __init__(self, value):
        self.value = value
        self.children = []  # For general trees
    
    def add_child(self, child_node):
        self.children.append(child_node)

class BinaryNode:
    """Binary tree node (max 2 children)."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

---

## 3. Binary Tree Traversals

### Depth First Search (DFS)

#### **Pre-order** (Root → Left → Right)
```python
def preorder(node):
    if not node:
        return
    print(node.value)        # Visit root first
    preorder(node.left)      # Traverse left subtree
    preorder(node.right)     # Traverse right subtree
```
**Use case**: Copying trees, getting prefix expressions.

#### **In-order** (Left → Root → Right)
```python
def inorder(node):
    if not node:
        return
    inorder(node.left)       # Traverse left subtree
    print(node.value)        # Visit root
    inorder(node.right)      # Traverse right subtree
```
**Use case**: BST retrieval in sorted order.

#### **Post-order** (Left → Right → Root)
```python
def postorder(node):
    if not node:
        return
    postorder(node.left)     # Traverse left subtree
    postorder(node.right)    # Traverse right subtree
    print(node.value)        # Visit root last
```
**Use case**: Deleting trees, evaluating postfix expressions.

### Breadth First Search (BFS)

```python
from collections import deque

def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```
**Use case**: Level-by-level traversal, finding shortest path.

---

## 4. Binary Search Tree (BST)

### Property
A **BST** maintains the invariant:
- **Left child value** < **Parent value** < **Right child value**

This property enables efficient searching.

### Operations & Big O Complexities

| Operation | Best/Average | Worst |
|-----------|--------------|-------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Inorder Traversal | O(n) | O(n) |

**Worst case** occurs when BST is skewed (like a linked list).

### Quick Search Implementation
```python
def search(node, value):
    if not node:
        return False
    if node.value == value:
        return True
    elif value < node.value:
        return search(node.left, value)
    else:
        return search(node.right, value)
```

---

## 5. Advanced Concepts

### AVL Tree
- **Self-balancing** BST: maintains height difference ≤ 1 between left & right subtrees.
- **Why?** Prevents skewing → guarantees O(log n) search even in worst case.
- **Trade-off**: Rotations during insertion/deletion add overhead.

### Red-Black Tree
- **Self-balancing** BST with color-based constraints (Red/Black nodes).
- **Why?** Less strict than AVL → fewer rotations, faster insertion/deletion.
- **Properties**: No two consecutive red nodes; all paths from root to leaf have equal black-node count.
- **Use**: Java HashMap, C++ std::map, databases.

### Heaps
- **Complete** binary tree where parent ≥ children (**Max Heap**) or parent ≤ children (**Min Heap**).
- **Property**: Only guarantees parent-child relationship, not BST ordering.
- **Operations**: Insert O(log n), Extract O(log n).
- **Use**: Priority queues, heap sort, Dijkstra's algorithm.

```python
import heapq

# Min heap (default in Python)
min_heap = [3, 1, 4, 1, 5]
heapq.heapify(min_heap)  # Converts to heap
heapq.heappush(min_heap, 0)
smallest = heapq.heappop(min_heap)  # Extracts minimum
```

---

## 6. Python Tips & Considerations

### Recursion in Trees
- **Why recursion dominates**: Trees are naturally recursive (node = value + subtrees). Recursion mirrors this elegantly.
- **Drawback**: Stack overhead; deep trees risk stack overflow.

### Python Recursion Limit
```python
import sys
print(sys.getrecursionlimit())      # Default: typically 1000
sys.setrecursionlimit(5000)         # Increase if needed (careful!)
```
**Warning**: Too high = system stack overflow; too low = RecursionError.

### Iterative Alternatives
For deep trees, use **explicit stacks** or **queues** instead of recursion:
```python
# Iterative in-order traversal
def inorder_iterative(root):
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.value)
        current = current.right
```

---

## Quick Reference

| Concept | Time | Space | Notes |
|---------|------|-------|-------|
| DFS Traversal | O(n) | O(h) stack | h = height |
| BFS Traversal | O(n) | O(w) queue | w = max width |
| BST Search (balanced) | O(log n) | O(h) | Skewed = O(n) |
| BST Search (worst) | O(n) | O(n) | Degraded to linked list |
| Heap Insert/Delete | O(log n) | O(1) | Amortized |

---

*This guide is optimized as a review sheet for quick reference during interviews or revision.*
