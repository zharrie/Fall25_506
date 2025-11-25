# Heaps and Priority Queues
"""
The Real-World Problem

Imagine you're a computer's operating system managing multiple jobs:
- Job A: Priority 22
- Job B: Priority 14
- Job C: Priority 98
- Job D: Priority 50
Which job should execute first?
Job C (98), then D (50), then A (22), then B (14)

Key Challenge: New jobs arrive constantly. We need to:
- Quickly find the highest priority job
- Efficiently add new jobs
- Remove jobs as they complete
- Why not use a fully sorted list? 
That's overkill! We only need the maximum element, not complete sorting.
"""

# Part 1: Max-Heap Concept
"""
A max-heap is a complete binary tree with one simple rule:
- Max-Heap Property: Every node's value ≥ its children's values

Visual Example
         99
        /  \
      85    72
     /  \   /
   40   15 30

Properties to notice:
- 99 ≥ 85 and 99 ≥ 72 (parent ≥ children)
- 85 ≥ 40 and 85 ≥ 15 (parent ≥ children)
- 72 ≥ 30 (parent ≥ child)
The root (99) is always the maximum value!

Why This Works
Since:
- Parent ≥ Children, AND
- Children ≥ Their children
- Then: Root ≥ All descendants (transitivity)
"""

# Part 2: Array Implementation & Index Formulas
"""
Why Arrays?
Heaps are complete binary trees - filled level by level, left to right. 
This makes array storage extremely efficient!

The Mapping
Visual tree:
         99        ← Index 0
        /  \
      85    72     ← Index 1, 2
     /  \   /  \
   40   15 30  20  ← Index 3, 4, 5, 6

Array representation:
Index:  0   1   2   3   4   5   6
Value: [99, 85, 72, 40, 15, 30, 20]

Critical Formulas (MEMORIZE THESE!)
For any node at index i:
- Parent index = (i - 1) // 2
- Left child index = 2 * i + 1
- Right child index = 2 * i + 2

Example Calculation:
Node at index 1 (value 85):
- Parent: (1-1)//2 = 0 ✓ (value 99)
- Left child: 2(1)+1 = 3 ✓ (value 40)
- Right child: 2(1)+2 = 4 ✓ (value 15)

Node at index 5 (value 30):
- Parent: (5-1)//2 = 2 ✓ (value 72)
- Left child: 2(5)+1 = 11 (doesn't exist)
- Right child: 2(5)+2 = 12 (doesn't exist)
"""

