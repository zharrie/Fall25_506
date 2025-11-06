class NaturalMergeSorter:
    def get_sorted_run_length(self, lst, start_index):
        # Establishing a path for if start_index is out of bounds
        if start_index < 0 or start_index >= len(lst):
            return 0
        length = 1
        i = start_index + 1
        while i < len(lst) and lst[i] >= lst[i-1]:
            length += 1
            i += 1
        return length
    
    def natural_merge_sort(self, lst):
        n = len(lst)
        if n <= 1:
            return

        i = 0
        while True:
            #First iteration starting at i
            first_len = self.get_sorted_run_length(lst, i)

            # If everything is good here, we're all set
            if first_len == n:
                return

            # If the first check reaches the end, wrap back to the start
            first_end = i + first_len
            if first_end == n:
                i = 0
                continue

            # Start second check immediately after
            second_start = first_end
            second_len = self.get_sorted_run_length(lst, second_start)
            second_end = second_start + second_len

            # Merge the first and second checks
            self.merge(lst, i, second_start - 1, second_end - 1)

            i = second_end
            if i >= n:
                i = 0
            

    
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
