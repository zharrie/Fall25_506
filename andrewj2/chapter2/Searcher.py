class Searcher:
    @staticmethod
    def binary_search(list, key, comparer):
        """
        Performs a binary search for a given key on a list of values, with a given comparator.

        Parameters
        ----------
        list : list of T
            A sorted list of values of type T.
        key : T
            The value to search for.
        comparer : Comparer
            A Comparer that compares values of type T.
        
        Returns
        -------
        int
            The index of the key value if it exists, or -1 if it does not.
        """
        return Searcher.__binary_search(list, 0, len(list)-1, key, comparer)
    
    @staticmethod
    def __binary_search(list, lo, hi, key, comparer):
        """
        Recursive method for the binary search.

        Parameters
        ----------
        list : list of T
            A sorted list of values of type T.
        lo : int
            The lower index of the current search partition.
        hi : int
            The upper index of the current search partition.
        key : T
            The value to search for.
        comparer : Comparer
            A Comparer that compares values of type T.
        
        Returns
        -------
        int
            The index of the key value if it exists, or -1 if it does not.
        """
        if lo > hi: return -1
        mid = (lo + hi) // 2
        comp = comparer.compare(list[mid], key)
        if comp == 0: return mid
        elif comp > 0: hi = mid-1
        elif comp < 0: lo = mid+1
        return Searcher.__binary_search(list, lo, hi, key, comparer)