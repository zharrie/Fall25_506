"""
A Simple Playlist Generator™
CSIT 506 - Final Project
By Vincent L. and Camila C.
2025. All rights reserved.
"""
#region Import Statement

# Python Standard Library Imports
import csv
import json
import time
from collections import defaultdict, deque

# Module imports
from verbose import verbose_log, set_verbose

from models import Song, Playlist, format_duration
from sorting import partition_song_list, quicksort_song_list, merge_songs, merge_sort_song_list
from searching import linear_search_songs, linear_search_songs_for_partial_title, binary_search_songs_by_title
from graph import SongGraph
from queues import ArrayQueue
from binarysearchtree import BinarySearchTree, BinarySearchTreeNode

#endregion Import Statement

#region goodbye
goodbye = """
               .            . .   ....-=+*#%@#.      
.    .  . . .    .  ..........-+#%%@@@@@@@@@@#.      
    .     .  ........:=*%@@@@@@@@@@@@@@@@@@@@#.      
.  . .      ....*@@@@@@@@@@@@@@@@@@@@@@@@@@@@#..     
       .    .  .#@@@@@@@@@@@@@@@@@@@@%*+=-:-##..   . 
.              .#@@@@@@@@@@@%#+-::....... .:##.      
    . .   .    .#@@@%#=:.. ....       .   .:##.... ..
         .     .#@...  .   .  . ..        .:##.  ..  
.              .#@...  .   ..           . .:##..     
 .     .    .  .#@..      .               .:##.  ..  
     .         .#@...    .   . ..         .:##.      
         .     .#@..   ..   .         .   .:##..     
     .    .    .#@...        .          ...:##...    
    .          .#@..        .         .   .:##. .  . 
 ..            .#@..     .     ..   .. .  .:##.      
.. ..    ...   .#@..           . .....:-==:-%#.   .  
.            . .#@..   ...  .. ...:*@@@@@@@@@#.  ..  
.   .   .  ..  .#@..       . ....*@@@@@@@@@@@#..     
     ......-+=-:#@.. .        ..*@@@@@@@@@@@@*.      
  .  ..=%@@@@@@@@@..          .:%@@@@@@@@@@@#:...  . 
   ..=@@@@@@@@@@@@.. .        ..+@@@@@@@@@%=...   .. 
. ..+@@@@@@@@@@@@%..          ...:+#%%#*=:...        
. .:%@@@@@@@@@@@%:..   .        .........   ..       
.  .+@@@@@@@@@@+....       ..  ..        .    .      
   ..:*#%%%#+-....  .  .  .    .                 .
######################################################      
##################### Thank you! #####################
######################################################
"""
#endregion goodbye

#region ASCII_colors
YELLOW = "\033[93m"
RED = "\033[91m"
GREEN = "\033[92m"
PURPLE = "\033[35m"
BLUE    = "\033[94m"
RESET = "\033[0m"
#endregion ASCII_colors

#region Menu
# ======================
# CLI / Menu
# ======================

def print_main_menu():
    """
    Print the main menu options.
    """
    print()
    print(f"{GREEN}#### A Simple Playlist Generator™ Main Menu ####.{RESET}")
    print()
    print("1. Browse library")
    print("2. Search songs")
    print("3. Sort library")
    print("4. Playlist Manager")
    print("5. Compare sorting performance")
    print("6. Get recommendations")
    print("7. Toggle verbose mode on/off")
    print(f"0. {RED}Exit{RESET}")


