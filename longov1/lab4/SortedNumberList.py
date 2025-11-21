'''
Step 3 + 4: Implement insert(), Run code and verify output

Implement SortedNumberList's insert() method to create a new node with the number argument as the node's data, 
then insert the node into the proper sorted position in the linked list. 
Ex: Suppose a SortedNumberList's current list is 23 → 47.25 → 86, then insert(33.5) is called. 
A new node with data value 33.5 is created and inserted between 23 and 47.25, 
thus preserving the list's sorted order and yielding: 23 → 33.5 → 47.25 → 86.

A list of numbers named numbers_to_insert is defined near the start of the main program code in main.py. 
Each is inserted into a SortedNumberList, and the list is printed after each insertion. 
Try changing the array's content, and verify that each output is a sorted list.

Step 5: Implement remove()

Implement SortedNumberList's remove() method. 
The method takes an argument for the number to remove from the list. 
If the number does not exist in the list, the list is not changed and False is returned. 
Otherwise, the first instance of the number is removed from the list and True is returned.

Once remove() is implemented, change the value of the include_removals variable, defined at the start of the main program code, from False to True. 
Run the code and make sure that the list is correct after each removal.

Try different tests in main.py as needed, then submit code for grading. Unit tests are used to grade submitted code, so output from main.py does not affect grading.
'''

from NumberList import NumberList
from NumberListNode import NumberListNode

class SortedNumberList(NumberList):
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):
        # TODO: Type your code here
        # Special case if list is empty
        new_node = NumberListNode(number)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        if number < self.head.get_data():
            new_node.set_next(self.head)
            self.head.set_previous(new_node)
            self.head = new_node
            return

        predecessor = self.head
        while predecessor.get_next() is not None and predecessor.get_next().get_data() < number:
            predecessor = predecessor.get_next()

        successor = predecessor.get_next()
        new_node.set_previous(predecessor)
        new_node.set_next(successor)
        predecessor.set_next(new_node)

        if successor is not None:
            successor.set_previous(new_node)
        else:
            self.tail = new_node
    
        pass
    
    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        # TODO: Type your code here
        removed = False

        current = self.head
        while current is not None and current.get_data() != number:
            current = current.get_next()

        if current is not None:
            predecessor = current.get_previous()
            successor = current.get_next()

            if predecessor is None:
                self.head = successor
            else:
                predecessor.set_next(successor)

            if successor is None:
                self.tail = predecessor
            else:
                successor.set_previous(predecessor)
        
            removed = True

        if removed == True:
            return True
        else:
            return False