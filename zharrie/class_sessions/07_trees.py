# Trees
"""
The key advantage of BSTs is performance. A linked list with 10,000 elements may require up to 10,000 comparisons to find an item. 
A balanced BST with the same number of elements requires only about 14 comparisons - that's roughly a 700x speedup!

Part 1: Foundation - Building the Basic Structure
1.1 From Linked Lists to Binary Trees
- A linked list, each node has up to one successor. 
- A binary tree extends this concept - each node has up to two children, called the left child and the right child. 
The term "binary" refers to these two children.

1.2 The BST Ordering Property
A binary search tree is a special type of binary tree that maintains a critical ordering property: for every node, all keys in the node's left subtree are smaller than the node's key, and all keys in the node's right subtree are larger than the node's key. 
This ordering property is what enables fast searching - at each step, we can eliminate half of the remaining tree from consideration.

1.3 Implementing the Basic Classes
Let's start by creating our foundational classes. 
The BSTNode class represents a single node with a key and references to its children:
"""

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# The BinarySearchTree class manages the overall tree structure with a reference to the root node:
class BinarySearchTree:
    def __init__(self):
        self.root = None

"""
1.4 Essential Terminology

- The root is the topmost node with no parent - in our implementation, this is self.root. 
- A leaf is a node with no children, meaning both its left and right attributes are None. 
- An internal node is any node that has at least one child, and a parent is simply a node that has children.

When discussing tree structure, an edge refers to the link from a node to its child (our left or right references). 
The depth of a node is the number of edges from the root to that node, so the root has depth 0. 
All nodes at the same depth form a level in the tree. 
The height of a tree is the largest depth of any node - for example, a tree with just a root has height 0.

A subtree is any node X together with all its descendants, forming a valid binary tree on its own. 
Ancestors of a node include its parent, the parent's parent, and so on up to the root. 
Descendants include the node's children, their children, and so on down the tree.
"""


# Part 2: Implementing Insertion
"""
2.1 The insert_node() Method
Adding nodes to our tree requires finding the correct position while maintaining the BST ordering property:
"""
def insert_node(self, new_node):
    # Check if tree is empty
    if self.root == None:
        self.root = new_node
    else:
        current_node = self.root
        while current_node != None:
            if new_node.key < current_node.key:
                # Go left
                if current_node.left == None:
                    current_node.left = new_node
                    current_node = None
                else:
                    current_node = current_node.left
            else:
                # Go right
                if current_node.right == None:
                    current_node.right = new_node
                    current_node = None
                else:
                    current_node = current_node.right
"""
2.2 How Insertion Works
If the tree is empty, insertion is simple - we just set the root to the new node. 
For non-empty trees, we start at the root and navigate down. 
At each step, if the new key is less than the current node's key, we try to go left. 
If the left child is None, we've found the insertion point and place the new node there. 
Otherwise, we move to the left child and continue searching. 
The same logic applies for the right side when the new key is greater than or equal to the current node's key. 
The result is that the new node is always inserted as a leaf, maintaining the BST ordering property.
"""

"""
2.4 Insertion Complexity

Since insertion traverses from the root to a leaf position, visiting one node per level, the analysis parallels that of search. 
A BST with N nodes has at least log 2(N) levels when balanced and at most N levels when completely unbalanced. 
This gives us a best case runtime of O(log N) and worst case of O(N). 
"""

""""
Part 3: Implementing Search

3.1 The Search Method
The search method locates a node with a specific key or returns None if not found:
"""
def search(self, desired_key):
    current_node = self.root
    while current_node is not None:
        # Return the node if the key matches
        if current_node.key == desired_key:
            return current_node
            
        # Navigate left if search key is less
        elif desired_key < current_node.key:
            current_node = current_node.left
            
        # Navigate right if search key is greater
        else:
            current_node = current_node.right
  
    # Key not found
    return None