def search_menu(library):
    """
    Handle the search submenu.

    library: MusicLibrary
    """
    print("\nSearch by:")
    print()
    print("1. Exact title")
    print("2. Artist")
    print("3. Genre")
    print("4. Partial title (substring)")
    print()
    search_choice = input("Select: ").strip()

    if search_choice == "1":
        title = input("Enter exact title: ")
        # Below are all the items we expect returned from the search exact title function, it includes the matched searched song as well as number of comparisons and elapsed time for algorithm comparison
        (
            linear_matches,
            linear_comparisons,
            linear_elapsed_time,
            binary_matches,
            binary_comparisons,
            binary_elapsed_time
        ) = library.search_exact_title(title)

        print("\nLinear search results:")
        if linear_matches:
            for song in linear_matches:
                print(" ", song) #print all the songs that matched
        else:
            print("  (no result)")
        # And print out comparisons and time for algorithm comparison
        print("Linear comparisons: " + str(linear_comparisons))
        print("Linear elapsed time: " + str(linear_elapsed_time))

        print("\nBinary search result:")
        if binary_matches:
            for song in binary_matches:
                print(" ", song) #print all the songs that matched
        else:
            print("  (no result)")
        # Print out comparisons and time for algorithm comparison
        print("Binary comparisons: " + str(binary_comparisons))
        print("Binary elapsed time: " + str(binary_elapsed_time))

    elif search_choice == "2":
        artist = input("Artist name: ").lower() # normalize as the artists names are saved normalized for easier searching with the search by artist function
        results = library.search_by_artist(artist)
        if not results:
            print("No songs found for that artist.")
        else:
            for song in results:
                print(" ", song)

    elif search_choice == "3":
        genre = input("Genre: ").lower() # normalize as the genre names are saved normalized for easier searching with the search by genre function
        results = library.search_by_genre(genre)
        if not results:
            print("No songs found for that genre.")
        else:
            for song in results:
                print(" ", song)

    elif search_choice == "4":
        substring = input("Substring: ")
        results = library.search_partial_title(substring) # call the function that will go through all songs to check if the substring is in the title
        if not results:
            print("No songs matched that substring.")
        else:
            for song in results:
                print(" ", song) # prints out every song that contains the search substring
    else:
        print(f"{RED}Invalid choice.{RESET}")


def sort_menu(library):
    """
    Handle the sort submenu.

    library: MusicLibrary
    """
    print("\nSort library by:")
    print()
    print("1. Title (A-Z)")
    print("2. Artist")
    print("3. Duration")
    print("4. Rating")
    print("5. Play count")
    print()
    attribute_choice = input("Select: ").strip()

    attribute_map = {
        "1": "title",
        "2": "artist",
        "3": "duration",
        "4": "rating",
        "5": "play_count",
    }

    if attribute_choice not in attribute_map:
        print(f"{RED}Invalid attribute choice.{RESET}")
        return

    attribute = attribute_map[attribute_choice]
    
    print()
    print("Choose sorting algorithm:")
    print()
    print("1. Quicksort")
    print("2. Merge Sort")
    num_attributes = ["rating", "play_count"]
    if attribute in num_attributes:
        print("3. Binary Search Tree Inorder (rating or play count least to greatest)")
        print("4. Binary Search Tree Reverse Inorder (rating or play count greatest to least)")
    algorithm_choice = input("\nSelect: ").strip()

    if algorithm_choice == "1":
        algorithm = "quick"
        algorithm_name = "Quicksort"
    elif algorithm_choice == "2":
        algorithm = "merge"
        algorithm_name = "Merge Sort"
    elif algorithm_choice == "3" and attribute == "rating":
        algorithm = "bst"
        algorithm_name = "Binary Search Tree Inorder (by rating)"
    elif algorithm_choice == "3" and attribute == "play_count":
        algorithm = "bst"
        algorithm_name = "Binary Search Tree Inorder (by play count)"
    elif algorithm_choice == "4" and attribute == "rating":
        algorithm = "rev_bst"
        algorithm_name = "Binary Search Tree Reverse Inorder (by rating)"
    elif algorithm_choice == "4" and attribute == "play_count":
        algorithm = "rev_bst"
        algorithm_name = "Binary Search Tree Reverse Inorder (by play count)"
    else:
        print(f"{RED}Invalid algorithm choice.{RESET}")
        return
    sorted_songs, elapsed_seconds = library.sort_library(attribute, algorithm)

    print(
        "\nSorting "
        + str(len(sorted_songs))
        + " songs by "
        + attribute
        + " using "
        + algorithm_name
        + " took "
        + f"{elapsed_seconds:.6f}"
        + " seconds."
    )

    print("\nTop 10 songs by " + attribute + ":")
    print()
    for song in sorted_songs[:10]:
        print(f" {song} - Times Played: {library._key_play_count(song)}")


