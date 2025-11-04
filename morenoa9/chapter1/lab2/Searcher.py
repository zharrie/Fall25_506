class Searcher:
    # Returns the index of the key in the sorted array, or -1 if the key is not
    # found.
    @staticmethod
    def binary_search(sorted_list, key, comparer):
        low=0
        high=len(sorted_list)-1

        while high>=low:
            mid=(high + low)//2
            result=comparer.compare(sorted_list[mid], key)

            if result<0:
                low=mid+1
            elif result>0:
                high=mid-1
            else:
                return mid

        return -1