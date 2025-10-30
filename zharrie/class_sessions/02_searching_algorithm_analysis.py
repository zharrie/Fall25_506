# Part 1: The Foundation - What Are Algorithms? 
"""
Algorithm: A well-defined, step-by-step sequence of instructions for accomplishing a task or solving a problem.

The Smartphone Contact Search Analogy

Imagine you have 500 contacts on your phone and need to find "Maria Santos":

Approach 1 - The Sequential Method:

Start with "Aaron Anderson"
Check "Aaron Baker"
Check "Aaron Chen"
Continue one by one...
Finally reach "Maria Santos" (maybe after checking 300+ contacts!)
Approach 2 - The Smart Method:

Scroll to the middle (around letter "M")
See you're at "Matthew Lee"
Maria comes before Matthew
Jump to middle of A-M section
Repeat until found

Question: "Which approach would you actually use? Why? What assumptions are you making?"

Key Insight: The second approach ONLY works because contacts are sorted alphabetically. This is our first lesson in algorithm design: the structure of your data affects which algorithms you can use.
"""


#Part 2: Linear Search - The Straightforward Approach
"""
Linear search is like reading a book page by page to find a specific sentence. You start at page 1 and check each page until you find it or reach the end.
Advantages:
✅ Simple to understand and implement
✅ Works on unsorted data
✅ Works on any data structure you can iterate through

Disadvantages:
❌ Slow for large datasets
❌ Wastes time checking irrelevant elements

Visual Step-by-Step Example
Let's search for the number 32 in this array:

Array: [2, 4, 7, 10, 11, 32, 45, 87]
Index:  0  1  2   3   4   5   6   7

Searching for: 32
Step-by-step execution:

Iteration 1:
  i = 0
  numbers[0] = 2
  Is 2 == 32? No → Continue
  
Iteration 2:
  i = 1
  numbers[1] = 4
  Is 4 == 32? No → Continue
  
Iteration 3:
  i = 2
  numbers[2] = 7
  Is 7 == 32? No → Continue
  
Iteration 4:
  i = 3
  numbers[3] = 10
  Is 10 == 32? No → Continue
  
Iteration 5:
  i = 4
  numbers[4] = 11
  Is 11 == 32? No → Continue
  
Iteration 6:
  i = 5
  numbers[5] = 32
  Is 32 == 32? YES! → Return index 5
  
Total comparisons: 6
"""

# Implementation
def linear_search(numbers, key):
    """
    Searches for 'key' in the 'numbers' array using linear search.
    
    How it works:
    - Examines each element from left to right
    - Compares each element with the search key
    - Returns immediately when found
    - Returns -1 if key is not in the array
    
    Args:
        numbers (list): A list of comparable elements (can be unsorted)
        key: The value to search for
    
    Returns:
        int: The index of key if found, -1 otherwise
    
    Time Complexity: O(N) where N is the length of the array
    Space Complexity: O(1) - only uses a constant amount of extra space
    """
    # Loop through each index in the array
    for i in range(len(numbers)):
        # Check if current element matches the key
        if numbers[i] == key:
            return i  # Found! Return the index
    
    # If we've checked all elements and haven't returned, key is not in array
    return -1


# Interactive test program
numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print('Array to search:', numbers)
print('Array length:', len(numbers))
print()

key = int(input('Enter an integer value to search for: '))
key_index = linear_search(numbers, key)

if key_index == -1:
    print(f'{key} was not found in the array.')
    print(f'We checked all {len(numbers)} elements.')
else:
    print(f'Success! Found {key} at index {key_index}.')
    print(f'We had to check {key_index + 1} elements.')

"""    
Understanding Efficiency: Best, Worst, and Average Cases
Let's analyze different scenarios with our array [2, 4, 7, 10, 11, 32, 45, 87]:

Best Case - O(1)

Searching for: 2 (first element)
Comparisons: 1
Result: Found at index 0
This is the best possible scenario!

Worst Case - O(N)

Scenario 1 - Element at the end:
Searching for: 87 (last element)
Comparisons: 8 (all elements)
Result: Found at index 7

Scenario 2 - Element not in array:
Searching for: 100
Comparisons: 8 (all elements)
Result: Not found (return -1)

These are the worst possible scenarios!
Average Case - O(N)


If we search for random elements:
- Sometimes we find it early (lucky!)
- Sometimes we find it late (unlucky!)
- On average, we check about N/2 elements

But in Big O notation, we drop constants:
O(N/2) = O(N)
"""

#Class Exercise 1
"""
Given array: [15, 3, 9, 21, 7, 12, 30, 5, 18, 27]

How many comparisons to find 30 using linear search?
How many comparisons to find 15?
How many comparisons to find 100 (not in array)?
If this array had 1,000,000 elements, what's the maximum comparisons needed?
"""

