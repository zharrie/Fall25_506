class Searcher:
    # Returns the index of the key in the sorted array, or -1 if the key is not
    # found.
    @staticmethod
    def binary_search(list, key, comparer):
        return Searcher.__binary_search(list, 0, len(list)-1, key, comparer)
    
    @staticmethod
    def __binary_search(list, lo, hi, key, comparer):
        if lo > hi: return -1
        mid = (lo + hi) // 2
        comp = comparer.compare(list[mid], key)
        if comp == 0: return mid
        elif comp > 0: hi = mid-1
        elif comp < 0: lo = mid+1
        return Searcher.__binary_search(list, lo, hi, key, comparer)