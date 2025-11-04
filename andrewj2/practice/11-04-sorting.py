class Sorter:
    @staticmethod
    def selection_sort(list):
        for i in range(len(list)-1):
            min_idx = i
            for j in range(i+1, len(list)-1):
                if list[j] < list[min_idx]:
                    min_idx = j
            tmp = list[i]
            list[i] = list[min_idx]
            list[min_idx] = tmp
        return list

print(Sorter.selection_sort([5,2,8,1,9,1,2,7,8,3,3,7,8,3,4,5,7,4,3,8,9,9,0,0,9,3]))