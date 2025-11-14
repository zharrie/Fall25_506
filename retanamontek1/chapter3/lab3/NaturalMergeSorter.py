class NaturalMergeSorter:
    def get_sorted_run_length(self, lst, start_index):
        i = start_index
        j = start_index + 1

        if len(lst) > start_index and j >= 0:

            while j < len(lst) and lst[i] <= lst[j]:
                i += 1
                j += 1
            return j - start_index
        else:
            return 0
        pass
    
    def natural_merge_sort(self, lst):
        i = 0
        while True:
            run1_length = self.get_sorted_run_length(lst, i)

            if run1_length == len(lst):
                break

            run2 = run1_length + i
            run2_length = self.get_sorted_run_length(lst, run2)

            left_last = run2 - 1
            right_last = run2 + run2_length -1

            self.merge(lst, i, left_last, right_last)

            i = right_last + 1

            if i >= len(lst):
                i=0


        pass
    
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