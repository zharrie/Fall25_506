"""
Intro to Data Structures and Algorithms

We're going to explore the fundamental building blocks of modern software: Data  Structures and Algorithms. 
It might sound intimidating, but my goal is to make these concepts intuitive and clear. 
Think of this session as learning how to organize information and create recipes to solve problems, which is the very heart of effective and efficient programming.

Part 1: What Are Data Structures and Why Do We Need Them?
The Core Idea: A data structure is simply a way of organizing, storing, and managing data in a computer so that we can perform operations on it effectively.

The Filing Cabinet Analogy: Imagine you have a thousand important documents.

You could throw them all into one big pile on the floor. This is storing your data, but it's not organized. Finding a specific document would be a nightmare.
You could stack them neatly in chronological order. Now they're organized, but if you need a document from the middle, you have to lift half the stack.
You could put them in a filing cabinet, sorted alphabetically by title. Now finding a specific document is much faster.
In this analogy, the pile, the stack, and the filing cabinet are all data structures. Each has its own method of organization, and each has strengths and weaknesses depending on the task. 

The operations we want to perform are key:
- Accessing: Reading the data at a specific location.
- Searching: Looking for a specific piece of data.
- Inserting: Adding new data to the structure.
- Deleting: Removing data from the structure.
Choosing the right "filing cabinet" for your data is critical for writing fast and scalable software.
"""

"""
Part 2: The Basic Toolbox - Common Data Structures
Let's explore our "toolbox" of fundamental data structures with simple Python examples.

1. Record (or Struct/Object)
Concept: A collection of related data items, where each item (a "field") has a name and a value.
Analogy: A single contact card in your phone with fields for "First Name," "Last Name," and "Phone Number."
"""

# Python Example: The simplest way to create a record in Python is by using a dictionary.
# A dictionary is a perfect and simple way to represent a record.
# Each key is a "field" and each value is the data for that field.
employee1 = {
    "first_name": "Maria",
    "last_name": "Lu",
    "title": "Software Developer",
    "salary": 95000
}

# Accessing a field is easy and readable.
print(f"Employee Name: {employee1['first_name']} {employee1['last_name']}")
# Output: Employee Name: Maria Lu
# Performance: Accessing a field in a record is very fast.

"""
2. Array
Concept: An ordered collection of elements where each element has a numbered position, called an index, starting from 0.
Analogy: A numbered row of mailboxes or a pill organizer.
"""
# Python Example: Python's built-in list is a powerful and easy-to-use dynamic array.
# An array (using a Python list) of integers.
scores = [35, 20, 7, 18, 10]

# Accessing an element by its index is very fast because the computer
# can calculate its position in memory instantly. Indexes start at 0.
print(f"The first score is: {scores[0]}")  # Output: 35
print(f"The third score is: {scores[2]}")  # Output: 7

# Adding an item to the end is usually fast.
scores.append(42)
print(f"Scores after adding to end: {scores}")

# Inserting in the middle requires shifting elements, which can be slow.
# To insert 50 at index 3, the elements 18, 10, and 42 must be shifted to the right.
scores.insert(3, 50)
print(f"Scores after inserting in middle: {scores}")
"""
Trade-offs:
Core Strength: Fast, predictable access to any element using its index (O(1)).
Use When: You need to read elements by their position frequently, and the size of the collection is either fixed or doesn't change often.

Best Use Cases:
Storing a Grid of Data: Think of the pixels on a screen or the cells in a spreadsheet. You need to be able to instantly access the element at (row, column). A 2D array is perfect for this.
A Collection of Elements to be Read Quickly: If you have a list of the 50 states in the USA and you want to get the 5th one, an array is ideal. You can access states[4] instantly.
As a Buffer: When programs read data from a file or a network, they often load it into a fixed-size array (a buffer) for temporary storage and processing.

When to Avoid: When you need to constantly add or remove elements from the middle of the collection. For example, modeling a line of text in a word processor with an array would be inefficient, as every character insertion or deletion would require shifting all subsequent characters.
"""