def playlist_menu(library):
    """
    Handle the playlist submenu.

    library: MusicLibrary
    """
    print("\nPlaylist Manager:")
    print()
    print("1. New playlist")
    print("2. Add songs to playlist")
    print("3. Remove songs from playlist")
    print("4. View playlist")
    print("5. Playback playlist")
    print("6. Save playlists to file")
    print("7. Load playlists from file")
    print()
    playlist_choice = input("Select: ").strip()

    if playlist_choice == "1":
        name = input("Playlist name: ")
        library.create_playlist(name)
        print(f"Playlist {name} created.")
        print(f"Would you like to continue working with {name}?")
        stay_on_pl_menu = input(f"\nType 'Yes' to return to the Playlist menu. Otherwise, enter any other input to return to the main menu: ").lower()
        if stay_on_pl_menu == "yes":
          playlist_menu(library)
        else:
          return

    elif playlist_choice in {"2", "3", "4", "5"}:
        #get and print out user's playlists as a reference
        all_playlists = library.get_all_playlists()
        if not all_playlists:
          print(f"You have no playlists, please create a playlist.")
          return
        elif playlist_choice == "6":
            print(f"Enter the playlist you want to save.")
            for pl_name, _ in all_playlists.items():
                print(f"{PURPLE}{pl_name}{RESET}")
        else:
          print(f"Enter the playlist you want to edit.")
          for pl_name, _ in all_playlists.items():
            print(f"{PURPLE}{pl_name}{RESET}")

        name = input("Playlist name: ")
        playlist = library.get_playlist(name)
        if not playlist:
            print("Playlist not found.")
            return

        if playlist_choice == "2":
            print("Enter song titles (one per line, 'done' to finish):")
            while True:
                title = input("Enter the name of a song, or type 'done' to finish: > ").strip()
                if title.lower() == "done":
                    break
                song, _ , _ = binary_search_songs_by_title(
                    library.sorted_songs_by_title_cache, title
                )
                if song:
                    #add the song and also prompt the user with song recommendations based on the song they just added
                    playlist.add_song(song)
                    print("Added:", song)
                    # setting base title for recommend from title
                    base_title = title
                    # make the call to get the recommendations
                    recommended_songs = library.recommend_from_title(base_title)
                    if not recommended_songs:
                        pass
                    print(f"\nRecommended songs:")
                    for song in recommended_songs:
                        print(" ", song)
                else:
                    # This enables substring search when adding songs, so a user can see all songs that match a substring
                    substring = title
                    matching_songs = library.search_partial_title(substring)
                    if matching_songs:
                      # if songs match the substring, ask the user if they intended to add that song and add or don't add based on their follow up
                      for song in matching_songs: # it will ask them for every song that matched the substring
                        print(f"Did you want to add {song} to your playlist?")
                        user_confirmation = input(f"Type 'Add' to add {song} (otherwise, all other inputs will not add {song}: ").strip()
                        if user_confirmation.lower() == "add":
                            playlist.add_song(song)
                            print("Added:", song)
                        else:
                            print(f"{song} not added.")
                    else:
                        print(f"Could not find song with title {title}.")
            print()
            print(playlist)

        elif playlist_choice == "3":
            title_to_remove = input("Title to remove: ")
            if playlist.remove_song_by_title(title_to_remove):
                print("Removed.")
            else:
                print("Song not found in playlist.")
            print(playlist)

        elif playlist_choice == "4":
            print()
            print(playlist)
            print()
            # if a user views a playlist, they are then prompted to stay on the playlist menu in case they then wanted to do something with it (just like right after they create a new playlist)
            print(f"Would you like to continue working with {name}?")
            stay_on_pl_menu = input(f"Type 'Yes' to return to the Playlist menu. Otherwise, enter any other input to return to the main menu: ").lower()
            if stay_on_pl_menu == "yes":
                playlist_menu(library)
            else:
                return

        elif playlist_choice == "5":
            library.simulate_playback(playlist)

    elif playlist_choice == "6":
        path = str("playlists.json")
        library.save_playlists(path)
        print("Playlists saved as", path)

    elif playlist_choice == "7":
        path = input("File name to load (for example: playlists.json): ")
        library.load_playlists(path)
        print("Playlists loaded.")

    else:
        print(f"{RED}Invalid choice. Returning to Main Menu.{RESET}")


def recommendations_menu(library):
    """
    Handle the recommendation submenu.

    library: MusicLibrary
    """
    print()
    base_title = input("Full song title for recommendations: ") # prompt user for a song they'd want recommendations for
    recommended_songs = library.recommend_from_title(base_title) # call the recommend song function
    if not recommended_songs: 
        return # if it is none then end
    print("\nRecommended songs:")
    for song in recommended_songs: 
        print(f" {song}") # print out all the recommended songs returned
        

