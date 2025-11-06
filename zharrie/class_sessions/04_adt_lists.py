# 1: Singly-Linked Lists
# 1.1 Introduction & Foundational Concepts
"""
What is a Singly-Linked List?
A linear data structure where elements are stored in nodes

Each node contains:
- Data: The actual value stored
- Next pointer: Reference to the next node in sequence

The list maintains references to:
- Head: First node in the list
- Tail: Last node in the list

Key Characteristic: Unidirectional traversal (can only move forward)
"""
# 1.2 Class Structure
#SinglyLinkedNode Class
class SinglyLinkedNode:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None
"""        
Explanation:
- self.data: Stores the actual value
- self.next: Initially None, will point to the next node when connected
Each node is independent and knows nothing about the list it belongs to

Example:
node_a = SinglyLinkedNode(95)  # Creates: [95 | None]
"""
# SinglyLinkedList Class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
"""
Explanation:
- Empty list starts with both head and tail as None
- head and tail will point to the same node when there's only one element
This structure allows O(1) access to both ends of the list
"""
#1.3 Core Operations
#1.3.1 Append Operation
def append(self, item):
    self.append_node(SinglyLinkedNode(item))

def append_node(self, new_node):
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node
"""        
Algorithm Walkthrough:

Step-by-step process:
- append(item) creates a new node and delegates to append_node()
- append_node(new_node) has two cases:

Case A: Empty List (self.head is None)
- Before: head → None, tail → None
- After:  head → [95|None] ← tail
Set both head and tail to new_node
The list now has exactly one element

Case B: Non-empty List
- Before: head → [95|•] → [42|None] ← tail
Adding 17:

Step 1: self.tail.next = new_node
        head → [95|•] → [42|•] → [17|None]
                         ↑tail
Step 2: self.tail = new_node
        head → [95|•] → [42|•] → [17|None]
                                  ↑tail
Link the current tail's next to the new node
Update tail reference to point to the new node
Time Complexity: O(1) - constant time, no traversal needed
"""
# 1.3.2 Prepend Operation
def prepend(self, item):
    self.prepend_node(SinglyLinkedNode(item))

def prepend_node(self, new_node):
    if self.head == None:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head = new_node
"""
Algorithm Walkthrough:

Case A: Empty List
Same as append - both head and tail point to the new node

Case B: Non-empty List
Before: head → [95|•] → [42|None] ← tail
Prepending 17:

Step 1: new_node.next = self.head
        [17|•] → [95|•] → [42|None] ← tail
         ↑new      ↑head

Step 2: self.head = new_node
        [17|•] → [95|•] → [42|None] ← tail
         ↑head

Final: head → [17|•] → [95|•] → [42|None] ← tail
Critical Detail: We must set new_node.next BEFORE updating self.head, otherwise we lose the reference to the original list!

Time Complexity: O(1)
"""

#1.3.3 Insert After Operation
def insert_node_after(self, current_node, new_node):
    if self.head == None:
        self.head = new_node
        self.tail = new_node
    elif current_node is self.tail:
        self.tail.next = new_node
        self.tail = new_node
    else:
        new_node.next = current_node.next
        current_node.next = new_node
"""
Algorithm Walkthrough:

Case A: Empty List
Insert becomes the only element

Case B: Inserting after the tail
Before: head → [95|•] → [42|None] ← tail
Insert 17 after tail (42):

Step 1: self.tail.next = new_node
        head → [95|•] → [42|•] → [17|None]
                         ↑tail
Step 2: self.tail = new_node
        head → [95|•] → [42|•] → [17|None] ← tail
This is essentially an append operation

Case C: Inserting in the middle
Before: head → [95|•] → [42|•] → [17|None] ← tail
Insert 88 after 95:

Step 1: new_node.next = current_node.next
        [88|•] → [42|•] → [17|None]
         ↑new
        head → [95|•]
                ↑current

Step 2: current_node.next = new_node
        head → [95|•] → [88|•] → [42|•] → [17|None] ← tail
                ↑current  ↑new
Critical Order: Set new_node.next first to preserve the chain!

Time Complexity: O(1) if we have a reference to the node, O(n) if we need to search first
"""

# 1.3.4 Search Operation (for insert_after)
def search(self, data_value):
    current_node = self.head
    while current_node != None:
        if current_node.data == data_value:
            return current_node
        current_node = current_node.next
    return None
