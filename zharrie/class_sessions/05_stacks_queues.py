"""
Tonight, we'll explore three essential Abstract Data Types (ADTs) that form the building blocks of countless algorithms and applications in computer science:

1. Stack - Last-In, First-Out (LIFO)
2. Queue - First-In, First-Out (FIFO)
3. Deque - Flexible access at both ends
"""

# 1: STACK - The LIFO Structure
# 1.1 Understanding Stacks
"""
Conceptual Model
A stack is like a stack of plates in a cafeteria:
- You can only add a plate to the top
- You can only remove a plate from the top
- The last plate you added is the first one you'll remove
- This is the LIFO (Last-In, First-Out) principle.

Core Operations
Operation	        Description	                                Visual Example
Push(stack, x)	    Add item x to the top	                    [77] → Push(99) → [99,77]
Pop(stack)	        Remove and return the top item	            [99,77] → Pop() returns 99 → [77]
Peek(stack)	        Look at the top item without removing it	[99,77] → Peek() returns 99 → [99,77]
IsEmpty(stack)	    Check if stack has no items	                [99,77] → IsEmpty() returns False
GetLength(stack)	Count the number of items	                [99,77] → GetLength() returns 2

Complete Example Sequence
Start: empty stack []
Push(7)    → [7]
Push(14)   → [14, 7]
Push(9)    → [9, 14, 7]
Push(5)    → [5, 9, 14, 7]
Pop()      → returns 5, stack is now [9, 14, 7]
Pop()      → returns 9, stack is now [14, 7]
Peek()     → returns 14, stack is still [14, 7]
Key Insight: The most recently added item is always the first to be removed.
"""
# 1.2 Stack Implementation #1: Using a Linked List
"""
Why Linked Lists Work Well
A singly-linked list naturally supports stack operations:
- The list's head becomes the stack's top
- Each node points to the node below it
- All operations happen at the head (constant time)

Visual Structure
Stack Top → [5] → [9] → [14] → [7] → None
            ↑
         (most recent)

Implementation Strategy
Push Operation (Prepending):
- Create a new node with the item
- Point the new node to the current top
- Update top to reference the new node

Before Push(3):     After Push(3):
Top → [5] → [9]     Top → [3] → [5] → [9]

Pop Operation (Removing Head):
- Save the top node's data
- Move top pointer to the next node
- Return the saved data

Before Pop():       After Pop():
Top → [3] → [5]     Top → [5] → [9]
"""

# Python Implementation
# Node class for the linked list
class StackNode:
    def __init__(self, data_value, next_node):
        self.data = data_value
        self.next = next_node

# Stack class using linked list
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, new_data):
        """Add an item to the top of the stack"""
        # Create new node that points to current top
        self.top = StackNode(new_data, self.top)
        return True
    
    def pop(self):
        """Remove and return the top item"""
        # Save the data from the top node
        popped_item = self.top.data
        
        # Move top pointer to the next node
        self.top = self.top.next
        
        return popped_item
    
    def peek(self):
        """Return the top item without removing it"""
        return self.top.data
    
    def is_empty(self):
        """Check if stack is empty"""
        return self.top == None
    
    def get_length(self):
        """Count the number of items in the stack"""
        node = self.top
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count
    
    def print(self, separator=", ", suffix=""):
        """Print stack from top to bottom"""
        node = self.top
        if node != None:
            print(node.data, end="")
            node = node.next
            while node != None:
                print(f"{separator}{node.data}", end="")
                node = node.next
            print(suffix, end="")



# Example
# Create and use the stack
num_stack = Stack()

# Push items
num_stack.push(45)
num_stack.push(56)
num_stack.push(11)

print("Stack after pushes: ", end="")
num_stack.print(", ", "\n")
# Output: Stack after pushes: 11, 56, 45

# Pop an item
popped_item = num_stack.pop()
print(f"Popped: {popped_item}")
# Output: Popped: 11

print("Stack after pop: ", end="")
num_stack.print(", ", "\n")
# Output: Stack after pop: 56, 45
"""
Time Complexity Analysis:

Push: O(1) - constant time
Pop: O(1) - constant time
Peek: O(1) - constant time
GetLength: O(n) - must traverse entire list
"""

