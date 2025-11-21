class NaturalMergeSorter:
    def get_sorted_run_length(self, lst, start_index):
        if start_index < 0 or start_index >= len(lst):
            return 0


        run_length = 1

        for i in range (start_index + 1,len(lst)):
            if lst[i] >= lst[i-1]:
                run_length += 1
            else:
                break

        return run_length
        pass
    

    def natural_merge_sort(self, lst):
        if len(lst) <= 1:
            return

        i = 0
        while True:
            # Step 1: Find first run
            run1_len = self.get_sorted_run_length(lst, i)
            if run1_len == len(lst):
                break  # entire list is sorted

            run1_end = i + run1_len - 1

            # If first run reaches the end, restart from beginning
            if run1_end >= len(lst) - 1:
                i = 0
                continue  # go back to start of loop

            # Step 2: Find second run
            run2_len = self.get_sorted_run_length(lst, run1_end + 1)
            run2_end = run1_end + run2_len

            # Step 3: Merge the two runs
            self.merge(lst, i, run1_end, run2_end - 1)

            # Step 4: Update i for next iteration
            if run2_end >= len(lst):
                i = 0
            else:
                i = run2_end
    
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
