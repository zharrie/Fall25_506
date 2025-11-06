class Searcher:
    # Returns the index of the key in the sorted array, or -1 if the key is not
    # found.
    @staticmethod
    def binary_search(sorted_list, key, comparer):
        # TODO: Type your code here
         # Initialize search range to entire array
        low = 0                    # Start of search range index
        high = len(sorted_list) - 1   # End of search range index
        # Continue searching while index range is not empty
        # (When low > high, the range is empty)
        while high >= low:
        # Calculate middle index of current range
        # Using floor division to ensure integer result
            mid = (high + low) // 2
            output = comparer.compare(sorted_list[mid], key)
        
            # Compare middle element with key and decide next step
            if output < 0:
                # Key is in the right half
                # Move low pointer to exclude left half and middle
                low = mid + 1
            #If output is higher than 0, it will check for the key in higher part of the sorted array    
            elif output > 0:
                # Key is in the left half
                # Move high pointer to exclude right half and middle
                high = mid - 1
                
            else:
                output == 0
                # Found the key! Return its index
                return mid
        return -1
        