#1.3 Stack Implementation #2: Using an Array
"""
Array Storage Structure
An array-based stack uses:
- stack_list: The array holding items
- length: Number of items currently in the stack

Organization:
Index:     0    1    2    3    4
Array:   [45] [56] [11] [ ] [ ]
         ↑              ↑
       bottom          top
                  (length=3)
Bottom item at index 0
Top item at index (length - 1)
Empty when length = 0

Bounded vs. Unbounded Stacks

Bounded Stack (Fixed Maximum):
- Cannot exceed a predetermined maximum size
- Returns false if push would exceed limit
- Example: A stack limited to 100 items

Unbounded Stack (Grows as Needed):
- Can grow indefinitely (limited only by memory)
- Automatically resizes the array when full
- More flexible but requires reallocation overhead
"""
# Simple Python Implementation
class Stack:
    """Simple unbounded stack using Python list"""
    
    def __init__(self):
        self.stack_list = []
    
    def push(self, item):
        """Add item to top of stack"""
        self.stack_list.append(item)
    
    def pop(self):
        """Remove and return top item"""
        return self.stack_list.pop()
    
    def peek(self):
        """Return top item without removing"""
        return self.stack_list[-1]
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.stack_list) == 0
    
    def get_length(self):
        """Return number of items"""
        return len(self.stack_list)

# Why this is simple: Python lists handle dynamic resizing automatically!

# Flexible Implementation (Bounded or Unbounded)
class Stack:
    """Stack that can be bounded or unbounded"""
    
    def __init__(self, optional_max_length=-1):
        """
        Initialize stack.
        If optional_max_length < 0: unbounded stack
        If optional_max_length >= 0: bounded stack with that maximum
        """
        self.stack_list = []
        self.max_length = optional_max_length
    
    def push(self, item):
        """Push item onto stack. Returns True if successful, False if full."""
        # Check if we're at maximum capacity
        if len(self.stack_list) == self.max_length:
            return False  # Stack is full
        
        # Add the item
        self.stack_list.append(item)
        return True
    
    def pop(self):
        """Remove and return top item"""
        return self.stack_list.pop()
    
    def peek(self):
        """Return top item without removing"""
        return self.stack_list[-1]
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.stack_list) == 0
    
    def get_length(self):
        """Return current number of items"""
        return len(self.stack_list)
    
    def get_max_length(self):
        """Return maximum capacity (-1 if unbounded)"""
        return self.max_length
    
# Examples
# Unbounded stack
unlimited = Stack()
unlimited.push(1)
unlimited.push(2)
unlimited.push(3)
# Can keep pushing indefinitely

# Bounded stack (max 2 items)
limited = Stack(2)
print(limited.push(1))  # True
print(limited.push(2))  # True
print(limited.push(3))  # False - stack is full!

# 1.4 Stack Summary
"""
When to Use Stacks
✓ Undo mechanisms - Text editors, graphics programs 
✓ Expression evaluation - Parsing mathematical expressions 
✓ Backtracking algorithms - Depth-first search, maze solving 
✓ Bracket matching - Checking balanced parentheses

Implementation Comparison
Feature	                Linked List	                    Array-Based
Push/Pop complexity	    O(1) always	                    O(1) amortized*
Memory overhead	        Higher (node pointers)	        Lower (contiguous storage)
Cache performance	    Worse (scattered nodes)	        Better (contiguous memory)
Size flexibility	    Always dynamic	                Depends on implementation
*Amortized means occasional O(n) for resize, but O(1) on average
"""
# 2: QUEUE - The FIFO Structure
"""
Conceptual Model
A queue is like waiting in line at a grocery store:
- People join at the back of the line
- People are served from the front of the line
- The first person to arrive is the first person served
- This is the FIFO (First-In, First-Out) principle.

Core Operations
Operation	                Description	                                Visual Example
Enqueue(queue, x)	        Add item x to the back	                    [43, 12] → Enqueue(77) → [43, 12, 77]
Dequeue(queue)	            Remove and return the front item	        [43, 12, 77] → Dequeue() returns 43 → [12, 77]
Peek(queue)	                Look at the front item without removing	    [43, 12, 77] → Peek() returns 43 → [43, 12, 77]
IsEmpty(queue)	            Check if queue has no items	                [43, 12, 77] → IsEmpty() returns False
GetLength(queue)	        Count the number of items	                [43, 12, 77] → GetLength() returns 3

Complete Example Sequence

Start: empty queue []
Enqueue(7)    → [7]
Enqueue(14)   → [7, 14]
Enqueue(9)    → [7, 14, 9]
Dequeue()     → returns 7, queue is now [14, 9]
Dequeue()     → returns 14, queue is now [9]
Peek()        → returns 9, queue is still [9]
Enqueue(25)   → [9, 25]
Key Insight: Items are processed in the exact order they arrive.
"""

