# Graph Representations
"""

Graphs are one of the most important and versatile data structures in computer science. 
Unlike trees, which have a hierarchical structure, graphs can represent any kind of connection between items.

Before we start, think about these real-world systems:

- How does Google Maps find the fastest route?
- How does Facebook suggest "People You May Know"?
- How do airline booking systems find flight connections?
All of these use graphs. Let's see how.
"""
# INTRODUCTION TO GRAPHS
"""
A graph is a data structure for representing connections among items.

A graph consists of:
- Vertices (nodes): Represent items
- Edges: Represent connections between two vertices
"""

"""
Example 1: Computer Network


    PC1 ━━━ Server1 ━━━ Server3
     ┃        ┃            ┃
     ┃      Server2 ━━━━━━━┫
     ┃        ┃
    PC2 ━━━━━━┛
5 vertices: PC1, PC2, Server1, Server2, Server3
6 edges: The connections between machines
"""

"""
Example 2: Social Network


    Maya ━━━ Jen ━━━ Thuy
      ┃
     Raj
4 vertices: Maya, Jen, Raj, Thuy
3 edges: The friendships
"""

"""
Key properties:
- A vertex can have multiple edges
- Each edge connects exactly two vertices
- With 4 vertices and at most one edge per pair: maximum 6 edges (formula: n(n-1)/2)
"""

#Adjacency, Paths, and Distance
"""
Adjacency: Two vertices are adjacent if connected by an edge.
- PC1 and Server1 are adjacent
- PC1 and Server3 are NOT adjacent

Path: A sequence of edges from a source vertex to a destination vertex.
- Path length: Number of edges in the path

Distance: The number of edges on the shortest path between two vertices.

    PC1 ━e2━ Server2 ━e5━ PC2
     ┃         ┃
     e1       e3
     ┃         ┃
   Server1 ━━━━┛

From PC1 to PC2:
- One path: e1, e3, e5 (length = 3)
- Shortest path: e2, e5 (length = 2)
- Distance = 2
"""
# Connected vs. Disconnected Graphs
"""
Connected graph: A path exists between every pair of vertices.
Disconnected graph: At least one pair of vertices has no path between them.

Connected:              Disconnected:
A━B━C━D                 A━B━C    D━E

In the disconnected graph, there's no path from A to D.
"""

# APPLICATIONS OF GRAPHS
"""
Let's see where graphs are used in real systems.

Application 1: Geographic Maps and Navigation
Navigation systems model maps as graphs:
- Vertices: Intersections and destinations
- Edges: Road segments
- Weights: Travel time or distance

          1min    5min     3min
    House ━━━━ A ━━━━ B ━━━━ Beach
                ┃      ┃
              10min   7min
                ┃      ┃
                C ━━━━ D
                  2min

The shortest path algorithm finds: House → A → B → Beach (total: 9 minutes)

Key insight: Edge weights can represent different things:
- Physical distance → shortest route
- Travel time with traffic → fastest route

Application 2: Flight Navigation
Airlines use graphs where:
- Vertices: Airports
- Edges: Direct flights
- Weights: Flight duration, cost, or other metrics

Important: This graph is dynamic:
- Weights change (delays, weather)
- Edges added/removed (flights scheduled/cancelled)

Application 3: Product Recommendations
E-commerce sites build product relationship graphs:

    Game1 ━━┓
    Game2 ━━╋━━ GameConsole ━━━ TV ━━━ BluRay
    Game3 ━━┛        ┃
                  Tablet

How it works:
- Customer buys: Game Console
- System recommends: Adjacent vertices (Game1, Game2, Game3, TV, Tablet)
- This is why Amazon shows "Frequently Bought Together."

Application 4: Social and Professional Networks
LinkedIn/Facebook use graphs:

- Vertices: People
- Edges: Connections (friendships or professional relationships)
- Use case: Finding connections

- Direct connections = distance 1
- Friends-of-friends = distance 2
- If Octavio wants to meet Wilford, the graph shows Manuel can introduce them
"""

# ADJACENCY LISTS
"""
Now: How do we store a graph in memory?

Adjacency List Representation
Concept: For each vertex, maintain a list of adjacent vertices.

Graph:                  Adjacency List:
A ━ B                   ┌───┬────────┐
┃   ┃                   │ A │ B, C   │
C ━ D                   │ B │ A, C, D│
 ╲ ╱                    │ C │ A, B   │
  ╳                     │ D │ B      │
                        └───┴────────┘
Critical observation: Each edge appears twice in the list.
Edge A-B creates: B in A's list, A in B's list

Space Complexity

Given:
- V vertices
- E edges
Space needed: O(V + E)

Why?
- Store V vertices
- Each edge creates 2 list entries
- Total ≈ V + 2E = O(V + E)

When to Use Adjacency Lists
Advantages:
- Space-efficient for sparse graphs (few edges relative to vertices)
- Easy to iterate through a vertex's neighbors

Disadvantages:
- Checking if two vertices are adjacent requires scanning a list (potentially slow)

Best for:
- Social networks (not everyone knows everyone)
- Computer networks
- Most real-world graphs (which tend to be sparse)
"""
# ADJACENCY MATRICES
"""
Adjacency Matrix Representation

Concept: A V × V matrix where element [i][j] is:
- 1 if edge exists from vertex i to j
- 0 otherwise

Graph:          Matrix:
A ━ B             A B C D
┃   ┃           ┌────────┐
C   D         A │0 1 1 0│
                B │1 0 0 1│
                C │1 0 0 0│
                D │0 1 0 0│
                  └────────┘

Properties:
- For undirected graphs: matrix is symmetric
- Diagonal typically all zeros (no self-loops)
- Each edge creates two 1's in the matrix

Space and Time Analysis
- Space: Always V² elements
1,000 vertices → 1,000,000 matrix elements
O(V²) space

- Time to check adjacency: O(1) - just look up matrix[i][j]

When to Use Adjacency Matrices
Advantages:
- Very fast adjacency checking
- Simple implementation

Disadvantages:
- Wastes space for sparse graphs (many zeros)
- O(V²) space regardless of edge count

Best for:
- Dense graphs (many edges)
- When frequent adjacency checks are needed
- Smaller graphs

Quick Comparison
Aspect	                Adjacency List	        Adjacency Matrix
Space	                     O(V + E)	                  O(V²)
Check adjacency	         O(V) worst case	         O(1)
Best for	                  Sparse graphs	         Dense graphs
Most common	               Yes	                   Less common

In practice: Most real-world graphs are sparse, so adjacency lists are more common.
"""

