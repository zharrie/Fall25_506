from NumberList import NumberList
from NumberListNode import NumberListNode

class SortedNumberList(NumberList):
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):
        cur_node = self.head
        if cur_node == None:
            self.head = NumberListNode(number)
            self.tail = self.head
            return
        while cur_node != None and cur_node.get_data() < number:
            cur_node = cur_node.get_next()
        if cur_node == None:
            self.tail.set_next(NumberListNode(number, previous_node = self.tail))
            self.tail = self.tail.get_next()
        else:
            pre_node = cur_node.get_previous()
            cur_node.set_previous(NumberListNode(number, cur_node, pre_node))
            if pre_node == None:
                self.head = cur_node.get_previous()
            else:
                pre_node.set_next(cur_node.get_previous())

    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        if self.head == None or number < self.head.get_data() or number > self.tail.get_data():
            return False
        cur_node = self.head
        while cur_node != None and cur_node.get_data() < number:
            cur_node = cur_node.get_next()
        if cur_node == None or cur_node.get_data() != number:
            return False
        pre_node = cur_node.get_previous()
        suc_node = cur_node.get_next()
        if pre_node != None: pre_node.set_next(suc_node)
        else: self.head = suc_node
        if suc_node != None: suc_node.set_previous(pre_node)
        else: self.tail = pre_node
        return True