"""
3.2 Understanding the Search Algorithm
The search algorithm starts at the root and enters a loop where three cases can occur. 
If the current node's key matches our desired key, we've found it and return the node immediately. 
If the desired key is less than the current node's key, the BST ordering property guarantees that the key must be in the left subtree, so we move to the left child. 
Similarly, if the desired key is greater, we move to the right child. We continue this process until we either find the key or reach a None reference, indicating the key doesn't exist in the tree.

The efficiency comes from the fact that each comparison eliminates half of the remaining tree from consideration. 
We only visit nodes along a single path from root to leaf, never exploring entire subtrees unnecessarily.

3.3 Analyzing Search Complexity
We say that a search operation visits a node when it accesses that node's key during the operation. 
In the worst case, we visit all nodes from the root down to the deepest leaf, requiring H + 1 comparisons where H is the tree's height. 
This gives us a runtime complexity of O(H).

The relationship between height and performance is crucial. 
In the best case with a balanced tree, the height H equals approximately log 2(N) where N is the number of nodes, giving us O(log N) performance. 
However, in the worst case with a completely unbalanced tree (essentially a linked list), H equals N - 1, degrading to O(N) performance. 
This is why tree balance matters so much for BST performance.

"""

# 2.5 Testing Our Implementation
tree = BinarySearchTree()
tree.insert_key(17)
tree.insert_key(32)
tree.insert_key(10)
tree.insert_key(3)
tree.insert_key(21)

# Search for keys 3 and 99
for search_key in [3, 99]:
    if tree.contains(search_key):
        print(f"Found node with key = {search_key}.")
    else:
        print(f"Key {search_key} not found.")
"""
This produces the output: Found node with key = 3. and Key 99 not found.. The resulting tree structure looks like this:


       17
      /  \
    10    32
   /     /
  3    21
"""

"""
Part 4: Understanding Tree Structures and Performance

Before we implement more complex operations, we need to understand how tree structure affects performance. 
Certain structural properties can guarantee better performance.

4.1 Complete Binary Trees
A binary tree is complete if all levels except possibly the last are completely filled, and all nodes in the last level are as far left as possible. 
The critical property of complete trees is that they minimize height. A complete tree with N nodes has height 
⌊log 2(N)⌋, which guarantees O(log N) performance for all operations. This is why balanced BSTs are so valuable in practice.

4.2 Full and Perfect Binary Trees

A full binary tree is one where every node has either 0 or 2 children - no nodes have exactly one child. 
A perfect binary tree is even more constrained: all internal nodes have exactly 2 children, and all leaf nodes are at the same level. 
Perfect trees represent the most balanced structure possible and guarantee optimal performance. However, perfect trees can only contain 
nodes for some height h, so we can't always achieve this structure for arbitrary numbers of nodes.
"""
"""
Part 5: Implementing Traversals
5.1 Understanding Traversal
A tree traversal algorithm visits all nodes in the tree exactly once and performs some operation on each node. 
To "visit a node" simply means to perform whatever action we're interested in - printing the node's key, saving it to a file, adding it to a list, or any other operation.

5.2 Inorder Traversal for Sorted Output
The most important traversal for BSTs is inorder traversal, which visits nodes in sorted order from smallest to largest. 
The pattern is simple: for each node, recursively visit the left subtree first, then visit the node itself, then recursively visit the right subtree.

"""
def print_inorder(self, node):
    if node is not None:
        self.print_inorder(node.left)    # Visit left subtree
        print(node.key)                   # Visit current node
        self.print_inorder(node.right)    # Visit right subtree

# This produces sorted output because of the BST ordering property. 
# The left subtree contains all smaller keys, the right subtree contains all larger keys, so visiting them in the order left-node-right naturally produces an ascending sequence. 
# For our example tree from earlier, inorder traversal produces: 3, 10, 17, 21, 32.
"""
5.3 Generalized Traversal with Functions
The previous implementation is limited because it only prints. 
What if we want to save keys to a file, add them to a list, or perform calculations? 
Rather than writing separate traversal methods for each use case, we can generalize by passing a function as a parameter:
"""

def inorder_traversal(self, node, visit_function):
    if node is not None:
        self.inorder_traversal(node.left, visit_function)
        visit_function(node.key)
        self.inorder_traversal(node.right, visit_function)

# Print keys
tree.inorder_traversal(tree.root, lambda key: print(key))

# Collect keys in a list
keys = []
tree.inorder_traversal(tree.root, lambda key: keys.append(key))