# BREADTH-FIRST SEARCH
"""
Traverse a graph - visit every vertex systematically.

BFS Concept
Breadth-First Search (BFS): Visits vertices in order of their distance from a starting vertex.

Think of it as exploring in layers:
- Visit starting vertex (distance 0)
- Visit all vertices at distance 1
- Visit all vertices at distance 2
- Continue...

Analogy: Finding friends-of-friends on social media
- Distance 1: Your friends
- Distance 2: Friends of your friends
- Distance 3: Friends of friends of friends

BFS Example
        A
       ╱ ╲
      B   D
     ╱ ╲
    E   F ━ C

Starting at A:
Distance 0: A Distance 1: B, D (neighbors of A) 
Distance 2: E, F (neighbors of B) 
Distance 3: C (neighbor of F)

BFS visit order: A, B, D, E, F, C
Note: Among same-distance vertices, order doesn't matter (could be A, D, B, E, F, C)
"""
# BFS Algorithm
"""
Data structures:
- Queue (frontierQueue): FIFO - first in, first out
- Set (discoveredSet): Tracks discovered vertices

Algorithm:
1. Enqueue starting vertex
2. Add starting vertex to discovered set
3. While queue not empty:
   a. Dequeue vertex (currentVertex)
   b. Visit currentVertex
   c. For each neighbor of currentVertex:
      - If not discovered:
        * Add to discovered set
        * Enqueue neighbor

Key terms:
- Discovered: When we first encounter a vertex
- Frontier: Vertices in the queue (discovered but not visited)
- Visited: Vertices we've dequeued and processed

BFS Applications
1. Shortest Path in Unweighted Graphs
- BFS naturally finds shortest distances
- Each vertex discovered at its minimum distance from start
2. Social Network Recommendations
- Distance 2 vertices = friends-of-friends
- Good candidates for "People You May Know"
3. Peer-to-Peer File Search
- Find closest computer with a file
- Minimizes network hops
Example: LinkedIn finds your distance-2 connections to suggest new contacts.
"""

# DEPTH-FIRST SEARCH
"""
DFS Concept
Depth-First Search (DFS): Explores as far as possible along each path before backtracking.

Analogy: Exploring a maze
- Choose a corridor, go as far as you can
- Hit a dead end? Backtrack to last junction
- Try a different path
- Repeat until all paths explored

Key difference from BFS:
- BFS explores breadth (layer by layer)
- DFS explores depth (one path at a time)

DFS Example
        A
       ╱ ╲
      B   D
     ╱ ╲
    E   F ━ C

Starting at A - one possible DFS order:
- Visit A
- Go to B (neighbor of A)
- Go to F (neighbor of B)
- Go to C (neighbor of F)
- Backtrack to F, then B, then A
- Go to D (other neighbor of A)
- DFS visit order: A, B, F, C, E, D

Important: DFS order is not unique - depends on which neighbor you choose first.
"""

# DFS Algorithm (Iterative)
"""
Data structures:
- Stack (vertexStack): LIFO - last in, first out
- Set (visitedSet): Tracks visited vertices

Algorithm:
1. Push starting vertex onto stack
2. While stack not empty:
   a. Pop vertex from stack (currentV)
   b. If currentV not visited:
      - Visit currentV
      - Add to visited set
      - Push all neighbors onto stack

Key difference from BFS: Uses stack instead of queue!
"""

# DFS Algorithm (Recursive)
"""
DFS can also be implemented recursively:
RecursiveDFS(currentV):
   If currentV not in visitedSet:
      Add currentV to visitedSet
      Visit currentV
      For each neighbor of currentV:
         RecursiveDFS(neighbor)
The recursive version uses the program call stack naturally.
"""

# BFS vs DFS Comparison
"""
Feature	                BFS	                                                    DFS
Data Structure	        Queue (FIFO)	                                        Stack/Recursion (LIFO)
Exploration	            Layer by layer	                                        Deep paths first
Shortest Path?	        Yes ✓	                                                No ✗
Use Cases	            Shortest paths, nearest neighbor, level-order	        Path exploration, cycle detection, topological sort

When to use which:
- Need shortest path? → BFS
- Need to explore all possibilities? → DFS
- Processing by distance/level? → BFS
- Backtracking problems? → DFS

"""
# KEY TAKEAWAYS
"""
Remember these points:
- Graphs model connections - they're everywhere in CS
- Choose your representation based on graph density
- BFS and DFS are fundamental building blocks
- BFS = breadth (layers), DFS = depth (paths)
"""

# QUICK PRACTICE QUESTIONS
"""
Question 1: If a graph has 5 vertices and 3 edges, is it guaranteed to be connected? 
Question 2: You need to find the shortest route between two cities. BFS or DFS? 
Question 3: An adjacency matrix for 100 vertices uses how much space? 
Question 4: In BFS, what data structure holds the frontier? 
Question 5: Can DFS visit vertices in multiple valid orders?
"""