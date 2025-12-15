COMPLEXITY ANALYSIS

## Data Structures Used

### Graph (Dictionary of Lists)
- Used to represent the campus map
- Keys represent buildings (nodes)
- Values represent connected buildings with distances (edges)
Reason:
Efficient adjacency lookup and easy traversal.

---

### Queue (deque)
- Used in BFS
Reason:
Ensures First-In-First-Out order required for level-by-level traversal.

---

### Priority Queue (Min-Heap)
- Used in Dijkstra’s algorithm
Reason:
Always selects the nearest unvisited node efficiently.

---

### Hash Maps (Python Dictionaries)
- Used for distance tracking, visited nodes, and previous nodes
Reason:
Provides constant-time lookup.

---

## Time Complexity Analysis

### Breadth-First Search (BFS)
- Visits each vertex and edge once  
- Time Complexity: 
  O(V + E)
  where V = number of buildings, E = number of paths

---

### Dijkstra’s Algorithm
- Uses a priority queue
- Each edge relaxation involves a heap operation
- Time Complexity:
  O((V + E) log V)

---

### Menu Operations
- Displaying menu and selecting options  
- O(1) per operation

---

## Space Complexity Analysis

### Graph Storage
- Stores all vertices and edges  
- O(V + E)

---

### BFS
- Queue and visited set  
- O(V)

---

### Dijkstra
- Distance dictionary, previous dictionary, priority queue  
- O(V)

---

## Trade-Offs and Design Decisions

- BFS is faster but does not consider distances  
- Dijkstra is slower but guarantees optimal paths  
- Estimated distances were used to focus on algorithmic concepts rather than geographic accuracy  
- A text-based interface was chosen for simplicity and clarity

---

## Conclusion
The system efficiently demonstrates how graph data structures and algorithms can be applied to real-world navigation problems.

---