# Part 3: INSERT Operation
"""
The INSERT Algorithm (Percolate Up)
Steps:
- Add the new element at the bottom-rightmost position (end of array)
- Compare with parent using formula: parent_index = (current - 1) // 2
- If new element > parent, SWAP
- Update current position to parent position
- Repeat until heap property is satisfied OR we reach the root

EXAMPLE 1: Building a Heap from Scratch

Let's insert: 50, 30, 70, 20, 60, 90

Step 1: Insert 50
Tree View:              Array View:
   [50]                 Index: 0
                        Value: [50]
No comparisons needed - single element is always a valid heap!

Step 2: Insert 30
BEFORE INSERT:
   50
   
STEP 2.1: Add 30 at next position (index 1)
   50
   /
 [30]                   Array: [50, 30]

STEP 2.2: Compare with parent
Current index: 1, value: 30
Parent index: (1-1)//2 = 0, value: 50
Is 30 > 50? NO → STOP (heap property satisfied!)

FINAL:
   50
   /
  30                    Array: [50, 30]

Step 3: Insert 70
BEFORE INSERT:
   50
   /
  30

STEP 3.1: Add 70 at next position (index 2)
   50
   /  \
  30  [70]              Array: [50, 30, 70]

STEP 3.2: Compare with parent
Current index: 2, value: 70
Parent index: (2-1)//2 = 0, value: 50
Is 70 > 50? YES → SWAP!

   [70]
   /  \
  30   50               Array: [70, 30, 50]

STEP 3.3: Check if done
Current index: 0 (root) → STOP

FINAL:
    70
   /  \
  30   50               Array: [70, 30, 50]

Step 4: Insert 20
BEFORE INSERT:
    70
   /  \
  30   50

STEP 4.1: Add 20 at next position (index 3)
    70
   /  \
  30   50
  /
[20]                    Array: [70, 30, 50, 20]

STEP 4.2: Compare with parent
Current index: 3, value: 20
Parent index: (3-1)//2 = 1, value: 30
Is 20 > 30? NO → STOP

FINAL:
    70
   /  \
  30   50
  /
 20                     Array: [70, 30, 50, 20]

Step 5: Insert 60
BEFORE INSERT:
    70
   /  \
  30   50
  /
 20

STEP 5.1: Add 60 at next position (index 4)
    70
   /  \
  30   50
  /  \
 20  [60]               Array: [70, 30, 50, 20, 60]

STEP 5.2: Compare with parent
Current index: 4, value: 60
Parent index: (4-1)//2 = 1, value: 30
Is 60 > 30? YES → SWAP!

    70
   /  \
 [60]  50
  /  \
 20   30                Array: [70, 60, 50, 20, 30]

STEP 5.3: Compare with new parent
Current index: 1, value: 60
Parent index: (1-1)//2 = 0, value: 70
Is 60 > 70? NO → STOP

FINAL:
    70
   /  \
  60   50
  /  \
 20   30                Array: [70, 60, 50, 20, 30]

Step 6: Insert 90 (Most Complex Example!)
BEFORE INSERT:
    70
   /  \
  60   50
  /  \
 20   30

STEP 6.1: Add 90 at next position (index 5)
    70
   /  \
  60   50
  /  \  /
 20  30 [90]            Array: [70, 60, 50, 20, 30, 90]

STEP 6.2: Compare with parent
Current index: 5, value: 90
Parent index: (5-1)//2 = 2, value: 50
Is 90 > 50? YES → SWAP!

    70
   /  \
  60   [90]
  /  \  /
 20  30 50              Array: [70, 60, 90, 20, 30, 50]

STEP 6.3: Compare with new parent
Current index: 2, value: 90
Parent index: (2-1)//2 = 0, value: 70
Is 90 > 70? YES → SWAP!

    [90]
   /  \
  60   70
  /  \  /
 20  30 50              Array: [90, 60, 70, 20, 30, 50]

STEP 6.4: Check if done
Current index: 0 (root) → STOP

FINAL MAX-HEAP:
    90
   /  \
  60   70
  /  \  /
 20  30 50              Array: [90, 60, 70, 20, 30, 50]
Summary: 90 "percolated up" from index 5 → 2 → 0 (root)
"""

# Part 4: REMOVE Operation
"""
The REMOVE Algorithm (Percolate Down)

Important: We ALWAYS remove the root (maximum element)

Steps:
- Save the root value (we'll return this)
- Move the last element in the array to the root
- Remove the last element from the array
- Compare current node with BOTH children
- Find the larger child
- If larger child > current node, SWAP with that child
- Update current position
- Repeat until heap property is satisfied OR we reach a leaf

EXAMPLE: Multiple Removals

Starting heap:
    90
   /  \
  60   70
  /  \  /
 20  30 50              Array: [90, 60, 70, 20, 30, 50]

Remove Operation 1: Remove 90
STEP 1.1: Save the root value
max_value = 90

STEP 1.2: Replace root with LAST element (index 5, value 50)
   [50]
   /  \
  60   70
  /  \
 20  30                 Array: [50, 60, 70, 20, 30]

STEP 1.3: Percolate down from root (index 0)
Current index: 0, value: 50
Left child index: 2(0)+1 = 1, value: 60
Right child index: 2(0)+2 = 2, value: 70

Find MAX among {50, 60, 70} → 70 is largest
Is 70 > 50? YES → SWAP with right child!

    70
   /  \
  60  [50]
  /  \
 20  30                 Array: [70, 60, 50, 20, 30]

STEP 1.4: Continue percolating down
Current index: 2, value: 50
Left child index: 2(2)+1 = 5 (doesn't exist)
Right child index: 2(2)+2 = 6 (doesn't exist)

No children → STOP

FINAL HEAP:
    70
   /  \
  60   50
  /  \
 20  30                 Array: [70, 60, 50, 20, 30]

RETURNED: 90

Remove Operation 2: Remove 70
STEP 2.1: Save the root value
max_value = 70

STEP 2.2: Replace root with LAST element (index 4, value 30)
   [30]
   /  \
  60   50
  /
 20                     Array: [30, 60, 50, 20]

STEP 2.3: Percolate down from root
Current index: 0, value: 30
Left child index: 1, value: 60
Right child index: 2, value: 50

Find MAX among {30, 60, 50} → 60 is largest
Is 60 > 30? YES → SWAP with left child!

    60
   /  \
 [30]  50
  /
 20                     Array: [60, 30, 50, 20]

STEP 2.4: Continue percolating down
Current index: 1, value: 30
Left child index: 2(1)+1 = 3, value: 20
Right child index: 2(1)+2 = 4 (doesn't exist)

Find MAX among {30, 20} → 30 is largest
Is 30 > 20? YES → Already in correct position, STOP

FINAL HEAP:
    60
   /  \
  30   50
  /
 20                     Array: [60, 30, 50, 20]

RETURNED: 70

Remove Operation 3: Remove 60
STEP 3.1: Save the root value
max_value = 60

STEP 3.2: Replace root with LAST element (index 3, value 20)
   [20]
   /  \
  30   50               Array: [20, 30, 50]

STEP 3.3: Percolate down from root
Current index: 0, value: 20
Left child index: 1, value: 30
Right child index: 2, value: 50

Find MAX among {20, 30, 50} → 50 is largest
Is 50 > 20? YES → SWAP with right child!

    50
   /  \
  30  [20]              Array: [50, 30, 20]

STEP 3.4: Continue percolating down
Current index: 2, value: 20
Left child index: 5 (doesn't exist)
Right child index: 6 (doesn't exist)

No children → STOP

FINAL HEAP:
    50
   /  \
  30   20               Array: [50, 30, 20]

RETURNED: 60

Notice the pattern: Each remove operation returns values in descending order: 90, 70, 60...
"""

