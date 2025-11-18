## Project 1: Campus Navigation System

### Description
Build a route-finding system for a campus or city map. Users can find the shortest path between locations, view all reachable destinations, and compare different pathfinding algorithms.

### Objectives
- Implement and understand graph data structures
- Apply shortest path algorithms
- Analyze algorithm performance
- Work with weighted graphs

### Required Data Structures
- Directed Graph: Represent locations (nodes) and paths (edges with weights)
- Priority Queue (Heap): For shortest path algorithm implementation
- Hash Map: Quick location lookup and storing location information

### Required Algorithms
- Dijkstra's Algorithm for shortest path
- BFS for finding all reachable locations

### Minimum Required Features
- Load Map Data
    - From file or hard-coded structure
    - Minimum 15 locations, 25 paths with distances/times
    - Shortest Path Finding

- Find path between any two locations
    - Display the route
    - Show total distance/time
    - Reachability

- Show all locations reachable from a starting point
    - Optionally within a distance limit

- Algorithm Comparison
    - Compare performance of 2 different pathfinding approaches
    - Display metrics (time, nodes explored, etc.)


## Sample Interaction
=== Campus Navigation System ===

Available locations:
1. Library
2. Student Center
3. Engineering Building
4. Science Hall
5. Dormitory A
... (15 total)

- Enter start location: Library
- Enter destination: Engineering Building

- Finding shortest path...
    - Shortest Path:
        - Library → Science Hall → Engineering Building

- Total distance: 450 meters
- Estimated time: 6 minutes
- Nodes explored: 8

Would you like to:
1. Find another route
2. Compare with BFS
4. Exit

Choice: 2
- Comparing Dijkstra's vs BFS:
    - Dijkstra's: 450m, 0.002s, optimal
    - BFS: 450m, 0.001s, optimal
    - Both found same optimal path.
