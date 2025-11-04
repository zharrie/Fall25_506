'''
Step 3: Implement the Searcher class's binary_search() method
Implement the Searcher class's static binary_search() method in the Searcher.py file. 
The function should perform a binary search on the sorted list (first parameter) for the key (second parameter). 
binary_search() returns the key's index if found, -1 if not found. Compare a list element to the key using the compare() method of the comparer object passed as binary_search()'s last argument.

Some test cases exist in main.py to test binary_search() with both string searches and integer searches. 
Some lists are sorted in ascending order, others in descending order. The proper Comparer object is passed to each binary_search() call. 
Clicking the Run button will display test case results, each starting with "PASS" or "FAIL". 
Ensure that all tests are passing before submitting code.

Each test in main.py only checks that binary_search() returns the correct result, 
but does not check the number of comparisons performed. The unit tests that grade submitted code check both binary_search()'s return value and the number of comparisons performed. 
The last unit test also uses lists with element types other than integers and strings.
        
'''
class Searcher:
    # Returns the index of the key in the sorted array, or -1 if the key is not
    # found.
    @staticmethod
    def binary_search(sorted_list, key, comparer):
        # TODO: Type your code here
        low = 0
        high = len(sorted_list) - 1

        while low <= high:
            mid = (low + high) // 2
            result = comparer.compare(sorted_list[mid], key)

            if result == 0:
                return mid
            elif result > 0:
                high = mid - 1
            else:
                low = mid + 1

        return -1
        #pass