# 2.2 Queue Implementation #1: Using a Linked List
"""
Why Linked Lists Work Well
A singly-linked list with both head and tail pointers naturally supports queue operations:
- front pointer → list's head (where we dequeue)
- end pointer → list's tail (where we enqueue)
- Enqueue at tail, dequeue from head

Visual Structure
Front → [17] → [24] → [18] → None
         ↑              ↑
      (dequeue)     (enqueue)
                      End

Implementation Strategy
Enqueue Operation (Appending):
- Create a new node with the item
- If queue is empty, set both front and end to the new node
- Otherwise, link the current end's next to the new node
- Update end to point to the new node
Before Enqueue(30):           After Enqueue(30):
Front → [17] → [24] ← End     Front → [17] → [24] → [30] ← End

Dequeue Operation (Removing Head):
- Save the front node's data
- Move front pointer to the next node
- If queue becomes empty, also set end to None
- Return the saved data
Before Dequeue():             After Dequeue():
Front → [17] → [24] ← End     Front → [24] ← End
"""

# Python Implementation
# Node class for the linked list
class QueueNode:
    def __init__(self, data_value, next_node=None):
        self.data = data_value
        self.next = next_node

# Queue class using linked list
class Queue:
    def __init__(self):
        self.front = None
        self.end = None
    
    def enqueue(self, new_data):
        """Add an item to the back of the queue"""
        # Create a new node
        new_node = QueueNode(new_data)
        
        # If queue is empty, front and end are the same
        if self.front == None:
            self.front = new_node
            self.end = new_node
        else:
            # Link current end to new node
            self.end.next = new_node
            # Update end pointer
            self.end = new_node
    
    def dequeue(self):
        """Remove and return the front item"""
        # Save the front node's data
        dequeued_item = self.front.data
        
        # Move front pointer to next node
        self.front = self.front.next
        
        # If queue is now empty, also update end
        if self.front == None:
            self.end = None
        
        return dequeued_item
    
    def peek(self):
        """Return the front item without removing it"""
        return self.front.data
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.front == None
    
    def print(self, separator=", ", suffix=""):
        """Print queue from front to back"""
        node = self.front
        if node != None:
            print(node.data, end="")
            node = node.next
            while node != None:
                print(f"{separator}{node.data}", end="")
                node = node.next
            print(suffix, end="")

# Example
# Create and use the queue
num_queue = Queue()

# Enqueue items
num_queue.enqueue(17)
num_queue.enqueue(24)
num_queue.enqueue(18)

print("Queue after enqueues: ", end="")
num_queue.print(", ", "\n")
# Output: Queue after enqueues: 17, 24, 18

# Dequeue an item
dequeued_item = num_queue.dequeue()
print(f"Dequeued: {dequeued_item}")
# Output: Dequeued: 17

print("Queue after dequeue: ", end="")
num_queue.print(", ", "\n")
# Output: Queue after dequeue: 24, 18
"""
Time Complexity Analysis:
- Enqueue: O(1) - constant time
- Dequeue: O(1) - constant time
- Peek: O(1) - constant time
"""