def compare_sort_menu(library):
    """
    Handle the sorting performance comparison submenu.

    library: MusicLibrary
    """
    print("\nCompare sorting performance by attribute:")
    print()
    print("1. Title")
    print("2. Artist")
    print("3. Duration")
    print("4. Rating")
    print("5. Play count")
    print()
    attribute_choice = input("Select: ").strip()

    # map user input to attribute strings
    attribute_map = { 
        "1": "title",
        "2": "artist",
        "3": "duration",
        "4": "rating",
        "5": "play_count",
    }

    if attribute_choice not in attribute_map:
        print(f"{RED}Invalid attribute.{RESET}")
        return

    attribute = attribute_map[attribute_choice]
    library.compare_sort_performance(attribute, sizes=[10, 20, 50, 100])

# ======================
# MusicLibrary: core manager
# ======================

class MusicLibrary():
    """
    Core manager for the smart playlist system.

    Attributes:
        songs_by_id: dictionary from song_id string to Song
        songs_by_artist: dictionary from artist string to list of Song
        songs_by_genre: dictionary from genre string to list of Song
        sorted_songs_by_title_cache: list of Song sorted by title
        song_similarity_graph: SongGraph instance
        playlists: dictionary from playlist name to Playlist
    """

    def __init__(self):
        # Hash-map based indices
        self.songs_by_id = {}
        self.songs_by_artist = defaultdict(list)
        self.songs_by_genre = defaultdict(list)

        # For binary search by title, need to keep a sorted list by title in order to use binary search as a search algorithm
        self.sorted_songs_by_title_cache = []

        # Graph for recommendations
        self.song_similarity_graph = SongGraph()

        # Playlists
        self.playlists = {}

    # ---------- Helper key functions ----------

    def _key_title_lower(self, song):
        """
        Key function: lowercased title.

        song: Song
        returns: string
        """
        return song.title.lower()

    def _key_artist_lower(self, song):
        """
        Key function: lowercased artist.

        song: Song
        returns: string
        """
        return song.artist.lower()

    def _key_duration(self, song):
        """
        Key function: duration in seconds.

        song: Song
        returns: integer
        """
        return song.duration_in_seconds

    def _key_rating(self, song):
        """
        Key function: rating.

        song: Song
        returns: float
        """
        return song.rating

    def _key_play_count(self, song):
        """
        Key function: play count.

        song: Song
        returns: integer
        """
        return song.play_count

    def _get_key_function_for_attribute(self, attribute):
        """
        Return a key function based on the attribute string.
        This replaces lambdas with named functions.

        attribute: string
        returns: function taking Song and returning a sortable key
        """
        if attribute == "title":
            return self._key_title_lower
        if attribute == "artist":
            return self._key_artist_lower
        if attribute == "duration":
            return self._key_duration
        if attribute == "rating":
            return self._key_rating
        if attribute == "play_count":
            return self._key_play_count
        raise ValueError("Unknown attribute: " + attribute)

    # ---------- Loading & indexing ----------

    def load_from_csv(self, path):
        """
        Load songs from a CSV file and build indices and graph.

        path: string (file path)
        """
        verbose_log("Loading music library from file: " + path)
        with open(path, newline="", encoding="utf-8") as file_handle: # create file handle
            csv_reader = csv.DictReader(file_handle) # create CSV reader
            songs_loaded_count = 0  # counter for loaded songs 
            for row in csv_reader: # iterate over each row in the CSV
                song = Song(
                    song_id=row["song_id"],
                    title=row["title"],
                    artist=row["artist"],
                    genre=row["genre"],
                    duration_in_seconds=int(row["duration_sec"]),
                    rating=float(row["rating"]),
                    play_count=int(row["play_count"]),
                )
                self._add_song_to_indices(song) # add song to indices
                songs_loaded_count += 1 # increment counter for songs loaded

        verbose_log("Finished reading " + str(songs_loaded_count) + " songs from CSV.")
        self._rebuild_sorted_title_cache() # rebuild sorted title cache
        self.song_similarity_graph.build_from_songs(
            list(self.songs_by_id.values()) # pass list of songs to build a song graph
        )
        verbose_log(
            "MusicLibrary now contains "
            + str(len(self.songs_by_id))
            + " songs after loading."
        )

    def _add_song_to_indices(self, song):
        """
        Insert a song into all hash-based indices.

        song: Song
        """
        self.songs_by_id[song.song_id] = song # index by id
        self.songs_by_artist[song.norm_artist].append(song) # index by artist
        self.songs_by_genre[song.norm_genre].append(song) # index by genre
        verbose_log(
            "Indexed song '"
            + song.title
            + "' by id, artist, and genre in the library."
        )

    def _rebuild_sorted_title_cache(self):
        """
        Rebuild the cached title-sorted list used for binary search.
        """
        self.sorted_songs_by_title_cache = list(self.songs_by_id.values()) # get all songs
        self.sorted_songs_by_title_cache.sort(key=self._key_title_lower) # sort by title (case-insensitive)
        verbose_log(
            "Rebuilt sorted-by-title cache for binary search, containing "
            + str(len(self.sorted_songs_by_title_cache))
            + " songs."
        )

    # ---------- Display ----------

    def list_songs(self, limit=20):
        """
        Print up to 'limit' songs from the library, sorted by title.

        limit: integer
        """
        song_list = list(self.songs_by_id.values()) # get all songs
        song_list.sort(key=self._key_title_lower) # sort by title (case-insensitive)
        print(
            "\nLibrary contains "
            + str(len(song_list))
            + " songs. Showing up to "
            + str(limit)
            + ":\n"
        )
        for song in song_list[:limit]: # print each song up to the limit
            print(" ", song)

    # ---------- Search ----------

    def search_exact_title(self, title):
        """
        Perform both linear and binary searches for the given title.

        title: string
        returns: (linear_matches, linear_comparisons, binary_matches, binary_comparisons)
        """

        song_list = list(self.songs_by_id.values()) # get all songs

        verbose_log(
            "Initiating EXACT TITLE search for '"
            + title
            + "' using both linear search and binary search."
        )

        # calls are made to linear & binary search for the purpose of comparing searching algorithms

        # linear search
        linear_matches, linear_comparisons, linear_elapsed_time = linear_search_songs(
            song_list, title #match_function
        )

        # binary search (on sorted title cache)
        binary_song, binary_comparisons, binary_elapsed_time = binary_search_songs_by_title(
            self.sorted_songs_by_title_cache, title
        )
        if binary_song:
            binary_matches = [binary_song]
        else:
            binary_matches = []

        return linear_matches, linear_comparisons, linear_elapsed_time, binary_matches, binary_comparisons, binary_elapsed_time

    def search_by_artist(self, artist):
        """
        Search by artist using the hash index.

        artist: string
        returns: list of Song
        """
        verbose_log("Performing hash-based artist lookup for '" + artist + "'.")
        # simple call to a function that searches by artist value
        return self.songs_by_artist.get(artist, [])

    def search_by_genre(self, genre):
        """
        Search by genre using the hash index.

        genre: string
        returns: list of Song
        """
        verbose_log("Performing hash-based genre lookup for '" + genre + "'.")
        # simple call to a function that searches by genre value
        return self.songs_by_genre.get(genre, [])

    def search_partial_title(self, substring):
        """
        Perform a substring search on titles using linear search.

        substring: string
        returns: list of Song
        """
        substring_norm = substring.lower() # normalize for case-insensitive search
        song_list = list(self.songs_by_id.values()) # get all songs

        verbose_log(
            "Starting PARTIAL TITLE substring search for '"
            + substring
            + "'."
        )
        # make the call to linear search, ie. the function that goes through all items and returns all where the substring is in the title
        matching_songs, number_of_comparisons, _ = linear_search_songs_for_partial_title(
            song_list, substring_norm 
        )
        verbose_log(
            "Partial title search completed with "
            + str(number_of_comparisons)
            + " comparisons and "
            + str(len(matching_songs))
            + " match(es)."
        )
        return matching_songs

    # ---------- Sorting ----------

    def sort_library(self, attribute, algorithm):
        """
        Return a new list of songs sorted by attribute using the specified algorithm.

        attribute: string, one of {"title", "artist", "duration", "rating", "play_count"}
        algorithm: string, one of {"quick", "merge", "bst"}
        returns: (sorted_song_list, elapsed_seconds)
        """

        song_list = list(self.songs_by_id.values())
        key_function = self._get_key_function_for_attribute(attribute)

        verbose_log(
            "Sorting library by '"
            + attribute
            + "' using '"
            + algorithm
            + "' algorithm on "
            + str(len(song_list))
            + " songs."
        )

        start_time = time.perf_counter()

        if algorithm == "quick":
            quicksort_song_list(song_list, 0, len(song_list) - 1, key_function)
        elif algorithm == "merge":
            merge_sort_song_list(song_list, 0, len(song_list) - 1, key_function)