"""
Algorithm Walkthrough:
List: head → [95|•] → [42|•] → [17|None]
Search for 42:

Iteration 1: current_node → [95|•]
             95 != 42, move to next

Iteration 2: current_node → [42|•]
             42 == 42, FOUND! Return this node

Search for 99:
Iterations 1-3: Not found in any node
Final: current_node = None, return None
Time Complexity: O(n) - worst case, must traverse entire list
"""

#1.3.5 Remove After Operation
def remove_node_after(self, current_node):
    if current_node == None:
        # Special case: remove head
        self.head = self.head.next
        if self.head == None:
            # Last item was removed
            self.tail = None
    elif current_node.next != None:
        succeeding_node = current_node.next.next
        current_node.next = succeeding_node
        if succeeding_node == None:
            # Last item was removed
            self.tail = current_node
"""
Algorithm Walkthrough:

Case A: Remove head (current_node == None)
Before: head → [95|•] → [42|•] → [17|None] ← tail

Step 1: self.head = self.head.next
        [95|•]  (orphaned, will be garbage collected)
        head → [42|•] → [17|None] ← tail

Subcase: If list becomes empty after removal
Before: head → [95|None] ← tail

Step 1: self.head = self.head.next
        self.head = None

Step 2: Check if self.head == None (it is)
        self.tail = None

Case B: Remove middle node
Before: head → [95|•] → [42|•] → [17|None] ← tail
Remove node after 95 (remove 42):

Step 1: succeeding_node = current_node.next.next
        succeeding_node → [17|None]

Step 2: current_node.next = succeeding_node
        head → [95|•] → [17|None] ← tail
        [42|•] is now orphaned

Case C: Remove tail
Before: head → [95|•] → [42|•] → [17|None] ← tail
Remove node after 42 (remove 17):

Step 1: succeeding_node = current_node.next.next
        succeeding_node = None

Step 2: current_node.next = succeeding_node
        head → [95|•] → [42|None]

Step 3: Check if succeeding_node == None (it is)
        self.tail = current_node
        head → [95|•] → [42|None] ← tail
Time Complexity: O(1) for the removal itself, O(n) if searching first
"""

#1.3.6 Remove Operation (by value)
def remove(self, item_to_remove):
    previous = None
    current = self.head
    while current != None:
        if current.data == item_to_remove:
            self.remove_node_after(previous)
            return True
        # Advance to next node
        previous = current
        current = current.next
    # Not found
    return False
"""
Algorithm Walkthrough:
List: head → [95|•] → [42|•] → [17|None]
Remove 42:

Iteration 1:
  previous = None
  current → [95|•]
  95 != 42, continue
  previous → [95|•], current → [42|•]

Iteration 2:
  previous → [95|•]
  current → [42|•]
  42 == 42, FOUND!
  Call remove_node_after(previous)
  This removes the node after [95], which is [42]
  Return True

Remove 99 (not in list):
  Loop completes without finding
  Return False

Why track previous? In a singly-linked list, we need the previous node to remove the current node (we can only modify next pointers).

Time Complexity: O(n)
"""
#Class Exercise: Trace the Algorithm
"""
Given this starting list:
head → [10|•] → [20|•] → [30|None] ← tail
Task: Draw the state of the list after each operation:
"""
list.append(40)
list.prepend(5)
list.remove(20)

#Expected output: Draw all intermediate steps!

# 2: Doubly-Linked Lists
"""
2.1 Introduction & Key Differences

What is a Doubly-Linked List?
Each node contains THREE components:
- Data: The actual value
- Next: Reference to the next node
- Previous: Reference to the previous node
Key advantage: Bidirectional traversal
Real-world analogy: A subway train where you can walk forward OR backward through cars.
"""
#2.2 Class Structure
#DoublyLinkedNode Class
class DoublyLinkedNode:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None
        self.previous = None
"""
Visualization:

Node structure: [prev | data | next]
Standalone node: [None | 95 | None]
"""
#DoublyLinkedList Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
#Same structure as singly-linked list, but nodes have bidirectional links.

#2.3 Core Operations - Detailed Algorithm Explanations
#2.3.1 Append Operation
def append(self, item):
    self.append_node(DoublyLinkedNode(item))

