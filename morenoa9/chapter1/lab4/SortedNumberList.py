from NumberList import NumberList
from NumberListNode import NumberListNode

class SortedNumberList(NumberList):
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):
        newnode= NumberListNode(number)
        
        if self.head is None:
            self.head= self.tail=newnode
            return
        
        if number<= self.head.get_data():
            newnode.set_next(self.head)
            self.head.set_previous(newnode)
            self.head=newnode
            return

        if number>= self.tail.get_data():
            newnode.set_previous(self.tail)
            self.tail.set_next(newnode)
            self.tail= newnode
            return
        
        current= self.head
        while current is not None and current.get_data()< number:
            current= current.get_next()

        previousnode= current.get_previous()
        newnode.set_next(current)
        newnode.set_previous(previousnode)
        previousnode.set_next(newnode)
        current.set_previous(newnode)
        
    
    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        current= self.head

        while current is not None:
            if current.get_data()== number:
                if current== self.head:
                    self.head= current.get_next()
                    if self.head is not None:
                        self.head.set_previous(None)
                    else:
                        self.tail=None
                
                elif current== self.tail:
                    self.tail= current.get_previous()
                    self.tail.set_next(None)
                else:
                    previousnode= current.get_previous()
                    nextnode=current.get_next()
                    previousnode.set_next(nextnode)
                    nextnode.set_previous(previousnode)
                return True
            current= current.get_next()
            
        return False