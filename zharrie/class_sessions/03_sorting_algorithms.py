# Sorting Algorithms
"""
Sorting isn't just academic—it's about understanding:

How to analyze algorithmic trade-offs
When "good enough" beats "optimal"
How data characteristics change everything
Let's dive in.
"""
#PART 1: The Foundation - Understanding O(N²)
# Selection Sort: The Obvious Approach
# Mental Model: Scan entire list, grab the smallest, place it first. Repeat.

def selection_sort(numbers):
   for i in range(len(numbers)-1):
      
      # Find index of smallest remaining element
      index_smallest = i
      for j in range(i+1, len(numbers)):
         
         if numbers[j] < numbers[index_smallest]:
            index_smallest = j
      
      # Swap numbers[i] and numbers[index_smallest]
      temp = numbers[i]
      numbers[i] = numbers[index_smallest]
      numbers[index_smallest] = temp

# Demo
# Create a list of numbers to sort
numbers = [10, 2, 78, 4, 45, 32, 7, 11]

# Display the contents of the list
print('UNSORTED:', numbers)

# Call the selection_sort() function
selection_sort(numbers)

# Display the (sorted) contents of the list
print('SORTED:', numbers)

#UNSORTED: [10, 2, 78, 4, 45, 32, 7, 11]
#SORTED: [2, 4, 7, 10, 11, 32, 45, 78]

"""
Complexity: O(N²)
Use when: Educational purposes, arrays < 50 elements
"""

#Insertion Sort: The Card Player's Approach
#Mental Model: Like sorting cards in your hand—take next card, insert where it belongs.
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        j = i

        # Insert numbers[i] into sorted part 
        # stopping once numbers[i] in correct position
        while j > 0 and numbers[j] < numbers[j - 1]:
            # Swap numbers[j] and numbers[j - 1]
            temp = numbers[j]
            numbers[j] = numbers[j - 1]
            numbers[j - 1] = temp
            j -= 1
    
# Create a list of unsorted values    
numbers = [10, 2, 78, 4, 45, 32, 7, 11]

# Print unsorted list
print('UNSORTED:', numbers)

# Call the insertion_sort function
insertion_sort(numbers)

# Print sorted list
print('SORTED:', numbers)
#UNSORTED: [10, 2, 78, 4, 45, 32, 7, 11]
#SORTED: [2, 4, 7, 10, 11, 32, 45, 78]

#The Secret Weapon: Performance on nearly-sorted data!
import time
import random

# Test on different data types
def benchmark(sort_func, data):
    start = time.time()
    sort_func(data.copy())
    return time.time() - start

size = 5000
random_data = [random.randint(1, 10000) for _ in range(size)]
sorted_data = list(range(size))

# Nearly sorted: sorted with 50 swaps
nearly_sorted = list(range(size))
for _ in range(50):
    i, j = random.randint(0, size-1), random.randint(0, size-1)
    nearly_sorted[i], nearly_sorted[j] = nearly_sorted[j], nearly_sorted[i]

print("Performance Comparison:")
print(f"Random data:        {benchmark(insertion_sort, random_data):.4f}s")
print(f"Already sorted:     {benchmark(insertion_sort, sorted_data):.4f}s")  # Nearly instant!
print(f"Nearly sorted:      {benchmark(insertion_sort, nearly_sorted):.4f}s")  # Very fast!

"""
Why? On sorted data, inner while-loop checks once and exits → O(N) instead of O(N²)

Use when:
Small datasets (< 50 elements)
Nearly sorted data
As part of hybrid algorithms (Timsort uses this!)
"""