# 5.4 Other Traversal Orders
# Reverse inorder traversal visits nodes from largest to smallest by reversing the pattern - visit right subtree, then node, then left subtree:
def reverse_inorder_traversal(self, node, visit_function):
    if node is not None:
        self.reverse_inorder_traversal(node.right, visit_function)
        visit_function(node.key)
        self.reverse_inorder_traversal(node.left, visit_function)

#Preorder traversal visits each node before its children (node, then left subtree, then right subtree):
def preorder_traversal(self, node, visit_function):
    if node is not None:
        visit_function(node.key)
        self.preorder_traversal(node.left, visit_function)
        self.preorder_traversal(node.right, visit_function)

# Postorder traversal visits each node after its children (left subtree, then right subtree, then node):
def postorder_traversal(self, node, visit_function):
    if node is not None:
        self.postorder_traversal(node.left, visit_function)
        self.postorder_traversal(node.right, visit_function)
        visit_function(node.key)

"""
Part 6: Successors and Predecessors

6.1 Understanding BST Ordering
A BST defines a natural ordering among nodes from smallest to largest. 
A node's successor is the next node in this sorted order. For example, in the sequence 3→10→17→21→32, the successor of 10 is 17. 
Similarly, a node's predecessor is the previous node in sorted order.

6.2 Finding a Successor
Finding a node's successor requires understanding two cases. 
If the node has a right subtree, the successor is the leftmost child of that right subtree. 
We find this by starting at the right child and following left pointers until we reach a node with no left child. 
This works because the right subtree contains all larger values, and the smallest of those larger values is the leftmost one.

If the node doesn't have a right subtree, the successor must be an ancestor. Specifically, it's the first ancestor for which this node is in the left subtree. 
We find this by traversing up the tree until we encounter a parent that we approached from the left.
For our example tree, the successor of 3 is 10 (first ancestor from left), the successor of 17 is 21 (leftmost in right subtree), and the successor of 32 is None (it's the largest node).
Understanding successors is crucial because we'll need this concept for the remove operation.


Part 7: Implementing Removal
7.1 The Three Cases of Removal
Removal is the most complex BST operation because we must maintain the tree structure and ordering property while removing a node. 
The strategy depends on how many children the node has.

- Case 1 handles removing a leaf node (no children) - we simply set the parent's pointer to None. This is straightforward because removing a leaf doesn't affect any other nodes.
- Case 2 handles removing a node with exactly one child - we replace the node with its child. The child "moves up" to take the removed node's place, maintaining all connections below it.
- Case 3 is the complex case: removing a node with two children. We can't simply replace it with one child since it has two. The solution is elegant: we find the node's successor (which is guaranteed to be in the right subtree and have at most one child), copy the successor's key into the current node, then remove the successor. 
This works because the successor is the perfect replacement - it's larger than everything in the left subtree and smaller than everything else in the right subtree.
"""
# 7.2 The Complete Implementation
def remove(self, key):
    parent = None
    current_node = self.root
    
    while current_node != None:
        if current_node.key == key:
            # Case 1: Remove leaf
            if current_node.left == None and current_node.right == None:
                if parent == None:
                    self.root = None
                elif parent.left is current_node:
                    parent.left = None
                else:
                    parent.right = None
                return True
                
            # Case 2A: Node with only left child
            elif current_node.left != None and current_node.right == None:
                if parent == None:
                    self.root = current_node.left
                elif parent.left is current_node:
                    parent.left = current_node.left
                else:
                    parent.right = current_node.left
                return True
                
            # Case 2B: Node with only right child
            elif current_node.left == None and current_node.right != None:
                if parent == None:
                    self.root = current_node.right
                elif parent.left is current_node:
                    parent.left = current_node.right
                else:
                    parent.right = current_node.right
                return True
                
            # Case 3: Node with two children
            else:
                # Find successor (leftmost child of right subtree)
                successor = current_node.right
                while successor.left != None:
                    successor = successor.left
                
                # Copy successor's key to current node
                current_node.key = successor.key
                
                # Continue loop to remove successor
                parent = current_node
                current_node = current_node.right
                key = successor.key
                
        elif current_node.key < key:
            parent = current_node
            current_node = current_node.right
        else:
            parent = current_node
            current_node = current_node.left
            
    return False