"""
3. Linked List
Concept: An ordered collection of items (nodes) where each node contains data and a pointer to the next node. They are not stored side-by-side in memory.
Analogy: A scavenger hunt. Each clue (a node) contains information and tells you the location of the next clue.
"""

# Python Example: To understand the concept, we'll build a short linked list manually.
# First, define the blueprint for a single node (a single clue in our scavenger hunt).
class Node:
    def __init__(self, data):
        self.data = data  # The data the node holds (e.g., 10, 5, 17)
        self.next = None  # The pointer to the next node, initially pointing to nothing

# Now, let's create our individual nodes.
node1 = Node(10)
node2 = Node(5)
node3 = Node(17)

# Now, let's link them together to form the chain: 10 -> 5 -> 17
# The 'head' of our list is node1.
node1.next = node2  # The node with 10 now points to the node with 5.
node2.next = node3  # The node with 5 now points to the node with 17.
# node3.next is already None, which marks the end of the list.

# To see our list, we must start at the beginning (node1) and follow the pointers.
print("Traversing the linked list:")
current_node = node1
while current_node is not None:
    print(current_node.data, end=" -> ")
    current_node = current_node.next # Move to the next node in the chain
print("None")
# Output: Traversing the linked list: 10 -> 5 -> 17 -> None

"""
Trade-offs:
Core Strength: Extremely fast insertion and deletion of elements, especially at the beginning and end (O(1)).
Use When: You have an ordered collection that needs to grow and shrink frequently. The order of items is important, but you don't need instant access to the Nth item.

Best Use Cases:
Music Playlists or Task Queues: You are constantly adding songs to the end, removing them from the middle, or moving them around. A linked list makes these insertions and deletions very cheap because you only need to update a few pointers, not shift large blocks of memory.
Implementing "Undo" Functionality: Each action a user takes (typing a word, deleting a line) can be a node in a linked list. Clicking "Undo" simply removes the last node from the list and reverses the action. This is a Stack, which is often implemented with a linked list.
Managing a Line (a Queue): Think of a line at a checkout counter. People are added to the back (tail) and served from the front (head). A linked list is perfect because adding to the tail and removing from the head are both very fast O(1) operations.

When to Avoid: When you need to frequently access elements by their index. Asking for the 500,000th song in a massive playlist would be very slow, as you'd have to traverse the list from the beginning.
"""

"""
4. Hash Table (or Dictionary)
Concept: A structure for storing key-value pairs. It uses a special function (a hash function) to convert the key into an array index, allowing for extremely fast lookups.

Analogy: A magical filing cabinet. You give it a key (the file's title), and it instantly tells you which drawer to open.
"""

# Python Example: Python's dict is a highly optimized hash table.
# Python's dictionary is a hash table. It's simple and powerful.
# Let's map student names (keys) to their grades (values).
student_grades = {
    "Maria": 92,
    "David": 85,
    "Emily": 98
}

# Accessing a value by its key is extremely fast, no matter how many students there are.
print(f"Emily's grade is: {student_grades['Emily']}") # Output: 98

# Adding a new student is just as fast.
student_grades["John"] = 89
print(f"John's grade is: {student_grades['John']}") # Output: 89

# Check if a student exists in the dictionary.
if "Maria" in student_grades:
    print("Maria is in the class.")

"""
Trade-offs:
Core Strength: Near-instantaneous lookup, insertion, and deletion of items based on a unique key (O(1) on average).
Use When: You need to store and retrieve data by a specific identifier or name. The primary operation is "finding" or "mapping."

Best Use Cases:
Phone Contacts or User Profiles: You want to find a person's information by using their name or user ID (the key). A hash table provides the fastest possible lookup.
Database Indexing: This is a critical real-world use. To find a user record in a massive database quickly, the database doesn't scan the entire file. Instead, it uses an index (a hash table) that maps the user_id (key) to the exact location of the user's data on the disk (value).
Caching: When a program performs an expensive calculation, it can store the result in a hash table with the input as the key. If the same input is requested again, the program can retrieve the result instantly from the cache instead of re-computing it.

When to Avoid: When you need the data to be sorted. Hash tables do not maintain any predictable order.
"""