# Part 5: SEARCH Operation - Understanding Heap Limitations
"""
Important Concept: Heaps Are NOT Optimized for Search!
Key Point: Unlike binary search trees, heaps do NOT maintain a left < parent < right ordering.

Search Example: Looking for value 30
Starting heap:
    90
   /  \
  60   70
  /  \  /
 20  30 50              Array: [90, 60, 70, 20, 30, 50]
Question: Where is 30?

Search Attempt - Why We Can't Use Binary Search

STEP 1: Start at root (index 0)
Check: Is 90 == 30? NO
Can we eliminate half the tree? NO!
  - 30 could be in left subtree (60 > 30 ✓)
  - 30 could be in right subtree (70 > 30 ✓)
  We must check BOTH sides!

STEP 2: Check left child (index 1)
Check: Is 60 == 30? NO
Must check both children of 60

STEP 3: Check left-left child (index 3)
Check: Is 20 == 30? NO
No children to check

STEP 4: Check left-right child (index 4)
Check: Is 30 == 30? YES! FOUND at index 4

Total comparisons: 4 out of 6 nodes
Worst case: We might have to check EVERY node! → O(n) time

Why Heaps Are Bad for Search - Visual Comparison
Binary Search Tree (BST) - Good for search:
    50
   /  \
  30   70
 /  \    \
20  40   90

Search for 40:
50 → "40 < 50, go left"
30 → "40 > 30, go right"
40 → FOUND!
Only 3 comparisons (O(log n))

Max-Heap - Bad for search:
    90
   /  \
  70   50
  /  \    \
60  30   40

Search for 40:
90 → "40 < 90, could be anywhere"
Must check: 70, 50, 60, 30, AND 40
All 6 nodes potentially! (O(n))

Conclusion: Heaps are designed for:
- Fast access to MAX/MIN → O(1)
- Fast insert/remove → O(log n)
NOT for searching arbitrary values → O(n)
"""

