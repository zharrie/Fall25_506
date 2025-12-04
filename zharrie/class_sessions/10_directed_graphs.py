# DIRECTED GRAPHS FUNDAMENTALS
"""
A directed graph (digraph) consists of:
- Vertices: Represent items or nodes
- Directed edges: Connections from a starting vertex to a terminating vertex

Key Concept - Adjacency:
- Vertex Y is adjacent to vertex X if an edge exists from X to Y
Important: Adjacency is directional (B adjacent to A ≠ A adjacent to B)

Real-World Applications:
- Website links (page A links to page B)
- Airline routes (flights from city to city)
- Social networks (follower relationships)
"""
# Paths and Cycles
"""
Path: A sequence of directed edges from a source vertex to a destination vertex.
Example: Path A → B → C → E

Cycle: A path that starts and ends at the same vertex.
Example: N → K → J → N

Graph Classification:
- Cyclic graph: Contains at least one cycle
- Acyclic graph: Contains no cycles
- DAG (Directed Acyclic Graph): Particularly useful for hierarchical relationships
"""
# Incoming and Outgoing Edges
"""
For any vertex V:
- Outgoing edge: Edge starting from V
- Incoming edge: Edge terminating at V
- Degree: Total edges containing V (incoming + outgoing)

Special cases:
- Vertex with 0 incoming edges = source vertex
- Vertex with 0 outgoing edges = sink vertex
"""

# WEIGHTED GRAPHS
"""
Edge Weights
A weighted graph associates a numerical weight (cost) with each edge, representing:
- Flight costs or distances
- Travel time (may differ by direction)
- Connection speeds
- Any quantifiable relationship
Note: Weighted graphs can be directed or undirected.

Path Length and Shortest Paths
- Path length = Sum of all edge weights along the path
- Shortest path: The path with minimum total weight between two vertices.

Example:
- Path 1: Paris → Nantes → Nice → Marseille = 1 + 4 + 3 = 8
- Path 2: Paris → Lyon → Nice → Marseille = 2 + 1 + 3 = 6 (shortest)

Negative Edge Weight Cycles
- Negative edge weight cycle: A cycle whose total weight is less than 0.
- Critical Issue: No shortest path exists in graphs with negative edge weight cycles!
- Each loop around the cycle further decreases the path length
- No minimum value can be determined
Example: Cycle with weights 5 and -7 has cycle length -2; infinite loops reduce it indefinitely
"""
# PYTHON IMPLEMENTATION - CLASSES
#Vertex and Edge Classes
#Vertex Class - Simple container for vertex label:
class Vertex:
    def __init__(self, vertex_label):
        self.label = vertex_label

# Edge Class - Represents directed edge with weight:
class Edge:
    def __init__(self, from_vertex, to_vertex, edge_weight):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = edge_weight

#Graph Class Data Structure
"""
Uses two dictionaries for efficient edge access:
- from_edges: Maps vertex → list of outgoing edges
- to_edges: Maps vertex → list of incoming edges
Design rationale: Many graph operations need quick access to incoming/outgoing edges.
"""
# Key Methods:
def get_edges(self):  # Returns set of all edges
    pass         
def get_edges_from(self, from_vertex):  # Returns outgoing edges
    pass
def get_edges_to(self, to_vertex):      # Returns incoming edges
    pass
def get_vertex(self, vertex_label):     # Finds vertex by label
    pass
def get_vertices(self):                 # Returns list of all vertices
    pass

#Graph Modification Methods
def add_vertex(self, new_vertex_label):
    new_vertex = Vertex(new_vertex_label)
    self.from_edges[new_vertex] = []
    self.to_edges[new_vertex] = []
    return new_vertex

def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
    if self.has_edge(from_vertex, to_vertex):
        return None  # Prevent duplicate edges
    new_edge = Edge(from_vertex, to_vertex, weight)
    self.from_edges[from_vertex].append(new_edge)
    self.to_edges[to_vertex].append(new_edge)
    return new_edge

def add_undirected_edge(self, vertexA, vertexB, weight = 1.0):
    # Creates two directed edges (bidirectional)
    edge1 = self.add_directed_edge(vertexA, vertexB, weight)
    edge2 = self.add_directed_edge(vertexB, vertexA, weight)
    return (edge1, edge2)

def has_edge(self, from_vertex, to_vertex):
    if from_vertex not in self.from_edges:
        return False
    edges = self.from_edges[from_vertex]
    for edge in edges:
        if edge.to_vertex is to_vertex:
            return True
    return False

# BREADTH-FIRST SEARCH (BFS)
"""
Vertex Visitor Pattern
Provides flexibility for operations during graph traversal.
"""
# Base class:
class VertexVisitor:
    def visit(self, vertex_to_visit):
        pass

