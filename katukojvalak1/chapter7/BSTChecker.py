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
        if root_node is None:
             return None

        
        visited_ids = set()

        def helper(node, min_key, max_key):
            if node is None:
                return None

            node_id = id(node)
            if node_id in visited_ids:
                return node
            visited_ids.add(node_id)

            key = node.get_key()
            if not (min_key < key < max_key):
                return node

            left_result = helper(node.get_left(), min_key, key)
            if left_result is not None:
                return left_result

            return helper(node.get_right(),key, max_key)

        return helper(root_node, float('-inf'), float('inf'))