#PART 2: Achieving O(N log N) - The Fast Algorithms
"""
Quicksort: Divide and Conquer
Big Idea: Partition array around a pivot, recursively sort each side.

The Partitioning Process:
Array: [10, 7, 8, 9, 1, 5]  Pivot: 8 (middle value)
Goal: [≤8 stuff] [≥8 stuff]

Use two pointers:
[10, 7, 8, 9, 1, 5]
 ↑low          ↑high

10 > 8, 5 < 8 → Swap them
[5, 7, 8, 9, 1, 10]
    ↑      ↑

Continue until pointers cross
Result: [5, 7, 1] [8, 9, 10]

Recursively sort each partition!
"""
# The partition() function used by quicksort.
def partition(numbers, start_index, end_index):
    # Select the middle value as the pivot.
    midpoint = start_index + (end_index - start_index) // 2
    pivot = numbers[midpoint]
   
    # "low" and "high" start at the ends of the list segment
    # and move towards each other.
    low = start_index
    high = end_index
   
    done = False
    while not done:
        # Increment low while numbers[low] < pivot
        while numbers[low] < pivot:
            low = low + 1
      
        # Decrement high while pivot < numbers[high]
        while pivot < numbers[high]:
            high = high - 1
      
        # If low and high have crossed each other, the loop
        # is done. If not, the elements are swapped, low is
        # incremented and high is decremented.
        if low >= high:
            done = True
        else:
            temp = numbers[low]
            numbers[low] = numbers[high]
            numbers[high] = temp
            low = low + 1
            high = high - 1
   
    # "high" is the last index in the left segment.
    return high

# The quicksort() algorithm
def quicksort(numbers, start_index, end_index):
    # Only attempt to sort the list segment if there are
    # at least 2 elements
    if end_index <= start_index:
        return
          
    # Partition the list segment
    high = partition(numbers, start_index, end_index)

    # Recursively sort the left segment
    quicksort(numbers, start_index, high)

    # Recursively sort the right segment
    quicksort(numbers, high + 1, end_index)

# Main program to test the quicksort algorithm.
numbers = [12, 18, 3, 7, 32, 14, 91, 16, 8, 57]
print('UNSORTED:', numbers)

quicksort(numbers, 0, len(numbers)-1)
print('SORTED:', numbers)

#UNSORTED: [12, 18, 3, 7, 32, 14, 91, 16, 8, 57]
#SORTED: [3, 7, 8, 12, 14, 16, 18, 32, 57, 91]

"""
Complexity:
Average:O(NlogN) - logN partition levels
Worst: O(N²) - when pivot always picks min/max (sorted data!)
Space: O(logN) - recursion stack
Use when: General-purpose sorting, memory constrained, average case matters most
"""

# Merge Sort: Guaranteed Performance
# Big Idea: Divide until trivial (size 1), then merge sorted halves.
"""

Visual:

[38, 27, 43, 3, 9, 82, 10]
        ↓ SPLIT
[38, 27, 43, 3] [9, 82, 10]
        ↓              ↓
[38, 27] [43, 3]   [9, 82] [10]
    ↓       ↓          ↓      ↓
[38][27] [43][3]   [9][82]  [10]
    ↓       ↓          ↓      ↓
[27, 38] [3, 43]   [9, 82]  [10]  ← MERGE
        ↓              ↓
[3, 27, 38, 43]  [9, 10, 82]
        ↓
[3, 9, 10, 27, 38, 43, 82]
"""

def merge(numbers, left_first, left_last, right_last):

    merged_size = right_last - left_first + 1
    merged_nums = [0] * merged_size
    merge_pos = 0
    left_pos = left_first
    right_pos = left_last + 1
    
    # Add smallest element from left or right partition to merged numbers
    while left_pos <= left_last and right_pos <= right_last:
        if numbers[left_pos] <= numbers[right_pos]:
            merged_nums[merge_pos] = numbers[left_pos]
            left_pos += 1
      
        else:
            merged_nums[merge_pos] = numbers[right_pos]
            right_pos += 1
       
        merge_pos += 1
  
    # If left partition is not empty, add remaining elements to merged numbers
    while left_pos <= left_last:
        merged_nums[merge_pos] = numbers[left_pos]
        left_pos += 1
        merge_pos += 1
    
    # If right partition is not empty, add remaining elements to merged numbers
    while right_pos <= right_last:
        merged_nums[merge_pos] = numbers[right_pos]
        right_pos += 1
        merge_pos += 1
    
    # Copy merged_nums back to numbers
    for merge_pos in range(merged_size):
        numbers[left_first + merge_pos] = merged_nums[merge_pos]


def merge_sort(numbers, start_index, end_index):
    if start_index < end_index:
        # Find the midpoint in the partition
        mid = (start_index + end_index) // 2
        
        # Recursively sort left and right partitions
        merge_sort(numbers, start_index, mid)
        merge_sort(numbers, mid + 1, end_index)
        
        # Merge left and right partitions in sorted order
        merge(numbers, start_index, mid, end_index)


