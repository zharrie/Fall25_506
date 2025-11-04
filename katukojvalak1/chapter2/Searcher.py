class Searcher:
    @staticmethod
    def binary_search(sorted_list, key, comparer):
        low=0
        high= len(sorted_list)-1

        while low <= high:
            mid = (low+high)//2

            comparision = comparer.compare(sorted_list[mid],key)

            if comparision==0:
                return mid
            elif comparision > 0:
                high=mid-1
            else:
                low = mid+1


        return -1