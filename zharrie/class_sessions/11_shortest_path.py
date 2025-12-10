# shortes Path
"""
Let's recall from last week, we talked about graphs.
A graph was a set of vertices (also called nodes) and edges between them. 
Thinking of vertices as cities or intersections, and edges as roads connecting them.

Often each edge has a weight:
- It might be a distance in kilometers.
- Or a travel time in minutes.
- Or a cost in dollars.

With such a weighted graph, there are several natural questions:
- Single‑source shortest path:
    If I pick one starting vertex, what is the shortest path from that start to every other vertex?
- Minimum spanning tree:
    How can I connect all vertices with edges so that:
    - Everything is connected (you can get from any vertex to any other), but the total cost (sum of weights) of all chosen edges is as small as possible?
- All‑pairs shortest path:
    What is the shortest path between every pair of vertices in the graph?


Tonight we are going to see algorithms that solve each of these problems:
- Dijkstra and Bellman–Ford solve the single‑source shortest path problem.
- Floyd–Warshall solves the all‑pairs shortest path problem.
- Kruskal solves the minimum spanning tree problem.

As we go, pay attention to:
- What problem each algorithm solves,
- What information each algorithm stores (distance, predecessor, sets, or matrix),
- And what limitations it has (especially regarding negative edge weights).
"""

# Dijkstra’s shortest path algorithm
"""
Dijkstra’s algorithm answers this question:
Given a start vertex, how do we find the shortest path from that start to all other vertices, assuming all edge weights are non‑negative?

Picture this: you stand at your home (the start vertex) in a city map. 
Initially, you only know the distance from home to itself: 0. 
You don’t know yet how far other intersections are, so we consider their distance as ‘infinity’ — meaning ‘no known path yet’.
The algorithm behaves like this:
- At any point, some vertices have tentative distances (our current best guesses).
- In each step, we choose the unvisited vertex with the smallest tentative distance — that one is the next we will “finalize”.
- From that vertex, we look at all roads (edges) leading out, and see if going through this vertex gives a shorter path to its neighbors.
- If it does, we update the neighbor’s distance and remember that to reach that neighbor, we should come from this vertex.
- We repeat this until all vertices are processed.

A key idea:
Because all edge weights are non‑negative, once a vertex is chosen as the current smallest‑distance vertex, its distance cannot be improved later. 
That makes Dijkstra’s algorithm correct under non‑negative weights, and also efficient.
"""
#The data we keep: distance and predecessor
"""
To make this work in code, for each vertex we store:
- distance: the best known distance from the start vertex to this vertex.
- pred_vertex: which vertex comes just before this vertex on the best path.

At the beginning:
- Every vertex has distance = infinity and pred_vertex = None.
- Only the start vertex has distance = 0 (it’s 0 away from itself).
- We also keep a set or list of unvisited vertices: vertices we have not finalized yet.


Walking through the algorithm (step by step)
Initialization
For all vertices:
Set distance = infinity
Set pred_vertex = None
For the start vertex:
Set distance = 0
Put all vertices into an unvisited list.

Main loop
While there are still vertices in the unvisited list:
Choose the vertex in unvisited that has the smallest distance. Call it current.
Remove current from unvisited. From now on, its distance is final.
For each neighbor adj of current:
Compute alternative = current.distance + weight(current, adj)
If alternative is smaller than adj.distance, then we have found a better path to adj:
Set adj.distance = alternative
Set adj.pred_vertex = current

End result
For every vertex, distance is the length of the shortest path from the start.
By following pred_vertex pointers backwards, we can reconstruct the path.
This update step (“if alternative < adj.distance, then update”) is often called relaxing an edge: we’re trying to “relax” or reduce the current distance if possible.
"""
# Python Implementation 
class Vertex:
    # Constructor for a new Vertex object. All vertex objects
    # start with a distance of positive infinity.
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None