# Create a list of unsorted values
numbers = [61, 76, 19, 4, 94, 32, 27, 83, 58]

# Print unsorted list
print(f"UNSORTED: {numbers}")

# Call merge_sort() to sort the list
merge_sort(numbers, 0, len(numbers) - 1)

# Print sorted list
print(f"SORTED: {numbers}")

#UNSORTED: [61, 76, 19, 4, 94, 32, 27, 83, 58]
#SORTED: [4, 19, 27, 32, 58, 61, 76, 83, 94]

"""
Complexity:
Always: O(NlogN) - guaranteed!
Space: O(N) - needs temp arrays

Use when:
- Need guaranteed O(NlogN)
- External sorting (data on disk)
- Stability matters
"""

#Quicksort vs Merge Sort: The Battle
"""
Aspect	            Quicksort	        Merge Sort
Average Time	    O(NlogN)            O(NlogN)
Worst Time          O(N²)               O(NlogN) ✓
Space	            O(logN) ✓	        O(N)
In-place?	        Yes ✓	            No
Practical speed	    Often faster ✓	    More predictable ✓

Pro tip: Real implementations use hybrid approaches—Python's Timsort combines merge sort + insertion sort!
"""

# PART 3: Algorithm Comparison & When to Use What
# The Performance Showdown
import random
import time

def benchmark_all(size):
    """Compare all algorithms"""
    data = [random.randint(1, 10000) for _ in range(size)]
    
    algorithms = {
        'Insertion': lambda d: insertion_sort(d),
        'Selection': lambda d: selection_sort(d),
        'Quicksort': lambda d: quicksort(d, 0, len(d)-1),
        'Merge Sort': lambda d: merge_sort(d, 0, len(d)-1),
        'Python Built-in': lambda d: sorted(d)
    }
    
    print(f"\n{'='*60}")
    print(f"Benchmarking {size} elements (random data)")
    print(f"{'='*60}")
    
    for name, algo in algorithms.items():
        if name == 'Selection' and size > 2000:
            print(f"{name:<20}: SKIPPED (too slow)")
            continue
            
        test_data = data.copy()
        start = time.time()
        algo(test_data)
        elapsed = time.time() - start
        print(f"{name:<20}: {elapsed:.6f}s")

# Run benchmarks
for size in [100, 1000, 5000]:
    benchmark_all(size)

# Decision Tree
def choose_algorithm(n, data_type, constraints):
    """Smart algorithm selection"""
    
    if n < 50:
        return "Insertion Sort (simple, fast for small N)"
    
    if data_type == "nearly_sorted":
        return "Insertion Sort (O(N) on nearly sorted!)"
    
    if constraints.get("guaranteed_time"):
        return "Merge Sort (always O(N log N))"
    
    if constraints.get("limited_memory"):
        return "Quicksort (O(log N) space)"
    
    return "Python's sort() - Timsort (optimized hybrid)"

# Examples
print(choose_algorithm(30, "random", {}))
print(choose_algorithm(10000, "nearly_sorted", {}))
print(choose_algorithm(1000000, "random", {"limited_memory": True}))
print(choose_algorithm(1000000, "random", {"guaranteed_time": True}))


#PART 4: Python's Built-in Sorting Powers
#Basic Sorting

# sorted() - returns new list
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = sorted(numbers)
print(f"Original: {numbers}")  # Unchanged
print(f"Sorted: {result}")

# .sort() - in-place
numbers.sort()
print(f"Modified: {numbers}")

# Descending
print(f"Descending: {sorted(numbers, reverse=True)}")

# Custom Sorting with Key Functions

# Case-insensitive string sorting
words = ["banana", "Apple", "cherry", "Banana"]
print(sorted(words))                    # ['Apple', 'Banana', 'banana', 'cherry']
print(sorted(words, key=str.lower))     # ['Apple', 'banana', 'Banana', 'cherry']

# Sorting by length
print(sorted(words, key=len))           # ['Apple', 'Banana', 'banana', 'cherry']

# Complex objects
students = [
    {"name": "Alice", "gpa": 3.8, "year": 3},
    {"name": "Bob", "gpa": 3.5, "year": 4},
    {"name": "Charlie", "gpa": 3.9, "year": 2}
]

# Sort by GPA (highest first)
by_gpa = sorted(students, key=lambda s: s['gpa'], reverse=True)
for s in by_gpa:
    print(f"{s['name']}: {s['gpa']}")

