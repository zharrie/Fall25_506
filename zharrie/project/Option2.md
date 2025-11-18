## Project 2: Social Network Analyzer

### Description
Analyze a social network to find connections, identify communities, and discover influential users. Implement graph algorithms to explore relationships and patterns.

### Objectives
- Understand undirected graph representation
- Apply graph traversal algorithms
- Calculate graph metrics
- Analyze network properties

### Required Data Structures
- Undirected Graph: Friendship network
- Hash Map: User profiles and quick lookup
- Queue: For BFS implementation
- List/Set: For storing traversal results

### Required Algorithms
- BFS and DFS for network traversal
- Shortest Path for degrees of separation
- Sorting Algorithms for ranking users
- Graph Connectivity analysis

### Minimum Required Features
- Load Network
    - From CSV file
    - Minimum 20 users, 30 friendship connections

- Connection Analysis
    - Find degree of separation between any two users
    - Find all friends within N degrees
    - Find mutual friends between two users

- Network Statistics
    - Most connected users (by number of friends)
    - Average connections per user
    - Network diameter (longest shortest path)

- Friend Recommendations
    - Suggest new friends (friends-of-friends not already connected)
    - Rank suggestions by mutual friends

### Sample Interaction
=== Social Network Analyzer ===

Network loaded successfully.
Total users: 25
Total connections: 38
Average connections per user: 3.04

Main Menu:
1. Find connection path
2. Friends within N degrees
3. Most connected users
4. Mutual friends
5. Friend suggestions
6. Network statistics
7. Exit

Choice: 1
- Enter first user: Alice
- Enter second user: Frank

Analyzing connection...

- Connection path found:
    - Alice → Bob → Emma → Frank

- Degrees of separation: 3
    - Path length: 3 intermediate connections

Choice: 3
Most Connected Users:
1. Emma (12 friends)
2. Bob (10 friends)
3. Charlie (8 friends)
4. Alice (7 friends)
5. David (6 friends)

Choice: 5

Enter user name: Alice

Friend suggestions for Alice:
1. Frank (3 mutual friends: Bob, Emma, Charlie)
2. Grace (2 mutual friends: Emma, David)
3. Henry (2 mutual friends: Bob, Charlie)
