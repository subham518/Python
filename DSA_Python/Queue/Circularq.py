class CircularQueue():
    def __init__(self, size):
        self.size = size
        # Initialize list with None to represent empty slots
        self.cq = [None] * size
        # Pointers: -1 indicates the queue is completely empty
        self.rear = self.front = -1

    def enqueue(self, value):
        """Adds an element to the rear of the queue"""
        # EDGE CASE: Queue Overflow
        # If the next position of rear is front, the circle is closed (full)
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full.")
        
        # EDGE CASE: First element being added
        elif self.rear == -1:
            self.rear = self.front = 0
            self.cq[self.rear] = value
        
        # STANDARD: Move rear forward circularly and add value
        else:
            self.rear = (self.rear + 1) % self.size
            self.cq[self.rear] = value

    def dequeue(self):
        """Removes and prints the element from the front"""
        # EDGE CASE: Queue Underflow
        if self.front == -1:
            print("Queue is Empty.")
        
        # EDGE CASE: Only one element left in the queue
        elif self.front == self.rear:
            print(f"Dequeued: {self.cq[self.front]}")
            # Reset pointers to -1 as the queue is now empty
            self.front = self.rear = -1
        
        # STANDARD: Print front value and move front forward circularly
        else:
            print(f"Dequeued: {self.cq[self.front]}")
            self.front = (self.front + 1) % self.size

    def display(self):
        """Helper to visualize the circular list state"""
        if self.front == -1:
            print("Queue is Empty.")
            return

        print("Current Queue: ", end="")
        temp = self.front
        while True:
            print(self.cq[temp], end=" ")
            if temp == self.rear:
                break
            temp = (temp + 1) % self.size
        print()

# --- Execution Trace ---
cq = CircularQueue(3)

cq.dequeue()      # 1. Empty check
cq.enqueue(10)    # 2. Front=0, Rear=0
cq.enqueue(20)    # 3. Front=0, Rear=1
cq.enqueue(30)    # 4. Front=0, Rear=2 (Now Full)
cq.enqueue(40)    # 5. Full check (cannot add 40)

cq.dequeue()      # 6. Dequeues 10, Front=1, Rear=2
cq.enqueue(40)    # 7. Wraps around! Rear moves from 2 to 0. Front=1, Rear=0

cq.display()      # 8. Should show 20, 30, 40