#region Binary Search Tree Sort
        elif algorithm == "bst":
            tree = BinarySearchTree(attribute)
            for song in song_list:
                tree.insert(song)
            song_list = tree.inorder_traversal() 
        elif algorithm == "rev_bst":
            tree = BinarySearchTree(attribute)
            for song in song_list:
                tree.insert(song)
            song_list = tree.reverse_inorder()
        #endregion
        else:
            raise ValueError("Unknown sorting algorithm")

        elapsed_seconds = time.perf_counter() - start_time

        verbose_log(
            "Sorting operation completed in "
            + f"{elapsed_seconds:.6f}"
            + " seconds."
        )
        return song_list, elapsed_seconds

    def compare_sort_performance(self, attribute, sizes):
        """
        Compare Quicksort vs Merge Sort on various input sizes.
        Prints timing results.

        attribute: string
        sizes: list of integers (input sizes)
        """

        base_song_list = list(self.songs_by_id.values())
        key_function = self._get_key_function_for_attribute(attribute)

        for size in sizes:
            if size > len(base_song_list):
                continue
            subset_song_list = base_song_list[:size]

            verbose_log(
                "Measuring Quicksort and Merge Sort performance on "
                + str(size)
                + " songs sorted by '"
                + attribute
                + "'."
            )

            # Quicksort
            quicksort_song_list_copy = subset_song_list.copy()
            start_time = time.perf_counter()
            quicksort_song_list(
                quicksort_song_list_copy,
                0,
                len(quicksort_song_list_copy) - 1,
                key_function
            )
            quicksort_elapsed = time.perf_counter() - start_time

            # Merge sort
            merge_sort_song_list_copy = subset_song_list.copy()
            start_time = time.perf_counter()
            merge_sort_song_list(
                merge_sort_song_list_copy,
                0,
                len(merge_sort_song_list_copy) - 1,
                key_function
            )
            merge_sort_elapsed = time.perf_counter() - start_time

            print(
                f"{size:4d} items: "
                f"Quicksort={quicksort_elapsed:.6f}s, "
                f"MergeSort={merge_sort_elapsed:.6f}s"
            )

    # ---------- Playlists + playback ----------

    def create_playlist(self, name):
        """
        Create a new playlist in the library.

        name: string
        returns: Playlist
        """
        playlist = Playlist(name)
        self.playlists[name] = playlist
        verbose_log('Stored playlist "' + name + '" in MusicLibrary.')
        return playlist

    def get_playlist(self, name):
        """
        Retrieve a playlist by name.

        name: string
        returns: Playlist or None
        """
        return self.playlists.get(name)
    