"""
Part 3: How Do We Calculate Efficiency? (Big O and Space Complexity)
When we say an algorithm is "fast" or "slow," we use Big O Notation to be precise. 
It describes how the resources (time or memory) required by an algorithm grow as the input size, N, increases.

Calculating Runtime Complexity (Big O Notation)
Let's find the Big O of a function by counting its steps relative to the input size N.

The Rules of Thumb:
- Single Operations are O(1): Any single, simple step like variable assignment, arithmetic (+, -), or accessing an array index (my_list[i]) is considered constant time, or O(1).
- Loops are O(n): A loop that runs N times (where N is the size of the input) contributes O(n).
- Nested Loops are O(n^2): A loop inside another loop that both run N times results in N*N operations, so O(n^2).
- Keep the Biggest Term: In a sum like O(n^2 + n), the n^2 term grows much faster and will dominate as n gets large. We simplify the whole expression to just O(n^2).
- Drop Constants: We care about the rate of growth, not the exact number of operations. An algorithm that takes 2n steps and one that takes n steps both grow linearly, so we simplify them both to O(n).
Example in Practice: Let's analyze a function that finds the largest number in a list.

"""

def find_max_value(numbers_list):
    # Assume the input list has a size of N.
    
    max_val = numbers_list[0]    # Step 1: An assignment and an access. This is O(1).
    
    for number in numbers_list:  # Step 2: This loop runs N times. This part is O(n).
        if number > max_val:     # Step 3: Inside the loop, a comparison. This is O(1).
            max_val = number     # Step 4: Inside the loop, an assignment. This is O(1).
            
    return max_val               # Step 5: A single return. This is O(1).
"""
Let's add it up:

Total operations: We have O(1) at the start, then a loop that runs N times. Inside the loop, the operations are O(1). Finally, we have an O(1) at the end.
Formula: Total Time = O(1) + N * O(1) + O(1) = O(1 + n + 1) = O(n + 2).

Apply the Rules:
- Keep the Biggest Term: In n + 2, the n term is the biggest. So we have O(n).
- (Rule 5, dropping constants, is also implicitly used here).
Final Answer: The runtime complexity of find_max_value is O(n). This means the time it takes to run is directly proportional to the number of items in the list.


Calculating Space Complexity
Space complexity measures how much additional memory an algorithm needs to run, as a function of the input size N. 
We usually ignore the space taken by the input itself and focus on the extra space.

Example 1: Constant Space O(1)

Let's look at our find_max_value function again.

The input numbers_list takes up N space.
Inside the function, we create one extra variable: max_val. This variable takes up a fixed, constant amount of space. 
It doesn't matter if the input list has 10 items or 10 million items; we still only need this one extra variable.
Final Answer: The auxiliary space complexity (extra space used) is O(1).
The real measure of an algorithm's efficiency is how much additional space it needs to do it's job.
"""
"""
Example 2: Linear Space O(n)
Now consider a function that duplicates a list.

"""

def duplicate_list(numbers_list):
    # The input list has a size of N.
    
    new_list = []                # We create a new, empty list.
    
    for number in numbers_list:  # The loop runs N times.
        new_list.append(number)  # We add N items to our new list.
        
    return new_list

"""
The new_list variable starts empty but grows with the input. For every one of the N items in the input, we add one item to new_list.
By the end, new_list will also hold N items. The extra memory required grows in direct proportion to the input size.
Final Answer: The auxiliary space complexity is O(n).
"""

"""
Common type of space complexity.

1. O(1) — Constant Space Complexity

This is the most space-efficient category. It means the algorithm requires the same, fixed amount of extra memory, regardless of the size of the input (n).

Analogy: You need one pencil and one measuring tape. It doesn't matter if you're building a small birdhouse (n=10) or a giant dining table (n=1,000,000). The number of tools on your workbench stays the same.

"""
# Example A: Summing a list
def sum_list(numbers):
    # The input 'numbers' takes O(n) space. We ignore this for auxiliary complexity.
    
    # We create ONE extra variable to hold the sum.
    total_sum = 0  # This is our O(1) auxiliary space.
    
    for number in numbers:
        total_sum += number
        
    return total_sum

