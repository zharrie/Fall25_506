# 1. Stack for Browser History (20 points)
# List as Stack ADT
# Instructions: Create a browser history manager using a stack. When you visit pages, they get added to history. The "back" button removes the most recent page.

class BrowserHistory:
    def __init__(self):
        self.history = []  # This is our stack
    
    def visit_page(self, url):
        """
        Visit a new page (add to history).
        Print which page was visited.
        """
        self.history.append(url)
        print(url)

    def go_back(self):
        """
        Go back to the previous page (remove most recent).
        Return the URL that was removed.
        If no history, return "No pages to go back to"
        """
        if len(self.history) == 0:
            return "No pages to go back to"
        return self.history.pop()
    
    def current_page(self):
        """
        Return the current page (most recent) without removing it.
        If no history, return "No pages in history"
        """
        if len(self.history) == 0:
            return "No pages in history"
        return self.history[len(self.history)-1]
    
    def show_history(self):
        """
        Print all pages in history, numbered from oldest to newest.
        If empty, print "No history"
        """
        if len(self.history) == 0:
            return "No history"
        for i in range(len(self.history)):
            print(self.history[i])

print("=== History ===\n")

# Test your code
browser = BrowserHistory()
browser.visit_page("google.com")
browser.visit_page("youtube.com")
browser.visit_page("github.com")
browser.visit_page("stackoverflow.com")

print("\n--- Current History ---")
browser.show_history()

print(f"\nCurrent page: {browser.current_page()}")

print("\n--- Going back ---")
removed = browser.go_back()
print(f"Went back from: {removed}")

print(f"\nCurrent page: {browser.current_page()}")

print("\n--- Current History ---")
browser.show_history()
"""
Expected Output:

Visited: google.com
Visited: youtube.com
Visited: github.com
Visited: stackoverflow.com

--- Current History ---
1. google.com
2. youtube.com
3. github.com
4. stackoverflow.com

Current page: stackoverflow.com

--- Going back ---
Went back from: stackoverflow.com

Current page: github.com

--- Current History ---
1. google.com
2. youtube.com
3. github.com
"""


# 2. Using Built-in Sort vs Manual Sort (10 points)
"""
Compare sorting approaches and understand when to use each.
Instructions:
- Create a list of 30 random numbers between 1-100
- Make two copies of this list
- Sort one copy using Python's built-in sort() method
- Sort the other copy using the selection_sort function provided below
- Print both results and verify they match
- Answer in comments: "When would you write your own sort vs using built-in sort?"
"""
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

print("\n=== Sorting ===")

lst1 = list(range(30))
import random as r
r.shuffle(lst1)
lst2 = list(lst1)

print("\n--- Before Sort ---")
print('list 1', lst1)
print('list 2', lst2)

lst1.sort()
selection_sort(lst2)

print("\n--- After Sort ---")
print('list 1', lst1)
print('list 2', lst2)

'''
ANSWER:
I would write my own sorting algorithm if the data was not completely random, and I knew something about what order it would be in before sorting.
'''


# 3. Recursive Functions (15 points)
# Instructions: Complete the recursive function that calculates the sum of all digits in a positive integer, and answer attached questions.
def sumDigits(n):
    """
    Recursively calculates the sum of all digits in a positive integer.
    
    Example: sumDigits(1234) returns 10 because 1 + 2 + 3 + 4 = 10
    """
    # Base case: if n is a single digit, return it
    if n < 10:
        return n
    
    # Recursive case: add last digit to sum of remaining digits
    return (n % 10) + sumDigits(n // 10)


print("\n=== Recursion ===")
# Test your function
print(sumDigits(1234))  # Should print: 10
print(sumDigits(99))    # Should print: 18
print(sumDigits(5))     # Should print: 5
"""
sumDigits(1234) = 4 + sumDigits(123)
                    = 4 + 3 + sumDigits(12)
                        = 4 + 3 + 2 + sumDigits(1)
                            = 4 + 3 + 2 + 1
                            = 10
Key Operations:
- n % 10 → gets the last digit (1234 % 10 = 4)
- n // 10 → removes the last digit (1234 // 10 = 123)
"""
# What is the main difference between a recursive function and an iterative function (one using loops)?
# Can every recursive function be written iteratively? Can every iterative function be written recursively?
# Give one advantage and one disadvantage of using recursion.