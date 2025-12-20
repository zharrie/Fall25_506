Music Library Manager
By: Anais Moreno

Description:

The Music Library Manager is a Python-based program that allows users to manage and explore a digital music collection. The application supports searching, sorting, playlist creation, simulated playback, and song recommendations based on similarity.
This project was designed to demonstrate the use of multiple data structures and algorithms, including hash maps, queues, sorting algorithms, and graph traversal, while providing a realistic and interactive experience.

Features Implemented
-Library Management

Load a music library from a CSV file (35 songs)
Display all songs in a clean, readable format
Store songs using hash maps for fast lookup

-Search Functionality

*Search by song title (supports partial/substring matching)
*Search by artist
*Search by genre

Uses linear search and hash-based lookup for comparison

-Sorting Capabilities

Sort songs by:

*Title
*Artist
*Duration
*Rating
*Play count

Implements Quick Sort and Merge Sort

Allows performance comparison between sorting algorithms

-Playlist Management

Create playlists
Add songs to playlists
Simulate playback using a queue (FIFO order)

-Song Recommendations

Graph-based recommendation system
Songs are connected by shared genres
Uses Breadth-First Search (BFS) to recommend similar songs

How to run Music Library Manager:

-Requirements
Python 3.8 or later
*This project ony uses Python;s built-in libraries: csv, collections, and time*

After requirements are fulfilled:
Download or clone the project folder
Make sure the data/songs.csv file exists(you could create your own, if not, one is already provided)
*Song data is simulated and used for educational purposes only.*
*Ratings and play counts are generated to demonstrate sorting and performance analysis*
Open a terminal in the project directory
Run the program:
python main.py


What is files are included:
*main.py
*song.py
*library.py
*sorting.py
*playlist.py
*recommendation.py
*data folder/songs.csv
*README.md
*complexity_analysis.md

Sample Outcome:

## 🧪 Sample Interaction

=== Smart Playlist Generator ===

Music library loaded: 35 songs

Main Menu:
1. Browse library
2. Search songs
3. Sort library
4. Create/edit playlist
5. Compare sorting performance
6. Exit

Choice: 3

Sort library by:
4. Rating

Choose sorting algorithm:
2. Merge Sort

Sorting 35 songs by rating using Merge Sort... Completed in 0.000X seconds.

Top 5 songs by rating:
"El Triste" - José José (Pop Latino / Balada Romántica) - 4.9★ [4:35]
...
