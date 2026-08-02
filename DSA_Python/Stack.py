class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.s = []

    def push(self, value):
        """Adds an element to the top of the stack"""
        # Using index 0 as the 'Top' of the stack
        self.s.insert(0, value)

    def peek(self):
        """Returns the top element without removing it"""
        # EDGE CASE: Checking if peek is called on an empty stack
        if self.isEmpty():
            raise Exception("Stack is Empty!! Cannot peek.")
        else:
            return self.s[0]
    
    def pop(self):
        """Removes and returns the top element"""
        # EDGE CASE: Checking if pop is called on an empty stack (Stack Underflow)
        if self.isEmpty():
            raise Exception("Stack is Empty!! Cannot pop.")
        else:
            # Removes element at index 0 (the current top)
            return self.s.pop(0)
        
    def isEmpty(self):
        """Helper: Returns True if the stack has no elements"""
        return len(self.s) == 0

    def size(self):
        """Helper: Returns the number of elements in the stack"""
        return len(self.s)

    def printS(self):
        """Prints the stack from bottom to top"""
        if self.isEmpty():
            print("Stack is empty.")
            return
        
        print("Stack (Bottom to Top):")
        # Iterates backwards through the list to show the 'Bottom' first
        for i in range(len(self.s) - 1, -1, -1):
            print(f"| {self.s[i]} |")
        print(" --- ")

# --- Testing the Implementation ---
obj = Stack()

# EDGE CASE: Testing peek/pop on empty stack
try:
    obj.peek()
except Exception as e:
    print(f"Caught expected error: {e}")

obj.push(10)
obj.push(20)
obj.push(30)

t1 = obj.peek()  # Should be 30
print(f"Peek: {t1}")

t2 = obj.pop()   # Should remove 30
print(f"Popped: {t2}")

t3 = obj.peek()  # Should now be 20
print(f"New Peek: {t3}")

obj.push(100)
obj.printS()
