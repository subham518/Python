class Node:
    def __init__(self, value=None):
        self.prev = None
        self.data = value
        self.next = None
    
class DoublyLL:
    def __init__(self):
        self.head = None

    def insertionAtBeginning(self, value):
        t = Node(value)
        # EDGE CASE: List is empty
        if self.head is None:
            self.head = t
            return
        
        # STANDARD: Push existing head forward
        t.next = self.head
        self.head.prev = t
        self.head = t

    def insertionInMiddle(self, value, data):
        """Inserts 'value' after the node containing 'data'"""
        if self.head is None:
            return

        temp = self.head
        while temp is not None:
            if temp.data == data:
                t = Node(value)
                t.next = temp.next
                t.prev = temp
                
                # EDGE CASE: data was found in the LAST node
                if temp.next is not None:
                    temp.next.prev = t
                
                temp.next = t
                return
            temp = temp.next
       
    def insertionAtEnd(self, value):
        t = Node(value)
        # EDGE CASE: List is empty
        if self.head is None:
            self.head = t
            return
        
        # Traverse to the last node
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        # Link new node to the end
        temp.next = t
        t.prev = temp
    
    def deleteDLL(self, value):
        # EDGE CASE: List is empty
        if self.head is None:
            return
        
        temp = self.head

        # EDGE CASE: Deleting the HEAD node
        if temp.data == value:
            self.head = temp.next
            if self.head: # If the list had more than one node
                self.head.prev = None
            return

        # Search for the value
        while temp is not None:
            if temp.data == value:
                # EDGE CASE: Deleting the LAST node
                if temp.next is None:
                    temp.prev.next = None
                else:
                    # STANDARD: Deleting a MIDDLE node
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                return
            temp = temp.next

    def PrintDoublyLL(self):
        if self.head is None:
            print("The list is empty.")
            return
        temp = self.head
        print("Current List: ", end="")
        while temp is not None:
            print(temp.data, end=" <-> " if temp.next else "")
            temp = temp.next
        print()

# --- Testing the implementation ---
obj = DoublyLL()
obj.insertionAtEnd(10)          # [10]
obj.insertionAtEnd(20)          # [10, 20]
obj.insertionAtEnd(30)          # [10, 20, 30]
obj.insertionAtBeginning(5)     # [5, 10, 20, 30]
obj.insertionInMiddle(25, 20)   # [5, 10, 20, 25, 30]
obj.deleteDLL(30)               # [5, 10, 20, 25]
obj.PrintDoublyLL()
