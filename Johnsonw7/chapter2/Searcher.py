class Searcher:
    # Returns the index of the key in the sorted array, or -1 if the key is not
    # found.
    @staticmethod
    def binary_search(sorted_list, key, comparer):
        low = 0
        high = len(sorted_list) - 1

        while low <= high:
            mid = (low + high) // 2
            cmp = comparer.compare(sorted_list[mid], key)

            if cmp == 0:
                return mid
            elif cmp > 0:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        pass