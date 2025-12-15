Complexity Analysis

Project: Music Library Manager
By: Anais Moreno

1. Data Structures Used

The Music Library Manager uses multiple data structures to support efficient searching, sorting, playlist management, and recommendations.

Hash maps (Python dictionaries) are used to index songs by artist and genre. These structures allow fast retrieval of songs when performing exact searches and avoid scanning the entire library. A list is used to store all songs in insertion order, which allows efficient iteration and sorting using different algorithms. A queue, implemented using collections. Deque, is used to simulate playlist playback in a First-In, First-Out manner. Finally, a graph is used to represent song similarity for the recommendation system, where songs are nodes and shared genres create edges.

2. Time Complexity Analysis
-Searching Operations

Searching by title uses a linear search over the list of all songs to support partial and substring matching. This operation runs in *O(n)* time, where n is the number of songs in the library.

Searching by artist and genre uses hash map lookups. Because artists and genres are stored as dictionary keys, these searches run in *O(1)* average time.

-Sorting Operations

The project implements two sorting algorithms to allow comparison.

*Quick Sort* has an average-case time complexity of *O(n log n)* and a worst-case time complexity of *O(n²)*.

*Merge Sort* runs in *O(n log n)* time in all cases.

Both algorithms are used to sort songs by different attributes such as title, duration, rating, and play count.

-Playlist Playback

Playlist playback iterates through the queue once to display songs in order. This operation runs in *O(n)* time, where n is the number of songs in the playlist.

-Recommendation System

The recommendation system uses a graph traversal algorithm. Breadth-First Search (BFS) is used to traverse the graph and recommend similar songs. BFS runs in *O(V + E)* time, where V is the number of songs and E is the number of similarity connections.

Building the recommendation graph requires comparing songs by genre, which has a worst-case time complexity of *O(n²)*. 

-Menu Loop

The main menu runs in a loop that processes user input. Each iteration runs in constant time, while the overall time complexity depends on which operation the user selects.

3. Space Complexity Analysis

Song storage requires *O(n)* space, as each song object is stored in memory. 

Hash maps also require *O(n)* space since songs are indexed by artist and genre. Sorting algorithms require additional memory: Quick Sort uses *O(log n)* space for recursion, while Merge Sort uses *O(n)* extra space for temporary arrays.

The recommendation graph requires *O(V + E)* space to store nodes and edges. The playlist queue requires *O(n)* space for the songs it contains.

4. Algorithm Comparison
-Quick Sort vs Merge Sort

Quick Sort and Merge Sort both have average time complexity of *O(n log n)*. However, Quick Sort can degrade to *O(n²)* in the worst case, while Merge Sort guarantees O(n log n) performance. Quick Sort uses less extra memory, while Merge Sort requires additional space but provides stable and predictable performance.

-Linear Search vs Hash-Based Search

Linear search is used for substring matching and requires O(n) time. Hash-based search provides *O(1)* average time for exact matches but requires additional memory and preprocessing.

5. Trade-offs and Design Decisions

Using both lists and hash maps allows the program to efficiently support sorting and fast searching. A queue was chosen for playlists because playback order matters and FIFO behavior models real-world playlists. Breadth-First Search was selected over Depth-First Search for recommendations because BFS returns the most closely related songs first, improving recommendation relevance.

6. Summary

This project demonstrates the practical use of multiple data structures and algorithms working together in a realistic application. Hash maps enable fast searches, lists support sorting, queues simulate playlists, and graphs power recommendations. By implementing and comparing sorting algorithms and analyzing their complexity, the project highlights how algorithm choices affect performance and design.