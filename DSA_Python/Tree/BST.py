class Node:
    def __init__(self, value):
        # Left pointer for storing smaller values
        self.left = None
        # Node content payload
        self.data = value 
        # Right pointer for storing larger values
        self.right = None

def insert(root, value):
    """Inserts a unique value into the correct position of the BST"""
    # BASE CASE: Found the insertion position, construct a new node here
    if root is None:
        return Node(value)
    
    # EDGE CASE: Deduplication. If value exists, ignore to maintain unique set properties
    if root.data == value:
        return root
    
    # RECURSIVE STEP: Branch left if incoming value is smaller than current node
    if root.data > value:
        root.left = insert(root.left, value)
    # RECURSIVE STEP: Branch right if incoming value is larger than current node
    else:
        root.right = insert(root.right, value)
    
    # Return structural layout back to parent stack frame
    return root

def search(root, value):
    """Recursively searches for a value and prints the result"""
    # BASE CASE: Reached leaf terminal bounds without finding value
    if root is None:
        print("Not Found")
        return
    
    # BASE CASE: Match found
    if root.data == value:
        print("Found")
        return
    
    # RECURSIVE STEP: Route search target left or right based on relative size
    if root.data > value:
        return search(root.left, value)
    else:
        return search(root.right, value)

def delete(root, value):
    """Removes a value from the BST while preserving structural invariants"""
    # BASE CASE: Element to delete is missing from the tree
    if root is None:
        return root
    
    # SEARCH PHASE: Navigate tree structural layers to find target node
    if root.data > value:
        root.left = delete(root.left, value)
    elif root.data < value:
        root.right = delete(root.right, value)
    
    # DELETION PHASE: Target node matching 'value' found
    else:
        # CASE 1: Node has only a Right child or No children (Leaf Node)
        if root.left is None:
            return root.right
        
        # CASE 2: Node has only a Left child
        elif root.right is None:
            return root.left
        
        # CASE 3: Node has Two children
        else:
            # Extract the lowest value node from the right subtree
            succ = get_inorderSuccessor(root)
            # Copy the successor value to the current node
            root.data = succ.data
            # Eliminate the duplicate successor node from the right subtree
            root.right = delete(root.right, succ.data)
            
    return root

def get_inorderSuccessor(root):
    """Utility helper: Finds the smallest element in the right subtree"""
    # Step into right subtree once
    curr = root.right
    # Slide left until hitting leftmost child leaf boundary
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

def inOrder(root):
    """LVR Traversal: Prints the BST values in ascending ordered format"""
    if root is not None:
        inOrder(root.left)         # Left boundary path check
        print(root.data, end=" ")  # Process node payload data
        inOrder(root.right)        # Right boundary path check

# --- Program Execution Lifecycle ---
# Setup Initial Root element
root = insert(None, 20)

# Build out complex structural branches
insert(root, 15)
insert(root, 30)
insert(root, 40)
insert(root, 18)
insert(root, 12)
insert(root, 11)

print("Initial Tree InOrder:")
inOrder(root)  # Outputs sorted values: 11 12 15 18 20 30 40
print("\n")

print("Executing Target Search:")
search(root, 40)   # Outputs: Found
search(root, 100)  # Outputs: Not Found

print("\nTree after deleting node 15 (Node with two children):")
delete(root, 15)
inOrder(root)  # Outputs sorted values: 11 12 18 20 30 40
print()


# Note:
# 1. inorder traversal of bst.
# 2. arrange the elements of bst in increasing order.
# 3. check the bst is valid or not.

# In all these 3 cases ans is inorder traversal, cause a valid bst means elemets are in increasing order and when inorder traversal is done for a bst it will print the elements in increasing order.