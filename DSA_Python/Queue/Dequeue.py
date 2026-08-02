class Dequeue:
    def __init__(self):
        # Initialize an empty list to store elements
        self.dq = []

    def isEmpty(self):
        """Checks if the deque has no elements"""
        return len(self.dq) == 0
    
    def insertionAtEnd(self, value):
        """Adds an element to the Rear (Right side)"""
        self.dq.append(value)

    def insertionAtFront(self, value):
        """Adds an element to the Front (Left side)"""
        # insert(0, value) shifts all existing elements to the right
        self.dq.insert(0, value)

    def deleteAtFront(self):
        """Removes and returns the element from the Front (Left side)"""
        # EDGE CASE: Deleting from an empty deque
        if self.isEmpty():
            return "Empty"
        else:
            # pop(0) removes the first item and shifts others to the left
            return self.dq.pop(0)
        
    def deleteAtEnd(self):
        """Removes and returns the element from the Rear (Right side)"""
        # EDGE CASE: Deleting from an empty deque
        if self.isEmpty():
            return "Empty"
        else:
            # pop() removes the last item (very efficient in Python)
            return self.dq.pop()
        
# --- Execution Trace ---
dq = Dequeue()

# 1. Initial State: Should be True and return "Empty" for deletions
print(f"Is Empty? {dq.isEmpty()}")
print(f"Delete End: {dq.deleteAtEnd()}")
print(f"Delete Front: {dq.deleteAtFront()}")

# 2. Insertions:
dq.insertionAtFront(10) # List: [10]
dq.insertionAtEnd(20)   # List: [10, 20]
dq.insertionAtFront(30) # List: [30, 10, 20]

# 3. State after insertions: Should be False
print(f"Is Empty? {dq.isEmpty()}")

# 4. Deletions:
print(f"Deleted from End: {dq.deleteAtEnd()}")     # Returns 20, List: [30, 10]
print(f"Deleted from Front: {dq.deleteAtFront()}") # Returns 30, List: [10]
