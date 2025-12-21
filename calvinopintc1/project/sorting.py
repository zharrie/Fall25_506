# ======================
# Sorting algorithms (quicksort and merge sort)
# ======================

from verbose import verbose_log 


def partition_song_list(song_list, start_index, end_index, key_function):
    """
    Partition function for quicksort.

    song_list: list of Song
    start_index: integer
    end_index: integer
    key_function: function that takes a Song and returns a sortable key
    returns: partition index (integer)
    """
    midpoint_index = start_index + (end_index - start_index) // 2  # choose midpoint index for pivot selection
    pivot_value = key_function(song_list[midpoint_index])  # compute the pivot key once so we can compare against it repeatedly

    left_index = start_index  # "low" pointer, starting at the left boundary
    right_index = end_index  # "high" pointer, starting at the right boundary

    partition_done = False  # use a boolean flag to control the outer loop

    verbose_log(f"Partitioning sub-array from index {start_index} to {end_index} with pivot value {pivot_value}.")

    while not partition_done:  # keep moving pointers until they cross
        while key_function(song_list[left_index]) < pivot_value:  # move left pointer right until we find something >= pivot
            left_index = left_index + 1  # increment

        while pivot_value < key_function(song_list[right_index]):  # move right pointer left until we find something <= pivot
            right_index = right_index - 1  # decrement

        if left_index >= right_index:  # when pointers cross, partitioning is complete
            partition_done = True  # set the flag to end the outer while loop
        else:
            verbose_log(f"Swapping songs at indices {left_index} and {right_index} during partition.")

            temp_song = song_list[left_index]  # store left item in a temp variable 
            song_list[left_index] = song_list[right_index]  # move right item into the left position
            song_list[right_index] = temp_song  # put the saved left item into the right position

            left_index = left_index + 1  # after swapping, move left pointer inward
            right_index = right_index - 1  # after swapping, move right pointer inward

    verbose_log(f"Partition complete; returning partition index {right_index}.")  # "high is the last index in the left segment"
    return right_index  # return the final right boundary of the left partition


def quicksort_song_list(song_list, start_index, end_index, key_function):
    """
    In-place quicksort of song_list[start_index:end_index+1].

    song_list: list of Song
    start_index: integer
    end_index: integer
    key_function: function that takes Song and returns sortable key
    """
    if end_index <= start_index:  # base case: 0 or 1 element means the segment is already sorted
        return  # stop recursion

    verbose_log(f"Quicksort called on range [{start_index}, {end_index}] ({end_index - start_index + 1} items).")

    partition_index = partition_song_list(song_list, start_index, end_index, key_function)  # partition the list segment around pivot
    quicksort_song_list(song_list, start_index, partition_index, key_function)  # recursively sort the left partition (inclusive)
    quicksort_song_list(song_list, partition_index + 1, end_index, key_function)  # recursively sort the right partition (exclusive of left)


def merge_songs(song_list, left_first_index, left_last_index, right_last_index, key_function):
    """
    Merge step for merge sort.

    song_list: list of Song
    left_first_index: integer
    left_last_index: integer
    right_last_index: integer
    key_function: function that takes Song and returns sortable key
    """
    merged_size = right_last_index - left_first_index + 1  # compute total items in the merge range
    merged_song_list = [None] * merged_size  # create temp list to hold merged results
    merge_position = 0  # index into merged_song_list where the next smallest element goes
    left_position = left_first_index  # pointer for the left partition
    right_position = left_last_index + 1  # pointer for the right partition (starts right after left_last_index)

    verbose_log(f"Merging sub-arrays [{left_first_index}, {left_last_index}] and [{left_last_index + 1}, {right_last_index}].")

    while left_position <= left_last_index and right_position <= right_last_index:  # keep merging while both sides still have items
        left_key = key_function(song_list[left_position])  # compute left key once for clarity
        right_key = key_function(song_list[right_position])  # compute right key once for clarity

        if left_key <= right_key:  # choose from left if it is smaller
            merged_song_list[merge_position] = song_list[left_position]  # place left song into merged list
            left_position = left_position + 1  # advance left pointer because we consumed that item
        else:
            merged_song_list[merge_position] = song_list[right_position]  # place right song into merged list
            right_position = right_position + 1  # advance right pointer because we consumed that item

        merge_position = merge_position + 1  # advance merge position after placing one item

    while left_position <= left_last_index:  # if left partition still has items, copy them over
        merged_song_list[merge_position] = song_list[left_position]  # copy the next left item into the merged list
        left_position = left_position + 1  # advance left pointer
        merge_position = merge_position + 1  # advance merged pointer

    while right_position <= right_last_index:  # if right partition still has items, copy them over
        merged_song_list[merge_position] = song_list[right_position]  # copy the next right item into the merged list
        right_position = right_position + 1  # advance right pointer
        merge_position = merge_position + 1  # advance merged pointer

    for offset in range(merged_size):
        song_list[left_first_index + offset] = merged_song_list[offset]
    verbose_log(f"Merge complete for range [{left_first_index}, {right_last_index}].")


def merge_sort_song_list(song_list, start_index, end_index, key_function):
    """
    Merge sort implementation.

    song_list: list of Song
    start_index: integer
    end_index: integer
    key_function: function that takes Song and returns sortable key
    """
    if start_index < end_index:  # only split/merge when there are at least 2 elements
        midpoint_index = (start_index + end_index) // 2  # compute midpoint
        verbose_log(f"Merge sort called on range [{start_index}, {end_index}] with midpoint {midpoint_index}.")

        merge_sort_song_list(song_list, start_index, midpoint_index, key_function)  # recursively sort left half
        merge_sort_song_list(song_list, midpoint_index + 1, end_index, key_function)  # recursively sort right half
        merge_songs(song_list, start_index, midpoint_index, end_index, key_function)  # merge sorted halves back together