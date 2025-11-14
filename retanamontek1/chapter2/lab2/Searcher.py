class Searcher:
    # Returns the index of the key in the sorted array, or -1 if the key is not
    # found.
    @staticmethod
    def binary_search(sorted_list, key, comparer):
        low = 0
        high = len(sorted_list) - 1

        while low <= high:
            k = (low + high)//2
            check = comparer.compare(key, sorted_list[k])

            if check ==0:
                return k

            elif check == 1:
                low = k + 1

            elif check == -1:
                high = k -1

        return -1    
        pass