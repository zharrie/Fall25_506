# 1: Understanding Linear Search
"""
Objective: Implement and test a basic linear search.
Instructions:
You are given this starter code:
"""
def linear_search(my_list, target):
    # TODO: Write a loop to go through each item in my_list
    # If you find the target, return its index
    # If you finish the loop without finding it, return -1
    pass

# Test your function
numbers = [10, 23, 45, 70, 11, 15]
print(linear_search(numbers, 70))   # Should print: 3
print(linear_search(numbers, 100))  # Should print: -1
"""
Complete the function
Test it with the provided test cases
Add one more test case of your own
Deliverable: Completed function with all test cases showing output.
"""


# 2: Binary Search with Sorted Data
"""
Objective: Use binary search on a sorted list.
Instructions:
Given a sorted list: [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
Use Python's bisect module (already implements binary search):
"""
import bisect

sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]

# Find the position where 23 would be inserted
position = bisect.bisect_left(sorted_numbers, 23)

# TODO: Check if the number at that position equals 23
# Print "Found at index: __" or "Not found"
"""
Search for: 23, 50, and 2
For each search, print whether it was found and at what index
Deliverable: Simple script testing binary search with three values.
"""

# 3: Selection Sort Step-by-Step
"""
Objective: Complete a partially written selection sort.
Instructions:
Here's selection sort with blanks - fill them in:
"""
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Find the minimum element in the remaining unsorted portion
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update min_index
        
        # TODO: Swap arr[i] with arr[min_index]
        # Write the swap code here
        
        print(f"After pass {i+1}: {arr}")  # Show progress
    
    return arr

# Test
numbers = [64, 25, 12, 22, 11]
result = selection_sort(numbers)
print(f"Final sorted: {result}")
"""
Fill in the swap code
Run it and observe the output after each pass
Deliverable: Completed function with output showing each pass.
"""

# 4: Using Built-in Sort vs Manual Sort
"""
Objective: Compare sorting approaches and understand when to use each.

Instructions:

Create a list of 10 random numbers between 1-100
Make two copies of this list
Sort one copy using Python's built-in sort() method
Sort the other copy using the selection_sort function from Exercise 3
Print both results and verify they match
Answer in comments: "When would you write your own sort vs using built-in sort?"
Deliverable: Script showing both sorting methods with comparison.
"""

# 5: Basic List Operations Practice
"""
Objective: Practice fundamental list operations.

Instructions:
Start with an empty list called my_courses
Perform these operations and print the list after each:
Add "Data Structures" to the list
Add "Algorithms" to the list
Add "Database Systems" to the list
Insert "Python Programming" at position 0
Remove "Algorithms"
Print the length of the list
Print the item at index 1
Handle each operation on a separate line with a print statement showing the result
Deliverable: Script showing each operation and the list state after each.
"""

# 6: List of Dictionaries - Student Records
"""
Objective: Work with lists containing dictionaries.
Instructions:
Create a list with 3 student dictionaries:
"""

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]
"""
Write code to:
Add a new student (your choice of name/score)
Print all student names
Find and print the student with the highest score
Calculate and print the average score
Deliverable: Script performing all four tasks with clear output labels.
"""

# 7: Simple Stack Using a List
"""
Objective: Implement basic stack operations.
Instructions:
Complete this Stack class:
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        # TODO: Add item to the end of self.items
        pass
    
    def pop(self):
        # TODO: Remove and return the last item
        # (Check if stack is empty first!)
        pass
    
    def is_empty(self):
        # TODO: Return True if items list is empty
        pass
    
    def peek(self):
        # TODO: Return the last item without removing it
        pass

# Test your stack
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())  # Should print 3
print(s.peek()) # Should print 2
"""
Fill in all TODO sections
Run the test code
Deliverable: Completed Stack class with test output.
"""

# 8: Reversing a String with a Stack
"""
Objective: Apply stack to solve a simple problem.
Instructions:
Use your Stack class from Exercise 7
Write a function that reverses a string using a stack:
"""

def reverse_string(text):
    s = Stack()
    
    # TODO: Push each character from text onto the stack
    
    # TODO: Pop each character and build the reversed string
    
    return reversed_text

# Test
print(reverse_string("HELLO"))  # Should print: OLLEH
print(reverse_string("Python")) # Should print: nohtyP
"""
Complete the function
Explain in a comment: "Why does using a stack reverse the string?"
Deliverable: Working reverse function with explanation.
"""

# 9: Simple Queue Using a List
"""
Objective: Implement basic queue operations.
Instructions:
Complete this Queue class:
"""

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        # TODO: Add item to the end of the list
        pass
    
    def dequeue(self):
        # TODO: Remove and return the FIRST item (index 0)
        # Check if queue is empty first!
        pass
    
    def is_empty(self):
        # TODO: Return True if empty
        pass
    
    def size(self):
        # TODO: Return the number of items
        pass

# Test
q = Queue()
q.enqueue("First")
q.enqueue("Second")
q.enqueue("Third")
print(q.dequeue())  # Should print: First
print(q.size())     # Should print: 2
"""
Fill in all methods
Test to show FIFO (First In, First Out) behavior
Deliverable: Completed Queue class with test output.
"""


# 10: Customer Service Queue
"""
Objective: Simulate a simple queue scenario.
Instructions:
Use your Queue class from Exercise 9
Simulate a customer service line:
"""

# Create a queue
service_queue = Queue()

# TODO: Add 5 customers to the queue (use names or numbers)

# TODO: Serve (dequeue) 2 customers, printing who is being served

# TODO: Print how many customers are still waiting

# TODO: Add 1 more customer to the queue

# TODO: Serve all remaining customers one by one
"""
Make the output clear with print statements like "Serving customer: ___"
Deliverable: Simulation with clear output showing queue behavior.
"""

# 11: Dictionary Basics (Hash Table)
"""
Objective: Practice using Python dictionaries as hash tables.
Instructions:
Create an empty dictionary called phone_book
Add these entries:
"Alice": "555-1234"
"Bob": "555-5678"
"Charlie": "555-9012"
Print Alice's phone number
Update Bob's number to "555-0000"
Check if "David" is in the phone book (print True/False)
Add "David": "555-1111"
Print all names in the phone book
Print the total number of entries
Deliverable: Script performing all operations with clear output.
"""


# 12: Counting with a Dictionary
"""
Objective: Use a dictionary to count occurrences.
Instructions:
Given this list of fruits:
"""

fruits = ["apple", "banana", "apple", "orange", "banana", "apple", "grape", "banana"]
"""
Write code to count how many times each fruit appears:
"""

fruit_count = {}

for fruit in fruits:
    # TODO: If fruit is already in fruit_count, add 1 to its count
    # If fruit is not in fruit_count, set its count to 1
    pass

print(fruit_count)
"""
After counting, print which fruit appears most often
Deliverable: Completed counting code with output.
"""