#region Get All Playlists
    def get_all_playlists(self):
        """
        Returns all playlists created by a user

        """
        return self.playlists
#endregion Get All Playlists

    def save_playlists(self, path):
        """
        Save playlists as JSON: {name: [song_id, ...], ...}

        path: string
        """
        playlist_serializable_data = {
            name: [song.song_id for song in playlist.song_list] # list of song IDs
            for name, playlist in self.playlists.items() # iterate over playlists
        }
        
        with open(path, "w", encoding="utf-8") as file_handle:
            json.dump(playlist_serializable_data, file_handle, indent=2)
        verbose_log("Saved " + str(len(self.playlists)) + " playlist(s) to " + path + ".")

    def load_playlists(self, path):
        """
        Load playlists from a JSON file, if present.

        path: string
        """
        try:
            with open(path, encoding="utf-8") as file_handle:
                stored_playlist_data = json.load(file_handle)
        except FileNotFoundError:
            verbose_log(
                "No playlist file found at "
                + path
                + "; starting with empty playlists."
            )
            return

        self.playlists.clear()
        loaded_playlists_count = 0
        for name, song_id_list in stored_playlist_data.items():
            playlist = Playlist(name)
            for song_id in song_id_list:
                song = self.songs_by_id.get(song_id)
                if song:
                    playlist.add_song(song)
            self.playlists[name] = playlist
            loaded_playlists_count += 1

        verbose_log("Loaded " + str(loaded_playlists_count) + " playlist(s) from " + path + ".")

    def simulate_playback(self, playlist):
        """
        Simulate playback using ArrayQueue.

        playlist: Playlist
        """
        if not playlist.song_list:
            print("Playlist is empty.")
            return

        verbose_log(
            "Starting playback simulation for playlist '"
            + playlist.name
            + "'."
        )
        playback_queue = ArrayQueue()
        for song in playlist.song_list:
            playback_queue.enqueue(song)

        print("\nPlayback Queue:")
        while not playback_queue.is_empty():
            #region Playback with Counter
            current_song = playback_queue.dequeue()
            #add to the play_count of every song "played" from the playlist
            current_song.play_count += 1

            print(f"[NOW PLAYING] '{current_song.title}' - {current_song.artist}/[{format_duration(current_song.duration_in_seconds)}] - [PLAY HISTORY] 'Played {str(current_song.play_count)} times.'") 
  

    # ---------- Recommendations ----------

    def recommend_from_title(self, title, maximum_results=5):
        """
        Find the song by title, then call BFS in the similarity graph.

        title: string
        maximum_results: integer
        returns: list of Song
        """
        verbose_log(
            "Generating recommendations based on base song title '"
            + title
            + "'."
        )
        #we don't need the other outputs from the binary search songs function so the "_" work as a placeholder to not get errors
        # binary search to check we have that song and also get the song object (since user is only giving us a string song title) with all its attributed needed for the recommendations call
        song, _ , _ = binary_search_songs_by_title( 
            self.sorted_songs_by_title_cache, title
        )
        if not song:
            print(f"{RED}No song with title {title} found for recommendations.{RESET}")
            return [] # if the song is not found return empty list
        
        # otherwise, call the recommendations function using the song graph. The song's song id is used as the starting node for BFS
        recommended_song_ids = self.song_similarity_graph.recommend_using_breadth_first_search(
            song.song_id, maximum_depth=2, maximum_results=maximum_results
        )
        recommended_songs = [] # we will save the songs the recommendations return to this list
        for song_id in recommended_song_ids:
            if song_id in self.songs_by_id:
                recommended_songs.append(self.songs_by_id[song_id])

        verbose_log(
            "Converted "
            + str(len(recommended_song_ids))
            + " recommended song id(s) into Song objects."
        )
        return recommended_songs


