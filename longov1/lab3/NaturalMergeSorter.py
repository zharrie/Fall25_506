'''
Step 1: Implement the get_sorted_run_length() method
Implement the get_sorted_run_length() method in NaturalMergeSorter.py. 

get_sorted_run_length() has two parameters:

[X] lst: A list of integers
[X] start_index: An integer for the run's starting index

[X] Return the number of list elements sorted in ascending order, starting at start_index and ending either at the end of the sorted run, or the end of the list, whichever comes first. 
[X] Return 0 if start_index is out of bounds.

File main.py has several test cases for get_sorted_run_length() that can be run by clicking the Run button. 
One test case also exists for natural_merge_sort(), but that can be ignored until step two is completed.
The program's output does not affect grading.
Submit for grading to ensure that the get_sorted_run_length() unit tests pass before proceeding.

Step 2: Implement the natural_merge_sort() method
Implement the natural_merge_sort() method in NaturalMergeSorter.py. natural_merge_sort() must:

[X] Start at index i=0
[X] Get the length of the first sorted run, starting at i
[X] Return if the first run's length equals the list's length
[X] If the first run ends at the list's end, reassign i=0 and repeat step 2
[X] Get the length of the second sorted run, starting immediately after the first
[X] Merge the two runs with the provided merge() method
[X] Reassign i with the first index after the second run, or 0 if the second run ends at the list's end
[X] Go to step 2
'''
class NaturalMergeSorter:
    def get_sorted_run_length(self, lst, start_index):
        if start_index < 0: 
            return 0 # Step 1: Return 0 if start_index is out of bounds.
        elif start_index >= len(lst):
            return 0 # Step 1: Return 0 if start_index is out of bounds.
        elif len(lst) == 0:
            return 0 # Step 1: Return 0 if start_index is out of bounds.

        run_length = 1
        i = start_index + 1
        while i < len(lst) and lst[i] >= lst[i - 1]:
            run_length += 1
            i += 1
        return run_length # Step 1: Return the number of list elements sorted in ascending order, starting at start_index and ending either at the end of the sorted run, or the end of the list, whichever comes first.
        #pass
    
    def natural_merge_sort(self, lst):
        if len(lst) <= 1:
            return

        i = 0  # Step 2: Start at index i=0
        while True: # Step 2: Go to step 2 (implicitly satisfied by the loop)
            len1 = self.get_sorted_run_length(lst, i) # Step 2: Get the length of the first sorted run, starting at i
            if len1 == len(lst): 
                return # Step 2: Return if the first run's length equals the list's length
            if i + len1 == len(lst):
                i = 0 # Step 2: If the first run ends at the list's end, reassign i=0 ...
                continue # ... and repeat step 2
            len2 = self.get_sorted_run_length(lst, i + len1) # Step 2: Get the length of the second sorted run, starting immediately after the first
            if len2 == 0:
                i = 0
                continue

            left_first = i
            left_last = i + len1 - 1
            right_last = i + len1 + len2 - 1
            self.merge(lst, left_first, left_last, right_last) # Step 2: Merge the two runs with the provided merge() method

            i = i + len1 + len2 # Step 2: Reassign i with the first index after the second run,
            if i == len(lst):
                i = 0  # ...or 0 if the second run ends at the list's end
            #pass
    ############################################################################################################################################################
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
