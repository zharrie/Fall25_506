# 1. Stack for Browser History (20 points)
# List as Stack ADT
# Instructions: Create a browser history manager using a stack. When you visit pages, they get added to history. The "back" button removes the most recent page.

class BrowserHistory:
    def __init__(self):
        self.history = []  # This is our stack

    def visit_page(self, url):

        # WJ - Add the new page to the history list
        self.history.append(url)
        # WJ - Confirm which page was visited
        print(f"Visited: {url}")


    def go_back(self):
        # WJ - Handling the case where there is no history
        if len(self.history) == 0:
            return "No pages to go back to"
        # WJ - Otherwise, pop and return the most recent url
        return self.history.pop()

    def current_page(self):
        """
        Return the current page (most recent) without removing it.
        If no history, return "No pages in history"
        """
        # WJ - Handling the case where the stack is empty (No current page)
        if len(self.history) == 0:
            return "No pages in history"
        # WJ - Otherwise, the current page is the element at the top of the stack (Last in the list)
        return self.history[-1]

    def show_history(self):
        """
        Print all pages in history, numbered from oldest to newest.
        If empty, print "No history"
        """
        # WJ - Handling the case where the stack is empty
        if len(self.history) == 0:
            print("No history")
            return
        # Otherwise, numbering through the pages and printing them in order with those numbers
        # Start numbering from 1 for user-friendly output
        for i, url in enumerate(self.history, start=1):
            print(f"{i}. {url}")
        pass



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

# Example lists of 30 random numbers (identical)
list1 = [34, 7, 23, 32, 5, 62, 32, 12, 78, 90, 11, 45, 67, 89, 21, 43, 54, 76, 88, 99,
         1, 3, 4, 6, 8, 10, 13, 14, 15, 16]
list2 = list1.copy()

# Ensuring they are the same
print(f"List1 Unsorted: {list1}")
print(f"List2 Unsorted: {list2}")

print(list1 == list2) # Should be True


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

selection_sort(list1)
list2.sort()

print(list1 == list2) # Should be True

print(f"List1 Sorted: {list1}")
print(f"List2 Sorted: {list2}")

"""
I would write my own sort function in educational contexts to understand sorting algorithms and their mechanics 
or to implement a project-specific functionality that might not be doable under the existing implementations.
"""

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


"""
WJ

The main difference between a recursive function and an iterative function is that a recursive function calls itself to solve smaller instances of the same problem, while an iterative function uses loops to repeat a block of code until a condition is met.

Yes, every recursive function can be written iteratively and vice versa.

One advantage is that code can be made shorter through recursion, making it easier to read and maintain
One disadvantage is that recursion can lead to higher memory usage

"""