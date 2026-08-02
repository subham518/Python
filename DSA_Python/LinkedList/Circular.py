class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next

class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertionAtBeginning(self, value):
        t = Node(value)
        # EDGE CASE: List is empty
        if self.head is None:
            self.head = t
            t.next = self.head  # Points to itself to maintain circularity
            return
    
        # Find the last node to update its 'next' pointer
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next
    
        t.next = self.head  # New node points to old head
        temp.next = t       # Last node points to new node
        self.head = t       # Update head to new node

    def insertionInMiddle(self, value, data):
         """Inserts 'value' after the node containing 'data'"""
         # EDGE CASE: List is empty
         if self.head is None:
              print("List empty. Cannot find target data.")
              return

         temp = self.head
         while True:
              if temp.data == data:
                   t = Node(value)
                   t.next = temp.next
                   temp.next = t
                   return
              temp = temp.next
              # EDGE CASE: Traversed full circle and didn't find 'data'
              if temp is self.head:
                  print(f"Data {data} not found.")
                  break

    def insertionAtEnd(self, value):
        t = Node(value)
        # EDGE CASE: List is empty
        if self.head is None:
            self.head = t
            t.next = self.head
            return
        
        # Traverse to the current last node
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next
        
        # Link last node to new node, and new node to head
        temp.next = t
        t.next = self.head

    def deleteCLL(self, value):
        # EDGE CASE: List is empty
        if self.head is None:
            print("Empty!!")
            return
        
        curr = self.head
        # EDGE CASE: Deleting the Head Node
        if curr.data == value:
            # Sub-Case: Head is the ONLY node
            if curr.next == self.head:
                self.head = None
                return
            
            # Sub-Case: Head node with multiple nodes (must update last node's pointer)
            last = self.head
            while last.next is not self.head:
                last = last.next
            self.head = self.head.next # Move head to next node
            last.next = self.head      # Close the circle with the new head
            return
        
        # STANDARD CASE: Deleting middle or last node
        prev = self.head
        curr = self.head.next
        while curr is not self.head:
            if curr.data == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
            
        print("Value not Found!!")

    def printCLL(self):
          if self.head is None:
               print("The list is empty.")
               return
               
          temp = self.head
          print("Current List: ", end="")
          # Traverse and print until we reach the head again
          while True:
               print(temp.data, end=" -> " if temp.next != self.head else "")
               temp = temp.next
               if temp == self.head:
                   break
          print(" (Back to Head)")

# --- Testing ---
obj = CircularLinkedList()
obj.insertionAtEnd(10)
obj.insertionAtEnd(20)
obj.insertionAtEnd(30)
obj.insertionAtBeginning(5)
obj.insertionInMiddle(25, 20)
obj.deleteCLL(30)
obj.printCLL()
