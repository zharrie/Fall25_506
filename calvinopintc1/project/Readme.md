# A Simple Playlist Generator™ 
## **CSIT 506 – Final Project**  
## **Authors:** *Vincent L. & Camila C.*
---

## Overview (What this project does)

**A Simple Playlist Generator™** is an interactive Python application that manages a music library, performs advanced searching and sorting operations, creates playlists, simulates playback, and recommends songs based on similarity. It aims to keeps its implementation simple, without resorting to external libraries.

This project demonstrates usage of:

- Hash maps  
- Trees (BST)  
- Graphs + BFS  
- Queues  
- Sorting algorithms (Quicksort, Merge Sort, BST inorder traversal)  
- Searching algorithms (Linear, and Binary lookup)

The system loads a library of 30 or more songs, either from a user-provided CSV or from a demo-generated CSV.

### Notable Features:

- Load a music library from CSV
- Hash maps for fast lookup by ID / artist / genre
- Sorting via Quicksort and Merge Sort
- BST-based sorting for rating and play count (inorder traversal)
- Graph-based song similarity + BFS recommendations
- Queue-based playlist playback simulation
- Linear and Binary searches
- Optional Verbose toggle for narrated execution

---

## Requirements (Dependencies)

- Recommended Python Version: 3.12.
- Standard Python Libraries used:
  - `csv`, 
  - `json`, 
  - `collections`, 
  - `time`

No external modules or dependencies necessary.

---

## Installation & Setup

1. Clone/download all files, and save to a folder.

2. Open a terminal or run main.py in a Python compatible IDE.

3. Start the program:

4. When prompted for a CSV file:

- Press Enter to auto-generate a demo CSV, or

- Enter the name of your CSV (must contain 30 or more songs and be located in same folder as main.py)

5. When prompted about verbose mode:

- Type y for verbose narration of script actions

- Type n for quiet mode

---
## Files

### .py files:

1. binarysearchtree.py
2. graph.py
3. main.py
4. models.py
5. queues.py
6. searching.py
7. sorting.py
8. verbose.py

### Can be generated:

1. demo_music_library.csv
2. playlists.json

### Documentation:

1. README.md
2. ComplexityAnalysis.md

Please ensure that you download from trusted mirrors and verify the checksums of your downloads to ensure their integrity and security. The authors will not be held responsible for any copies obtained from unauthorized or untrusted sources.

---
## List of Features Implemented

### Search
- Exact title search (linear + binary)
- Artist search (hash-based)
- Genre search (hash-based)
- Partial substring title search

### Sorting
Sort by:
- Title  
- Artist  
- Duration  
- Rating  
- Play count  

Using:
- Quicksort  
- Merge Sort  
- Binary Search Tree Inorder (Play count and rating, only)
- Binary Search Tree Reverse Inorder (Play count and rating, only)


### Playlists
- Create playlists  
- Add/remove songs  
- View playlists  
- Simulate playback using an ArrayQueue  
- Save/load playlists (playlists.json)

### Recommendations
- Graph of song similarities  
- Breadth-first Search (BFS) recommendation engine (depth ≤ 2)

### Performance Comparison
- Compare Quicksort vs Merge Sort  
- Compare Binary Search vs Linear Search

### Verbose Mode
- Narrated script execution for educational demonstration.

---

## Data Structures & Algorithms Used

### Data Structures
- Hash maps (`songs_by_id`, `songs_by_artist`, `songs_by_genre`)
- Binary Search Tree (rating sort)
- Graph (adjacency list)
- Array-based queue (playback simulation)
- Lists (sorting, searching)

### Algorithms
- Linear search  
- Binary search  
- Hash-based lookup  
- Quicksort  
- Merge sort  
- BST inorder traversal  
- BFS graph traversal

---

## Usage

### 1. Browse Library
Displays up to 20 songs sorted by title.

### 2. Search Songs
Options:
- Exact title (linear + binary search)
- Artist (hash lookup)
- Genre (hash lookup)
- Partial substring title search (linear)

### 3. Sort Library
Choose:
- Attribute: title, artist, duration, rating, play count
- Algorithm: Quicksort, Merge Sort, BST (Play count and rating, only)

Outputs:
- Sorted results
- Execution time

### 4. Playlist Manager
Create playlists, add/remove songs, inspect contents, simulate playback using a queue-based playback simulation.