# Part 6: Min-Heap - The Opposite Structure
"""
Min-Heap Property
- Min-Heap Property: Every node's value ≤ its children's values
- Root contains the MINIMUM value!

Building a Min-Heap: Complete Example

Insert sequence: 50, 30, 70, 20, 60

Min-Heap Insert 50
   50                   Array: [50]

Min-Heap Insert 30
STEP 1: Add 30           STEP 2: Compare & Swap
   50                       30
   /                        /
 [30]                      50

Is 30 < 50? YES → SWAP

Array: [30, 50]

Min-Heap Insert 70
STEP 1: Add 70           STEP 2: Compare
   30                       30
   /  \                     /  \
  50  [70]                 50  70

Is 70 < 30? NO → STOP (already valid)

Array: [30, 50, 70]

Min-Heap Insert 20
STEP 1: Add 20           STEP 2: Compare & Swap
   30                       30
   /  \                     /  \
  50  70                  [20] 70
  /                        /
[20]                      50

Is 20 < 50? YES → SWAP

Array: [30, 20, 70, 50]

STEP 3: Continue         STEP 4: Swap with root
   [30]                     20
   /  \                     /  \
  20  70                   30  70
  /                        /
 50                       50

Is 20 < 30? YES → SWAP

Array: [20, 30, 70, 50]

Min-Heap Insert 60
STEP 1: Add 60           STEP 2: Compare
   20                       20
   /  \                     /  \
  30  70                   30  70
  /  \                     /  \
 50  [60]                 50  60

Is 60 < 30? NO → STOP

Array: [20, 30, 70, 50, 60]

FINAL MIN-HEAP:
    20      ← MINIMUM at root!
   /  \
  30   70
  /  \
 50  60

"""
# Part 7: Heapsort Algorithm
"""
The Big Idea
- Convert an unsorted array into a max-heap (heapify)
- Repeatedly remove the max and place it at the end
- Result: Sorted array!

Complete Heapsort Trace

Initial unsorted array: [30, 20, 50, 10, 40]

PHASE 1: HEAPIFY
- Goal: Convert array into a valid max-heap
- Strategy: Start from the last non-leaf node and percolate down

Starting array: [30, 20, 50, 10, 40]

Initial tree (NOT a heap):
      30
     /  \
   20    50
   /  \
 10   40

Step 1: Find last non-leaf node
Last index: 4
Last non-leaf: (5//2) - 1 = 1

Step 2: Percolate down from index 1 (value 20)
BEFORE:                  AFTER:
     30                      30
    /  \                    /  \
  [20]  50                [40]  50
   /  \                    /  \
 10   40                 10   20

Compare 20 with children (10, 40)
40 is largest → SWAP

Array: [30, 40, 50, 10, 20]

Step 3: Percolate down from index 0 (value 30)
STEP A:                  STEP B:
     [30]                   50
     /  \                  /  \
   40   50                40  [30]
   /  \                   /  \
 10   20                10   20

Compare 30 with children (40, 50)
50 is largest → SWAP

Array: [50, 40, 30, 10, 20]

No more swaps needed.

HEAPIFIED!
     50
    /  \
  40    30
  /  \
10   20

PHASE 2: SORTING
Repeatedly swap root with last element, then percolate down

Iteration 1: Extract 50
STEP 1: Swap root with last    STEP 2: Percolate down
     50                              40
    /  \                            /  \
  40    30                        20    30
  /  \                            /
10   [20]                       10         [50]

Swap positions 0 and 4
Array: [20, 40, 30, 10 | 50]
         ↑____________↑  (sorted)

STEP 3: Fix heap on [20, 40, 30, 10]
     [20]                     40
     /  \                    /  \
   40   30        →        20   30
   /                       /
 10                      10

Array: [40, 20, 30, 10 | 50]

Iteration 2: Extract 40
STEP 1: Swap root with last
     40                         
    /  \                        
  20    30                      
  /                             
[10]                            

Swap positions 0 and 3
Array: [10, 20, 30 | 40, 50]
                    (sorted)

STEP 2: Percolate down [10, 20, 30]
     [10]                    30
     /  \         →         /  \
   20   30                20   10

Array: [30, 20, 10 | 40, 50]

Iteration 3: Extract 30
STEP 1: Swap root with last
     30
    /  \
  20   [10]

Swap positions 0 and 2
Array: [10, 20 | 30, 40, 50]
              (sorted)

STEP 2: Percolate down [10, 20]
     [10]              20
      /       →        /
    20                10

Array: [20, 10 | 30, 40, 50]

Iteration 4: Extract 20
STEP 1: Swap root with last
    20
    /
  [10]

Swap positions 0 and 1
Array: [10 | 20, 30, 40, 50]
           (sorted)

FINAL SORTED ARRAY: [10, 20, 30, 40, 50] ✓
Summary: Heapsort operates in O(n log n) time with O(1) extra space!
"""

