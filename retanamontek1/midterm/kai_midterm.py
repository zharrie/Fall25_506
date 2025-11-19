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
        # add url to to the end of the history stack
        self.history.append(url)

    
    def go_back(self):
        """
        Go back to the previous page (remove most recent).
        Return the URL that was removed.
        If no history, return "No pages to go back to"
        """

        # If the length of history is 0, that means it's empty and should print the statement
        if len(self.history) == 0:
          print('No pages to go back to')

        # If not empty, then use pop() to remove the most recently appended url. Aka, the last item.
        #removed item is stored and then returned
        else:
          removed = self.history.pop()
          return removed
    
    def current_page(self):
        """
        Return the current page (most recent) without removing it.
        If no history, return "No pages in history"
        """
        # Same as in the previous function. If length is 0, then it's empty.
        if len(self.history) == 0:
          print('No pages in history')

        # If not empty, then return the last item in the stack/list
        else:
          return self.history[-1]
    
    def show_history(self):
        """
        Print all pages in history, numbered from oldest to newest.
        If empty, print "No history"
        """
        # Same as in the previous function. If length is 0, then it's empty.
        if len(self.history) == 0:
          print('No pages in history')

        # If not empty, then loop through everything in history and print it out
        else:
          for i in self.history:
            print(i)
        

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
#######################################

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
#creating random list + copy
# Created by importing random. Then having the range be 1-100 and the output amount is set to 30
import random
list1 = random.sample(range(1, 100), 30)
list2 = list1.copy()

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

# Using built in sort()
list1.sort()
list1

# Using selection_sort()
selection_sort(list2)
list2

'''
They both output the same. I'm not sure when it's best to use which. I know that the built in sort() method uses < less than. Selection sort might be faster.
'''

######################

# 3. Recursive Functions (15 points)
'''
Honestly for this one, it does the job, but it's iterates through the string with a for loop. Not recursive couldn't figure that out.

'''
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


    # n % 10 gives us the last number of the digit. n//10 gives us the remaining digits. Then it'll recursively do the rest because it's adding with sumDigit (aka, calling the function again).
    return (n % 10 + sumDigits(n // 10))


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
'''
Recursive functions call on themselves
'''

# Can every recursive function be written iteratively? Can every iterative function be written recursively?
'''
Yes for the first question and no for the second.
'''
# Give one advantage and one disadvantage of using recursion.
'''
Less code? I would have to write more lines to do it iteratively with a for loop
'''