def append_node(self, new_node):
    if self.head == None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node
"""
Algorithm Walkthrough:

Case A: Empty List
Before: head → None, tail → None
After:  head → [None|95|None] ← tail

Case B: Non-empty List
Before: head → [None|95|•] ↔ [•|42|None] ← tail

Adding 17:

Step 1: self.tail.next = new_node
        head → [None|95|•] ↔ [•|42|•] → [None|17|None]
                              ↑tail

Step 2: new_node.previous = self.tail
        head → [None|95|•] ↔ [•|42|•] ↔ [•|17|None]
                              ↑tail

Step 3: self.tail = new_node
        head → [None|95|•] ↔ [•|42|•] ↔ [•|17|None] ← tail
Critical Difference from Singly-Linked: We must set BOTH forward and backward links!

Time Complexity: O(1)
"""

#2.3.2 Prepend Operation
def prepend(self, item):
    self.prepend_node(DoublyLinkedNode(item))

def prepend_node(self, new_node):
    if self.head == None:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node
"""
Algorithm Walkthrough:

Case B: Non-empty List
Before: head → [None|95|•] ↔ [•|42|None] ← tail

Prepending 17:

Step 1: new_node.next = self.head
        [None|17|•] → [None|95|•] ↔ [•|42|None] ← tail
                       ↑head

Step 2: self.head.previous = new_node
        [None|17|•] ↔ [•|95|•] ↔ [•|42|None] ← tail
                       ↑head

Step 3: self.head = new_node
        [None|17|•] ↔ [•|95|•] ↔ [•|42|None] ← tail
         ↑head
Time Complexity: O(1)
"""

#2.3.3 Insert After Operation
def insert_node_after(self, current_node, new_node):
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    elif current_node is self.tail:
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node
    else:
        successor_node = current_node.next
        new_node.next = successor_node
        new_node.previous = current_node
        current_node.next = new_node
        successor_node.previous = new_node
"""
Algorithm Walkthrough:

Case C: Insert in middle (most complex)
Before: head → [None|95|•] ↔ [•|42|•] ↔ [•|17|None] ← tail
Insert 88 after 95:

Step 1: successor_node = current_node.next
        successor_node points to [•|42|•]

Step 2: new_node.next = successor_node
        [None|88|•] → [•|42|•]
         ↑new          ↑successor

Step 3: new_node.previous = current_node
        [•|95|•] ← [•|88|•] → [•|42|•]
         ↑current   ↑new       ↑successor

Step 4: current_node.next = new_node
        [•|95|•] → [•|88|•] → [•|42|•]
         ↑current   ↑new       ↑successor
        
        Note: [95]'s old link to [42] is replaced

Step 5: successor_node.previous = new_node
        [•|95|•] ↔ [•|88|•] ↔ [•|42|•]
         ↑current   ↑new       ↑successor

Final: head → [None|95|•] ↔ [•|88|•] ↔ [•|42|•] ↔ [•|17|None] ← tail

Four Pointer Updates Required:
- new_node.next → successor
- new_node.previous → current
- current_node.next → new_node
- successor_node.previous → new_node
Why this order matters: We need to get successor_node reference before we modify current_node.next!

Time Complexity: O(1) with node reference
"""

#2.3.4 Search Operation
def search(self, data_value):
    current_node = self.head
    while current_node != None:
        if current_node.data == data_value:
            return current_node
        current_node = current_node.next
    return None

#Algorithm: Same as singly-linked list (we could also search backward from tail if beneficial)
#Time Complexity: O(n)

#2.3.5 Remove Operation
def remove(self, item_to_remove):
    node_to_remove = self.search(item_to_remove)
    if node_to_remove != None:
        self.remove_node(node_to_remove)
        return True
    return False

def remove_node(self, current_node):
    successor = current_node.next
    predecessor = current_node.previous
    
    if successor != None:
        successor.previous = predecessor
    
    if predecessor != None:
        predecessor.next = successor
    
    if current_node == self.head:
        self.head = successor
    
    if current_node == self.tail:
        self.tail = predecessor
