class BSTNode:
    def __init__(self, node_key, left_child = None, right_child = None):
        self.key = node_key
        self.left = left_child
        self.right = right_child
    
    def contains(self, key):
        return self.search(key) != None
    
    def get_key(self):
        return self.key
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    # Inserts a new key into the subtree rooted at this node, provided the key
    # doesn't already exist
    def insert_key(self, key):
        # Duplicate keys not allowed
        if self.contains(key):
            return False
        
        # Allocate and insert the new node
        self.insert_node(BSTNode(key))
        return True
    
    def insert_keys(self, keys):
        for key in keys:
            self.insert_key(key)
    
    def insert_node(self, new_node):
        current_node = self
        while current_node != None:
            if new_node.get_key() < current_node.get_key():
                if current_node.get_left() != None:
                    current_node = current_node.get_left()
                else:
                    # Insert new node as current_node's left child
                    current_node.set_left(new_node)
                    current_node = None
            else:
                if current_node.get_right() != None:
                    current_node = current_node.get_right()
                else:
                    # Insert new node as current_node's right child
                    current_node.set_right(new_node)
                    current_node = None
    
    def search(self, search_key):
        current_node = self
        while current_node != None:
            # Return current_node if the key matches
            if current_node.key == search_key:
                return current_node
            
            # Branch left or right
            elif search_key < current_node.key:
                current_node = current_node.get_left()
            else:
                current_node = current_node.get_right()
        # Key not found
        return None
    
    def set_key(self, new_key):
        self.key = new_key
        return self
    
    def set_left(self, new_left):
        self.left = new_left
        return self
    
    def set_right(self, new_right):
        self.right = new_right
        return self