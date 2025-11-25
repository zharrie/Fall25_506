from BSTNode import BSTNode

class BSTChecker:
    # check_BST_validity() determines if the tree is a valid BST. If so, None
    # is returned. If not, the first (in preorder traversal) node in violation
    # of BST requirements is returned. Such a node will be one of the following:
    # - A node in the left subtree of an ancestor with a lesser or equal key
    # - A node in the right subtree of an ancestor with a greater or equal key
    # - A node that is encountered more than once during traversal
    
    @staticmethod
    def check_BST_validity(root_node):
        # TODO: Type your code here
        def helper(node, min_key, max_key, seen_keys):
            if node is None:
                return None
            
            key = node.get_key()
            
            # Check for duplicate keys
            if key in seen_keys:
                return node
            seen_keys.add(key)
            
            # Check BST property violations
            if (min_key is not None and key <= min_key) or (max_key is not None and key >= max_key):
                return node
            
            # Recur for left and right subtrees
            left_violation = helper(node.get_left(), min_key, key, seen_keys)
            if left_violation is not None:
                return left_violation
            
            right_violation = helper(node.get_right(), key, max_key, seen_keys)
            return right_violation
        return helper(root_node, None, None, [])