# Sort by year, then GPA within year
by_year_gpa = sorted(students, key=lambda s: (s['year'], -s['gpa']))

# Real-World Example: E-commerce Product Sorting
products = [
    {"name": "Laptop", "price": 1299, "rating": 4.5, "stock": 5},
    {"name": "Mouse", "price": 79, "rating": 4.8, "stock": 150},
    {"name": "Keyboard", "price": 129, "rating": 4.3, "stock": 0},
    {"name": "Monitor", "price": 499, "rating": 4.6, "stock": 23}
]

def smart_sort_key(product):
    """Sort by: in stock first, then rating, then price"""
    return (
        0 if product['stock'] > 0 else 1,  # In stock first
        -product['rating'],                 # Higher rating first
        product['price']                    # Lower price first
    )

sorted_products = sorted(products, key=smart_sort_key)

for p in sorted_products:
    status = "✓ In Stock" if p['stock'] > 0 else "✗ Out"
    print(f"{p['name']:<12} ${p['price']:>4} ★{p['rating']} {status}")


# PART 5: Real-World Applications & Pro Tips
# Case Study 1: When NOT to Sort


# Bad: Sorting to find max
numbers = list(range(100000))
random.shuffle(numbers)

# Slow way
import time
start = time.time()
max_val = sorted(numbers)[-1]
slow_time = time.time() - start

# Fast way
start = time.time()
max_val = max(numbers)
fast_time = time.time() - start

print(f"Sorting to find max: {slow_time:.6f}s")
print(f"Direct max():        {fast_time:.6f}s")
print(f"Speedup: {slow_time/fast_time:.1f}x")

# Case Study 2: Nearly Sorted Data

# Real scenario: Sorting timestamps that arrive mostly in order
def generate_nearly_sorted(n, disorder_percent=1):
    """Generate data that's mostly sorted"""
    data = list(range(n))
    swaps = int(n * disorder_percent / 100)
    for _ in range(swaps):
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        data[i], data[j] = data[j], data[i]
    return data

nearly_sorted = generate_nearly_sorted(10000, disorder_percent=1)

# Compare algorithms
print("Nearly Sorted Data (1% disorder):")
print(f"Insertion: {benchmark(insertion_sort, nearly_sorted):.6f}s")
print(f"Quicksort: {benchmark(lambda d: quicksort(d, 0, len(d)-1), nearly_sorted):.6f}s")
# Insertion sort wins on nearly sorted data!

# PART 6: Summary & Key Takeaways

# The Complete Picture
algorithm_guide = {
    "Simple (O(N²))": {
        "Selection Sort": "Educational only",
        "Insertion Sort": "Small/nearly-sorted data - actually useful!"
    },
    
    "Fast (O(N log N))": {
        "Quicksort": "General purpose, fast average case",
        "Merge Sort": "Guaranteed performance, external sorting"
    },
    
    "Specialized": {
        "Counting Sort": "Limited range integers - O(N)!",
        "Radix Sort": "Fixed-length data - O(N)!",
        "Heap Select": "Top K elements - O(N log K)"
    },
    
    "Production": {
        "Python's sort()": "USE THIS - it's Timsort, optimized hybrid"
    }
}
"""
Your Decision Framework

Step 1: Can you avoid sorting entirely? (max, min, top-k)
Step 2: Data size < 50? → Insertion sort
Step 3: Nearly sorted? → Insertion sort
Step 4: Otherwise → Python's sorted() / .sort()
Step 5: Only optimize if profiling shows sorting is bottleneck

Common Pitfalls

❌ Sorting inside loops
❌ Sorting when you only need max/min
❌ Using O(N²)algorithms on large data
❌ Ignoring data characteristics

✅ Use built-in sort unless you have specific reasons
✅ Consider nearly-sorted data patterns
✅ Use heapq for top-K problems
✅ Profile before optimizing
"""

# Class Exercise
# Given the array [5, 2, 8, 1, 9]:
# Manually trace the step-by-step execution of each sorting algorithm covered in class, clearly showing the intermediate steps on paper.

# HW
# 1.Implement each algorithm in Python based on your manual tracing.
# 2.Compare the algorithms by printing their performance metrics (e.g., number of comparisons or execution time).
# 3.Deep Dive: Read about Timsort - Python's hybrid approach

