# training_graph.py

from collections import deque
# deque is ideal for BFS because popleft() is O(1) compared to list pop(0) which is O(n).
from typing import Dict, List, Optional
from models import Course, Role


class Graph:
    """
    Simple undirected graph using an adjacency list.
    Nodes are represented as strings, e.g.:
        "skill:communication"
        "course:C01"
        "role:R01"
    """

    def __init__(self) -> None:
        #Initialize empty adjacency list
        self.adj: Dict[str, List[str]] = {}

    # Define add_node method
    def add_node(self, node: str) -> None:
        if node not in self.adj:
            self.adj[node] = []

    # Define add_edge method
    def add_edge(self, u: str, v: str) -> None:
        """
        Add an undirected edge between u and v.
        """
        self.add_node(u)
        self.add_node(v)
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if u not in self.adj[v]:
            self.adj[v].append(u)

    # Define neighbors method
    def neighbors(self, node: str) -> List[str]:
        return self.adj.get(node, [])




# Define build_training_graph function
def build_training_graph(
    courses: Dict[str, Course],
    roles: Dict[str, Role],
) -> Graph:
    """
    Build a graph that connects:

        skill -> course -> role

    We add:
      - For each course and each skill it teaches:
            edge between "skill:<skill_name>" and "course:<course_id>"
      - For each role, required skill, and each course teaching that skill:
            edge between "course:<course_id>" and "role:<role_id>"

    This lets us find paths like:
        skill:conflict_resolution -> course:C01 -> role:R01
    """
    g = Graph()

    # Build edges between skills and courses.
    for course in courses.values():
        course_node = f"course:{course.id}"
        for skill in course.skills:
            #Ensuring naming consistency
            skill_name = skill.strip().lower()
            skill_node = f"skill:{skill_name}"
            g.add_edge(skill_node, course_node)

    # Build edges between course and role (if course teaches a role-required skill).
    # For each role, for each required skill, connect all matching courses.
    for role in roles.values():
        role_node = f"role:{role.id}"
        for req_skill in role.required_skills:
            skill_name = req_skill.strip().lower()
            skill_node = f"skill:{skill_name}"
            # For each course that teaches this skill, connect course <-> role
            for course in courses.values():
                if skill_name in course.skills:
                    course_node = f"course:{course.id}"
                    g.add_edge(course_node, role_node)

    return g


#This function performs a breadth-first search to find the shortest path in the graph.
# It returns a list of node IDs if a path is found, or None otherwise.
# It is useful for finding training paths from missing skills to target roles.
#We used breadth-first instead of depth-first search because BFS guarantees the shortest path in an unweighted graph.
# graph: The Graph object representing the training graph.
# start: The starting node ID (e.g., "skill:communication").
# goal: The goal node ID (e.g., "role:R01").
def bfs_shortest_path(
    graph: Graph,
    start: str,
    goal: str,
) -> Optional[List[str]]:
    """
    Breadth-first search to find the shortest path from start to goal.
    Returns a list of node IDs if a path is found, or None otherwise.
    """
    # Check if start and goal are in the graph
    # If either the start or goal node is not present in the graph's adjacency list,
    # we return None immediately, indicating that no path can exist.
    # This is a quick check to avoid unnecessary processing.
    # It ensures that we only attempt to find paths between nodes that actually exist in the graph.
    if start not in graph.adj or goal not in graph.adj:
        return None

    # Initialize BFS structures
    # deque is used for efficient popping from the front of the queue
    # visited set keeps track of visited nodes to avoid cycles
    # parent dictionary to reconstruct the path later
    # We start by initializing the queue with the start node,
    # marking it as visited, and setting its parent to None.
    # This sets up the necessary data structures for the BFS algorithm to operate correctly.
    queue = deque([start])
    # Visited set prevents cycles / repeated work
    visited = {start}
    # Parent pointers used to reconstruct the final path.
    parent: Dict[str, Optional[str]] = {start: None}

    found = False

    # While there are nodes to explore in the queue
    # We continue the search until there are no more nodes to explore (the queue is empty).
    while queue:
        current = queue.popleft()
        # if we reached the goal, stop searching
        # goal was defined as a parameter to the function above
        if current == goal:
            found = True
            break

        # Explore neighbors
        # For each neighbor of the current node, if it hasn't been visited yet,
        # we mark it as visited, set its parent to the current node,
        # and add it to the queue for further exploration.
        # This process continues until we either find the goal node or exhaust all possibilities.
        # This ensures that we explore the graph level by level, which is characteristic of BFS.
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # If we finish exploring the graph without finding the goal node,
    # we return None to indicate that no path exists between the start and goal nodes.
    if not found:
        return None

    # Reconstruct path from goal back to start using parent pointers
    # By following these parent pointers from the goal node back to the start node,
    # we can reconstruct the path taken to reach the goal. 
    # This is important because BFS explores nodes level by level,
    # so we need to backtrack in order to find the actual path.
    path: List[str] = []
    node: Optional[str] = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path