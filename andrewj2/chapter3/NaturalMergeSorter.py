class NaturalMergeSorter:
    def get_sorted_run_length(self, lst, i):
        if i >= len(lst): return 0
        n = 1
        i += 1
        while i < len(lst) and lst[i-1] <= lst[i]:
            n += 1
            i += 1
        return n
    
    def natural_merge_sort(self, lst):
        i = 0
        while True:
            l = self.get_sorted_run_length(lst, i)
            if l == len(lst): break
            if i+l == len(lst):
                i = 0
                continue
            r = self.get_sorted_run_length(lst, i+l)
            self.merge(lst, i, i-1+l, i-1+l+r)
            i = i+l+r
            if i >= len(lst): i = 0

    def merge(self, numbers, left_first, left_last, right_last):
        merged_size = right_last - left_first + 1
        merged_numbers = [0] * merged_size
        merge_pos = 0
        left_pos = left_first
        right_pos = left_last + 1
        
        # Add smallest element from left or right partition to merged numbers
        while left_pos <= left_last and right_pos <= right_last:
            if numbers[left_pos] <= numbers[right_pos]:
                merged_numbers[merge_pos] = numbers[left_pos]
                left_pos += 1
            else:
                merged_numbers[merge_pos] = numbers[right_pos]
                right_pos += 1
            merge_pos += 1
        
        # If left partition isn't empty, add remaining elements to
        # merged_numbers
        while left_pos <= left_last:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
            merge_pos += 1
        
        # If right partition isn't empty, add remaining elements to
        # merged_numbers
        while right_pos <= right_last:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
            merge_pos += 1
        
        # Copy merged numbers back to numbers
        for merge_pos in range(merged_size):
            numbers[left_first + merge_pos] = merged_numbers[merge_pos]
