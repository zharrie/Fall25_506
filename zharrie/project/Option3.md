## Project 3: Smart Playlist Generator

### Description
Build a music library manager that can organize songs, create playlists, play music (simulate), and recommend songs based on similarity.

### Objectives
- Work with multiple data structures simultaneously
- Compare searching algorithms
- Analyze sorting algorithm performance
- Implement recommendation systems using graphs

### Required Data Structures
- Hash Map: Song storage by ID, artist index, genre index
- Binary Search Tree OR Heap: Sorting by different attributes
- Graph: Song similarity for recommendations
- Queue: Playlist playback simulation

### Required Algorithms
- Multiple Sorting Algorithms (Quick Sort, Merge Sort - compare performance)
- Search Algorithms (linear search, binary search, hash-based lookup)
- Graph Traversal for recommendations

### Minimum Required Features

- Library Management
    - Load library from file (minimum 30 songs)
    - Display library with formatting

- Search Functionality
    - Search by: exact title, artist, genre
    - Partial matching (substring search)

- Sorting Capabilities
    - Sort library by: title, artist, duration, rating, play count
    - Implement at least 2 different sorting algorithms

- Playlist Creation
    - Create playlist with selected songs
    - Add/remove songs from playlist
    - Save/load playlists

- Performance Comparison
    - Compare sorting algorithm performance
    - Show execution times for different input sizes

### Sample Interaction
=== Smart Playlist Generator ===

Music library loaded: 32 songs

Main Menu:
1. Browse library
2. Search songs
3. Sort library
4. Create/edit playlist
5. Compare sorting performance
6. Exit

Choice: 3

Sort library by:
1. Title (A-Z)
2. Artist
3. Duration
4. Rating
5. Play count

Select: 4

Choose sorting algorithm:
1. Quick Sort
2. Merge Sort

Select: 2

Sorting 32 songs by rating using Merge Sort...
Completed in 0.0023 seconds.

Top 5 songs by rating:
1. "Bohemian Rhapsody" - Queen (Rock) - 5.0★ [6:07]
2. "Imagine" - John Lennon (Pop) - 4.9★ [3:15]
3. "Hotel California" - Eagles (Rock) - 4.8★ [6:30]
4. "Billie Jean" - Michael Jackson (Pop) - 4.8★ [4:54]
5. "Smells Like Teen Spirit" - Nirvana (Rock) - 4.7★ [5:01]

Choice: 4

Playlist Manager:
1. New playlist
2. Add songs
3. Remove songs
4. View playlist

Select: 1

Playlist name: Rock Classics

Select: 2

Enter song titles (one per line, 'done' to finish):
> Bohemian Rhapsody
Added: "Bohemian Rhapsody" - Queen
> Hotel California
Added: "Hotel California" - Eagles
> done

Playlist "Rock Classics" now has 2 songs (12:37 total)

Select: 3

Playback Queue:
→ "Bohemian Rhapsody" - Queen [6:07] (now playing)
  "Hotel California" - Eagles [6:30]