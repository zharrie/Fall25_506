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
            return root_node

        visited= set()

        stack= [(root_node,float('-infinity'),float('infinity'))]

        while stack:
            node,min_key,max_key= stack.pop()

            if node in visited:
                return node
            visited.add(node)

            key= node.get_key()

            if not (min_key< key< max_key):
                return node
           
            right= node.get_right()
            left=node.get_left()
            
            if right is not None:
                stack.append((right,key,max_key))

            if left is not None:
                stack.append((left,min_key,key))
                
        return None