# Part 3: Binary Search - The Clever Approach
"""
The Critical Requirement: Sorted Data
Important: Binary search ONLY works on sorted arrays!
Why? Because the algorithm makes decisions based on comparisons:

If middle element < key → key MUST be in the right half
If middle element > key → key MUST be in the left half
This logic only works if the array is sorted!

The Divide and Conquer Strategy
Binary search uses a "divide and conquer" approach:
- Divide: Look at the middle element
- Conquer: Determine which half contains the target
- Repeat: Search only that half
Each step eliminates half of the remaining elements!

Detailed Visual Walkthrough
Let's search for 11 in a sorted array:

Initial array: [2, 4, 7, 10, 11, 32, 45, 87]
Indices:        0  1  2   3   4   5   6   7

Searching for: 11
Iteration 1:

Current search range: [2, 4, 7, 10, 11, 32, 45, 87]
                       ↑                          ↑
                      low=0                    high=7

Calculate middle: mid = (0 + 7) // 2 = 3

Check numbers[3] = 10

Compare: Is 10 == 11? No
         Is 10 < 11? Yes → Search RIGHT half

Update: low = mid + 1 = 4

New search range: [11, 32, 45, 87]
                   ↑            ↑
                 low=4       high=7
Iteration 2:


Current search range: [11, 32, 45, 87]
                       ↑            ↑
                     low=4       high=7

Calculate middle: mid = (4 + 7) // 2 = 5

Check numbers[5] = 32

Compare: Is 32 == 11? No
         Is 32 > 11? Yes → Search LEFT half

Update: high = mid - 1 = 4

New search range: [11]
                   ↑
                low=4
                high=4
Iteration 3:


Current search range: [11]
                       ↑
                    low=4
                    high=4

Calculate middle: mid = (4 + 4) // 2 = 4

Check numbers[4] = 11

Compare: Is 11 == 11? YES! ✓

Return: 4
Total comparisons: 3 (compared to 5 for linear search)
"""
"""
Understanding Floor Division (//)

Why do we use // instead of /?
Array indices must be integers!
"""
# Problem with regular division:
mid = (7 + 0) / 2
mid = 3.5  # ❌ Can't use 3.5 as an array index!

# Solution with floor division:
mid = (7 + 0) // 2
mid = 3  # ✓ Integer index!

# More examples:
7 // 2 = 3   #(not 3.5)
8 // 2 = 4   #(not 4.0, though it's the same)
9 // 2 = 4   #(not 4.5)
# Floor division always rounds down to the nearest integer.

# Implementation
def binary_search(numbers, key):
    """
    Searches for 'key' in the SORTED 'numbers' array using binary search.
    
    How it works:
    - Maintains a search range with 'low' and 'high' pointers
    - Repeatedly checks the middle element
    - Eliminates half of the remaining elements each iteration
    - Continues until element is found or range is empty
    
    Args:
        numbers (list): A SORTED list of comparable elements
        key: The value to search for
    
    Returns:
        int: The index of key if found, -1 otherwise
    
    Time Complexity: O(log N) where N is the length of the array
    Space Complexity: O(1) - only uses a constant amount of extra space
    """
    # Initialize search range to entire array
    low = 0                    # Start of search range
    high = len(numbers) - 1    # End of search range
    
    # Continue searching while range is not empty
    # (When low > high, the range is empty)
    while high >= low:
        # Calculate middle index of current range
        # Using floor division to ensure integer result
        mid = (high + low) // 2
        
        # Compare middle element with key and decide next step
        if numbers[mid] < key:
            # Key is in the right half
            # Move low pointer to exclude left half and middle
            low = mid + 1
            
        elif numbers[mid] > key:
            # Key is in the left half
            # Move high pointer to exclude right half and middle
            high = mid - 1
            
        else:
            # numbers[mid] == key
            # Found the key! Return its index
            return mid
    
    # Loop ended without finding key
    # This means low > high (empty range)
    return -1


# Interactive test program
numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print('Sorted array:', numbers)
print('Array length:', len(numbers))
print('Note: Binary search requires the array to be sorted!')
print()

key = int(input('Enter an integer value to search for: '))
key_index = binary_search(numbers, key)

if key_index == -1:
    print(f'{key} was not found in the array.')
else:
    print(f'Success! Found {key} at index {key_index}.')

