class NaturalMergeSorter:
    def get_sorted_run_length(self, lst, start_index):
        #starting at index 0, check if the next element is sorted, stop when it isn't
        if start_index > len(lst)-1:
            return 0
        else:
            length = 1 #since at least the start_index will be the length
            for i in range(start_index, len(lst)-1):
                if lst[i] > lst[i+1]:
                    break #stop as soon as the next element is larger
                else:
                    length += 1
                
        return length


    
    def natural_merge_sort(self, lst):
        # print statements used to check my work along the way, commented out now
        # step 1: starting at index 0 find the first run
        i=0
        while i < len(lst):
            # print(lst) #used this to check my work
            run1 = self.get_sorted_run_length(lst, i)
            #if run1 is the whole list, then the list is sorted
            if run1 == len(lst):
                return
            # print("run 1 leng:", run1)
            #save left start & end to call merge later
            L_starting_index = i
            L_ending_index = (i + run1) - 1
            #if run1 ends at the end of the list, reset i=0
            while L_ending_index == len(lst)-1:
                i = 0
                run1 = self.get_sorted_run_length(lst, i)
                L_starting_index = i
                L_ending_index = (i + run1) - 1
            #find the second run
            run2 = self.get_sorted_run_length(lst, L_ending_index+1)
            # print("run 2 leng:", run2)
            #find the right end
            R_ending_index = (L_ending_index + run2)
            #merge the two runs
            # print(lst[L_starting_index], lst[L_ending_index], lst[R_ending_index])
            self.merge(lst, L_starting_index,L_ending_index, R_ending_index)
            i = R_ending_index + 1
            if i >= len(lst):
                i = 0
            # print(i)

    
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
