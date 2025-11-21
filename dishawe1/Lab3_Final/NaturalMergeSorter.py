class NaturalMergeSorter:
    def get_sorted_run_length(self, lst, start_index):
        if start_index < 0 or start_index > len(lst)-1:
            return 0
        else:
           end_index = len(lst) - 1
           for i in range(start_index, len(lst)-1): 
                if lst[i] > lst[i + 1]:
                    end_index = i 
                    break
        return (end_index - start_index) + 1

    
    def natural_merge_sort(self, lst):
        i = 0
        #Get length of the first sorted run starting at i
        while True:
            length_first_sorted_run = self.get_sorted_run_length(lst, i)
            second_run_start_index = i + length_first_sorted_run
            if length_first_sorted_run == len(lst):
                return #list is already sorted
            elif second_run_start_index == len(lst):
                i = 0 #was at end of list so starting over
                continue #goes back to top of while loop
            #Get length of second sorted run
            length_second_sorted_run = self.get_sorted_run_length(lst, second_run_start_index)          
            third_run_start_index = (second_run_start_index + length_second_sorted_run)
            #Merge the two runs using the merge() method
            self.merge(lst,i, second_run_start_index -1, third_run_start_index-1)           
            #After second run, if ends at list end, reassign i to 0: this happens due to Continue
            #Reassign i with the first index after the second run    
            i = third_run_start_index

    
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
