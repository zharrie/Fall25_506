from NumberList import NumberList
from NumberListNode import NumberListNode

class SortedNumberList(NumberList):
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):
        #self is the list that I'm trying to insert a new node in to
        newNode = NumberListNode(number, next_node = None, previous_node = None)
        if self.head is None: #if list is empty just add newNode
            self.head = newNode
            self.tail = newNode
        else:
            currentNode = self.head
            if currentNode.data > newNode.data:
                currentNode.previous = newNode
                newNode.next = currentNode
                self.head = newNode
                return #return exits the function
            while currentNode.data <= newNode.data: #compares current node to new node
            #while current node is less than or equal to new node
                if currentNode.next is None: #and if no node after the current node, add new node after
                    currentNode.next = newNode 
                    newNode.previous = currentNode
                    self.tail = newNode
                    break
                else:
                    #but if the node after the current node is greater than new node
                    if currentNode.next.data > newNode.data:
                        temp = currentNode.next
                        currentNode.next = newNode
                        newNode.previous = currentNode
                        newNode.next = temp
                        temp.previous = newNode
                        break
                currentNode = currentNode.next
                #tested this by running main.py      
    
    
    
    # Remove the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        if self.head is None: #if list is empty, node to remove not in list, return false
            return False
        else:
            current_node = self.head           
            number_to_remove = number
            successor = current_node.next
            predecessor = current_node.previous
        while True: 
            if current_node.data == number_to_remove:
                if successor != None:
                    successor.previous = predecessor
                if predecessor != None:
                    predecessor.next = successor
                if current_node == self.head:
                    self.head = successor
                if current_node == self.tail:
                    self.tail = predecessor
                return True  
            predecessor = current_node
            current_node = successor
            if current_node is None:
                return False
            successor = current_node.next
        #if the number does not exist in the list, return false

    #Once remove() implemented,change value of include_removals variable 
    #from False to True - Done!