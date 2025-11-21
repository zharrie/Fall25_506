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
        
        # First establish a helper function to recursively check if the subtree is rooted at node
        def _check_node(node, min_key, max_key, visited):
            if node is None:
                return None
            if node in visited:
                return node
            visited.add(node)
            key = node.get_key()

            if min_key is not None and key <= min_key:
                return node

            if max_key is not None and key >= max_key:
                return node

            bad_node = _check_node(node.get_left(), min_key, key, visited)
            if bad_node is not None:
                return bad_node

            bad_node = _check_node(node.get_right(), key, max_key, visited)
            if bad_node is not None:
                return bad_node

            return None

        visited = set()
        return _check_node(root_node, None, None, visited)