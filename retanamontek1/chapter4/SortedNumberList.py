from NumberList import NumberList
from NumberListNode import NumberListNode

class SortedNumberList(NumberList):
    def __init__(self):
        self.head = None
        self.tail = None
        return
    
    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):

        new_node = NumberListNode(number)

        #if list is empty
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return

        curNode = self.head

        # if the head is greater than the number (aka, inserting a new head)
        if number < curNode.get_data():
            new_node.set_next(self.head)
            self.head.set_previous(new_node)
            self.head = new_node
            
        else: 

            # goes until the node that it needs to succeed    
            while curNode.get_next() != None and curNode.get_next().get_data() < number:
                curNode = curNode.get_next()

            successor_node = curNode.get_next()

            new_node.set_previous(curNode)
            new_node.set_next(successor_node)
            curNode.set_next(new_node)

            if self.tail == curNode:
                self.tail = new_node
            else:
                successor_node.set_previous(new_node)

        pass
    
    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        curNode = self.head
        
        while curNode.get_data() != number:
            curNode = curNode.get_next()

        successor_node = curNode.get_next()
        predecessor_node = curNode.get_previous()

        if curNode == self.head:
            self.head = successor_node
            if self.head != None:
                self.head.set_previous(None)

            return

        if curNode == self.tail:
            self.tail = predecessor_node
            if self.tail != None:
                self.tail.set_next(None)

            return

        predecessor_node.set_next(successor_node)
        successor_node.set_previous(predecessor_node)
        
        return False