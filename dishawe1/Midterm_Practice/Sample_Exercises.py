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
    for i in range(len(my_list)):
        #ED Code starts here
        #check if current element matches the key
        if my_list[i] == target:
            return i #Found! Return the index
        else:
            return -1  # Not found
        #ED Code ends here


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
#ED Code starts here
if position < len(sorted_numbers) and sorted_numbers[position] == 23:
    # Print "Found at index: __" or "Not found"
    print("Found at index:", position)
else:
    print("Not found")  
# Repeat for 50 and 2
position = bisect.bisect_left(sorted_numbers, 50)
if position < len(sorted_numbers) and sorted_numbers[position] == 50:
    print("Found at index:", position)
else:
    print("Not found")

position = bisect.bisect_left(sorted_numbers, 2)
if position < len(sorted_numbers) and sorted_numbers[position] == 2:
    print("Found at index:", position)
else:
    print("Not found")

    #ED Code ends here

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
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
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
#ED Code starts here
# Create a list of 10 random numbers between 1-100
random_list = [98, 34, 76, 12, 54, 23, 89, 45, 67, 10]
print(sorted(random_list)) #returns a copy of the list which is sorted, so you can print it
print(selection_sort(random_list)) #returns the actual list, which is sorted
#ED Code ends here




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
#ED Code starts here
my_courses = []
my_courses.append("Data Structures")
print(my_courses)
my_courses.append("Algorithms")
print(my_courses)
my_courses.append("Database Systems")
print(my_courses)
my_courses.insert(0, "Python Programming")
my_courses.remove("Algorithms")
print(my_courses)
print(len(my_courses))
print(my_courses[1])
#ED Code ends here

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
#ED Code starts here
students.append({"name": "David", "score": 88})
highest_score = -1
highest_score_student = ""
num_students = len(students)
score_sum = 0
for student in students:
    print(student["name"])
    if student["score"] > highest_score:
        highest_score = student["score"]
        highest_score_student = student["name"]
    score_sum += student["score"]
print(f"Highest score: {highest_score_student} with score {highest_score}")
print(f"Average score: {score_sum / num_students}")
#ED Code ends here


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
        self.items.append(item)

    
    def pop(self):
        # TODO: Remove and return the last item
        # (Check if stack is empty first!)
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  
    
    def is_empty(self):
        # TODO: Return True if items list is empty
        return len(self.items) == 0
    
    def peek(self):
        # TODO: Return the last item without removing it
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

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
    for char in text:
        s.push(char)
     # TODO: Pop each character and build the reversed string
    reversed_text = ""
    while not s.is_empty():
        reversed_text += s.pop()   
    return reversed_text


# Test
print(reverse_string("HELLO"))  # Should print: OLLEH
print(reverse_string("Python")) # Should print: nohtyP
"""
Complete the function
Explain in a comment: "Why does using a stack reverse the string?"

#Last in, first out (LIFO) nature of stacks means that the last character pushed onto the stack will be the first one popped off, effectively reversing the order of characters.

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
        self.items.append(item)

    
    def dequeue(self):
        # TODO: Remove and return the FIRST item (index 0)
        # Check if queue is empty first!
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
    
    def is_empty(self):
        # TODO: Return True if empty
        return len(self.items) == 0
    
    def size(self):
        # TODO: Return the number of items
        return len(self.items)

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
service_queue.enqueue("Customer 1")
service_queue.enqueue("Customer 2") 
service_queue.enqueue("Customer 3")
service_queue.enqueue("Customer 4")
service_queue.enqueue("Customer 5")


# TODO: Serve (dequeue) 2 customers, printing who is being served
for _ in range(2):
    served_customer = service_queue.dequeue()
    print(f"Serving customer: {served_customer}")

# TODO: Print how many customers are still waiting
print(f"Customers still waiting: {service_queue.size()}")


# TODO: Add 1 more customer to the queue
service_queue.enqueue("Customer 6") 
print(f"Added Customer 6 to the queue.")

# TODO: Serve all remaining customers one by one
while not service_queue.is_empty():
    served_customer = service_queue.dequeue()
    print(f"Serving customer: {served_customer}")
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
#ED Code starts here
phone_book = {}
phone_book["Alice"] = "555-1234"
phone_book["Bob"] = "555-5678"
phone_book["Charlie"] = "555-9012"
print(phone_book["Alice"])
phone_book["Bob"] = "555-0000"
print("David" in phone_book)
phone_book["David"] = "555-1111"
for name in phone_book:
    print(name)
print(len(phone_book))
# ED Code ends here

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
#ED Code starts here
fruit_count = {}

for fruit in fruits:
    # TODO: If fruit is already in fruit_count, add 1 to its count
    # If fruit is not in fruit_count, set its count to 1
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1
print(fruit_count)
print(max(fruit_count, key=fruit_count.get))   
print(f"The fruit that appears most often is: {max(fruit_count, key=fruit_count.get)}")
#ED Code ends here
"""
After counting, print which fruit appears most often
Deliverable: Completed counting code with output.
"""