"""
Algorithm Walkthrough:
Before: head → [None|95|•] ↔ [•|42|•] ↔ [•|17|None] ← tail
Remove 42:

Step 1: Identify nodes
        predecessor → [None|95|•]
        current_node → [•|42|•]
        successor → [•|17|None]

Step 2: successor.previous = predecessor
        [None|95|•] ↔ [•|42|•]   [•|17|None]
                       (isolated) ↑
                                  points back to 95

Step 3: predecessor.next = successor
        [None|95|•] → [•|17|None]
                   ↖︎
        [•|42|•] is now isolated

Final: head → [None|95|•] ↔ [•|17|None] ← tail

Special Cases Handled:
Remove head:
current_node == self.head
predecessor = None

Skip: predecessor.next = successor (would cause error)
Execute: self.head = successor
Result: head pointer moves to second node

Remove tail:
current_node == self.tail
successor = None

Skip: successor.previous = predecessor (would cause error)
Execute: self.tail = predecessor
Result: tail pointer moves to second-to-last node

Remove only node:
Both predecessor and successor are None
self.head = None
self.tail = None
Key Advantage: We can remove ANY node directly without tracking its predecessor!

Time Complexity: O(n) to search, O(1) to remove
"""
#Class Exercise 2.1: Trace the Algorithm
"""
Given this starting list:
head → [None|10|•] ↔ [•|20|•] ↔ [•|30|None] ← tail
Task: Draw the state of the list after each operation, showing ALL pointers:

list.insert_after(node_with_20, new_node_with_25)
list.remove(20)
"""
"""
2.5 Key Takeaways for Doubly-Linked Lists

Advantages over Singly-Linked:
- Bidirectional traversal
- Can remove a node without tracking predecessor
- Can traverse backward from tail

Disadvantages:
- Extra memory per node (previous pointer)
- More pointer updates per operation
- Slightly more complex to implement correctly
"""

#3: Array-Based Lists
"""
3.1 What is an Array-Based List?

Uses a contiguous block of memory (array) to store elements
Maintains two key values:
- length: Number of actual items in the list
- allocation_size: Total capacity of the underlying array
Python's built-in list type uses this implementation!

Key Concept: Over-allocation
- Array is typically larger than needed
- Allows efficient appending without constant reallocation
Trade-off: memory vs. time efficiency
Real-world analogy: A parking lot with 100 spaces but only 30 cars. You don't need to rebuild the parking lot every time a new car arrives!
"""
#3.2 Class Structure
class ArrayList:
    def __init__(self, initial_allocation_size = 10):
        self.allocation_size = initial_allocation_size
        self.length = 0
        self.array = [None] * initial_allocation_size
"""
Visualization:
After initialization (size=10):
array: [None, None, None, None, None, None, None, None, None, None]
       0     1     2     3     4     5     6     7     8     9
- length: 0
- allocation_size: 10

Critical Understanding:
- length tracks how many items we've actually added
- Indices 0 to length-1 contain valid data
- Indices length to allocation_size-1 are unused (None)
"""

# 3.3 Core Operations - Detailed Algorithm Explanations
# 3.3.1 Append Operation
def append(self, new_item):
    # Resize if the array is full
    if self.allocation_size == self.length:
        self.resize(self.length * 2)
    
    # Insert the new item at index equal to self.length
    self.array[self.length] = new_item
    
    # Increment the array's length
    self.length = self.length + 1
"""
Algorithm Walkthrough:
Scenario 1: Space available
Before: [95, 42, None, None, None]
        length = 2, allocation_size = 5

Append 17:

Step 1: Check if full
        2 == 5? No, skip resize

Step 2: Insert at index = length
        self.array[2] = 17
        [95, 42, 17, None, None]

Step 3: Increment length
        self.length = 3

After: [95, 42, 17, None, None]
       length = 3, allocation_size = 5

Scenario 2: Array is full, needs resizing
Before: [95, 42, 17, 88, 23]
        length = 5, allocation_size = 5

Append 99:

Step 1: Check if full
        5 == 5? Yes, resize to 5 * 2 = 10
        [95, 42, 17, 88, 23, None, None, None, None, None]
        length = 5, allocation_size = 10

Step 2: Insert at index = length
        self.array[5] = 99
        [95, 42, 17, 88, 23, 99, None, None, None, None]

Step 3: Increment length
        self.length = 6

After: [95, 42, 17, 88, 23, 99, None, None, None, None]
       length = 6, allocation_size = 10

Time Complexity:
- Best/Average case: O(1)
- Worst case: O(n) when resizing (but amortized O(1))
"""
# 3.3.2 Resize Operation
def resize(self, new_allocation_size):
    # Create a new array with the indicated size
    new_array = [None] * new_allocation_size
    
    # Copy items in current array into the new array
    for i in range(self.length):
        new_array[i] = self.array[i]
    
    # Assign the array data member with the new array
    self.array = new_array
    
    # Update the allocation size
    self.allocation_size = new_allocation_size