"""    
Efficiency Analysis: Why Binary Search is Amazing

Best Case - O(1):
Searching for: 10 (happens to be middle element)
Comparisons: 1

Worst Case - O(log N):
For an array of size N, maximum comparisons = ⌈log₂ N⌉ + 1

Examples:

Array size 8:
Maximum comparisons = log₂(8) + 1 = 3 + 1 = 4

Why? Because we can halve the array at most 3 times:
8 → 4 → 2 → 1

Array size 16:
Maximum comparisons = log₂(16) + 1 = 4 + 1 = 5
16 → 8 → 4 → 2 → 1

Array size 1024:
Maximum comparisons = log₂(1024) + 1 = 10 + 1 = 11
1024 → 512 → 256 → 128 → 64 → 32 → 16 → 8 → 4 → 2 → 1

The Power of Logarithmic Growth:
Array Size	        Linear Search (worst)	    Binary Search (worst)	    Improvement
8	                8	                        4	                        2x faster
16	                16	                        5	                        3x faster
100	                100	                        7	                        14x faster
1,000	            1,000	                    10	                        100x faster
10,000	            10,000	                    14	                        714x faster
1,000,000	        1,000,000	                20	                        50,000x faster!
1,000,000,000	    1,000,000,000	            30	                        33 million times faster!

Think about this: With 1 billion elements, binary search needs at most 30 comparisons!
"""
#Class Exercise 2
"""
Given sorted array: [3, 7, 12, 19, 23, 28, 35, 41, 50, 67, 72, 88, 91, 95, 99] (15 elements)

Manually trace binary search for 50. Show each iteration.
How many comparisons are needed?
What's the maximum comparisons for this 15-element array?
If we had 128 elements, what's the maximum comparisons?
"""


#Part 4: Comparing Algorithms - The Scientific Approach
# Let's modify both algorithms to count comparisons so we can see the difference in real-time:

def linear_search(numbers, key):
    """Linear search with comparison counting"""
    comparisons = 0  # Counter for comparisons
    
    for i in range(len(numbers)):
        comparisons += 1  # Increment before each comparison
        if numbers[i] == key:
            return i, comparisons
    
    return -1, comparisons


def binary_search(numbers, key):
    """Binary search with comparison counting"""
    comparisons = 0  # Counter for comparisons
    low = 0
    high = len(numbers) - 1
    
    while high >= low:
        mid = (high + low) // 2
        comparisons += 1  # Increment before each comparison
        
        if numbers[mid] < key:
            low = mid + 1
        elif numbers[mid] > key:
            high = mid - 1
        else:
            return mid, comparisons
    
    return -1, comparisons


# Comprehensive test program
numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print('=' * 60)
print('ALGORITHM COMPARISON DEMO')
print('=' * 60)
print(f'Array: {numbers}')
print(f'Size: {len(numbers)} elements')
print('=' * 60)

key = int(input('\nEnter an integer key to search for: '))
print()

# Test linear search
print('--- LINEAR SEARCH ---')
key_index, comparisons = linear_search(numbers, key)
if key_index == -1:
    print(f'Result: {key} was NOT found')
    print(f'Comparisons made: {comparisons}')
    print(f'(Checked all {len(numbers)} elements)')
else:
    print(f'Result: Found {key} at index {key_index}')
    print(f'Comparisons made: {comparisons}')
    print(f'(Had to check {comparisons} element(s))')

print()

# Test binary search
print('--- BINARY SEARCH ---')
key_index, comparisons = binary_search(numbers, key)
if key_index == -1:
    print(f'Result: {key} was NOT found')
    print(f'Comparisons made: {comparisons}')
else:
    print(f'Result: Found {key} at index {key_index}')
    print(f'Comparisons made: {comparisons}')

print()
print('=' * 60)
"""
Sample Output Analysis

Example 1: Searching for 32
Array: [2, 4, 7, 10, 11, 32, 45, 87]

--- LINEAR SEARCH ---
Result: Found 32 at index 5
Comparisons made: 6

--- BINARY SEARCH ---
Result: Found 32 at index 5
Comparisons made: 2

Analysis: Binary search used 50% fewer comparisons!

Example 2: Searching for 2
Array: [2, 4, 7, 10, 11, 32, 45, 87]

--- LINEAR SEARCH ---
Result: Found 2 at index 0
Comparisons made: 1

--- BINARY SEARCH ---
Result: Found 2 at index 0
Comparisons made: 3

Analysis: Linear search was faster this time!
(But this is the best case for linear search - very rare)

Example 3: Searching for 100 (not in array)
Array: [2, 4, 7, 10, 11, 32, 45, 87]

--- LINEAR SEARCH ---
Result: 100 was NOT found
Comparisons made: 8

--- BINARY SEARCH ---
Result: 100 was NOT found
Comparisons made: 4

Analysis: Binary search used 50% fewer comparisons even when element doesn't exist!

When to Use Which Algorithm?
Use Linear Search when:
✓ Data is unsorted (binary search won't work!)
✓ Dataset is very small (< 10-20 elements)
✓ You need to search only once (sorting overhead not worth it)
✓ Elements are constantly being added/removed (keeping sorted is expensive)

Use Binary Search when:
✓ Data is already sorted or can be sorted
✓ Dataset is large (hundreds, thousands, or more elements)
✓ You need to perform multiple searches (sorting overhead amortized)
✓ Data is relatively static (not changing frequently)

Real-world analogy:
Linear search: Looking for a specific card in a shuffled deck
Binary search: Looking up a word in a dictionary
"""

#Part 5: Big O Notation - The Language of Algorithm Analysis
"""
Why Do We Need Big O Notation?
✓ Independent of hardware
✓ Independent of programming language
✓ Focused on scalability (how it grows with input size)

Understanding Constant Time Operations
Before we analyze algorithms, we need to understand what counts as a "single operation."
A constant time operation = an operation that always takes the same amount of time, regardless of input size
"""
# Examples of O(1) operations:
# 1. Arithmetic operations
x = 5 + 3
y = a * b
z = n // 2
remainder = n % 2