#2.3 Queue Implementation #2: Using an Array (Circular Buffer)
"""
The Challenge with Arrays
Unlike stacks, queues have a problem with simple array implementation.

What's Wrong with a Simple Array?
Let's see what happens if we implement a queue with a basic array approach:

Simple (but wrong) approach:
We'll put items starting at index 0, and keep track of where the front and back are.

Initial state:
Array: [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ]
Index:  0    1     2    3    4    5   6    7

Enqueue(10):
Array: [10] [  ] [  ] [  ] [  ] [  ] [  ] [  ]
        ↑
       front & back

Enqueue(20):
Array: [10] [20] [  ] [  ] [  ] [  ] [  ] [  ]
        ↑    ↑
      front back

Enqueue(30):
Array: [10] [20] [30] [  ] [  ] [  ] [  ] [  ]
        ↑         ↑
      front      back

So far so good! But now watch what happens when we dequeue:
Dequeue() → removes 10
Array: [  ] [20] [30] [  ] [  ] [  ] [  ] [  ]
             ↑    ↑
           front back

Dequeue() → removes 20
Array: [  ] [  ] [30] [  ] [  ] [  ] [  ] [  ]
                  ↑
              front & back

Enqueue(40):
Array: [  ] [  ] [30] [40] [  ] [  ] [  ] [  ]
                  ↑    ↑
                front back

Enqueue(50):
Array: [  ] [  ] [30] [40] [50] [  ] [  ] [  ]
                  ↑         ↑
                front      back

... continue adding more items ...

Array: [  ] [  ] [30] [40] [50] [60] [70] [80]
                  ↑                        ↑
                front                     back

Now try to Enqueue(90):
Array: [  ] [  ] [30] [40] [50] [60] [70] [80] [??]
        ↑    ↑
     WASTED SPACE!

THE PROBLEM:
- We have 2 empty spaces at the beginning (indices 0 and 1)
- But we can't use them because back keeps moving forward
- We'll run out of space even though the array isn't actually full!
- This is inefficient and wasteful!

- The Circular Buffer Solution
Instead of treating the array as a straight line, treat it as a circle.

Linear thinking (wrong):
[0] → [1] → [2] → [3] → [4] → [5] → [6] → [7] → END! ❌

Circular thinking (correct):
      [0] → [1]
      ↑      ↓
    [7]      [2]
      ↑      ↓
    [6]      [3]
      ↑      ↓
      [5] ← [4]

After [7] comes [0] again! ✓
When you reach the end of the array, you wrap around to the beginning!

How Do We Create This "Wraparound"?
The Modulo Operator (%)
The modulo operator gives you the remainder after division.

Examples with array size 8:
Index calculation: position % 8

0 % 8 = 0
1 % 8 = 1
2 % 8 = 2
...
7 % 8 = 7
8 % 8 = 0  ← Goes back to 0!
9 % 8 = 1  ← Goes to 1!
10 % 8 = 2 ← Goes to 2!
This automatically creates the wraparound effect!

- How Circular Buffer Works
What We Track
Instead of tracking front and back positions, we track:
- queue_list - the array itself
- front_index - where the first item is located
- length - how many items are currently in the queue
- max_size - the size of the array

Why length instead of back?
We can calculate where to add new items using: (front_index + length) % max_size
It's easier to check if the queue is full: length == max_size

The Two Core Operations
ENQUEUE (Adding an Item)
Steps:
- Check if queue is full: if length == max_size
- Calculate where to put the new item: position = (front_index + length) % max_size
- Place the item: queue_list[position] = item
- Increment length: length += 1

Why this formula works:
- front_index tells us where the queue starts
- + length skips over all existing items to find the back
- % max_size wraps around if we go past the end

DEQUEUE (Removing an Item)
Steps:
- Check if queue is empty: if length == 0
- Get the front item: item = queue_list[front_index]
- Move front forward: front_index = (front_index + 1) % max_size
- Decrement length: length -= 1
- Return the item

Why this formula works:
- front_index + 1 moves to the next position
- % max_size wraps to 0 if we were at the end

Complete Visual Example
Let's use a small array (size 5) to see every detail:

Initial State:
Array:  [  ] [  ] [  ] [  ] [  ]
Index:   0     1    2    3    4

front_index = 0
length = 0
max_size = 5

Operation 1: Enqueue(A)
Calculate position: (0 + 0) % 5 = 0
Array:  [A] [  ] [  ] [  ] [  ]
         ↑
    front_index = 0
    length = 1

Operation 2: Enqueue(B)
Calculate position: (0 + 1) % 5 = 1
Array:  [A] [B] [  ] [  ] [  ]
         ↑
    front_index = 0
    length = 2
    
Queue order: A → B

Operation 3: Enqueue(C)
Calculate position: (0 + 2) % 5 = 2
Array:  [A] [B] [C] [  ] [  ]
         ↑
    front_index = 0
    length = 3
    
Queue order: A → B → C

Operation 4: Dequeue() → Returns A
Get item at index 0 (front_index) New front_index: (0 + 1) % 5 = 1
Array:  [  ] [B] [C] [  ] [  ]
              ↑
    front_index = 1
    length = 2
    
Queue order: B → C

Operation 5: Dequeue() → Returns B
Get item at index 1 (front_index) New front_index: (1 + 1) % 5 = 2
Array:  [  ] [  ] [C] [  ] [  ]
                   ↑
    front_index = 2
    length = 1
    
Queue order: C

Operation 6: Enqueue(D)
Calculate position: (2 + 1) % 5 = 3
Array:  [  ] [  ] [C] [D] [  ]
                   ↑
    front_index = 2
    length = 2
    
Queue order: C → D

Operation 7: Enqueue(E)
Calculate position: (2 + 2) % 5 = 4
Array:  [  ] [  ] [C] [D] [E]
                   ↑
    front_index = 2
    length = 3
    
Queue order: C → D → E

Operation 8: Enqueue(F) ← THE WRAPAROUND!
Calculate position: (2 + 3) % 5 = 5 % 5 = 0 

The position wraps to index 0!
Array:  [F] [  ] [C] [D] [E]
                  ↑
    front_index = 2
    length = 4
    
Queue order: C → D → E → F
             ↑           ↑
          index 2     index 0
See how F is at index 0, but C is still the front because front_index = 2!

Operation 9: Enqueue(G)
Calculate position: (2 + 4) % 5 = 6 % 5 = 1
Array:  [F] [G] [C] [D] [E]
                 ↑
    front_index = 2
    length = 5 (FULL!)
    
Queue order: C → D → E → F → G
             ↑              ↑
          index 2        index 1

Operation 10: Dequeue() → Returns C
Get item at index 2 (front_index) New front_index: (2 + 1) % 5 = 3
Array:  [F] [G] [  ] [D] [E]
                      ↑
    front_index = 3
    length = 4
    
Queue order: D → E → F → G

Operation 11: Dequeue() → Returns D
Get item at index 3 New front_index: (3 + 1) % 5 = 4
Array:  [F] [G] [  ] [  ] [E]
                           ↑
    front_index = 4
    length = 3
    
Queue order: E → F → G

Operation 12: Dequeue() → Returns E
Get item at index 4 New front_index: (4 + 1) % 5 = 5 % 5 = 0
front_index wraps back to 0!
Array:  [F] [G] [  ] [  ] [  ]
         ↑
    front_index = 0 (wrapped!)
    length = 2
    
Queue order: F → G
"""
# Implementation
class CircularQueue:
    def __init__(self, size):
        """Initialize an empty circular queue"""
        self.queue_list = [None] * size  # Create array of given size
        self.front_index = 0              # Where the front item is
        self.length = 0                   # How many items we have
        self.max_size = size              # Maximum capacity
    
    def enqueue(self, item):
        """Add an item to the back of the queue"""
        # Step 1: Check if queue is full
        if self.length == self.max_size:
            print("Queue is full!")
            return False
        
        # Step 2: Calculate where to put the item (with wraparound)
        position = (self.front_index + self.length) % self.max_size
        
        # Step 3: Place the item
        self.queue_list[position] = item
        
        # Step 4: Increase length
        self.length += 1
        
        return True
    
    def dequeue(self):
        """Remove and return the front item"""
        # Step 1: Check if queue is empty
        if self.length == 0:
            print("Queue is empty!")
            return None
        
        # Step 2: Get the front item
        item = self.queue_list[self.front_index]
        
        # Step 3: Move front_index forward (with wraparound)
        self.front_index = (self.front_index + 1) % self.max_size
        
        # Step 4: Decrease length
        self.length -= 1
        
        # Step 5: Return the item
        return item
    
    def peek(self):
        """Look at the front item without removing it"""
        if self.length == 0:
            return None
        return self.queue_list[self.front_index]
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.length == 0
    
    def is_full(self):
        """Check if queue is full"""
        return self.length == self.max_size
    
    def get_length(self):
        """Return the number of items"""
        return self.length
