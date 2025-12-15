import heapq
from collections import deque

# CAMPUS GRAPH

# Each key is a campus building (node)
# Each value is a list of (neighbor_building, distance_in_meters)
# Distances are approximate walking distances

graph = {
    "Student Center": [
        ("Sprague Library", 120),
        ("Susan A. Cole Hall", 180),
        ("Memorial Auditorium", 150),
        ("University Police", 160)
    ],

    "Sprague Library": [
        ("Student Center", 120),
        ("Science Hall", 160)
    ],

    "Science Hall": [
        ("Sprague Library", 160),
        ("Center for Computing & Information Science", 140)
    ],

    "Center for Computing & Information Science": [
        ("Science Hall", 140),
        ("University Hall", 170)
    ],

    "University Hall": [
        ("Center for Computing & Information Science", 170),
        ("Susan A. Cole Hall", 130)
    ],

    "Susan A. Cole Hall": [
        ("Student Center", 180),
        ("University Hall", 130),
        ("Freeman Hall", 200)
    ],

    "Freeman Hall": [
        ("Susan A. Cole Hall", 200),
        ("Student Recreation Center", 220)
    ],

    "Student Recreation Center": [
        ("Freeman Hall", 220),
        ("Panzer Athletic Center", 190)
    ],

    "Panzer Athletic Center": [
        ("Student Recreation Center", 190),
        ("Red Hawk Parking Deck", 300)
    ],

    "Red Hawk Parking Deck": [
        ("Panzer Athletic Center", 300),
        ("Yogi Berra Stadium", 350)
    ],

    "Yogi Berra Stadium": [
        ("Red Hawk Parking Deck", 350)
    ],

    "Memorial Auditorium": [
        ("Student Center", 150),
        ("Life Hall", 140)
    ],

    "University Police": [
        ("Student Center", 160)
    ],

    "Life Hall": [
        ("Memorial Auditorium", 140),
        ("School of Communication and Media", 120)
    ],

    "School of Communication and Media": [
        ("Life Hall", 120)
    ]
}

locations = list(graph.keys())


# BREADTH-FIRST SEARCH (BFS)

from collections import deque

def bfs_reachable(start_location):
    """
    Performs BFS to find all locations reachable from start_location.

    Parameters:
        start_location (str): The building from which traversal starts.

    Returns:
        list: List of reachable locations in BFS order.
    """

    visited = set()        # To keep track of visited locations
    queue = deque()        # Queue for BFS traversal
    reachable = []         # Result list

    # Start BFS
    visited.add(start_location)
    queue.append(start_location)

    while queue:
        current = queue.popleft()
        reachable.append(current)

        # Visit all neighboring buildings
        for neighbor, _distance in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return reachable

def calculate_path_distance(path):
    total_distance = 0

    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]

        for neighbor, weight in graph[current]:
            if neighbor == next_node:
                total_distance += weight
                break

    return total_distance


# DIJKSTRA'S ALGORITHM (SHORTEST PATH)

import heapq

def dijkstra_shortest_path(start_location, end_location):
    """
    Finds the shortest path between two locations using Dijkstra's Algorithm.

    Parameters:
        start_location (str): Starting building
        end_location (str): Destination building

    Returns:
        tuple:
            total_distance (int)
            path (list of str)
            nodes_explored (int)
    """

    # Step 1: Initialize distances and previous nodes
    distances = {location: float('inf') for location in graph}
    distances[start_location] = 0

    previous = {location: None for location in graph}

    # Step 2: Priority queue
    priority_queue = [(0, start_location)]
    nodes_explored = 0

    # Step 3: Main loop
    while priority_queue:
        current_distance, current_location = heapq.heappop(priority_queue)
        nodes_explored += 1

        # Stop early if destination reached
        if current_location == end_location:
            break

        # Ignore outdated queue entries
        if current_distance > distances[current_location]:
            continue

        # Explore neighbors
        for neighbor, weight in graph.get(current_location, []):
            new_distance = current_distance + weight

            # Relaxation step
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_location
                heapq.heappush(priority_queue, (new_distance, neighbor))

    # Step 4: Reconstruct path
    if distances[end_location] == float('inf'):
        return float('inf'), [], nodes_explored

    path = []
    current = end_location
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return distances[end_location], path, nodes_explored

