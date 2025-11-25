from BSTNode import BSTNode

def preorder_with_min_max(node, min_val = None, max_val = None, visitFn = lambda n,a: None):
    if node == None: return
    
    visitFn(node, min_val, max_val)

    preorder_with_min_max(node.left, min_val, node.key, visitFn)
    preorder_with_min_max(node.right, node.key, max_val, visitFn)

class BSTChecker:
    def __init__(self, root):
        self.root = root
        self.visited = []

    def validate(self):

        def validate_node(node, min_val, max_val):
            if node.key in self.visited or (min_val != None and node.key <= min_val) or (max_val != None and node.key >= max_val):
                raise ValueError(node)

            self.visited.append(node.key)

        try:
            preorder_with_min_max(self.root, visitFn = validate_node)
        except ValueError as e:
            return e.args[0]
        return None

    # check_BST_validity() determines if the tree is a valid BST. If so, None
    # is returned. If not, the first (in preorder traversal) node in violation
    # of BST requirements is returned. Such a node will be one of the following:
    # - A node in the left subtree of an ancestor with a lesser or equal key
    # - A node in the right subtree of an ancestor with a greater or equal key
    # - A node that is encountered more than once during traversal
    @staticmethod
    def check_BST_validity(root):
        return BSTChecker(root).validate()