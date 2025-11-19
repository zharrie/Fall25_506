"""
# A few sample exercises to review for your midterm.
# 1- Write a Python program to create a queue and display all the members and size
of the queue. (Import the queue library,
# do not create the class)
"""
from queue import Queue
# Create a Queue
my_queue = Queue()
# Add elements to the Queue
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)
my_queue.put(4)
# Store the initial size of the Queue
queue_size = my_queue.qsize()
# Display all members of the Queue
print("Members of the Queue:")
while not my_queue.empty():
print(my_queue.queue[0]) # Display the front element of the queue
my_queue.get() # Remove the front element from the queue
# Check the size of the Queue
print("Size of the Queue:", queue_size)
# 2- Write a function to reverse a string using a stack.
def reverse_string(input_string):
stack = []
# Push each character onto the stack
for char in input_string:
stack.append(char)
reversed_string = ''
# Pop characters from the stack to construct the reversed string
while len(stack) != 0:
reversed_string += stack.pop()
return reversed_string
# Example usage:
input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print("Original string:", input_str)
print("Reversed string:", reversed_str)
# 3- Create a hash table to count the frequency of words in a given text.
def count_word_frequency(text):
words = text.split()
word_freq = {}
for word in words:
# Removing punctuation and converting to lowercase for uniformity
word = word.strip('.,?!;:"').lower()
# Counting the frequency of each word
if word in word_freq:
word_freq[word] += 1
else:
word_freq[word] = 1
return word_freq
# Example text
input_text = "In Python, dictionaries are examples of hash maps. Hash tables are
cool!"
# Count word frequency in the text
word_frequency = count_word_frequency(input_text)
# Display the word frequency
print("Word Frequency:")
for word, freq in word_frequency.items():
print(f"'{word}': {freq}")
# 4- Implement a function to perform a binary search on a sorted list and return
the index of the target element, or -1 if not found.
def binary_search(arr, target):
low = 0
high = len(arr) - 1
while low <= high:
mid = (low + high) // 2
if arr[mid] == target:
return mid
elif arr[mid] < target:
low = mid + 1
else:
high = mid - 1
return -1
# Test case
sorted_list = [2, 5, 7, 12, 18, 23, 35, 42]
target_element = 18
result = binary_search(sorted_list, target_element)
print(f"Index of {target_element}: {result}")
