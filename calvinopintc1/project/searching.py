
# ======================
# Searching algorithms
# ======================
import time  # used to measure how long searching takes
from verbose import verbose_log 


def linear_search_songs(song_list, title):
    """
    Perform a linear search through a list of songs.

    song_list: list of Song objects
    match_function: a helper function that takes a Song and returns True
                    if the song matches the search condition
    returns: (matching_songs_list, number_of_comparisons, elapsed_seconds)
    """

    matched_song = [] # instantiate empty list for holding matched songs
    number_of_comparisons = 0  # counts how many songs we check
    start_time = time.perf_counter()  # start timing as close to the loop as possible

    for i in range(len(song_list)):
        number_of_comparisons += 1  # increment before comparing
        
        song = song_list[i]  # grab the current Song object with the index
        if song.title.lower() == title.lower(): #need to see if the song title matches the searched title
            matched_song.append(song) #if it does, append to the matched songs list

    elapsed_seconds = time.perf_counter() - start_time  # compute how long the loop took

    verbose_log( 
        "Linear search completed with " 
        + str(number_of_comparisons)
        + " comparisons and "
        + str((len(matched_song)))
        + " match(es)."
    )

    return matched_song, number_of_comparisons, elapsed_seconds  # return the songs that matched list, # of comps & time


def linear_search_songs_for_partial_title(song_list, substring_norm):
    """
    Perform a linear search through a list of songs based on a normalized substring.
    This is like the linear_search_songs method but it considers that multiple songs may have substrings that match what is being searched.
    Therefore this method needs to check all the way down the list and compare each song (basically always worst case)

    song_list: list of Song objects
    match_function: a helper function that takes a Song and returns True
                    if the song matches the search condition
    returns: (matching_songs_list, number_of_comparisons)
    """
    matching_songs = [] # for this one we will append to a matching songs list since there is likely going to be more than 1 song

    number_of_comparisons = 0  # counts how many songs we check
    start_time = time.perf_counter()  # start timing as close to the loop as possible

    for song in song_list: #also, we need to go through the whole list, not just until we find the first match
        number_of_comparisons += 1 #this will end up being the length of the list

        if substring_norm in song.title.lower(): #check if the substring is a part of the song title string
            matching_songs.append(song) #if so append to our list declared earlier
    elapsed_seconds = time.perf_counter() - start_time 
    
    verbose_log(
        "Linear search completed with "
        + str(number_of_comparisons)
        + " comparisons and "
        + str(len(matching_songs))
        + " match(es)."
    )
    return matching_songs, number_of_comparisons, elapsed_seconds

#note, binary search only works for a sorted list, so we need to have a sorted list of songs before using this
def binary_search_songs_by_title(sorted_song_list, title):
    """
    Perform a binary search for a song title in a sorted list.

    sorted_song_list: list of Song objects sorted by title
    title: string (exact title to search for)
    returns: (Song object or None, number_of_comparisons, elapsed_seconds)
    """
    verbose_log( 
        "Starting binary search for title '" 
        + title 
        + "' in "
        + str(len(sorted_song_list)) 
        + " sorted songs."
    )

    # the search range spans the whole array at the beginning
    low_index = 0  #beginning of search range
    high_index = len(sorted_song_list) - 1  # end of current search range
    title_norm = title.lower()  # we need to match the title, normalizing it for better experience
    
    number_of_comparisons = 0  # counts comparisons
    start_time = time.perf_counter()  # start timing right before the while loop for accurate measurement

    while high_index >= low_index:  # keep searching while the range is not empty
        mid_index = (high_index + low_index) // 2  # compute middle index using floor division, ensures an iteger result
        number_of_comparisons += 1  # increment before comparing

        mid_song = sorted_song_list[mid_index]  # get the middle Song so we can read its title
        mid_title = mid_song.title.lower()  # normalize the mid title for case-insensitive comparison

        #note: the verbose log will impact the time computation, to get accurate measure the verbose needs to toggle off
        verbose_log(
            "Binary search comparison #"
            + str(number_of_comparisons)  # show which comparison this is
            + ": checking index "
            + str(mid_index)  # show which index we are testing
            + " with title '"
            + mid_title  # show the normalized title we are comparing against
            + "'."
        )

        if mid_title < title_norm:  # if mid title is alphabetically before the target, target must be to the right
            low_index = mid_index + 1  # move low past mid to eliminate the left half
        elif mid_title > title_norm:  # if mid title is alphabetically after the target, target must be to the left
            high_index = mid_index - 1  # move high before mid to eliminate the right half
        else:  # otherwise, mid_title == title_lower, meaning we found the exact title
            elapsed_seconds = time.perf_counter() - start_time  # stop timing right when we find the result
            
            verbose_log(
                "Binary search found title at index "
                + str(mid_index)  # show where it was found
                + " after "
                + str(number_of_comparisons)  # show how many comparisons were needed
                + " comparisons."
            )

            return mid_song, number_of_comparisons, elapsed_seconds  # return the Song object

    elapsed_seconds = time.perf_counter() - start_time  # if loop ends, we didn't find it, so compute elapsed time of that

    verbose_log( 
        "Binary search did not find title after "
        + str(number_of_comparisons)  
        + " comparisons."
    )

    return None, number_of_comparisons, elapsed_seconds 

