from NumberList import NumberList
from NumberListNode import NumberListNode

class SortedNumberList(NumberList):
    def __init__(self):
        self.head = None
        self.tail = None
    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):
        #allocate the node
        new_node = NumberListNode(number)
                    
        #inserting when the list is empty
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        #when list is not empty
        else:
            if new_node.get_data() > self.tail.get_data():
                #if the item to add is greater, append it

                self.tail.next = new_node
                new_node.set_previous(self.tail) 
                self.tail = new_node
            elif new_node.get_data() < self.head.get_data():
                #if it is lesser, preprend it

                new_node.set_next(self.head)
                self.head.previous = new_node
                self.head = new_node
            else:
                # else go through the list starting at the tail,
                # if the new value is greater than tail -> previous,
                # then it should be placed there since the list's head and tail
                # are in sorted order

                current_node = self.tail
                while new_node.previous == None and current_node is not self.head:
                    if new_node.get_data() > current_node.previous.get_data():
                        successor = current_node
                        predecessor = current_node.previous
                        new_node.set_next(successor)
                        new_node.set_previous(predecessor)
                        predecessor.next = new_node
                        successor.previous = new_node
                    else:
                        current_node = current_node.previous

    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        current_node = self.head
        while current_node != None:
            if current_node.get_data() == number:
                successor = current_node.next
                predecessor = current_node.previous

                if successor != None:
                    successor.set_previous(predecessor)
                if predecessor != None:
                    predecessor.set_next(successor)
                if current_node == self.head:
                    self.head = successor
                if current_node == self.tail:
                    self.tail = predecessor
                return True
            else:
                current_node = current_node.next
        
        return False