# 2. Comparisons
if x < y:
    pass

# 3. Array access by index
value = arr[5]
arr[10] = 42

# 4. Variable assignments
temp = x
x = y
y = temp

# 5. Return statements
# return x

# 6. Basic function calls (non-recursive, no loops inside)
print(x)
abs(-5)

# NOT constant time:
# Operations that depend on input size

# Loops - O(N)
for i in range(n):
    print(i)

# String operations on large strings
long_string.upper()  # O(length of string)

# List operations
my_list.append(x)  # Usually O(1), but occasionally O(N)
my_list.insert(0, x)  # O(N) - has to shift all elements!

# Recursive calls
factorial(n)  # Depends on n

"""
Big O Notation: The Formal Definition
Big O notation describes the upper bound of an algorithm's growth rate.
More simply: How does runtime grow as input size (N) increases?

The Rules for Determining Big O
"""
# Rule 1: Keep only the highest-order term

# Example 1:
def example1(arr):
    n = len(arr)
    # This loop: N operations
    for i in range(n):
        print(arr[i])
    
    # This single operation: 1 operation
    print("Done")

# Total: N + 1 operations
# Big O: O(N + 1) → O(N)
# We drop the +1 because N dominates as N grows large

# Example 2:
def example2(arr):
    n = len(arr)
    # Nested loops: N × N = N² operations
    for i in range(n):
        for j in range(n):
            print(arr[i], arr[j])
    
    # Single loop: N operations
    for i in range(n):
        print(arr[i])
    
    # Single operation: 1 operation
    print("Done")

# Total: N² + N + 1 operations
# Big O: O(N² + N + 1) → O(N²)
# We keep only N² because it grows fastest
# Why? Let's see with actual numbers:
"""

N	    N²	        N	    1	    Total	    N² percentage
10	    100	        10	    1	    111	        90%
100	    10,000	    100	    1	    10,101	    99%
1,000	1,000,000	1,000	1	    1,001,001	99.9%
As N grows, N² dominates completely!
"""

# Rule 2: Drop constant coefficients
# Example 3:
def example3(arr):
    # First loop: N operations
    for i in range(len(arr)):
        print(arr[i])
    
    # Second loop: N operations
    for i in range(len(arr)):
        print(arr[i])
    
    # Third loop: N operations
    for i in range(len(arr)):
        print(arr[i])

# Total: 3N operations
# Big O: O(3N) → O(N)
# We drop the coefficient 3

"""
Why?    Constants don't affect growth rate:

N	    3N	    5N	    100N
10	    30	    50	    1,000
100	    300	    500	    10,000
1,000	3,000	5,000	100,000
All grow linearly! The coefficient doesn't change the pattern.
"""

# Step-by-Step Big O Analysis Examples

#Example 1: Simple Loop
def print_array(arr):
    for i in range(len(arr)):  # Line 1
        print(arr[i])          # Line 2

# Analysis:
# Line 1: Loop executes N times (where N = len(arr))
# Line 2: Each iteration does O(1) work (printing)
# 
# Total: N iterations × O(1) per iteration = O(N)

#Example 2: Two Sequential Loops
def print_twice(arr):
    # First loop
    for i in range(len(arr)):
        print(arr[i])
    
    # Second loop
    for i in range(len(arr)):
        print(arr[i] * 2)

# Analysis:
# First loop: O(N)
# Second loop: O(N)
# 
# Total: O(N) + O(N) = O(2N) = O(N)
# Sequential operations ADD

# Example 3: Nested Loops (Same Size)
def print_pairs(arr):
    for i in range(len(arr)):       # Outer loop: N times
        for j in range(len(arr)):   # Inner loop: N times
            print(arr[i], arr[j])   # O(1) work

# Analysis:
# Outer loop: N iterations
# Inner loop: N iterations (for EACH outer iteration)
# Work per iteration: O(1)
#
# Total: N × N × O(1) = O(N²)
# Nested loops MULTIPLY

# Example 4: Nested Loops (Dependent)
def print_triangular(arr):
    n = len(arr)
    for i in range(n):           # Outer: N times
        for j in range(i):       # Inner: 0, 1, 2, ..., N-1 times
            print(arr[i], arr[j])

# Analysis:
# Iteration 1: inner loop runs 0 times
# Iteration 2: inner loop runs 1 time
# Iteration 3: inner loop runs 2 times
# ...
# Iteration N: inner loop runs N-1 times
#
# Total: 0 + 1 + 2 + ... + (N-1) = N(N-1)/2 = (N² - N)/2
#
# Big O: O((N² - N)/2) = O(N²/2 - N/2) = O(N²)
# We drop constants and lower-order terms

