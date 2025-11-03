from Comparer import Comparer
from DescendingComparer import DescendingComparer
from Searcher import Searcher

def print_searches(sorted_list, search_keys, comparer, expected_results,
    key_in_quotes):
    # If key_in_quotes is true, " characters surround the key in output
    # statements. Otherwise empty strings surround the key.
    extra = "\"" if key_in_quotes else ""
    
    # Iterate through list of search keys and search for each
    pass_count = 0
    for i in range(len(search_keys)):
        # Get the key to search for
        search_key = search_keys[i]
        
        # Peform the search
        index = Searcher.binary_search(sorted_list, search_key, comparer)
        
        # Compare actual result against expected
        expected = expected_results[i]
        if index == expected:
            print(f"PASS: Search for key {extra}{search_key}{extra}", end="")
            print(f" returned {expected}.")
            
            pass_count += 1
        else:
            print(f"FAIL: Search for key {extra}{search_key}{extra}", end="")
            print(f" should have returned {expected}, but returned ", end="")
            print(f"{index}.")
    
    print(f"{pass_count} of {len(search_keys)} tests passed")

# Main program code follows

# Perform sample searches with strings
sorted_fruits = [ "Apple", "Apricot", "Banana", "Blueberry", "Cherry", "Grape",
    "Grapefruit", "Guava", "Lemon", "Lime", "Orange", "Peach", "Pear",
    "Pineapple", "Raspberry", "Strawberry"
]
fruit_searches = [ "Nectarine", "Mango", "Guava", "Strawberry", "Kiwi",
    "Apple", "Raspberry", "Carrot", "Lemon", "Bread"
]
expected_fruit_search_results = [ -1, -1, 7, 15, -1, 0, 14, -1, 8, -1 ]
print_searches(sorted_fruits, fruit_searches, Comparer(),
    expected_fruit_search_results, True)

# Perform sample searches with strings sorted descending
fruits_descending = [ "Strawberry", "Raspberry", "Pineapple", "Pear", "Peach",
    "Orange", "Lime", "Lemon", "Guava", "Grapefruit", "Grape", "Cherry",
    "Blueberry", "Banana", "Apricot", "Apple"
]
fruit_searches = [ "Nectarine", "Mango", "Guava", "Strawberry", "Kiwi",
    "Apple", "Raspberry", "Carrot", "Lemon", "Bread"
]
expected_results_fruits_descending = [ -1, -1, 8, 0, -1, 15, 1, -1, 7, -1 ]
print_searches(fruits_descending, fruit_searches, DescendingComparer(),
    expected_results_fruits_descending, True)
    
# Perform sample searches with integers
integers = [11, 21, 27, 34, 42, 58, 66, 71, 72, 85, 88, 91, 98]
integer_searches = [42, 23, 11, 19, 87, 98, 54, 66, 92, 1, 14, 21, 66, 87, 83]
expected_integer_search_results = [
    4, -1, 0, -1, -1, 12, -1, 6, -1, -1, -1, 1, 6, -1, -1
]
print_searches(integers, integer_searches, Comparer(), \
    expected_integer_search_results, False)

# Perform sample searches with integers sorted descending
integers_descending = [87, 71, 64, 58, 54, 51, 23, 17, 16, 10]
integer_descending_searches = [66, 51, 71, 11, 12, 10, 87, 64]
expected_descending_search_results = [
    -1, 5, 1, -1, -1, 9, 0, 2
]
print_searches(integers_descending, integer_descending_searches, \
    DescendingComparer(), expected_descending_search_results, False)