# Whether the list has 5 elements or 5 million, the function only ever
# needs one extra variable: 'total_sum'.
# Therefore, the auxiliary space complexity is O(1).

"""
Example B: An "in-place" algorithm
An algorithm that modifies the input directly without creating a new data structure is the classic example of O(1) space.
"""

def reverse_list_in_place(numbers):
    # This algorithm reverses the list by swapping elements.
    # It only needs a few variables to keep track of positions.
    
    left_index = 0              # One variable: O(1) space
    right_index = len(numbers) - 1 # Another variable: O(1) space
    
    while left_index < right_index:
        # We need one temporary variable to perform the swap.
        temp = numbers[left_index] # A third variable: O(1) space
        numbers[left_index] = numbers[right_index]
        numbers[right_index] = temp
        
        left_index += 1
        right_index -= 1
        
    return numbers

# The total number of extra variables (left_index, right_index, temp) is 3.
# This number does not change whether the input list has 10 elements or 10,000.
# It's a fixed amount of extra space.
# Therefore, the auxiliary space complexity is O(1).

"""
2. O(n) — Linear Space Complexity
This means the amount of extra memory the algorithm needs grows in direct proportion to the size of the input (n).

Analogy: You are painting a set of chair parts. To avoid getting paint everywhere, you lay each part down on a large piece of newspaper. If you have 10 parts (n=10), you need a small newspaper. If you have 100 parts (n=100), you need a newspaper ten times as big. The workbench space you need is directly proportional to the number of parts.
Example: Duplicating a list

This is the most straightforward example of O(n) space complexity.
"""

def duplicate_list(numbers):
    # The input 'numbers' has a size of n.
    
    # We create a NEW list to store the copy.
    new_list = []  # Initially O(1), but it will grow.
    
    for number in numbers:
        # For every one of the 'n' items in the input,
        # we add one item to our new_list.
        new_list.append(number)
        
    return new_list

# If the input list has 10 items, 'new_list' will end up with 10 items.
# If the input has 1 million items, 'new_list' will have 1 million items.
# The extra space required is directly proportional to 'n'.
# Therefore, the auxiliary space complexity is O(n).

"""
3. O(log n) — Logarithmic Space Complexity
This is a more advanced, but important, case. It means the extra space grows very slowly as the input gets much larger. This is most commonly seen in recursive algorithms.

The Key Concept: The Call Stack. Every time a function calls itself (recursion), the computer uses a small amount of memory on the "call stack" to remember where it was. This memory is a form of auxiliary space.
Analogy: Imagine a set of nested boxes. To get to the innermost box, you have to open each outer box. The stack of open lids represents the memory used. In O(log n) recursion, the number of nested calls is very small compared to the input size.

Example: Recursive Binary Search
Binary search works by repeatedly halving the input. The number of times you can halve a set of n items before you get to one is log₂(n).
"""

def recursive_binary_search(numbers, target, left, right):
    # This function uses space on the call stack for each recursive call.
    
    if left > right:
        return -1 # Base case: target not found
    
    middle = (left + right) // 2
    
    if numbers[middle] == target:
        return middle
    elif numbers[middle] < target:
        # Recursive call. A new "frame" is added to the call stack.
        return recursive_binary_search(numbers, target, middle + 1, right)
    else:
        # Recursive call. A new "frame" is added to the call stack.
        return recursive_binary_search(numbers, target, left, middle - 1)