# Example 5: Sequential Different Operations
def mixed_operations(arr):
    # Part 1: Single operation
    print("Start")                  # O(1)
    
    # Part 2: Linear loop
    for i in range(len(arr)):       # O(N)
        print(arr[i])
    
    # Part 3: Quadratic nested loops
    for i in range(len(arr)):       # O(N²)
        for j in range(len(arr)):
            print(arr[i] + arr[j])
    
    # Part 4: Another single operation
    print("End")                    # O(1)

# Analysis:
# Total: O(1) + O(N) + O(N²) + O(1)
#      = O(N²)
# We keep only the highest-order term
"""
The Growth Rate Hierarchy

From fastest to slowest (best to worst):
"""

# O(1) - Constant
def get_first(arr):
    return arr[0]  # Always 1 operation

# Examples: 1, 1, 1, 1, 1, 1, ...
# Doesn't grow at all!

# O(log N) - Logarithmic
def binary_search(arr, key):
    # Cuts search space in half each iteration
    # Already shown earlier
    pass

# Examples for N = 1024:
# Operations: ~10
# Growth: Very slow!

# O(N) - Linear
def linear_search(arr, key):
    # Checks each element once
    pass

# Examples: 10, 100, 1000, 10000
# Grows proportionally to input

# O(N log N) - Linearithmic
def merge_sort(arr):
    # Efficient sorting algorithm
    # We'll study this later
    pass

# Examples for N = 1000:
# Operations: ~10,000
# Growth: Moderate

# O(N²) - Quadratic
def bubble_sort(arr):
    # Nested loops over array
    pass

# Examples: 100, 10000, 1000000
# Growth: Fast! Bad for large N

# O(2^N) - Exponential
def fibonacci_recursive(n):
    # Makes two recursive calls each time
    pass

# Examples: 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
# Growth: Extremely fast! Usually impractical


