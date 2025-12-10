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

        # function to run recursively
        def validating(node, left, right):
            
            if node is None:
                return None

            curNode = node.get_key()
            
            # returns the node if there is a problem. otherwise it keeps running until there's a problem or it ends with None
            if (left is not None and curNode <= left) or (right is not None and curNode >= right):
                return node

            # check left. If wrong, return problem node
            left_check = validating(node.get_left(), left, curNode)
            # So if left_check gives us soemthing that isn't None, then it'll return the node
            if left_check:
                return left_check

            # check right. If wrong, return problem node
            right_check = validating(node.get_right(), curNode, right)
            # Same as left_check, but with the right nodes
            if right_check:
                return right_check
            
            return None

        return validating(root_node, None, None)