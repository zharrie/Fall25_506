from NumberList import NumberList
from NumberListNode import NumberListNode

class SortedNumberList(NumberList):
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):
        new_node = NumberListNode(number)

        # In case of empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # In case of smallest number
        if number <= self.head.get_data():
            new_node.set_next(self.head)
            self.head.set_previous(new_node)
            self.head = new_node
            return  

        # In case of largest number
        if number >= self.tail.get_data():
            new_node.set_previous(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
            return

        # In case of in between
        current = self.head
        while current is not None and current.get_data() < number:
            current = current.get_next()
        prev = current.get_previous()
        new_node.set_previous(prev)
        new_node.set_next(current)
        prev.set_next(new_node)
        current.set_previous(new_node)
        

    
    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        current = self.head

        # Search through
        while current is not None and current.get_data() != number:
            current = current.get_next()

        # In case of no result
        if current is None:
            return False

        # In case of one item
        if current == self.head and current == self.tail:
            self.head = None
            self.tail = None
            return True

        # In case of first item
        if current == self.head:
            next = current.get_next()
            next.set_previous(None)
            self.head = next
            return True

        # In case of last item
        if current == self.tail:
            prev = current.get_previous()
            prev.set_next(None)
            self.tail = prev
            return True

        prev = current.get_previous()
        next = current.get_next()
        prev.set_next(next)
        next.set_previous(prev)
        return True