class NumberListNode:
    # Constructs this node with the specified numerical data value. The next
    # and previous references are optional and each defaults to None.
    def __init__(self, initial_data, next_node = None, previous_node = None):
        self.data = initial_data
        self.next = next_node
        self.previous = previous_node
    
    # Gets this node's data
    def get_data(self):
        return self.data
    
    # Gets this node's next reference
    def get_next(self):
        return self.next
    
    # Gets this node's previous reference
    def get_previous(self):
        return self.previous
    
    # Sets this node's data
    def set_data(self, new_data):
        self.data = new_data
    
    # Sets this node's next reference
    def set_next(self, new_next):
        self.next = new_next
    
    # Sets this node's previous reference
    def set_previous(self, new_previous):
        self.previous = new_previous