"""
label is just the name of the vertex (like “A” or “B”).
distance starts as infinity, meaning “we don’t know a path yet”.
pred_vertex starts as None, meaning “we don’t know where we came from”.
"""
def dijkstra_shortest_path(g, start_vertex):
    # Put all vertices in an unvisited queue.
    unvisited_queue = []
    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)

    # start_vertex has a distance of 0 from itself
    start_vertex.distance = 0

    # Repeat until unvisited_queue is empty
    while len(unvisited_queue) > 0:
        
        # Visit vertex with minimum distance from start_vertex
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)

        # Check possible paths from current_vertex to all neighbors
        for adj_vertex in g.adjacency_list[current_vertex]:
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
            alternative_path_distance = current_vertex.distance + edge_weight
                  
            # If shorter path from start_vertex to adj_vertex is found,
            # update adj_vertex's distance and predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex
"""
The unvisited_queue is our list of vertices we still need to process.
The for loop that finds smallest_index is where we select the vertex with the smallest tentative distance.
current_vertex is the vertex we just selected; we consider its neighbors.
For each neighbor, we compute a possible new distance through current_vertex. If it’s better, we update the neighbor’s distance and pred_vertex.
"""

#Reconstructing the shortest path
"""
Once Dijkstra has run, we have the pred_vertex field set so that each vertex know who its predecessor is on the best path from the start.
To build the path from the start to some end_vertex, we walk backwards from end_vertex to start_vertex using these predecessor pointers.
"""
def get_shortest_path(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ''
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = ' -> ' + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path
"""
Start at the end_vertex.
While we haven’t reached the start yet:
Add the current vertex’s label at the front of the path string.
Move current_vertex to its predecessor.
Finally, add the start vertex’s label in front.
"""

# Example
"""
Suppose the path is A → C → D → F.
pred_vertex of F is D, of D is C, of C is A.
This function would walk F → D → C → A and build the string "A -> C -> D -> F".
"""

# Important limitation: no negative weights
"""
Dijkstra assumes all edge weights are non‑negative.
If there is a negative edge, Dijkstra’s choice of “current smallest distance vertex” might be wrong, because a later negative edge could dramatically lower a distance that we think is final.
That is exactly why we need another algorithm, Bellman–Ford, for graphs with negative edge weights.
"""

# Bellman–Ford shortest path algorithm
"""
Why we need Bellman–Ford
Bellman–Ford solves the same problem as Dijkstra:
Find the shortest paths from a single start vertex to all other vertices.

The difference is:
- Bellman–Ford allows negative edge weights.
- It can also detect negative weight cycles — situations where you can keep going around a cycle and keep decreasing the total cost, so a ‘shortest’ path doesn’t exist.
- The trade‑off is that Bellman–Ford is generally slower than Dijkstra, because it does more work: it repeatedly scans all edges.”

Core idea
The idea is based on a very simple observation:
- If you had only paths with 1 edge, you’d consider all edges once to find the best distance for each vertex.
- If you allow 2 edges, you can improve some of those distances by going through intermediate vertices.
- If you allow 3 edges, you might improve further, and so on.
- In a graph with V vertices, any shortest simple path (no repeated vertices) can have at most V − 1 edges. 
So if we relax all edges V − 1 times, we’re guaranteed to have found all shortest paths, as long as there is no negative cycle.

We again keep for each vertex:
- distance from start (initially infinity),
- pred_vertex (initially None).

Bellman–Ford algorithm
Initialization
For every vertex currentV in the graph:
Set currentV.distance = infinity
Set currentV.pred_vertex = None
Set startV.distance = 0.

Main relaxation loop (V − 1 times)
Repeat the following V − 1 times:
For each vertex currentV in the graph:
For each adjacent vertex adjV (meaning there is an edge from currentV to adjV):
Let edgeWeight be the weight of the edge from currentV to adjV.
Compute alternative = currentV.distance + edgeWeight.
If alternative < adjV.distance:
Set adjV.distance = alternative.
Set adjV.pred_vertex = currentV.
This is just like Dijkstra’s “relaxation” step, but instead of choosing a best vertex and expanding neighbors, here we blindly relax every edge, and we do this V − 1 times.

Negative cycle check
After V − 1 iterations, we do one more pass over all edges.
If we can still reduce any distance, that means there is a negative cycle, because the only way to keep reducing distances beyond V − 1 relaxations is by going around a cycle.
In that case, we report that a negative cycle exists and we can’t define a single shortest path.
"""

# Python Implementation
def bellman_ford(graph, start_vertex):
    # Initialize all vertex distances to infinity and
    # and predecessor vertices to None.
    for current_vertex in graph.adjacency_list:
        current_vertex.distance = float('inf') # Infinity
        current_vertex.pred_vertex = None

    # start_vertex has a distance of 0 from itself
    start_vertex.distance = 0

    # Main loop is executed |V|-1 times to guarantee minimum distances.
    for i in range(len(graph.adjacency_list)-1):
        for current_vertex in graph.adjacency_list:
            for adj_vertex in graph.adjacency_list[current_vertex]:
                edge_weight = graph.edge_weights[(current_vertex, adj_vertex)]
                alternative_path_distance = current_vertex.distance + edge_weight

                # If shorter path from start_vertex to adj_vertex is found,
                # update adj_vertex's distance and predecessor
                if alternative_path_distance < adj_vertex.distance:
                   adj_vertex.distance = alternative_path_distance
                   adj_vertex.pred_vertex = current_vertex

    # Check for a negative edge weight cycle
    for current_vertex in graph.adjacency_list:
        for adj_vertex in graph.adjacency_list[current_vertex]:
            edge_weight = graph.edge_weights[(current_vertex, adj_vertex)]
            alternative_path_distance = current_vertex.distance + edge_weight

             # If shorter path from start_vertex to adj_vertex is still found,
             # a negative edge weight cycle exists
            if alternative_path_distance < adj_vertex.distance:
                return False

    return True
"""
First part: initialization (same idea as Dijkstra).
Middle part: for i in range(len(graph.adjacency_list)-1) is the V − 1 main iterations, each going over all edges and relaxing them.
Last part: additional pass over edges to detect if any distance can still be improved → negative cycle exists.
Path reconstruction is the same idea as in Dijkstra: follow pred_vertex backwards from the destination to the start.
"""
# Minimum Spanning Tree: Kruskal’s algorithm
"""
Clarifying the problem: MST vs shortest path

It’s important to separate shortest path from minimum spanning tree.

Shortest path:
We usually care about one start and one end. We want the cheapest route between them.

Minimum spanning tree (MST): We have an undirected, connected, weighted graph.
We want to choose some edges so that:
- All vertices are connected,
- There are no cycles (it’s a tree),
- The total sum of the chosen edges’ weights is as small as possible.

Think of designing a network:
- You want to connect all cities with cables or roads.
- You don’t care about the exact shortest route between every pair; you only care that every city is reachable and that the total construction cost is minimal.
That’s what an MST gives you.

Intuition behind Kruskal’s algorithm
Kruskal’s algorithm builds the MST in a greedy way:
- Consider all edges sorted by weight from smallest to largest.
- Start with no edges chosen and every vertex isolated.
- Repeatedly add the cheapest edge that:
- Connects two vertices that were previously in different groups,
- And therefore does not create a cycle.
- Stop when all vertices are in one connected group.
To efficiently keep track of which vertices are connected together, we use a structure that manages disjoint sets of vertices. 
At the start, each vertex is its own set. When we add an edge between two sets, we merge those sets.

The helper classes
EdgeWeight
EdgeWeight is a simple object that stores:
- a from_vertex,
- a to_vertex,
- and a weight.
It also defines comparison operators so we can put it into a priority queue (min‑heap) and always get the smallest weight edge first.

VertexSetCollection
This class maintains a collection of sets of vertices:
- Each set represents a connected component (a group of vertices that are already connected by chosen edges).
- vertex_map is a dictionary mapping each vertex to the set containing it.
- get_set(v) returns the set that contains vertex v.
- merge(set1, set2) combines two sets when we add an edge connecting these two components.
As we add edges, we gradually merge sets until all vertices are in a single set.
"""

#Kruskal’s algorithm
def minimum_spanning_tree(graph):
    # edge_list starts as a list of all edges from the graph
    edge_list = []
    for edge in graph.edge_weights:
        edge_weight = EdgeWeight(edge[0], edge[1], graph.edge_weights[edge])
        edge_list.append(edge_weight)
    # Turn edge_list into a priority queue (min heap)
    heapq.heapify(edge_list)

    # Initialize the collection of vertex sets
    vertex_sets = VertexSetCollection(graph.adjacency_list)

    # result_list is initially an empty list
    result_list = []

    while len(vertex_sets) > 1 and len(edge_list) > 0:
        # Remove edge with minimum weight from edge_list
        next_edge = heapq.heappop(edge_list)
        
        # set1 = set in vertex_sets containing next_edge's 'from' vertex
        set1 = vertex_sets.get_set(next_edge.from_vertex)
        # set2 = set in vertex_sets containing next_edge's 'to' vertex
        set2 = vertex_sets.get_set(next_edge.to_vertex)
        
        # If the 2 sets are distinct, then merge
        if set1 is not set2:
            # Add next_edge to result_list
            result_list.append(next_edge)
            # Merge the two sets within the collection
            vertex_sets.merge(set1, set2)

    return result_list
"""
edge_list contains all edges; heapq.heapify turns it into a priority queue where heappop returns the smallest weight edge.
vertex_sets starts with each vertex in its own set.
In the while loop:
We repeatedly take the cheapest remaining edge.
We check whether its two endpoints are in different sets.
If yes: adding this edge will connect two separate components, so we accept it and merge the sets.
If no: the edge would create a cycle inside an existing component, so we skip it.
At the end, result_list is the set of edges forming the minimum spanning tree.
"""

# All‑pairs shortest path: Floyd–Warshall
"""
The all‑pairs view and the distance matrix
So far, we’ve focused on shortest paths from one chosen start vertex.

Sometimes we want something stronger:
What are the shortest path lengths between every pair of vertices in the graph?

A natural way to represent this is with a matrix:
- If there are V vertices, we have a V × V matrix dist_matrix.
- Row i, column j stores the shortest distance from vertex i to vertex j.

The Floyd–Warshall algorithm computes this entire matrix. It can handle:
-negative edge weights, but not negative cycles (if there is a negative cycle, some shortest paths don’t exist because you can keep looping and making the path cheaper).

Initialization of the matrix
Before we run the main algorithm, we build the initial dist_matrix:
For all i and j, set dist_matrix[i][j] = infinity – we start by assuming no paths.
For every vertex i, set dist_matrix[i][i] = 0 – the distance from a vertex to itself is 0.
For every edge from vertex u to vertex v with weight w, set dist_matrix[index(u)][index(v)] = w – we know at least the one‑edge paths.
This matrix now represents the shortest path lengths if we only allow paths of at most one edge (direct edges).

The main Floyd–Warshall idea
The core idea is:
Gradually allow paths that are allowed to go through more and more possible intermediate vertices, and update the distances when we find shorter ones.
We consider vertices in some order: 0, 1, 2, …, V−1. For each vertex k in that order, we ask:

‘Suppose we are allowed to use vertex k as an intermediate stop on the path from i to j. 
Does going i -> k -> j give us a shorter distance than our current dist_matrix[i][j]?’

For each triple of indices (i, j, k):
currentLength = dist_matrix[i][j] (current best known distance from i to j),
possibleLength = dist_matrix[i][k] + dist_matrix[k][j] (distance if we go via k).
If possibleLength < currentLength, we update dist_matrix[i][j].
By the time we have processed all possible k, we will have the shortest path distances between all pairs.
"""

# Python Implementation
def all_pairs_shortest_path(graph):
    vertices = graph.get_vertex_list()
    num_vertices = len(vertices)

    # Initialize dist_matrix to a num_vertices x num_vertices matrix 
    # with all values set to infinity
    dist_matrix = []
    for i in range(0, num_vertices):
        dist_matrix.append([float("inf")] * num_vertices)

    # Set each distance for vertex to same vertex to 0
    for i in range(0, num_vertices):
        dist_matrix[i][i] = 0

    # Finish matrix initialization
    for edge in graph.edge_weights:
        dist_matrix[vertices.index(edge[0])][vertices.index(edge[1])] = graph.edge_weights[edge]

    # Loop through vertices
    for k in range(0, num_vertices):
        for toIndex in range(0, num_vertices):
            for fromIndex in range(0, num_vertices):
                currentLength = dist_matrix[fromIndex][toIndex]
                possibleLength = dist_matrix[fromIndex][k] + dist_matrix[k][toIndex]
                if possibleLength < currentLength:
                    dist_matrix[fromIndex][toIndex] = possibleLength

    return dist_matrix
"""
vertices = graph.get_vertex_list() gives us a consistent order of vertices; we use their indices in the matrix.
The first loops build the initial matrix as described (infinity everywhere, 0 on the diagonal, direct edges set to their weight).
The triple nested loops implement the main Floyd–Warshall logic:
Outer loop: choose allowed intermediate vertex k.
Inner loops: check all fromIndex and toIndex.
If routing via k is better, update the entry.
"""
# Reconstructing a specific path from the matrix
"""
The dist_matrix from Floyd–Warshall tells us how long the shortest paths are, but not which edges they use.

To reconstruct a specific path from start_vertex to end_vertex, we can work backwards:
Start at end_vertex.
Look at all edges that enter the current vertex (incoming_edges).
Among these, find an edge u -> current such that:
dist(start, current) = dist(start, u) + weight(u, current)
That means u is the vertex before current on some shortest path.
Move to u, add this edge to the beginning of the path.
Repeat until you reach the start vertex.
"""
# reconstruct path
def reconstruct_path(graph, start_vertex, end_vertex, dist_matrix):
    vertices = graph.get_vertex_list()
    start_index = vertices.index(start_vertex)
    path = []
    
    # Backtrack from the ending vertex
    current_index = vertices.index(end_vertex)
    while current_index != start_index:
        incoming_edges = graph.get_incoming_edges(vertices[current_index])
        
        found_next = False
        for current_edge in incoming_edges:
            expected = dist_matrix[start_index][current_index] - graph.edge_weights[current_edge]
            actual = dist_matrix[start_index][vertices.index(current_edge[0])]
            if expected == actual:
                # Update current vertex index
                current_index = vertices.index(current_edge[0])
                
                # Prepend current_edge to path
                path = [current_edge] + path
                
                # The next vertex in the path was found
                found_next = True
                
                # The correct incoming edge was found, so break the inner loop
                break

        if found_next == False:
            return None # no path exists

    return path

"""
graph.edge_weights[current_edge] is the weight of the candidate last edge.
If the shortest distance from start to current minus that weight equals the distance from start to current_edge[0], then this edge is consistent with the shortest path.
If no such edge is found at some step, that means no path exists.
"""

# Summary: when to use which algorithm
"""
Dijkstra’s algorithm
Problem: shortest paths from one start vertex to all others.
Requirement: no negative edge weights.
Strategy: repeatedly choose the closest unvisited vertex and relax its outgoing edges.
Data per vertex: distance, pred_vertex.

Bellman–Ford
Problem: same as Dijkstra (single‑source shortest paths).
Allows negative weights and detects negative cycles.
Strategy: relax all edges V − 1 times, then check once more for negative cycles.
Data per vertex: distance, pred_vertex.

Kruskal’s MST
Problem: connect all vertices in an undirected, connected graph with minimum total edge weight.
Strategy: use a greedy approach:
Take edges from smallest weight upward,
Avoid cycles by checking/merging disjoint vertex sets.
Data structures: priority queue of edges; sets of vertices.

Floyd–Warshall
Problem: shortest paths between all pairs of vertices.
Allows negative weights but not negative cycles.
Strategy: dynamic programming on a distance matrix; gradually allow more intermediate vertices.
Data: a V × V matrix containing distances; optional path reconstruction using incoming edges.
"""