# Part 8: Python Implementation

#The MaxHeap Class
class MaxHeap:
    def __init__(self):
        self.heap_array = []  # Simple list - no Node class needed!

# Percolate Up Method (for INSERT)
def percolate_up(self, node_index):
    while node_index > 0:
        # Calculate parent index
        parent_index = (node_index - 1) // 2
        
        # Check for violation
        if self.heap_array[node_index] <= self.heap_array[parent_index]:
            return  # Heap property satisfied!
        else:
            # Swap current node with parent
            temp = self.heap_array[node_index]
            self.heap_array[node_index] = self.heap_array[parent_index]
            self.heap_array[parent_index] = temp
            
            # Move up to parent position
            node_index = parent_index

# Percolate Down Method (for REMOVE)
def percolate_down(self, node_index):
    child_index = 2 * node_index + 1
    value = self.heap_array[node_index]

    while child_index < len(self.heap_array):
        # Find the max among the node and its children
        max_value = value
        max_index = -1
        i = 0
        
        # Check both children (if they exist)
        while i < 2 and i + child_index < len(self.heap_array):
            if self.heap_array[i + child_index] > max_value:
                max_value = self.heap_array[i + child_index]
                max_index = i + child_index
            i = i + 1

        # Check if heap property is satisfied
        if max_value == value:
            return  # Done!
        else:
            # Swap with larger child
            temp = self.heap_array[node_index]
            self.heap_array[node_index] = self.heap_array[max_index]
            self.heap_array[max_index] = temp
            
            # Move down to child position
            node_index = max_index
            child_index = 2 * node_index + 1

# Insert Method
def insert(self, value):
    # Step 1: Add to end of array
    self.heap_array.append(value)
    
    # Step 2: Restore heap property by percolating up
    self.percolate_up(len(self.heap_array) - 1)

# Trace Example:
heap = MaxHeap()
heap.insert(50)  
# heap_array: [50]

heap.insert(30)  
# heap_array: [50, 30]

heap.insert(70)  
# After append: [50, 30, 70]
# After percolate_up: [70, 30, 50]

# Remove Method
def remove(self):
    # Step 1: Save the max (root)
    max_value = self.heap_array[0]
    
    # Step 2: Replace root with last element
    replace_value = self.heap_array.pop()
    
    if len(self.heap_array) > 0:
        self.heap_array[0] = replace_value
        
        # Step 3: Restore heap property by percolating down
        self.percolate_down(0)
    
    return max_value

# Trace Example:
# Starting heap: [70, 30, 50]
max_val = heap.remove()
# Removed 70
# After pop: replace_value = 50, heap_array = [70, 30]
# After assignment: heap_array = [50, 30]
# After percolate_down: heap_array = [50, 30]
# Returns: 70

# Part 9: Heapsort in Python
def max_heap_percolate_down(node_index, heap_list, list_size):
    """
    Note: list_size allows us to work with a subset of the list
    This is crucial for heapsort!
    """
    child_index = 2 * node_index + 1
    value = heap_list[node_index]

    while child_index < list_size:
        max_value = value
        max_index = -1
        i = 0
        
        while i < 2 and i + child_index < list_size:
            if heap_list[i + child_index] > max_value:
                max_value = heap_list[i + child_index]
                max_index = i + child_index
            i = i + 1
                                    
        if max_value == value:
            return

        # Swap
        temp = heap_list[node_index]
        heap_list[node_index] = heap_list[max_index]
        heap_list[max_index] = temp
        
        node_index = max_index
        child_index = 2 * node_index + 1


def heap_sort(numbers):
    # PHASE 1: Heapify
    i = len(numbers) // 2 - 1
    while i >= 0:
        max_heap_percolate_down(i, numbers, len(numbers))
        i = i - 1
                
    # PHASE 2: Sort
    i = len(numbers) - 1
    while i > 0:
        # Swap max to end
        temp = numbers[0]
        numbers[0] = numbers[i]
        numbers[i] = temp

        # Fix heap on remaining elements
        max_heap_percolate_down(0, numbers, i)
        i = i - 1

