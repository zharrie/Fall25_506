
# ======================
# BST for sorting by numerical values
# ======================

from verbose import verbose_log  # keep the same import so this file stays compatible with the project


class BinarySearchTreeNode:
    """
    Node for the binary search tree.

    Attributes:
        key: tuple (rating, title) or (play_count, title)
        song: Song object
        left: left child node or None
        right: right child node or None
    """

    def __init__(self, key, song):
        self.key = key  # assign the key value to the tree's node
        self.song = song  # assign the Song object as data so traversal can return songs
        self.left = None  # left child starts empty because this is a new leaf node
        self.right = None  # right child starts empty because this is a new leaf node


#region Stiched
class BinarySearchTree:
    """
    Simple BST can take an attribute (rating or play count).
    Used to demonstrate tree-based sorting by a numerical data point.
    """

    def __init__(self, attribute):
        self.root = None  # start with an empty tree
        self.attribute = attribute  # recognize what numeric field we are sorting by ("rating" or "play_count") to create the tree accordingly
        verbose_log("Initialized empty BinarySearchTree.")  # log for debug / demo output

    def insert(self, song):
        """
        Insert a song into the tree using (attribute, title) as the key.

        song: Song
        """
        # the key inserted will be based on the attribute passed
        if self.attribute == "rating":
            key = (song.rating, song.title)  # rating first so primary sort is numeric, title breaks ties
        elif self.attribute == "play_count":
            key = (song.play_count, song.title)  # play_count first so primary sort is numeric, title breaks ties
        else:
            key = (0, song.title)  # this is a fallback so the code won't break if a non compatible attribute somehow got passed

        new_node = BinarySearchTreeNode(key, song)  # finally, make and insert the node to the tree

        # If there is no root yet (tree is empty) the new node becomes the root
        if self.root is None:
            self.root = new_node  # set the first node as the root of the tree
            verbose_log("Inserted root node in BinarySearchTree: " + str(song))  # log what we inserted
            return  # insertion is done

        # For when the tree is not empty:
        current_node = self.root  # start from the root because every BST insert begins there
        while current_node is not None: # while loop will keep going until the node is inserted basically (a spot is found for the node)
            verbose_log("Comparing new node key " + str(key) + " to existing node key " + str(current_node.key) + " for BST insertion.")  # show the comparison step-by-step
            
            # these are the actual steps to follow to insert
            if key < current_node.key:
                # New key is "smaller", so we need to go left (BST rules)
                if current_node.left is None:
                    current_node.left = new_node  # found an empty left spot, so insert here
                    verbose_log("Inserted new node to the LEFT of current node.")  # log the direction chosen so we can check it works
                    return  # insert is done
                current_node = current_node.left  # keep going to the left until we find an empty spot
            else:
                # New key is "greater or equal", so we go right
                if current_node.right is None:
                    current_node.right = new_node  # found an empty right spot, so insert here
                    verbose_log("Inserted new node to the RIGHT of current node.")  # log the direction chosen
                    return  # insert is done
                current_node = current_node.right  # keep going right until we find an empty spot

    def inorder_traversal(self):
        """
        Perform an inorder traversal.

        returns: list of Song objects sorted by rating (and title)

        This is needed for using BST sort, which is an option we provide users to sort their songs (for rating and play count)
        """
        ordered_song_list = []  # this list will collect songs in sorted order as we traverse

        def visit(node):
            if node is not None:  # base case for recursion. will stop when we hit an empty child
                visit(node.left)  # visit left subtree first because it holds the "smaller" keys
                ordered_song_list.append(node.song)  # then visit the current node (in sorted position)
                visit(node.right)  # finally visit right subtree because it holds the "larger" keys

        verbose_log("Starting inorder traversal of BinarySearchTree.")  # log when traversal begins
        visit(self.root)  # start traversal at the root node
        verbose_log("Inorder traversal produced " + str(len(ordered_song_list)) + " songs.")  # log how many songs we returned
        return ordered_song_list  # return the sorted list of Song objects

    #region Rev. inorder traversal
    def reverse_inorder(self):
        """
        Perform reverse inorder to be able to sort high to low as well

        Returns: list of song objects in greatest to least order

        After implementing the BST sort with inorder traversal we realized it would also
        be good to be able to return things from greatest to lease (the reverse order of the BST)
        so we created reverse_inorder to give users that option as well.
        """
        ordered_song_list = []  # this list will collect songs from greatest to least

        def visit(node):
            if node is not None:  # base case for recursion. will stop when we hit an empty child
                visit(node.right)  # visit right subtree first because it holds the "larger" keys
                ordered_song_list.append(node.song)  # then visit the current node (next largest)
                visit(node.left)  # finally visit left subtree because it holds the "smaller" keys

        verbose_log("Starting reverse inorder traversal of BinarySearchTree.")  # log when reverse traversal begins
        visit(self.root)  # start traversal at the root node
        verbose_log("Reverse inorder traversal produced " + str(len(ordered_song_list)) + " songs.")  # log how many songs we returned
        return ordered_song_list  # return the reverse-sorted list of Song objects
    #endregion
#endregion
