from BSTNode import BSTNode
from BSTChecker import BSTChecker
import random

# Makes and returns a randomly generated, valid BST with at least 10,000 nodes
def make_random_tree():
    MAX_KEY = 999999
    # Determine a sufficiently large tree size
    tree_size = 10000 + random.randrange(10000)
    
    # Make the tree's root
    root = BSTNode(random.randrange(MAX_KEY + 1))
    
    # Add random keys until the desired size is reached
    key_count = 1
    while key_count < tree_size:
        if root.insert_key(random.randrange(MAX_KEY + 1)):
            key_count += 1
    
    return root

# Performs a test of BSTChecker.check_BST_validity() given the tree's root and
# and expected return value
def test_tree(root_node, expected):
    bad_node = BSTChecker.check_BST_validity(root_node)
    
    passed = False
    if bad_node is expected:
        print("PASS: check_BST_validity() returned ", end="")
        if expected != None:
            print(f"the node with key {expected.get_key()}")
        else:
            print("None for a valid tree")
        passed = True
    else:
        print("FAIL: check_BST_validity() returned ", end="")
        
        # Special case message if badNode and expected are non-null with equal
        # keys
        if bad_node != None and expected != None and bad_node.get_key() == expected.get_key():
            print(f"a node with key {bad_node.get_key()}, but not the " +
                "correct node. During a preorder traversal, the node with " +
                "the second occurrence of a duplicate key must be returned.")
        elif bad_node != None:
            print(f"the node with key {bad_node.get_key()}, but should " +
                "have returned ", end="")
            if expected != None:
                print(f"the node with key {expected.get_key()}")
            else:
                print("None since the tree is valid")
        else:
            print("None for an invalid tree")
        passed = False
    
    return passed

# Main program code follows

# Tree 1 - invalid
# Tree 1 is the left tree in the "Examples of key-related problems" figure
print("Tree 1: ", end="")
tree1_node50 = BSTNode(50, BSTNode(20), BSTNode(60))
root1 = BSTNode(
    40,
    tree1_node50,
    BSTNode(
        80,
        BSTNode(70),
        BSTNode(90)
    )
)
test_tree(root1, tree1_node50)

# Tree 2 - invalid
# Right tree in the "Examples of key-related problems" figure
print("Tree 2: ", end="")
tree2_node66 = BSTNode(66)
root2 = BSTNode(
    77,
    BSTNode(
        44,
        BSTNode(33),
        BSTNode(55)
    ),
    BSTNode(
        88,
        tree2_node66,
        BSTNode(99)
    )
)
test_tree(root2, tree2_node66)

# Tree 3 - valid
# Randomly generated tree
print("Tree 3: ", end="")
test_tree(make_random_tree(), None)
   
# Tree 4 - invalid
# Left tree in the "Examples of child-related problems" figure
print("Tree 4: ", end="")
tree4_node75 = BSTNode(75, None, BSTNode(88))
root4 = BSTNode(
    50,
    BSTNode(
        25,
        None,
        BSTNode(37, None, tree4_node75)
    ),
    tree4_node75
)
test_tree(root4, tree4_node75)
   
# Tree 5 - invalid
# Right tree in the "Examples of child-related problems" figure
print("Tree 5: ", end="")
tree5_node55 = BSTNode(55)
root5 = BSTNode(
    44,
    BSTNode(22, BSTNode(11), BSTNode(33)),
    tree5_node55
)
tree5_node55.set_right(root5)
test_tree(root5, root5)
   
# Tree 6 - invalid
# Tree 6's node 13 is the left child of both node 14 and node 86
print("Tree 6: ", end="")
tree6_node13 = BSTNode(
    13,
    BSTNode(
        12,
        BSTNode(8, BSTNode(6), BSTNode(10)),
        None
    ),
    None
)
tree6_node86 = BSTNode(86, tree6_node13, BSTNode(87))
root6 = BSTNode(
    38,
    BSTNode(14, tree6_node13, None),
    BSTNode(
        66,
        None,
        BSTNode(
            81,
            BSTNode(73),
            BSTNode(88, tree6_node86, BSTNode(91))
        )
    )
)
test_tree(root6, tree6_node13)
   
# Trees 7 and 8 - valid
# Randomly generated trees
print("Tree 7: ", end="")
test_tree(make_random_tree(), None)
print("Tree 8: ", end="")
test_tree(make_random_tree(), None)

# Tree 9 - invalid
# Duplicate key 63
print("Tree 9: ", end="")
tree9_node63_lower = BSTNode(63)
root9 = BSTNode(
    63,
    BSTNode(
        47,
        None,
        BSTNode(57, BSTNode(50), None)
    ),
    BSTNode(
        77,
        tree9_node63_lower,
        BSTNode(88, BSTNode(71), BSTNode(89))
    )
)
test_tree(root9, tree9_node63_lower)

# Tree 10 - invalid
# Several duplicate keys. Leftmost leaf with 25 is the first problematic node.
print("Tree 10: ", end="")
tree10_node25_leftmost = BSTNode(25)
root10 = BSTNode(
    50,
    BSTNode(
        25,
        BSTNode(12, BSTNode(10), tree10_node25_leftmost),
        BSTNode(37, BSTNode(25), BSTNode(50))
    ),
    BSTNode(
        75,
        BSTNode(62, BSTNode(55), BSTNode(68)),
        BSTNode(88, BSTNode(75), BSTNode(89))
    )
)
test_tree(root10, tree10_node25_leftmost)