"""
Key Concepts Summary

The Three Magic Formulas
Operation	                        Formula	                                What It Does
Where to enqueue	                (front_index + length) % max_size	    Finds the back position with wraparound
Where front goes after dequeue	    (front_index + 1) % max_size	        Moves front forward with wraparound
Is full?	                        length == max_size	                    All slots are occupied
Is empty?	                        length == 0	                            No items in queue

Why Modulo (%) is Essential

Without modulo:
position = front_index + length
# If front_index = 3, length = 4, array size = 5
# position = 7 (OUT OF BOUNDS! ❌)

With modulo:
position = (front_index + length) % max_size
# If front_index = 3, length = 4, max_size = 5
# position = 7 % 5 = 2 (wraps around! ✓)
"""

"""
Bounded vs. Unbounded Queues

Bounded Queue:
- Has a fixed maximum capacity
- Returns false if enqueue would exceed max_length
- Never resizes

Unbounded Queue:
- Can grow indefinitely
- Automatically resizes when full
- max_length is negative to indicate unbounded
"""

# Complete ArrayQueue Class
class ArrayQueue:
    def __init__(self, maximum_length=-1):
        """
        Initialize queue.
        If maximum_length < 0: unbounded queue
        If maximum_length >= 0: bounded queue
        """
        self.queue_list = [0]  # Start with size 1
        self.front_index = 0
        self.length = 0
        self.max_length = maximum_length
    
    def enqueue(self, item):
        """Add item to back of queue"""
        # Check if at maximum capacity
        if self.length == self.max_length:
            return False
        
        # Resize if array is full
        if self.length == len(self.queue_list):
            self.resize()
        
        # Calculate position and insert
        item_index = (self.front_index + self.length) % len(self.queue_list)
        self.queue_list[item_index] = item
        self.length += 1
        return True
    
    def dequeue(self):
        """Remove and return front item"""
        to_return = self.queue_list[self.front_index]
        self.length -= 1
        self.front_index = (self.front_index + 1) % len(self.queue_list)
        return to_return
    
    def peek(self):
        """Return front item without removing"""
        return self.queue_list[self.front_index]
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.length == 0
    
    def get_length(self):
        """Return number of items in queue"""
        return self.length
    
    def get_max_length(self):
        """Return maximum capacity"""
        return self.max_length
    
    def resize(self):
        """Double the array size"""
        new_size = len(self.queue_list) * 2
        if self.max_length >= 0 and new_size > self.max_length:
            new_size = self.max_length
        
        new_list = [0] * new_size
        for i in range(self.length):
            item_index = (self.front_index + i) % len(self.queue_list)
            new_list[i] = self.queue_list[item_index]
        
        self.queue_list = new_list
        self.front_index = 0