### 5. Compare sorting performance
Compares Quicksort vs Merge Sort across multiple list sizes and prints timing for each.

### 6. Get Recommendations
Entering a song will cause the system uses a similarity graph and BFS to recommend similar songs (based on shared artist and genre).

### 7. Toggle Verbose Mode
Turn detailed internal script narration on or off at runtime. Please note: this may affect sorting times. 

---

## Example Inputs + Outputs

### Searching for song by partial string
  ```
    #### A Simple Playlist Generator™ Main Menu ####.

    1. Browse library
    2. Search songs
    3. Sort library
    4. Playlist Manager
    5. Compare sorting performance
    6. Get recommendations
    7. Toggle verbose mode on/off
    0. Exit

    Choice: 2

    Search by:

    1. Exact title
    2. Artist
    3. Genre
    4. Partial title (substring)

    Select: 4
    Substring: of
    [VERBOSE] Starting PARTIAL TITLE substring search for 'of'.
    [VERBOSE] Linear search completed with 30 comparisons and 2 match(es).
    [VERBOSE] Partial title search completed with 30 comparisons and 2 match(es).
      "Shape of You" | Ed Sheeran (Pop) | 4.4★ | [3:53]
      "All of Me" | John Legend (R&B) | 4.5★ | [4:29]
  ```

  ### Toggling off verbose, getting song recommendations
  ```
    Choice: 7

    Verbose mode is now OFF.

    #### A Simple Playlist Generator™ Main Menu ####.

    1. Browse library
    2. Search songs
    3. Sort library
    4. Playlist Manager
    5. Compare sorting performance
    6. Get recommendations
    7. Toggle verbose mode on/off
    0. Exit

    Choice: 6

    Full song title for recommendations: Zombie

    Recommended songs:
    "Bohemian Rhapsody" | Queen (Rock) | 5.0★ | [6:07]
    "Hotel California" | Eagles (Rock) | 4.8★ | [6:30]
    "Smells Like Teen Spirit" | Nirvana (Rock) | 4.7★ | [5:01]
    "Good Vibrations" | The Beach Boys (Rock) | 4.5★ | [3:36]
    "Hey Jude" | The Beatles (Rock) | 4.9★ | [7:11]
  ```

  ### Sorting library by rating, using Binary Search Tree Inorder
  ```
    #### A Simple Playlist Generator™ Main Menu ####.

    1. Browse library
    2. Search songs
    3. Sort library
    4. Playlist Manager
    5. Compare sorting performance
    6. Get recommendations
    7. Toggle verbose mode on/off
    0. Exit

    Choice: 3

    Sort library by:

    1. Title (A-Z)
    2. Artist
    3. Duration
    4. Rating
    5. Play count

    Select: 4

    Choose sorting algorithm:

    1. Quicksort
    2. Merge Sort
    3. Binary Search Tree Inorder (rating or play count least to greatest)
    4. Binary Search Tree Reverse Inorder (rating or play count greatest to least)

    Select: 3

    Sorting 30 songs by rating using Binary Search Tree Inorder (by rating) took 0.000212 seconds.

    Top 10 songs by rating:

    "Radioactive" | Imagine Dragons (Rock) | 4.4★ | [3:06] - Times Played: 190
    "Shape of You" | Ed Sheeran (Pop) | 4.4★ | [3:53] - Times Played: 230
    "All of Me" | John Legend (R&B) | 4.5★ | [4:29] - Times Played: 160
    "Believer" | Imagine Dragons (Rock) | 4.5★ | [3:24] - Times Played: 205
    "Good Vibrations" | The Beach Boys (Rock) | 4.5★ | [3:36] - Times Played: 65
    "Smooth" | Santana (Rock) | 4.5★ | [4:58] - Times Played: 85
    "Take On Me" | A-ha (Pop) | 4.5★ | [3:45] - Times Played: 175
    "Viva La Vida" | Coldplay (Pop) | 4.5★ | [4:02] - Times Played: 210
    "Halo" | Beyonce (Pop) | 4.6★ | [4:21] - Times Played: 170
    "Numb" | Linkin Park (Rock) | 4.6★ | [3:05] - Times Played: 220
  ```
---

## Known Limitations
- Enabling verbose mode may increase the amount of time searches and comparisons will take.

---

## License
MIT License

Copyright (c) 2025 *Vincent L. & Camila C.*

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.