def bfs_shortest_path(start, end):
    from collections import deque

    visited = set()
    queue = deque()
    parent = {}

    visited.add(start)
    queue.append(start)
    parent[start] = None

    nodes_explored = 0

    while queue:
        current = queue.popleft()
        nodes_explored += 1

        if current == end:
            break

        for neighbor, _ in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    if end not in parent:
        return [], nodes_explored

    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    return path, nodes_explored

#COMPARISION BFS VS DIJKSTRA
def compare_bfs_vs_dijkstra(start, end):
    print("\n--- Algorithm Comparison ---")

    bfs_path, bfs_nodes = bfs_shortest_path(start, end)
    bfs_distance = calculate_path_distance(bfs_path) if bfs_path else float('inf')

    dijkstra_distance, dijkstra_path, dijkstra_nodes = dijkstra_shortest_path(start, end)

    print("\nBFS Result:")
    if bfs_path:
        print("Path:", " → ".join(bfs_path))
        print("Total Distance:", bfs_distance, "meters")
        print("Nodes Explored:", bfs_nodes)
    else:
        print("No path found.")

    print("\nDijkstra Result:")
    if dijkstra_path:
        print("Path:", " → ".join(dijkstra_path))
        print("Total Distance:", dijkstra_distance, "meters")
        print("Nodes Explored:", dijkstra_nodes)
    else:
        print("No path found.")

    print("\nConclusion:")
    if bfs_distance == dijkstra_distance:
        print("Both algorithms found the same distance.")
    else:
        print("Dijkstra found a shorter path because it considers edge weights.")


# MENU-DRIVEN USER INTERFACE

def show_locations():
    """Displays all campus locations with numbers."""
    print("\nAvailable Campus Locations:")
    for idx, location in enumerate(locations, start=1):
        print(f"{idx}. {location}")


def get_location_from_user(prompt):
    """
    Prompts the user to select a location using number input.
    Returns the selected location name.
    """
    while True:
        show_locations()
        choice = input(prompt).strip()

        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        index = int(choice)
        if 1 <= index <= len(locations):
            return locations[index - 1]
        else:
            print("Invalid choice. Try again.")


def main():
    print("===================================")
    print("  CAMPUS NAVIGATION SYSTEM")
    print("  Montclair State University")
    print("===================================")

    while True:
        print("\nMain Menu:")
        print("1. Show all campus locations")
        print("2. Find shortest path between two locations")
        print("3. Show all reachable locations from a starting point (BFS)")
        print("4. Compare BFS and Dijkstra")
        print("5. Exit")


        choice = input("Enter your choice (1-4): ").strip()

        # Option 1: Show locations
        if choice == "1":
            show_locations()

        # Option 2: Shortest path (Dijkstra)
        elif choice == "2":
            print("\n--- Shortest Path Finder ---")
            start = get_location_from_user("Select START location number: ")
            end = get_location_from_user("Select DESTINATION location number: ")

            if start == end:
                print("Start and destination are the same.")
                continue

            distance, path, explored = dijkstra_shortest_path(start, end)

            if distance == float('inf'):
                print(f"No path found from {start} to {end}.")
            else:
                print("\nShortest Path:")
                print(" → ".join(path))
                print(f"Total Distance: {distance} meters")
                print(f"Nodes Explored: {explored}")

        # Option 3: Reachable locations (BFS)
        elif choice == "3":
            print("\n--- Reachable Locations (BFS) ---")
            start = get_location_from_user("Select starting location number: ")
            reachable = bfs_reachable(start)

            print(f"\nFrom {start}, you can reach:")
            for place in reachable:
                print(f"- {place}")
        # Option 4: Compare BFS and Dijkstra
        elif choice == "4":
            print("\n--- Compare BFS and Dijkstra ---")
            start = get_location_from_user("Select START location number: ")
            end = get_location_from_user("Select DESTINATION location number: ")

            compare_bfs_vs_dijkstra(start, end)


        # Option 5: Exit
        elif choice == "5":
            print("\nExiting Campus Navigation System. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-4.")


# Program entry point
if __name__ == "__main__":
    main()