"""
Algorithm Walkthrough:
Before: self.array = [95, 42, 17]
        length = 3, allocation_size = 3
Resize to 6:

Step 1: Create new array
        new_array = [None, None, None, None, None, None]

Step 2: Copy elements (i = 0 to length-1)
        i=0: new_array[0] = self.array[0] = 95
        i=1: new_array[1] = self.array[1] = 42
        i=2: new_array[2] = self.array[2] = 17
        
        new_array = [95, 42, 17, None, None, None]

Step 3: Replace old array
        self.array = new_array
        (old array is garbage collected)

Step 4: Update allocation_size
        self.allocation_size = 6

After: self.array = [95, 42, 17, None, None, None]
       length = 3, allocation_size = 6
Important: Only elements from 0 to length-1 are copied (not the None values)

Time Complexity: O(n) where n = length
"""

#3.3.3 Prepend Operation
def prepend(self, new_item):
    # Resize if the array is full
    if self.allocation_size == self.length:
        self.resize(self.length * 2)
    
    # Shift all array items to the right
    for i in reversed(range(1, self.length+1)):
        self.array[i] = self.array[i-1]
    
    # Insert the new item at index 0
    self.array[0] = new_item
    
    # Update the array's length
    self.length = self.length + 1
"""
Algorithm Walkthrough:
Before: [95, 42, 17, None, None]
        length = 3, allocation_size = 5

Prepend 88:

Step 1: Check if full (not full in this case)

Step 2: Shift elements right
        reversed(range(1, 4)) produces: 3, 2, 1
        
        i=3: self.array[3] = self.array[2]
             [95, 42, 17, 17, None]
                      ↑    ↑
                    copy  paste
        
        i=2: self.array[2] = self.array[1]
             [95, 42, 42, 17, None]
                  ↑    ↑
                copy  paste
        
        i=1: self.array[1] = self.array[0]
             [95, 95, 42, 17, None]
              ↑    ↑
            copy  paste

Step 3: Insert new item at index 0
        self.array[0] = 88
        [88, 95, 42, 17, None]

Step 4: Increment length
        self.length = 4

After: [88, 95, 42, 17, None]
       length = 4, allocation_size = 5

Why reversed range?
If we went forward (1, 2, 3):
i=1: array[1] = array[0] → [95, 95, 17, None]
i=2: array[2] = array[1] → [95, 95, 95, None]
i=3: array[3] = array[2] → [95, 95, 95, 95]
WRONG! We're copying the same value repeatedly.

By going backward, we preserve each value before overwriting it.
Time Complexity: O(n) - must shift all elements
"""

#3.3.4 Insert After Operation
def insert_after(self, index, new_item):
    # Resize if the array is full
    if self.allocation_size == self.length:
        self.resize(self.length * 2)
    
    # Shift all the array items to the right
    for i in reversed(range(index+1, self.length+1)):
        self.array[i] = self.array[i-1]
    
    # Insert the new item
    self.array[index+1] = new_item
    
    # Update the array's length
    self.length = self.length + 1
"""
Algorithm Walkthrough:
Before: [95, 42, 17, 88, None, None]
        length = 4, allocation_size = 6

Insert 99 after index 1 (after 42):

Step 1: Check if full (not full)

Step 2: Shift elements from index+1 to length-1
        reversed(range(2, 5)) produces: 4, 3, 2
        
        i=4: self.array[4] = self.array[3]
             [95, 42, 17, 88, 88, None]
                          ↑    ↑
        
        i=3: self.array[3] = self.array[2]
             [95, 42, 17, 17, 88, None]
                      ↑    ↑
        
        i=2: self.array[2] = self.array[1]
             [95, 42, 42, 17, 88, None]
                  ↑    ↑

Step 3: Insert new item at index+1
        self.array[2] = 99
        [95, 42, 99, 17, 88, None]
                 ↑
            inserted here

Step 4: Increment length
        self.length = 5

After: [95, 42, 99, 17, 88, None]
       length = 5, allocation_size = 6
Key difference from prepend: Only shifts elements from index+1 onward, not the entire array

Time Complexity: O(n) worst case (inserting after index 0), O(1) best case (inserting after last element)
"""