#region MAIN
def main():
    """
    Main program loop.
    """
    global VERBOSE_ENABLED # flag for verbose logging, global scope

    print(f"{GREEN}Welcome to A Simple Playlist Generator™.{RESET}")

    # Verbosity Toggle
    prompt = f"{YELLOW}Enable verbose mode for narrated demo? (y/n): {RESET}"  # pre-colorize the prompt string before it's wrapped in input()
    verbose_response = input(prompt).strip().lower()
    VERBOSE_ENABLED = (verbose_response == "y") # set enablement flag based on user input
    set_verbose(VERBOSE_ENABLED)

    print("\nIf you press Enter without typing a file name, a demo CSV will be created automatically.")
    csv_path = input("Enter name of music library CSV (>= 30 songs): ").strip()

    # -------------------------------
    # FALLBACK: User pressed ENTER
    # -------------------------------
    if csv_path == "":
        csv_path = "demo_music_library.csv"
        print("\nNo file provided. Creating demo CSV at '" + csv_path + "'...")

        # Build 30 demo songs
        demo_songs = [
            ["1", "Bohemian Rhapsody", "Queen", "Rock", 367, 5.0, 120],
            ["2", "Imagine", "John Lennon", "Pop", 195, 4.9, 95],
            ["3", "Hotel California", "Eagles", "Rock", 390, 4.8, 110],
            ["4", "Billie Jean", "Michael Jackson", "Pop", 294, 4.8, 130],
            ["5", "Smells Like Teen Spirit", "Nirvana", "Rock", 301, 4.7, 100],
            ["6", "Like a Rolling Stone", "Bob Dylan", "Folk", 369, 4.7, 80],
            ["7", "Respect", "Aretha Franklin", "Soul", 148, 4.6, 70],
            ["8", "Good Vibrations", "The Beach Boys", "Rock", 216, 4.5, 65],
            ["9", "Hey Jude", "The Beatles", "Rock", 431, 4.9, 150],
            ["10", "Purple Rain", "Prince", "Pop", 480, 4.8, 140],
            ["11", "Superstition", "Stevie Wonder", "Soul", 250, 4.7, 90],
            ["12", "Smooth", "Santana", "Rock", 298, 4.5, 85],
            ["13", "Rolling in the Deep", "Adele", "Pop", 228, 4.6, 200],
            ["14", "Shape of You", "Ed Sheeran", "Pop", 233, 4.4, 230],
            ["15", "Lose Yourself", "Eminem", "Hip-Hop", 326, 4.9, 250],
            ["16", "All of Me", "John Legend", "R&B", 269, 4.5, 160],
            ["17", "Halo", "Beyonce", "Pop", 261, 4.6, 170],
            ["18", "Thunderstruck", "AC/DC", "Rock", 292, 4.7, 155],
            ["19", "Uptown Funk", "Bruno Mars", "Pop", 270, 4.6, 300],
            ["20", "Viva La Vida", "Coldplay", "Pop", 242, 4.5, 210],
            ["21", "Radioactive", "Imagine Dragons", "Rock", 186, 4.4, 190],
            ["22", "Numb", "Linkin Park", "Rock", 185, 4.6, 220],
            ["23", "Believer", "Imagine Dragons", "Rock", 204, 4.5, 205],
            ["24", "Thriller", "Michael Jackson", "Pop", 358, 4.9, 280],
            ["25", "Wonderwall", "Oasis", "Rock", 258, 4.6, 240],
            ["26", "Enter Sandman", "Metallica", "Metal", 331, 4.7, 175],
            ["27", "Zombie", "The Cranberries", "Rock", 306, 4.6, 160],
            ["28", "Dream On", "Aerosmith", "Rock", 273, 4.7, 140],
            ["29", "Take On Me", "A-ha", "Pop", 225, 4.5, 175],
            ["30", "Beat It", "Michael Jackson", "Pop", 258, 4.8, 260],
        ]
        
        # Write CSV
        with open(csv_path, "w", newline="", encoding="utf-8") as file: # create file handle
            writer = csv.writer(file) # create CSV writer
            writer.writerow([
                "song_id", "title", "artist", "genre",
                "duration_sec", "rating", "play_count"
            ])
            for row in demo_songs: # write each demo song row
                writer.writerow(row) # write row to CSV   

            print("Demo CSV created with 30 songs.\n")


    # -------------------------------
    # Load library normally
    # -------------------------------
    music_library = MusicLibrary()
    music_library.load_from_csv(csv_path)
    print(
        "\nMusic library loaded: "
        + str(len(music_library.songs_by_id))
        + " songs"
    )

    # Try to load playlists from a default file (optional)
    music_library.load_playlists("playlists.json")

    # Main menu loop
    while True:
        print_main_menu()
        user_choice = input("\nChoice: ").strip()

        if user_choice == "1":
            music_library.list_songs()

        elif user_choice == "2":
            search_menu(music_library)

        elif user_choice == "3":
            sort_menu(music_library)

        elif user_choice == "4":
            playlist_menu(music_library)

        elif user_choice == "5":
            compare_sort_menu(music_library)

        elif user_choice == "6":
            recommendations_menu(music_library)

        elif user_choice == "7":
            if VERBOSE_ENABLED:
                VERBOSE_ENABLED = False
                set_verbose(False)
                print()
                print(f"{RED}Verbose mode is now OFF.{RESET}")

            else:
                VERBOSE_ENABLED = True
                set_verbose(True)
                print()
                print(f"{GREEN}Verbose mode is now ON.{RESET}")
        
        elif user_choice == "0":
            # Autosave playlists as a convenience, on exit
            music_library.save_playlists("playlists.json")
            print(f"{BLUE}{goodbye}{RESET}")
            break

        else:
            print()
            print(f"{RED}Invalid choice. Try again.{RESET}")


if __name__ == "__main__":
    main()

#endregion MAIN