# 2.5 Queue Summary
"""
When to Use Queues
✓ Task scheduling - Operating systems, print queues 
✓ Breadth-first search - Graph traversal algorithms 
✓ Buffer management - Data streaming, I/O buffering 
✓ Request handling - Web servers, message queues 
✓ Simulation - Modeling waiting lines, customer service
"""

# 3: DEQUE - The Double-Ended Queue
"""
3.1 Understanding Deques

Conceptual Model
A deque (pronounced "deck") is the most flexible of our three structures:
- You can add items to either the front or the back
- You can remove items from either the front or the back
- It combines the capabilities of both stacks and queues
Think of it as: A line where people can join or leave from either end (though this would be chaotic in real life!).

Core Operations
The deque has four fundamental operations:
Operation	                Description	                Visual Example
PushFront(deque, x)	        Insert at the front	        [59, 63] → PushFront(41) → [41, 59, 63]
PushBack(deque, x)	        Insert at the back	        [59, 63] → PushBack(41) → [59, 63, 41]
PopFront(deque)	            Remove from the front	    [59, 63, 19] → PopFront() returns 59 → [63, 19]
PopBack(deque)	            Remove from the back	    [59, 63, 19] → PopBack() returns 19 → [59, 63]

Complete Operation Set
Operation	            Description	                Example (starting: 59, 63, 19)
PushFront(deque, 41)	Insert at front	            Result: 41, 59, 63, 19
PushBack(deque, 41)	    Insert at back	            Result: 59, 63, 19, 41
PopFront(deque)	        Remove from front	        Returns: 59, Result: 63, 19
PopBack(deque)	        Remove from back	        Returns: 19, Result: 59, 63
PeekFront(deque)	    View front (no remove)	    Returns: 59, Unchanged
PeekBack(deque)	        View back (no remove)	    Returns: 19, Unchanged
IsEmpty(deque)	        Check if empty	            Returns: False
GetLength(deque)	    Count items	                Returns: 3

Complete Example Sequence

Start: empty deque []
PushBack(10)     → [10]
PushBack(20)     → [10, 20]
PushFront(5)     → [5, 10, 20]
PushBack(30)     → [5, 10, 20, 30]
PopFront()       → returns 5, deque is now [10, 20, 30]
PopBack()        → returns 30, deque is now [10, 20]
PeekFront()      → returns 10, deque is still [10, 20]
PeekBack()       → returns 20, deque is still [10, 20]
"""