# Example implementation:
class ListVertexVisitor(VertexVisitor):
    def __init__(self):
        self.visited_vertices = []
    
    def visit(self, vertex_to_visit):
        self.visited_vertices.append(vertex_to_visit)

#  BFS Algorithm
"""
Purpose: Visit all reachable vertices level-by-level from a starting vertex.
Data Structures:
- discovered_set: "Set of discovered vertices"
- frontier_queue: "Queue of discovered but unvisited vertices"
- distances: "Dictionary mapping vertex → distance from start"
"""
# Algorithm:
def breadth_first_search(self, start_vertex, visitor, distances):
    discovered_set = set()
    frontier_queue = Queue()
    
    distances[start_vertex] = 0
    frontier_queue.put(start_vertex)
    discovered_set.add(start_vertex)
    
    while frontier_queue.qsize() > 0:
        current_vertex = frontier_queue.get()
        visitor.visit(current_vertex)
        
        for edge in self.get_edges_from(current_vertex):
            if edge.to_vertex not in discovered_set:
                frontier_queue.put(edge.to_vertex)
                discovered_set.add(edge.to_vertex)
                distances[edge.to_vertex] = distances[current_vertex] + 1

# Key characteristic: Uses Queue (FIFO) - guarantees level-order traversal.
# Applications: Shortest path in unweighted graphs, social network distances, web crawling.

# DEPTH-FIRST SEARCH (DFS)
# Vertex Visitor for DFS
# Example implementation:
class PrintVertexVisitor(VertexVisitor):
    def visit(self, vertex_to_visit):
        print(f"{vertex_to_visit.label} ", end="")

# DFS Algorithm
"""
Purpose: Explore as far as possible along each path before backtracking.

Data Structures:
- vertex_stack: Stack of vertices to visit
- visited_set: Set of already visited vertices (prevents infinite loops in cycles)
"""
# Algorithm:
def depth_first_search(self, start_vertex, visitor):
    vertex_stack = [start_vertex]
    visited_set = set()
    
    while len(vertex_stack) > 0:
        current_vertex = vertex_stack.pop()
        
        if current_vertex not in visited_set:
            visitor.visit(current_vertex)
            visited_set.add(current_vertex)
            
            for edge in self.get_edges_from(current_vertex):
                vertex_stack.append(edge.to_vertex)
"""
Key characteristic: Uses Stack (LIFO) - explores deeply before broadly.
Critical: The visited_set prevents infinite loops in cyclic graphs.
Applications: Cycle detection, topological sorting, maze solving, connected components.
"""

# TOPOLOGICAL SORT
"""
Definition and Requirements
Topological sort: An ordering of vertices in a DAG such that for every edge X → Y, X appears before Y in the ordering.

Requirements:
- Graph must be directed
- Graph must be acyclic
- Visual property: If vertices are arranged left-to-right in topological order, all edges point left-to-right.
- Important: A graph can have multiple valid topological sorts.

Real-World Application
Graph representation:
Vertices = Courses
Edge Math 101 → Phys 101 means Math 101 must be taken first

Example valid orderings:
Math 101, Phys 101, CS 101, CS 102, CS 103
CS 101, Math 101, Phys 101, CS 102, CS 103
Math 101, CS 101, CS 102, Phys 101, CS 103
All satisfy prerequisite constraints.

Topological Sort Algorithm
Concept: Track incoming edge counts; process vertices with no remaining incoming edges.

Algorithm Steps:
Initialization:
- Count incoming edges for each vertex
- Add all vertices with count = 0 to a collection
- Main Loop (until collection is empty):

- Remove a vertex from collection → add to result
- For each outgoing edge from this vertex:
- Decrement the destination vertex's count
- If count becomes 0, add destination to collection

Pseudocode:
GraphTopologicalSort(graph) {
    resultList = new empty list
    noIncoming = new empty stack
    
    for each vertex V in graph {
        V.inCount = number of incoming edges to V
        if (V.inCount == 0)
            Push V to noIncoming
    }
    
    while (noIncoming is not empty) {
        currentVertex = Pop from noIncoming
        Append currentVertex to resultList
        
        for each outgoing edge E from currentVertex {
            Decrement E.toVertex's count
            if (E.toVertex's count is 0)
                Push E.toVertex to noIncoming
        }
    }
    
    return resultList
}

Complexity: O(V + E) where V = vertices, E = edges
Cycle Detection: If result doesn't contain all vertices, graph has a cycle.
"""

# Key Takeaways
"""
- Directed graphs model one-way relationships; adjacency is not symmetric
- Weighted graphs add quantitative relationships between vertices
- Negative cycles make shortest paths undefined
- BFS finds shortest paths in unweighted graphs using queue traversal
- DFS explores all paths using stack traversal; requires visited tracking
- Topological sort orders DAG vertices respecting dependencies
- Visitor pattern provides flexible vertex processing during traversal
- Python implementation uses dictionaries for efficient edge access
"""
