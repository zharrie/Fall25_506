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

        # If the tree has no nodes, it automatically qualifies as a valid BST.
        if root_node is None:
            return None # If the tree is a valid BST, None must be returned.

        visited_ids = set()

        # Node key must be strictly less than all keys in its right subtree and strictly greater than all keys in its left subtree.
        # As soon as a violation is encountered, like a node's key being out of range or a node being visited a second time, return that node.
        def helper(node, min_key, max_key):
            
            if node is None:
                return None # If the tree is a valid BST, None must be returned.
            
            node_id = id(node)
            if node_id in visited_ids:
                return node # ... A node that is encountered more than once during traversal
            visited_ids.add(node_id)

            key = node.get_key()

            
            if min_key is not None and key <= min_key:
                return node # ... A node in the left subtree of an ancestor with a lesser or equal key

            
            if max_key is not None and key >= max_key:
                return node # ... A node in the right subtree of an ancestor with a greater or equal key

            # Preorder traversal: first detect whether the parent node is in violation of BST requirements, followed by the left and right subtrees.
            left_problem = helper(node.get_left(), min_key, key)
            if left_problem is not None:
                return left_problem # ... Otherwise the first-encountered problematic node must be returned.


            right_problem = helper(node.get_right(), key, max_key)
            if right_problem is not None:
                return right_problem # ... Otherwise the first-encountered problematic node must be returned.

            return None # If neither subtree produced an error, this branch is valid.

        result = helper(root_node, None, None)
        print(result)
        return result # If the tree is a valid BST, None must be returned.