# Part 10: Priority Queues
"""
The ADT (Abstract Data Type)
A priority queue is a queue where items are ordered by priority, not arrival time.

Common Operations:
- Operation	        Description	                            Example
- Enqueue(item)	    Insert item by priority	                Add patient with priority 8
- Dequeue()	        Remove highest priority item	        Treat most critical patient
- Peek()	        View highest priority (don't remove)	Check next patient
- IsEmpty()	        Check if queue is empty	                Any patients waiting?
- GetLength()	    Count items in queue	                How many patients?
"""
"""
Real-World Example: Emergency Room Priority Queue

Let's trace patient arrivals and treatment:

Patient 1 Arrives: John (broken finger, priority 3)
Priority Queue (Max-Heap):
   3 (John)

Array: [John(3)]

Patient 2 Arrives: Sarah (chest pain, priority 9)
STEP 1: Insert Sarah(9)
   3
   /
  9              Array: [John(3), Sarah(9)]

STEP 2: Percolate up (9 > 3, swap)
   9
   /
  3              Array: [Sarah(9), John(3)]

Current queue: Sarah will be treated first!

Patient 3 Arrives: Mike (headache, priority 2)
STEP 1: Insert Mike(2)
   9
   /  \
  3    2         Array: [Sarah(9), John(3), Mike(2)]

No swaps needed (2 < 9)

Current queue order: Sarah(9), John(3), Mike(2)

Patient 4 Arrives: Emma (broken arm, priority 7)
STEP 1: Insert Emma(7)
   9
   /  \
  3    2
  /
 7               Array: [Sarah(9), John(3), Mike(2), Emma(7)]

STEP 2: Compare with parent
7 > 3? YES → SWAP

   9
   /  \
  7    2
  /
 3               Array: [Sarah(9), Emma(7), Mike(2), John(3)]

Current queue: Sarah will be treated, then Emma

Doctor Ready: Dequeue (Treat Highest Priority)
TREATING: Sarah(9)

STEP 1: Remove root
Removed: Sarah(9)

STEP 2: Replace with last (John)
   3
   /  \
  7    2         Array: [John(3), Emma(7), Mike(2)]

STEP 3: Percolate down
Compare 3 with children (7, 2)
7 is largest → SWAP

   7
   /  \
  3    2         Array: [Emma(7), John(3), Mike(2)]

NEXT PATIENT: Emma(7)
"""
"""
Implementation with Heaps

Priority Queue Operation	     Heap Operation	                Time Complexity
Enqueue	                         Insert (percolate up)	        O(log n)
Dequeue	                         Remove root (percolate down)	O(log n)
Peek	                         Access root element	        O(1)
IsEmpty	                         Check if heap is empty	        O(1)
GetLength	                     Return heap size	            O(1)

Why heaps are perfect for priority queues:
✓ Root always has highest priority
✓ Insert/remove are efficient: O(log n)
✓ Simple array implementation
✓ No wasted space
"""
# Summary and Key Takeaways
"""
Heap Properties

Complete binary tree (filled level-by-level, left-to-right)
Max-heap: Parent ≥ Children (root = maximum)
Min-heap: Parent ≤ Children (root = minimum)
Root always contains the extreme value

Core Operations & Complexity
Insert: Add at end, percolate UP → O(log n)
Remove: Remove root, replace with last, percolate DOWN → O(log n)
Peek/Find Max: Access root → O(1)
Search: Must check all nodes → O(n)  NOT efficient!

Array Implementation Formulas
Parent index: (i - 1) // 2
Left child index: 2i + 1
Right child index: 2i + 2

Applications
Priority Queues (emergency rooms, job scheduling, task management)
Heapsort (in-place O(n log n) sorting algorithm)
Graph algorithms (Dijkstra's shortest path, Prim's MST)
Finding k largest/smallest elements
"""
# Practice Questions
"""
1. Build a max-heap by inserting: 25, 15, 40, 10, 50, 30
- Draw each step
- Show the final array
- Remove operations: Starting with your heap from Q1, show each step of removing the max three times

2. Index calculations: In a heap with array [80, 60, 70, 40, 50, 30, 20]:
- What are the children of index 1?
- What is the parent of index 5?
- Draw the tree structure

3. Min-heap: Convert the array [50, 20, 70, 10, 40] into a min-heap
4. Heapsort trace: Sort [15, 10, 30, 20, 5] using heapsort - show all steps
"""