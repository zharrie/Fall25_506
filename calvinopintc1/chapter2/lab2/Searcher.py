class Searcher:
    # Returns the index of the key in the sorted array, or -1 if the key is not
    # found.
    @staticmethod
    def binary_search(sorted_list, key, comparer):
        # TODO: Type your code here
        max = len(sorted_list) - 1
        min = 0
        while min <= max: 
            mid = (min + max) // 2
            comp = comparer.compare(sorted_list[mid], key)
            if comp == 0:
                return mid
            elif comp == 1:
                max = mid - 1
            else:
                min = mid + 1
        return -1