# 3.2 Deque Implementations
"""
Implementation Options

Deques can be implemented using:
- Doubly-linked list - Most natural, efficient at both ends
- Circular array - Similar to queue, but need to handle both ends
- Python's collections.deque - Optimized built-in implementation
Note: For teaching purposes, we focus on the conceptual understanding. In practice, Python's collections.deque is highly optimized.

Doubly-Linked List Approach (Conceptual)
Front                                Back
  ↓                                   ↓
[None] ← [5] ↔ [10] ↔ [20] ↔ [30] → [None]

Each node has:
- data - the item
- next - pointer to next node
- prev - pointer to previous node
This allows O(1) operations at both ends.
"""
#Python's Built-in Deque
from collections import deque

# Create a deque
dq = deque()

# Operations
dq.append(10)        # PushBack: [10]
dq.append(20)        # PushBack: [10, 20]
dq.appendleft(5)     # PushFront: [5, 10, 20]
dq.append(30)        # PushBack: [5, 10, 20, 30]

item = dq.popleft()  # PopFront: returns 5, deque is [10, 20, 30]
item = dq.pop()      # PopBack: returns 30, deque is [10, 20]

front = dq[0]        # PeekFront: returns 10
back = dq[-1]        # PeekBack: returns 20

# 3.3 Deque Summary
"""
When to Use Deques
✓ Sliding window problems - Maximum in sliding window 
✓ Palindrome checking - Compare from both ends 
✓ Undo/Redo systems - Navigate history in both directions 
✓ Work stealing algorithms - Task schedulers 
✓ Browser history - Forward and back navigation

Relationship to Stack and Queue

A deque is a generalization:
- Restrict to PushBack + PopBack = Stack
- Restrict to PushBack + PopFront = Queue
- Use all four operations = Deque
"""
# 4: Comparative Analysis
# 4.1 Side-by-Side Comparison
"""
Aspect	            Stack	            Queue	                Deque
Access Pattern	    One end (top)	    Two ends (front/back)	Both ends freely
Ordering	        LIFO	            FIFO	                Flexible
Primary Ops	        Push, Pop	        Enqueue, Dequeue	    PushFront, PushBack, PopFront, PopBack
Real-World	        Stack of plates	    Waiting in line	        Double-ended line
Main Use	        Recursion, undo	    Scheduling, BFS	        Sliding window, palindromes
"""

# 4.2 Time Complexity Summary
"""
Linked List Implementations

Operation	                Stack	    Queue	    Deque
Insert (front/top)	        O(1)	    -	        O(1)
Insert (back/end)	        -	        O(1)	    O(1)
Remove (front/top)	        O(1)	    O(1)	    O(1)
Remove (back/end)	        -	        -	        O(1)
Peek	                    O(1)	    O(1)	    O(1)
GetLength	                O(n)*	    O(n)*	    O(n)*
*Can be O(1) if you maintain a length variable

Array Implementations
Operation	                Stack	            Queue	            Deque
Insert	                    O(1) amortized	    O(1) amortized	    O(1) amortized
Remove	                    O(1)	            O(1)	            O(1)
Peek	                    O(1)	            O(1)	            O(1)
GetLength	                O(1)	            O(1)	            O(1)

4.3 Space Complexity
Implementation	            Space Complexity	        Notes
Linked List	                O(n)	                    Additional pointer overhead per node
Array (bounded)	            O(k)	                    k = maximum capacity (may waste space)
Array (unbounded)	        O(n)	                    Exact space varies with resize strategy
"""
# Exercises
# 1.Write a function that removes all items from a stack.
def clear_stack(stack):
    # Your code here
    pass

# Test
s = Stack()
s.push(1)
s.push(2)
s.push(3)
clear_stack(s)
print(s.is_empty())  # Should print: True

# 2.Write a function to count items in a queue without destroying it.
def count_queue_items(queue):
    # Your code here
    pass

# Test
q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
print(count_queue_items(q))  # Should print: 3

# 3. Check if a string has balanced parentheses (only one type: ( and )).
def is_balanced_simple(text):
    """
    Input: "(()())"  → True
    Input: "(()"     → False
    Input: "())"     → False
    """
    # Your code here
    pass