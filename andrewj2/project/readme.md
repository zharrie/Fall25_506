# Social Network Analyzer (Final Project, CSIT506 Fall '25)

### Author
Jasper Andrew

### Description
This tool analyzes a social network graph to find connections, identify communities, and discover influential users.

### Usage
`python3 main.py <CSV-PATH>`, e.g. `python3 main.py network-small.csv`  
The program's textual menus are simple, just type the option you want and press `Enter` to submit.

### Features
- Search users by name (substring) or number of connections
- Display user information
- Find connection paths between users
- List all users within N degrees of connectivity
- Find mutual connections between users
- Suggest new connections based on mutual friendships
- Display statistics about the network
- Choose between BFS/Dijkstra or Floyd-Warshall algorithms (Note: FW is very bad on large graphs)

### Dependencies
- Python 3+

### Sample Interaction
```
❯ py main.py network-small.csv

=== Social Network Analyzer ===

> Network load: Success

[MAIN MENU]
  [q] Exit program
  [w] Print current menu
  [1] Options
  [2] Users
  [3] Statistics
>> 2
[USERS MENU]
  [q] Previous menu
  [w] Print current menu
  [1] Search users
  [2] Select user
  [3] Display current user
  [4] Connection path
  [5] Users within N degrees
  [6] Mutual friends
  [7] Friend suggestions
>> 2
> No user selected
Enter user ID>> 1
> Current user: 1: Izayah Chen (9 friends)
>> 7
> Friend suggestions for Izayah Chen:
> 	70: Yael Irwin (11 friends, 3 mutual friends)
> 	66: Leon Sharp (10 friends, 3 mutual friends)
> 	52: Addison Ibarra (10 friends, 2 mutual friends)
> 	62: Janiyah Chavez (8 friends, 2 mutual friends)
> 	72: Madelyn Hill (8 friends, 2 mutual friends)
> 	04: Kamari Wang (7 friends, 2 mutual friends)
> 	78: Ricky Newman (7 friends, 2 mutual friends)
> 	15: Kasey Zhang (6 friends, 2 mutual friends)
> 	34: Devan Grimes (6 friends, 2 mutual friends)
> 	32: Alejandro Montoya (3 friends, 2 mutual friends)
>> 2
```

### Analysis

#### Data Structures
- `User` class:
   - Friend List (`set`): Stores the IDs of a user's connections (effectively an adjacency list).
- `Network` class:
   - User Map (`dict`): Stores the user objects (vertices) as values, with their IDs as keys.
- Breadth-First Search:
   - Frontier Queues (`list`): Keeps track of vertices that have been discovered, but not visited. I have two frontier queues so that I can go one level of depth at a time, and stop after any given depth level for efficiency.
   - Discovered Set (`set`): Keeps track of vertices that have been discovered, so that it is not enqueued twice.
- Depth-First Search:
   - Vertex Stack (`list`): Keeps track of vertices that need to be processed.
   - Visited Set (`set`): Keeps track of vertices that have been visited.
- Dijkstra Shortest Path:
   - Unvisited Set (`list`): Keeps track of vertices that need to be processed. Implemented as a `list` because of `pop(i)` functionality.
   - Distance/Predecessor Map (`dict`): Keeps track of distances and predecessors for each vertex.
- Floyd-Warshall All Pairs Shortest Path:
   - Distance Matrix (`list[list]`): A matrix containing the distance between every pair of vertices.

#### Complexity
| Algorithm                              | Time Complexity | Space Complexity |
|----------------------------------------|-----------------|------------------|
| Breadth-First Search                   | O(V+E)          | O(V)             |
| Depth-First Search                     | O(V+E)          | O(V)             |
| Dijkstra Shortest Path                 | O(V²)           | O(V)             |
| Floyd-Warshall All Pairs Shortest Path | O(V³)           | O(V²)            |

#### Comparison/Trade-Offs: Dijkstra and Floyd-Warshall
I wanted to use the all-pairs distance matrix, since it the data in this project is static and I would only have to generate the matrix once. In theory it's a good idea, and if this were a program with a lot of static data, and I was going to do a very high number of operations on the data, it might be more efficient in the long run to generate the matrix ahead of time. However, even with only a couple thousand vertices, my implementation of the Floyd-Warshall algorithm took over an hour to complete, making it not very practical for this scenario. Also, if the data were being dynamically updated, the distance matrix would be out of date and require maintenance, which might make it less efficient overall, depending on how costly it would be to update the matrix. I switched to using primarily Dijkstra's shortest path algorithm and breadth-first search, which need to be repeated each time, but are much more efficient in the short term. However, the program still has the option to use Floyd-Warshall, just for fun.