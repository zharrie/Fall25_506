# Base class for a double-linked list of NumerListNodes
class NumberList:
    def __init__(self):
        self.head = None
        self.tail = None
   
    def get_head(self):
        return self.head
    
    def to_string(self, separator = ", ", prefix = "", suffix = ""):
        # Start the result with the prefix
        result = prefix
        
        # Start traversal at the list's head
        node = self.head
        
        # First node's data is added without accompanying separator
        if node != None:
            result += f"{node.get_data():.2f}"
            node = node.get_next()
        else:
            # Special case for empty list
            result += "empty"
        
        # Remaining nodes are added with separator before
        while node != None:
            result += f"{separator}{node.get_data():.2f}"
            node = node.get_next()
        
        # Suffix is added last
        result += suffix
        
        return result
    
    # Returns a string with this list's contents in order from head to tail
    def __str__(self):
        return self.to_string()