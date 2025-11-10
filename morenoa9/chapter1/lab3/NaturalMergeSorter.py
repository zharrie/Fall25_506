class NaturalMergeSorter:
    def get_sorted_run_length(self, lst, start_index):
        if start_index <0 or start_index >=len(lst):
            return 0
        
        runlength=1
        for i in range(start_index, len(lst)-1):
            if lst[i] <=lst[i+1]:
                runlength +=1
            else:
                break
        return runlength
    
    def natural_merge_sort(self, lst):
        if len(lst) <=1:
            return
        while True:
            i=0
            merged=False

            while i < len(lst):
                first_runlength=self.get_sorted_run_length(lst,i)
                if first_runlength==0:
                    return
                if i+first_runlength>=len(lst):
                    break
                
                secondstart=i+first_runlength
                second_runlength= self.get_sorted_run_length(lst, secondstart)

                self.merge(lst,i,secondstart-1,secondstart+second_runlength-1)
                merged=True

                i=secondstart+second_runlength

                if i >=len(lst):
                    break

            if not merged:
                break
        
    
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