# Let's trace the call stack for a list of 8 items (n=8).
# You want to find an element.
#
# 1. recursive_binary_search(..., left=0, right=7) -> calls...
# 2.   recursive_binary_search(..., left=4, right=7) -> calls...
# 3.     recursive_binary_search(..., left=4, right=5) -> calls...
# 4.       recursive_binary_search(..., left=5, right=5) -> returns
#
# At its deepest point, there are 4 function calls on the stack.
# Notice that for n=8, log₂(8) = 3. The stack depth is proportional to log(n).
#
# If n was 1,000,000, the stack depth would only be about 20 (log₂(1,000,000) ≈ 19.9).
# The space needed on the call stack grows very slowly.
# Therefore, the auxiliary space complexity is O(log n).
"""
Summary Table

Complexity	        Meaning	                                                            Key Phrase	              Prime Example
O(1)	            The extra space is fixed and does not change with input size.	    "Constant Space"	      Summing a list, swapping elements in-place.
O(n)	            The extra space grows in direct proportion to the input size.	    "Linear Space"	          Creating a copy of a list.
O(log n)	        The extra space grows very slowly as the input size grows.	        "Logarithmic Space"	      The call stack in a typical recursive binary search.

"""


"""
Key Takeaways

1. There is No "Best" Data Structure, Only Trade-offs.
This is the single most important lesson. No data structure is perfect for every situation. An array is fantastic for quick access by index but terrible for insertions in the middle. A linked list is the opposite. A hash table gives you lightning-fast lookups but sacrifices order. The job of an engineer is to choose the structure with the right trade-offs for the problem at hand.

2. Structure Dictates Performance.
The way data is organized directly determines how fast you can perform operations on it. Searching for a name in an unsorted list of a million people is slow. Searching for that same name in a hash table is instantaneous. The choice of data structure is not a minor detail—it is often the primary factor that determines whether a program is fast and scalable or slow and unusable.

3. Big O Notation is the Language of Efficiency.
We need a standardized way to talk about "fast" and "slow." Big O notation is that language. It's not about timing an algorithm with a stopwatch; it's about understanding how its performance scales as the input data grows. Students should leave knowing the difference between O(1) (excellent), O(log n) (great), O(n) (fair), and O(n^2) (bad), and why it matters so much for large datasets.

4. Problem Solving Starts with Identifying the Core Operations.
Before writing a single line of code, you must analyze the problem. 
Ask yourself: 
- What will I be doing most often with this data?
- Will I be searching for specific items frequently? (Consider a hash table or binary search tree).
- Will I be adding and removing items from the ends constantly? (Consider a linked list or deque).
- Will I need to access items by a stable position number? (Consider an array/list). Identifying the primary operations (access, search, insert, delete) is the first step to choosing the right data structure.

5. Data Structures and Algorithms are Two Sides of the Same Coin.
A data structure is just an organized pile of data until an algorithm comes along to operate on it. 
Conversely, an algorithm's efficiency is fundamentally limited by the data structure it uses. 
Binary Search is a brilliant algorithm, but it only works on a sorted array. 
Dijkstra's algorithm needs a graph to find the shortest path. You cannot think about one without considering the other.

"""

"""
Part 4: Introductory Exercises - Choose Your Tool
Now it's your turn to think like a programmer. For each scenario below, choose the best data structure from our toolbox (Array/List, Linked List, Hash Table/Dictionary). 
The most important part is to explain WHY you chose it, based on the operations required.

Exercise 1: Your Phone's Contacts
Scenario: You are designing the contacts app on a smartphone. The most common action is looking up a person's phone number by their name.
Question: Which data structure would you use to store the contacts? Why?

Exercise 2: A Web Browser's "Undo Closed Tab" Feature
Scenario: You are implementing the "Undo Closed Tab" feature. When a user closes a tab, you need to remember it so you can reopen it. The feature should always reopen the most recently closed tab first.
Question: Which data structure would be a good fit for this? What are its strengths for this specific problem? (This is a "Last-In, First-Out" or LIFO problem).

Exercise 3: The Line at a Movie Theater
Scenario: You are writing software to manage the line for a popular movie. The rule is simple: the first person to get in line is the first person to get a ticket.
Question: This "First-In, First-Out" (FIFO) behavior is a classic pattern. Which data structure would you model this line with?

"""