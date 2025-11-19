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
        # my code with comments:
        self.history.append(url) #add the page to history list by appending
        print("Visited:", url) #this prints the page that was visite
    
    def go_back(self):
        """
        Go back to the previous page (remove most recent).
        Return the URL that was removed.
        If no history, return "No pages to go back to"
        """
        # my code with comments
        #first let's check if there is history
        if len(self.history) != 0:
            #if we have history, pop the first item of the list
            popped_page = self.history.pop() #.pop() will return the popped item so just need to save it
            return popped_page #return the removed URL
        else:
            no_pages = "No pages to go back to"
            return no_pages #return the no pages message
    
    def current_page(self):
        """
        Return the current page (most recent) without removing it.
        If no history, return "No pages in history"
        """
        # my code with comments
        #first let's check if there is history
        if len(self.history) != 0:
            #if we have history, peek at it
            peek_page = self.history[-1] #index -1 of the list will always show the last item in the list
            return peek_page #return the removed URL
        else:
            no_history = "No pages in history"
            return no_history #return the no history message
    
    def show_history(self):
        """
        Print all pages in history, numbered from oldest to newest.
        If empty, print "No history"
        """
        # my code with comments
        #first let's check if there is history
        if len(self.history) == 0:
            no_hist = "No history"
            return no_hist #return the no history message
        #if we do have history go through the following
        #since history list is a stack, the oldest item is at index 0
        for search in self.history:
            search_index = self.history.index(search) #I want the search index to number the list
            search_index = search_index + 1 #plus 1 so the number list starts at 1
            print(search_index, ":", search)


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

# my code with comments

#making a list of 30 random numbers between 1-100
my_list = [5, 10, 3, 44, 66, 12, 78, 99, 30, 22, 56, 98, 23, 54, 97, 74, 32, 18, 76, 25, 76, 88, 44, 90, 50, 26, 79, 82, 92, 30]

#making 2 copies
my_list_copy = my_list
my_list_copy_2 = my_list

#sort with built in .sort
my_list_copy.sort()

#sort with provided selection sort:
selection_sort(my_list_copy_2)

#print both results
print(my_list_copy)
print(my_list_copy_2)

#verify they match
print(my_list_copy == my_list_copy_2)

"""
Python built in sort is quite efficient for sorting most lists. Some special cases exist where perhaps you
may want to use a different approach to sort. For example, if a list were nearly sorted (and you were aware of this)
and insertion sort algorithm may be much more efficient as it has a runtime of O(n) in these cases. The only other
scenarios is which you may want to use a sorting function you wrote yourself is if you have a very specified use case
for how you want your items sorted, something beyond just descending order or even by strings etc. Otherwise, self
created sorting algorithms are mainly beneficial for educational and understanding purposes.
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

    #I was not able to come up with the recursive case in enough time but I was 
    #able to do it iteratively 
    
    n_string = str(n)
    sum = 0

    for char in n_string:
        int_n = int(char)
        sum = sum+ int_n

    return sum


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
"""
The main difference between recursive and iterative functions is that recursive functions call themselves, while iterative functions
simply repeat a set number of times or until a specified condition is met.
"""
# Can every recursive function be written iteratively? Can every iterative function be written recursively?
"""
It is possible to write recursive functions iteratively and vice versa. However, it would be simpler to call on the function itself again
then make it execute iteratively and, by the same token, for some functions it is easier to make them iterative than to make them call themselves
over again.
"""
# Give one advantage and one disadvantage of using recursion.
"""
One advantage of using recursion is you can have a briefer and more readable chunk of code or script. One disadvantage is that recursive
functions can have high runtime complexities, such as the fibonacci sequence example where the runtime complexity is exponential.
"""