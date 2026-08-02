# DSA with Python: 
# Singly Linked List Implementation

class Node:
    def __init__(self, info, next=None):
         self.data = info
         self.next = next

class SinglyLinkedList:
     def __init__(self, head=None):
          self.head = head

     def insertionAtBeginning(self, value):
          # Edge Case: Works for both empty and non-empty lists
          t1 = Node(value)
          t1.next = self.head
          self.head = t1

     def insertionInMiddle(self, value, data):
          # Edge Case 1: List is empty
          if self.head is None:
               print("List is empty, cannot insert after a value.")
               return

          t1 = Node(value)
          temp = self.head
          
          # Edge Case 2: Using 'while temp' ensures we check every node, 
          # including the very last one.
          while temp is not None:
               if temp.data == data:
                    # Simultaneous assignment prevents breaking the chain
                    t1.next, temp.next = temp.next, t1
                    return
               temp = temp.next
          
          # Edge Case 3: Value 'data' was not found in the list
          print(f"Value {data} not found in the list.")

     def insertionAtEnd(self, value):
          t1 = Node(value)
          # Edge Case 1: List is empty, make new node the head
          if self.head is None:
               self.head = t1
          else:
               temp = self.head
               # Stop at the last node (where next is None)
               while temp.next is not None:
                    temp = temp.next
               temp.next = t1

     def deleteLL(self, value):
          temp = self.head
          prev = temp
          
          # Edge Case 1: If the node to be deleted is the head
          if(temp.data == value):
               self.head = temp.next
               
          # Traverse the list to find the value
          while(temp.next != None):
               if(temp.data == value):
                    # Value found in middle: link previous node to next node
                    prev.next = temp.next
                    break
               else:
                    # Move pointers forward
                    prev = temp
                    temp = temp.next
                    
          # Edge Case 2: Check if the value is at the very last node
          if(temp.data == value):
               prev.next = None
     
     def printLL(self):
          # Edge Case: List is empty
          if self.head is None:
               print("The list is empty.")
               return
               
          temp = self.head
          print("Current List: ", end="")
          while temp is not None:
               print(temp.data, end=" -> " if temp.next else "")
               temp = temp.next
          print() # New line

# --- Testing the Implementation ---

obj = SinglyLinkedList()

# 1. Test insertion at end
obj.insertionAtEnd(10)
obj.insertionAtEnd(20)
obj.insertionAtEnd(30)

# 2. Test insertion at beginning
obj.insertionAtBeginning(5)

# 3. Test insertion in middle (after 20)
obj.insertionInMiddle(40, 20)

# 4. Test insertion after the LAST node
obj.insertionInMiddle(50, 30)

# 5. Test Deletion of a middle node
obj.deleteLL(20)

# 6. Test Deletion of the head node
obj.deleteLL(5)

# 7. Test Deletion of the tail node
obj.deleteLL(50)

# Final Print
obj.printLL()
