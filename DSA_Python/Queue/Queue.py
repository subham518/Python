class Queue:
    def __init__(self):
        # Initialize an empty list to store queue elements
        self.q = []

    def isEmpty(self):
        """Returns True if the queue has no elements, False otherwise"""
        return len(self.q) == 0
    
    def insert(self, value):
        """Enqueue: Adds an element to the end of the queue"""
        # append() adds the value to the tail/back of the list
        self.q.append(value)

    def delete(self):
        """Dequeue: Removes and returns the first element added"""
        # EDGE CASE: Check if queue is empty before removing (Underflow)
        if self.isEmpty():
            print("Queue is Empty!! Cannot delete.")
            return None
        else:
            # pop(0) removes the element at the head/front of the list
            return self.q.pop(0)

    def peek(self):
        """Returns the front element without removing it"""
        # EDGE CASE: Check if queue is empty
        if self.isEmpty():
            print("Queue is Empty!!")
            return None
        return self.q[0]

    def display(self):
        """Prints the current state of the queue"""
        if self.isEmpty():
            print("Queue is empty.")
        else:
            # Shows the order from Front to Back
            print("Front ->", " -> ".join(map(str, self.q)), "<- Rear")

# --- Testing the Implementation ---
q = Queue()

# Check if empty (Should return True)
print(f"Is queue empty? {q.isEmpty()}")

# EDGE CASE: Deleting from an empty queue
q.delete()

# Inserting (Enqueuing) elements
q.insert(10)
q.insert(20)
q.insert(30)

# Check if empty (Should return False)
print(f"Is queue empty? {q.isEmpty()}")

# Deleting (Dequeuing) elements - Should be 10 then 20
print(f"Deleted: {q.delete()}")
print(f"Deleted: {q.delete()}")

# Peek at the next element (Should be 30)
print(f"Front element: {q.peek()}")

# Show final state
q.display()
