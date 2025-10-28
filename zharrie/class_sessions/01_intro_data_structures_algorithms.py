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
In this analogy, the pile, the stack, and the filing cabinet are all data structures. Each has its own method of organization, and each has strengths and weaknesses depending on the task. The operations we want to perform are key:

Accessing: Reading the data at a specific location.
Searching: Looking for a specific piece of data.
Inserting: Adding new data to the structure.
Deleting: Removing data from the structure.
Choosing the right "filing cabinet" for your data is critical for writing fast and scalable software.

Part 2: The Basic Toolbox - Common Data Structures

Let's explore our "toolbox" of fundamental data structures with simple Python examples.

1. Record (or Struct/Object)
Concept: A collection of related data items, where each item (a "field") has a name and a value.
Analogy: A single contact card in your phone with fields for "First Name," "Last Name," and "Phone Number."

Python Example: The simplest way to create a record in Python is by using a dictionary.

"""

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

Python Example: Python's built-in list is a powerful and easy-to-use dynamic array.

"""

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

Strengths: Very fast access to elements by index.
Weaknesses: Slow to insert or delete elements in the middle.

3. Linked List
Concept: An ordered collection of items (nodes) where each node contains data and a pointer to the next node. They are not stored side-by-side in memory.
Analogy: A scavenger hunt. Each clue (a node) contains information and tells you the location of the next clue.

Python Example: To understand the concept, we'll build a short linked list manually.

"""

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
Strengths: Fast for inserting or deleting items at the beginning or end.
Weaknesses: Slow to access an element in the middle (must traverse from the head).

4. Hash Table (or Dictionary)
Concept: A structure for storing key-value pairs. It uses a special function (a hash function) to convert the key into an array index, allowing for extremely fast lookups.

Analogy: A magical filing cabinet. You give it a key (the file's title), and it instantly tells you which drawer to open.

Python Example: Python's dict is a highly optimized hash table.

"""

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
Strengths: Extremely fast for lookups, insertions, and deletions by key.
Weaknesses: Unordered. The items are not stored in any particular sequence.

Part 3: How Do We Calculate Efficiency? (Big O and Space Complexity)
When we say an algorithm is "fast" or "slow," we use Big O Notation to be precise. 
It describes how the resources (time or memory) required by an algorithm grow as the input size, N, increases.

Calculating Runtime Complexity (Big O Notation)
Let's find the Big O of a function by counting its steps relative to the input size N.

The Rules of Thumb:
Single Operations are O(1): Any single, simple step like variable assignment, arithmetic (+, -), or accessing an array index (my_list[i]) is considered constant time, or O(1).
Loops are O(n): A loop that runs N times (where N is the size of the input) contributes O(n).
Nested Loops are O(n^2): A loop inside another loop that both run N times results in N*N operations, so O(n^2).
Keep the Biggest Term: In a sum like O(n^2 + n), the n^2 term grows much faster and will dominate as n gets large. We simplify the whole expression to just O(n^2).
Drop Constants: We care about the rate of growth, not the exact number of operations. An algorithm that takes 2n steps and one that takes n steps both grow linearly, so we simplify them both to O(n).
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
Keep the Biggest Term: In n + 2, the n term is the biggest. So we have O(n).
(Rule 5, dropping constants, is also implicitly used here).
Final Answer: The runtime complexity of find_max_value is O(n). This means the time it takes to run is directly proportional to the number of items in the list.
Calculating Space Complexity
Space complexity measures how much additional memory an algorithm needs to run, as a function of the input size N. We usually ignore the space taken by the input itself and focus on the extra space.

Example 1: Constant Space O(1)

Let's look at our find_max_value function again.

The input numbers_list takes up N space.
Inside the function, we create one extra variable: max_val. This variable takes up a fixed, constant amount of space. It doesn't matter if the input list has 10 items or 10 million items; we still only need this one extra variable.
Final Answer: The auxiliary space complexity (extra space used) is O(1).

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