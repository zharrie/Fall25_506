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
        trav_list = [] #initiating a list to keep track of traversals
        #the inf floats set and endless range for easy checking of the root node
        return BSTChecker.recursivePreorder(root_node, float('-inf'), float('inf'), trav_list)

    def recursivePreorder(root_node, lower_range, upper_range, trav_list):
        #this is the initial check of the preorder algorithm
        if root_node is None:
            return

        #get node value for ease    
        currentNode = root_node.get_key()
       
        #check if the node is present in the list of traversed nodes
        for N in trav_list:
            if N == currentNode:
                #if it is present, return right away
                return root_node
        #if not we will add to our list so we know we visited the node
        trav_list.append(currentNode)

        #check the node is within the proper range
        if not lower_range <= currentNode <= upper_range:
            #if it is not, then return it right away (the root node is not impacted since the range starts with infinity)
            return root_node

        #first recursive call for the left subtree since we are using preorder
        l_subtree_checks = BSTChecker.recursivePreorder(root_node.get_left(), lower_range, currentNode, trav_list)
        
        #need to obtain the results of the recursive check of the substrees in order to return the findings and not None
        if l_subtree_checks is not None:
            return l_subtree_checks
        
        #second recursive call to the right substrees
        r_subtree_checks= BSTChecker.recursivePreorder(root_node.get_right(), currentNode, upper_range, trav_list)
        if r_subtree_checks is not None:
            return r_subtree_checks

        #return none means the tree is valid
        return None