# Each case must handle the special situation where we're removing the root (parent is None), updating the root reference instead of a parent's child pointer. The Case 3 implementation is particularly clever - after copying the successor's key, we reassign our variables and let the loop continue, which will then handle removing the successor node using either Case 1 or Case 2.

"""
Part 8: Advanced Implementation - Set ADT

8.1 Building a Set with BST
Now that we understand basic BSTs, let's build a complete Set abstract data type. 
A Set stores unique elements and supports operations like add, remove, search, union, intersection, and difference. 
We'll implement this using a BST, though in production you'd typically use a balanced BST or hash table for guaranteed performance.

8.2 Enhanced BSTNode with Parent Tracking
For our Set implementation, we need nodes that track their parent in addition to their children. 
This enables easier navigation for finding successors:
"""
class BSTNode:
    def __init__(self, data, parent, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def count(self):
        left_count = 0 if self.left == None else self.left.count()
        right_count = 0 if self.right == None else self.right.count()
        return 1 + left_count + right_count

    def get_successor(self):
        # If right subtree exists, find its leftmost child
        if self.right != None:
            successor = self.right
            while successor.left != None:
                successor = successor.left
            return successor
        
        # Otherwise, go up until we find an ancestor from the left
        node = self
        while node.parent != None and node == node.parent.right:
            node = node.parent
        return node.parent

    def replace_child(self, current_child, new_child):
        if current_child is self.left:
            self.left = new_child
            if self.left:
                self.left.parent = self
        elif current_child is self.right:
            self.right = new_child
            if self.right:
                self.right.parent = self
# The count() method recursively counts all nodes in the subtree. The get_successor() method implements the successor algorithm we discussed earlier. The replace_child() method handles updating child pointers while maintaining the bidirectional parent-child links.
"""
8.3 Enabling Iteration with BSTIterator
To support Python's for element in my_set: syntax, we need an iterator class:
"""

class BSTIterator:
    def __init__(self, node):
        self.node = node

    def __next__(self):
        return self.next()

    def next(self):
        if self.node == None:
            raise StopIteration
        current = self.node.data
        self.node = self.node.get_successor()
        return current
    
# This iterator stores our current position in the tree. Each time next() is called, it returns the current node's data and advances to the successor. When we reach the end (node is None), it raises StopIteration as required by Python's iterator protocol. The result is that iterating through the set visits elements in sorted order.

"""
8.4 Set Initialization and Key Functions
The Set class initialization introduces an important concept - the get-key function:
"""
class Set:
    def __init__(self, get_key_function=None):
        self.storage_root = None
        if get_key_function == None:
            self.get_key = lambda el: el
        else:
            self.get_key = get_key_function
# The get-key function extracts a "key" from an element for comparison purposes. For simple elements like integers or strings, the element itself is the key - that's what lambda el: el means. This lambda function is shorthand for a function that takes an element and returns it unchanged. For complex elements like objects, we might extract a specific field. For example, if we're storing Person objects, we might use lambda person: person.name to use the name as the key for comparisons.

# 8.5 Making the Set Iterable
def __iter__(self):
    if self.storage_root == None:
        return BSTIterator(None)
    # Find minimum (leftmost) node
    min_node = self.storage_root
    while min_node.left != None:
        min_node = min_node.left
    return BSTIterator(min_node)
# This method enables iteration by finding the minimum element (leftmost node) and returning an iterator starting there. Since the iterator follows successors, it will visit all elements in sorted order.

# 8.6 Core Set Methods
#The add() method inserts a new element if it doesn't already exist:
def add(self, new_element):
    new_element_key = self.get_key(new_element)
    if self.node_search(new_element_key) != None:
        return False

    new_node = BSTNode(new_element, None)
    if self.storage_root == None:
        self.storage_root = new_node
    else:
        node = self.storage_root
        while node != None:
            if new_element_key < self.get_key(node.data):
                if node.left:
                    node = node.left
                else:
                    node.left = new_node
                    new_node.parent = node
                    return True
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = new_node
                    new_node.parent = node
                    return True
# The search methods provide both internal (returns node) and external (returns data) interfaces:
def node_search(self, key):
    node = self.storage_root
    while node != None:
        node_key = self.get_key(node.data)
        if node_key == key:
            return node
        elif key > node_key:
            node = node.right
        else:
            node = node.left
    return None

def search(self, key):
    node = self.node_search(key)
    return node.data if node != None else None
# The length method uses our count implementation:

def __len__(self):
    return 0 if self.storage_root == None else self.storage_root.count()

# 8.7 Set Removal
# The removal implementation handles the same three cases but uses recursion and the replace_child helper:
def remove(self, key):
    self.remove_node(self.node_search(key))

def remove_node(self, node_to_remove):
    if node_to_remove != None:
        # Case 1: Two children
        if node_to_remove.left != None and node_to_remove.right != None:
            successor = node_to_remove.get_successor()
            data_copy = successor.data
            self.remove_node(successor)
            node_to_remove.data = data_copy
        
        # Case 2: Root node (1 or 0 children)
        elif node_to_remove is self.storage_root:
            self.storage_root = node_to_remove.left if node_to_remove.left != None else node_to_remove.right
            if self.storage_root:
                self.storage_root.parent = None
        
        # Case 3: Internal with left child only
        elif node_to_remove.left != None:
            node_to_remove.parent.replace_child(node_to_remove, node_to_remove.left)
        
        # Case 4: Internal with right child only or leaf
        else:
            node_to_remove.parent.replace_child(node_to_remove, node_to_remove.right)

# 8.8 Set Operations
# The real power of the Set ADT comes from set operations. Union combines all elements from both sets:
def union(self, other_set):
    result = Set(self.get_key)
    for element in self:
        result.add(element)
    for element in other_set:
        result.add(element)
    return result

# Intersection returns only elements present in both sets:
def intersection(self, other_set):
    result = Set(self.get_key)
    for element in self:
        if other_set.search(self.get_key(element)) != None:
            result.add(element)
    return result

# Difference returns elements in this set but not in the other:
def difference(self, other_set):
    result = Set(self.get_key)
    for element in self:
        if other_set.search(self.get_key(element)) == None:
            result.add(element)
    return result

# Filter selects elements satisfying a condition:
def filter(self, predicate):
    result = Set(self.get_key)
    for element in self:
        if predicate(element):
            result.add(element)
    return result

# Map transforms all elements with a function:
def map(self, map_function):
    result = Set(self.get_key)
    for element in self:
        result.add(map_function(element))
    return result

# These operations enable powerful data manipulation. For example, numbers.filter(lambda x: x % 2 == 0) extracts all even numbers, while numbers.map(lambda x: x * x) squares all values.

"""
Part 9: Real-World Applications

9.1 File Systems
Trees naturally represent hierarchical data, making them ideal for file systems. 
A directory structure is inherently a tree - the root directory contains subdirectories and files, subdirectories contain their own subdirectories and files, and so on. 
Our tree implementations can model this structure efficiently.

9.2 Binary Space Partitioning in Graphics
Binary Space Partitioning (BSP) is a powerful technique used in 3D graphics and game engines. 
The idea is to repeatedly divide space into two regions and catalog which objects are in each region. 
A BSP tree stores this information - each node represents a region of space and the objects it contains.
In a graphics application, when rendering a scene, the viewer's position determines which objects are visible. 
By performing a lookup in the BSP tree based on the viewer's position, we can quickly eliminate large portions of the scene that aren't visible. For a game world with 10,000 objects, a naive approach would check all 10,000 objects every frame. With a BSP tree, we might check only about 14 nodes and end up rendering perhaps 100 objects - a 100x performance improvement that makes real-time graphics possible.
"""

"""
Practice Exercises

Exercise 1: Build BST with keys 50, 30, 70, 20, 40, 60, 80
- Draw the tree. What's the height?
- Perform inorder and preorder traversals

Exercise 2: Find successors of 20, 40, 50, 80 in above tree

Exercise 3: Remove node 30 from tree. Which case? What's the result?

Exercise 4: Implement get_max() method to return largest key
"""