# Class Exercise 3
# Determine the Big O complexity of each function:
# Problem 1
def mystery1(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Problem 2
def mystery2(arr):
    for i in range(len(arr)):
        for j in range(10):  # Note: Fixed number!
            print(arr[i] + j)

# Problem 3
def mystery3(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                print(i, j, k)

# Problem 4
def mystery4(n):
    i = 1
    while i < n:
        print(i)
        i = i * 2  # Note: Doubling!

# Problem 5
def mystery5(arr):
    if len(arr) == 0:
        return 0
    
    mid = len(arr) // 2
    return arr[mid]

# Part 6: Advanced Big O Analysis
"""
Composite Functions and Big O Rules
Sometimes we combine functions. Here are the rules:

Rule 1: Constant multiplied by function
c × O(f(N)) = O(f(N))

Examples:
5 × O(N) = O(N)
100 × O(N²) = O(N²)

Rule 2: Constant added to function
c + O(f(N)) = O(f(N))

Examples:
10 + O(N) = O(N)
1000 + O(log N) = O(log N)

Rule 3: Function multiplied by function
g(N) × O(f(N)) = O(g(N) × f(N))

Examples:
N × O(N) = O(N²)
log N × O(N) = O(N log N)
Rule 4: Function added to function


g(N) + O(f(N)) = O(g(N) + f(N))
                = O(max(g(N), f(N)))  # Keep larger term

Examples:
N + O(N²) = O(N²)
N² + O(N) = O(N²)
"""

# Example 1: Multiple Phases
def complex_algorithm(arr):
    n = len(arr)
    
    # Phase 1: Initialize
    max_val = arr[0]                    # O(1)
    
    # Phase 2: Find maximum
    for i in range(n):                  # O(N)
        if arr[i] > max_val:
            max_val = arr[i]
    
    # Phase 3: Nested search
    for i in range(n):                  # O(N²)
        for j in range(n):
            if arr[i] + arr[j] == max_val:
                print(i, j)
    
    # Phase 4: Final print
    print(max_val)                      # O(1)
    
# Total analysis:
# O(1) + O(N) + O(N²) + O(1)
# = O(N²)  (keep highest order term)

# Example 2: Conditional Branches
def conditional_algorithm(arr):
    n = len(arr)
    
    if n < 100:
        # Small array: use simple algorithm
        for i in range(n):              # O(N)
            print(arr[i])
    else:
        # Large array: use complex algorithm
        for i in range(n):              # O(N²)
            for j in range(n):
                print(arr[i] + arr[j])

# Analysis:
# We analyze the WORST CASE
# Worst case: n ≥ 100, so we execute the else block
# Big O: O(N²)

# Best Case, Worst Case, Average Case
# For any algorithm, we can analyze three scenarios:

# Example: Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
"""
Best Case: Key is at the first position

Operations: 1
Big O: Ω(1) (Big Omega notation for lower bound)
Worst Case: Key is at the last position or not in array

Operations: N
Big O: O(N) (Big O notation for upper bound)
Average Case: Key is randomly distributed

Operations: N/2 on average
Big O: Θ(N) (Big Theta notation - both upper and lower bound)
Most commonly, we focus on WORST CASE analysis because:

Guarantees performance in all scenarios
Average case requires assumptions about input distribution
Best case is often not representative
"""
# Class Exercise 4
# Analyze these more complex functions:

# Problem 1
def problem1(arr):
    n = len(arr)
    # Process first half
    for i in range(n // 2):
        print(arr[i])
    # Process second half
    for i in range(n // 2, n):
        print(arr[i])

# Problem 2
def problem2(arr):
    n = len(arr)
    i = 0
    while i < n:
        for j in range(i, n):
            print(arr[j])
        i += 1

# Problem 3
def problem3(arr1, arr2):
    for x in arr1:
        for y in arr2:
            print(x, y)

# Problem 4
def problem4(n):
    for i in range(n):
        j = 1
        while j < n:
            print(i, j)
            j = j * 2

"""
What is Recursion?

Recursion is a problem-solving technique where a function calls itself to solve smaller instances of the same problem.

Key Analogy: Russian nesting dolls (Matryoshka dolls)
Each doll contains a smaller version of itself
Eventually you reach the smallest doll (base case)
Then you can put them back together

The Two Essential Components
1. Base Case: A simple case that can be solved directly (stops the recursion) 
2. Recursive Case: Break the problem into smaller pieces and call the function again

Without a base case, recursion never stops → infinite recursion → stack overflow!

Example 1: Factorial
Mathematical Definition:
n! = n × (n-1) × (n-2) × ... × 2 × 1

Examples:
5! = 5 × 4 × 3 × 2 × 1 = 120
3! = 3 × 2 × 1 = 6
1! = 1

Recursive Insight:
5! = 5 × 4!
4! = 4 × 3!
3! = 3 × 2!
2! = 2 × 1!
1! = 1  ← Base case!

Pattern: n! = n × (n-1)!
"""
# Implementation:
def factorial(n):
    """
    Calculate factorial of n using recursion.
    
    Base case: factorial(1) = 1
    Recursive case: factorial(n) = n × factorial(n-1)
    """
    # Base case: simplest problem we can solve directly
    if n == 1:
        print(f"  Base case: factorial(1) = 1")
        return 1
    
    # Recursive case: solve smaller problem
    else:
        print(f"  Computing: {n} × factorial({n-1})")
        result = n * factorial(n - 1)
        print(f"  Returning: {n} × factorial({n-1}) = {result}")
        return result

# Test it
print("Computing factorial(5):")
print("=" * 40)
answer = factorial(5)
print("=" * 40)
print(f"Final answer: {answer}")

"""
Output:
Computing factorial(5):
========================================
  Computing: 5 × factorial(4)
  Computing: 4 × factorial(3)
  Computing: 3 × factorial(2)
  Computing: 2 × factorial(1)
  Base case: factorial(1) = 1
  Returning: 2 × factorial(1) = 2
  Returning: 3 × factorial(2) = 6
  Returning: 4 × factorial(3) = 24
  Returning: 5 × factorial(4) = 120
========================================
Final answer: 120
Visual Call Stack:


factorial(5)
  ↓ calls factorial(4)
    ↓ calls factorial(3)
      ↓ calls factorial(2)
        ↓ calls factorial(1)
        ← returns 1
      ← returns 2 × 1 = 2
    ← returns 3 × 2 = 6
  ← returns 4 × 6 = 24
← returns 5 × 24 = 120
"""

# Example 2: Fibonacci Numbers
"""
The Sequence:

Position: 0  1  2  3  4  5  6  7  8   9   10
Value:    0  1  1  2  3  5  8  13 21  34  55

Rule: Each number = sum of previous two numbers
Recursive Definition:


F(0) = 0          ← Base case 1
F(1) = 1          ← Base case 2
F(n) = F(n-1) + F(n-2)   ← Recursive case
"""
#Implementation:
def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Base cases: F(0) = 0, F(1) = 1
    Recursive case: F(n) = F(n-1) + F(n-2)
    
    WARNING: This implementation is inefficient for large n!
    """
    # Base case 1
    if n == 0:
        return 0
    
    # Base case 2
    elif n == 1:
        return 1
    
    # Recursive case: needs TWO recursive calls
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test it
print("First 10 Fibonacci numbers:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

"""
Output:

First 10 Fibonacci numbers:
F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34
Visual: Computing F(5)


                    F(5)
                   /    \
                F(4)    F(3)
               /   \    /   \
            F(3)  F(2) F(2) F(1)
           /  \   /  \  /  \
        F(2) F(1) F(1) F(0) F(1) F(0)
        /  \
     F(1) F(0)

Notice: We compute F(2) THREE times! Very inefficient!
Time Complexity: O(2^N) - Exponential! (Very bad!)

For n=5, we make 15 function calls
For n=10, we make 177 function calls
For n=20, we make 21,891 function calls
For n=40, we make ~2 billion function calls!
"""

#Example 3: Recursive Binary Search
# We can also implement binary search recursively:
def binary_search_recursive(numbers, key, low, high):
    """
    Recursive implementation of binary search.
    
    Args:
        numbers: Sorted array
        key: Value to search for
        low: Start index of search range
        high: End index of search range
    
    Returns:
        Index of key if found, -1 otherwise
    """
    # Base case: empty range
    if low > high:
        print(f"  Range empty (low={low}, high={high}). Not found.")
        return -1
    
    # Calculate middle
    mid = (low + high) // 2
    print(f"  Checking range [{low}..{high}], mid={mid}, value={numbers[mid]}")
    
    # Check middle element
    if numbers[mid] < key:
        # Recursive case: search right half
        print(f"  {numbers[mid]} < {key}, search right half")
        return binary_search_recursive(numbers, key, mid + 1, high)
    
    elif numbers[mid] > key:
        # Recursive case: search left half
        print(f"  {numbers[mid]} > {key}, search left half")
        return binary_search_recursive(numbers, key, low, mid - 1)
    
    else:
        # Found it!
        print(f"  Found {key} at index {mid}!")
        return mid

# Test it
numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print(f"Array: {numbers}")
print("\nSearching for 11:")
print("=" * 50)
result = binary_search_recursive(numbers, 11, 0, len(numbers) - 1)
print("=" * 50)
print(f"Result: index {result}")

"""
Output:


Array: [2, 4, 7, 10, 11, 32, 45, 87]

Searching for 11:
==================================================
  Checking range [0..7], mid=3, value=10
  10 < 11, search right half
  Checking range [4..7], mid=5, value=32
  32 > 11, search left half
  Checking range [4..4], mid=4, value=11
  Found 11 at index 4!
==================================================
Result: index 4
Time Complexity: Still O(log N)!

Each recursive call processes half the remaining elements
Same efficiency as iterative version
Space Complexity: O(log N) instead of O(1)

Each recursive call uses stack space
Maximum depth = log N
Recursion vs Iteration
"""

# Recursive version:
def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative version:
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
"""
Comparison:
Aspect	            Recursion	                Iteration
Code clarity	    Often clearer	            Can be more verbose
Memory usage	    Uses stack (more)	        Uses less memory
Performance	        Slower (function calls)	    Faster
Natural fit	        Trees, divide-and-conquer	Sequential processing
Risk	            Stack overflow	            Infinite loop

When to use recursion:
✓ Problem naturally divides into smaller subproblems
✓ Working with tree/graph structures
✓ Divide-and-conquer algorithms
✓ Code clarity is important and stack depth is manageable

When to use iteration:
✓ Simple sequential processing
✓ Memory is constrained
✓ Maximum performance needed
✓ Deep recursion would cause stack overflow

"""

# Class Exercise 5

# Problem 1: Write a recursive function to calculate the sum of numbers from 1 to n.

# Problem 2: Trace the execution of this recursive function:

def mystery(n):
    if n <= 0:
        return 0
    return n + mystery(n - 2)

# What does mystery(7) return?
# Problem 3: What's wrong with this recursive function?
def broken(n):
    return n + broken(n - 1)

# Part 8: Analyzing Recursive Algorithms
# Recurrence Relations
# When we analyze recursive algorithms, the runtime function T(N) contains itself!
"""
Example: Binary Search


T(N) = O(1) + T(N/2)
       ↑      ↑
       |      └─ Recursive call on half the data
       └─ Constant time operations (comparison, calculate mid)
This is called a recurrence relation: a function defined in terms of itself with smaller input.

Method 1: Count the Recursive Calls
Binary Search:
How many times do we recurse?
N → N/2 → N/4 → N/8 → ... → 1

Examples:
16 → 8 → 4 → 2 → 1  (4 steps)
32 → 16 → 8 → 4 → 2 → 1  (5 steps)
64 → 32 → 16 → 8 → 4 → 2 → 1  (6 steps)

Pattern: log₂(N) steps
Each step does O(1) work
Total: O(log N)

Linear Factorial:
factorial(N) calls factorial(N-1) calls factorial(N-2) ... calls factorial(1)
N → N-1 → N-2 → ... → 1
Number of calls: N
Each call does O(1) work
Total: O(N)

Method 2: Recursion Trees
A recursion tree visualizes the recursive calls and work done at each level.
Example: Fibonacci (inefficient version)
                         fib(5) ................. Level 0: 1 call
                        /      \
                    fib(4)      fib(3) .......... Level 1: 2 calls
                   /    \       /    \
               fib(3) fib(2) fib(2) fib(1) ..... Level 2: 4 calls
              /   \   /   \   /   \
          fib(2) fib(1) fib(1) fib(0) fib(1) fib(0) ... Level 3: 8 calls (continuing)
          /   \
      fib(1) fib(0)

Pattern:
- Level 0: 1 call = 2^0
- Level 1: 2 calls = 2^1
- Level 2: 4 calls = 2^2
- Level 3: 8 calls = 2^3
- ...
- Level k: 2^k calls

Maximum depth: N (when we reach fib(0))
Total calls: 2^0 + 2^1 + 2^2 + ... + 2^N ≈ 2^N
Time Complexity: O(2^N) - Exponential!

Common Recurrence Patterns
Pattern 1: Single recursive call on half
T(N) = O(1) + T(N/2)
Example: Binary search
Solution: O(log N)

Pattern 2: Single recursive call on N-1
T(N) = O(1) + T(N-1)
Example: Factorial
Solution: O(N)

Pattern 3: Two recursive calls on half
T(N) = O(1) + 2T(N/2)
Example: (Coming later - tree traversal)
Solution: O(N)

Pattern 4: Two recursive calls on N-1
T(N) = O(1) + T(N-1) + T(N-2)
Example: Fibonacci (naive)
Solution: O(2^N)

Pattern 5: Recursive calls with linear work
T(N) = O(N) + 2T(N/2)
Example: Merge sort (coming later)
Solution: O(N log N)
"""

# Detailed Analysis: Recursive Binary Search
def binary_search_recursive(numbers, key, low, high):
    if low > high:            # O(1) - comparison
        return -1
    
    mid = (low + high) // 2   # O(1) - arithmetic
    
    if numbers[mid] < key:    # O(1) - comparison
        return binary_search_recursive(numbers, key, mid + 1, high)  # T(N/2)
    elif numbers[mid] > key:  # O(1) - comparison
        return binary_search_recursive(numbers, key, low, mid - 1)   # T(N/2)
    else:
        return mid            # O(1) - return
# Recurrence relation:
# T(N) = O(1) + T(N/2)

# Class Exercise 6

# Problem 1: Analyze the time complexity:
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

# Problem 2: Analyze the time complexity:
def print_binary(n):
    if n > 0:
        print_binary(n // 2)
        print(n % 2)


#Part 9: Comprehensive Summary & Decision Framework
"""
Algorithm Complexity Quick Reference

Algorithm	                Best Case	    Average Case	    Worst Case	    Space	                                When to Use
Linear Search	            O(1)	        O(N)	            O(N)	        O(1)	                                Small or unsorted data
Binary Search	            O(1)	        O(log N)	        O(log N)	    O(1) iterative, O(log N) recursive	    Large sorted data
Binary Search (Recursive)	O(1)	        O(log N)	        O(log N)	    O(log N)	                            Educational, naturally recursive problems

Big O Hierarchy (Remember This!)
FAST → O(1) → O(log N) → O(N) → O(N log N) → O(N²) → O(2^N) → SLOW

Decision Framework: Which Algorithm to Choose?

Question 1: Is your data sorted?
❌ No → Linear search (or sort first if multiple searches needed)
✅ Yes → Continue to Question 2

Question 2: How large is your dataset?
Small (< 100 elements) → Either works, linear search is simpler
Large (> 1000 elements) → Binary search for sure

Question 3: How many searches will you perform?
One search → Linear search might be fine
Many searches → Invest in sorting, use binary search

Question 4: Can you modify the data?
No modifications → Use binary search on sorted data
Frequent insertions/deletions → Consider other data structures (hash tables, balanced trees)
"""

# Common Big O Patterns in Code
# Pattern Recognition Guide:

# O(1) - Constant
def is_constant(arr):
    return arr[0] + arr[1]  # Fixed number of operations

# O(log N) - Logarithmic
def is_logarithmic(n):
    i = 1
    while i < n:
        i = i * 2  # Multiplying/dividing → logarithmic

# O(N) - Linear
def is_linear(arr):
    for item in arr:  # Single loop through data
        print(item)

# O(N log N) - Linearithmic
def is_linearithmic(arr):
    for i in arr:            # N times
        j = 1
        while j < len(arr):  # log N times
            j = j * 2

# O(N²) - Quadratic
def is_quadratic(arr):
    for i in arr:      # N times
        for j in arr:  # N times (nested)
            print(i, j)

# O(2^N) - Exponential
def is_exponential(n):
    if n <= 1:
        return 1
    return is_exponential(n-1) + is_exponential(n-1)  # Two branches each call


# Key Takeaways
"""
Algorithm choice matters more than hardware for large inputs
- Better algorithm on slow computer beats worse algorithm on fast computer
- For 1 million elements: O(log N) vs O(N) = 50,000x difference!

Big O focuses on scalability, not exact runtime
- Drop constants and lower-order terms
- O(N) and O(100N) are the same in Big O
- But O(N) and O(N²) are fundamentally different

Recursion is powerful but has tradeoffs
✓ Elegant and natural for many problems
✓ Essential for divide-and-conquer
❌ Uses more memory (stack)
❌ Can be inefficient if not designed carefully (like naive Fibonacci)

Analyze worst-case by default
- Provides guaranteed performance
- Best-case is often misleading
- Average-case requires assumptions about input

Space complexity matters too
- Iterative: usually O(1) extra space
- Recursive: O(depth) extra space on call stack
- For binary search: iterative uses O(1), recursive uses O(log N)
"""