#3.3.5 Search Operation
def search(self, item):
    # Iterate through the entire array
    for i in range(self.length):
        # If the current item matches the search item
        if self.array[i] == item:
            return i
    
    # If the loop finishes without returning
    return -1
"""
Algorithm Walkthrough:
Array: [95, 42, 17, 88, None, None]
       length = 4

Search for 17:

i=0: array[0] = 95, 95 == 17? No
i=1: array[1] = 42, 42 == 17? No
i=2: array[2] = 17, 17 == 17? Yes! Return 2

Search for 99:

i=0: array[0] = 95, 95 == 99? No
i=1: array[1] = 42, 42 == 99? No
i=2: array[2] = 17, 17 == 99? No
i=3: array[3] = 88, 88 == 99? No
Loop completes, return -1
Important: We only search indices 0 to length-1, not the entire allocated array

Time Complexity: O(n) - linear search
"""

#3.3.6 Remove At Operation
def remove_at(self, index):
    # Make sure the index is valid
    if index >= 0 and index < self.length:
        # Shift items from the given index
        for i in range(index, self.length-1):
            self.array[i] = self.array[i+1]
        
        # Update the array's length
        self.length = self.length - 1
"""
Algorithm Walkthrough:
Before: [95, 42, 17, 88, 23, None, None]
        length = 5, allocation_size = 7

Remove at index 2 (remove 17):

Step 1: Validate index
        2 >= 0 and 2 < 5? Yes, proceed

Step 2: Shift elements left from index to length-2
        range(2, 4) produces: 2, 3
        
        i=2: self.array[2] = self.array[3]
             [95, 42, 88, 88, 23, None, None]
                      ↑copy from here
                  ↑paste here
        
        i=3: self.array[3] = self.array[4]
             [95, 42, 88, 23, 23, None, None]
                          ↑copy from here
                      ↑paste here

Step 3: Decrement length
        self.length = 4

After: [95, 42, 88, 23, 23, None, None]
                        ↑
                  duplicated but beyond length
       length = 4, allocation_size = 7

Effective list: [95, 42, 88, 23]
Note: The last element is duplicated but it's beyond length, so it's ignored

Why not clear the duplicate? Not necessary - it's beyond the valid range and will be overwritten when needed

Time Complexity: O(n) worst case (removing first element), O(1) best case (removing last element)
"""
# ClassExercise 3.1: Analyze Space Efficiency
# Given an ArrayList with these operations:
list = ArrayList(10)  # initial allocation
list.append(1)
list.append(2)
list.append(3)
"""
Questions:
- What is length after these operations?
- What is allocation_size?
- How many array slots are wasted?
- What is the space utilization percentage? (length / allocation_size * 100)
- Is this waste acceptable? Why or why not?
"""
# 3.6 Key Takeaways for Array-Based Lists
"""
Advantages:
- O(1) random access by index
- Better cache locality (contiguous memory)
- Less memory overhead per element (no pointers)
- Simpler implementation
- Great for stacks and general-purpose use

Disadvantages:
- O(n) insertions/deletions (except at end)
- Wasted space from over-allocation
- Expensive resizing operation
- Fixed memory block (can't use fragmented memory)
"""

# Integration & Real-World Applications
"""
Decision Framework: Which List Should I Use?

Use Array-Based List when:
✅ Random access needed (accessing by index)
✅ Mostly appending to the end
✅ Memory is contiguous
✅ Simplicity is important
Examples: Stack, general-purpose list, accessing elements by position

Use Singly-Linked List when:
✅ Frequent insertions/deletions at head
✅ Forward-only traversal is sufficient
✅ Unknown/dynamic size
✅ Memory fragmentation is a concern
Examples: Queue, blockchain, task scheduling, free lists

Use Doubly-Linked List when:
✅ Bidirectional traversal needed
✅ Frequent insertions/deletions anywhere
✅ Need to remove nodes efficiently
✅ Implementing LRU cache, browser history
"""