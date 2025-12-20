from NumberList import NumberList
from NumberListNode import NumberListNode

class SortedNumberList(NumberList):
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):
        new_node = NumberListNode(number,next_node= None, previous_node= None)
        if self.head is None:
            self.head = self.tail = new_node
            return
        
        current_node = self.head
        #insert before head
        if new_node.data <= current_node.data:
            new_node.next = current_node
            current_node.previous = new_node
            self.head = new_node
            return

        while current_node is not None:
            if current_node.next is None:
                current_node.next = new_node
                new_node.previous = current_node
                self.tail = new_node
                break
            elif current_node.next.data > new_node.data:
                temp= current_node.next 
                current_node.next = new_node
                new_node.previous = current_node
                new_node.next = temp 
                temp.previous = new_node
                break
            current_node = current_node.next


        pass
    
    
    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        if self.head is None:
            return False

        current_node = self.head
        successor = current_node.next
        predecessor = current_node.previous

        while current_node is not None:
            if current_node.data == number:
                if successor is not None:
                    successor.previous = predecessor
                if predecessor is not None:
                    predecessor.next = successor
                if current_node == self.head:
                    self.head = successor
                if current_node == self.tail:
                    self.tail = predecessor
                return True

            predecessor = current_node
            current_node = successor
            if current_node is not None:
                successor = current_node.next
        return False