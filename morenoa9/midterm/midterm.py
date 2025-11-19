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
        self.history.append(url) #adding url to history,appeninding it as it'a the first url or new url
        print(f"Visited: {url}")
    
    def go_back(self):
        """
        Go back to the previous page (remove most recent).
        Return the URL that was removed.
        If no history, return "No pages to go back to"
        """
        if not self.history:
            return "No pages to go back to"
        return self.history.pop() #here I'm returning the previous url(if its exists)
        #by popping it. popping it because it will return it and not go back to it afterwrds
    
    def current_page(self):
        """
        Return the current page (most recent) without removing it.
        If no history, return "No pages in history"
        """
        if not self.history:
            return "No pages in history"
        return self.history[-1] #again, if the there aren't any preious urls, it'll return the message. 
        #If not, i'm returning the last url (calling it back)
    
    def show_history(self):
        """
        Print all pages in history, numbered from oldest to newest.
        If empty, print "No history"
        """
        if not self.history:
            print("No history")
            return
        for i, page in enumerate(self.history, start= 1):
            print(f"{i}. {page}")  #again, no history will give no results, otherwise its would return the pages
            #index and the url that has been visited. I used enumerate just so it could look better.


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


# 3. Recursive Functions (15 points)
# Instructions: Complete the recursive function that calculates the sum of all digits in a positive integer, and answer attached questions.
def sumDigits(n):
    """
    Recursively calculates the sum of all digits in a positive integer.
    """
    # Base case: if n is a single digit, return it
    if n < 10:
        return n
    
    # Recursive case: add last digit to sum of remaining digits
    return (n % 10) + sumDigits(n // 10) 
""" here I got the mod for the last digit to be added with the sumDigits, which would return the results """


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
"""The recursive function repeats by calling itself and using the call stack, while an iterative function repeats using loops without additional stack calls. """
# Can every recursive function be written iteratively? Can every iterative function be written recursively?
# Give one advantage and one disadvantage of using recursion.
"""
One advantage of using recursion is simplifying the code and understanding it
where someone who doesn't code code understand. A disadvantage would be the amount of memory
it would use. """