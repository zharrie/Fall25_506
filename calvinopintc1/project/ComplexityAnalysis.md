# Complexity Analysis
## **CSIT 506 – Final Project**  
## **Authors:** *Vincent L. & Camila C.*

## binarysearchtree.py

DATA STRUCTURES USED:
- Binary Search Tree (BST)
  - Stores songs keyed by a sortable numeric attribute (e.g., rating or play_count) with a tie-breaker (such as title).
  - Chosen because search and insert operations follow a single root-to-leaf path, which is efficient when the tree remains balanced.

TIME COMPLEXITY (for N nodes, tree height H):
- insert(song)
  - Best:  O(log N) when the tree is balanced.
  - Worst: O(N) when the tree is completely unbalanced.
- search / contains(key)
  - Best:  O(log N) when balanced.
  - Worst: O(N) when unbalanced.
  - General form: O(H), since only one path from root to leaf is explored.
- inorder traversal
  - O(N), because each node is visited exactly once.

SPACE COMPLEXITY:
- Data structure storage:
  - O(N) for storing N nodes.
- Auxiliary space:
  - O(log N) for recursion stack depth in balanced cases.
  - O(N) in the worst case when the tree is highly unbalanced.

ALGORITHM COMPARISON:
- Balanced BST:
  - Time: O(log N) for search and insert.
  - Space: O(N).
- Unbalanced BST:
  - Time: O(N) for search and insert.
  - Space: O(N).

TRADE-OFFS:
- A balanced BST provides fast logarithmic operations.
- If insertion order causes imbalance, performance degrades to linear time.

---

## graph.py

DATA STRUCTURES USED:
- Graph implemented using an adjacency list
  - Each vertex maps to a list of neighboring vertices (and optional weights).
  - Chosen because storage grows with the number of vertices and edges, not with V².
- Queue and set
  - Used for traversal bookkeeping and to track visited vertices.

TIME COMPLEXITY (for V vertices, E edges, N songs):
- Graph construction using pairwise comparisons
  - O(N²) when each song is compared against every other song.
- Adjacency check
  - Adjacency list: O(V) in the worst case (scan neighbor list).
  - Adjacency matrix (comparison point): O(1).

SPACE COMPLEXITY:
- Adjacency list:
  - O(V + E).
- Adjacency matrix (comparison point):
  - O(V²).
- Auxiliary space:
  - O(V) for queues/sets used during traversal.

ALGORITHM COMPARISON:
- Adjacency List:
  - Space: O(V + E).
  - Adjacency check: O(V) worst case.
- Adjacency Matrix:
  - Space: O(V²).
  - Adjacency check: O(1).

TRADE-OFFS:
- Adjacency lists are memory-efficient for sparse graphs but slower for adjacency checks.
- Adjacency matrices provide constant-time checks but consume significantly more memory.

---

## models.py

DATA STRUCTURES USED:
- Python list
  - Stores Song objects in a defined order.
  - Chosen for simplicity and ease of iteration.

TIME COMPLEXITY (for N songs):
- append(song)
  - Typical: O(1).
  - Occasional: O(N) when resizing occurs.
- Single-pass scans (e.g., filtering or checking each song once)
  - O(N).
- Nested comparisons over the list
  - O(N²).

SPACE COMPLEXITY:
- Data structure storage:
  - O(N) for storing songs.
- Auxiliary space:
  - O(1) when only fixed extra variables are used.
  - O(N) when creating new lists proportional to input size.

ALGORITHM COMPARISON:
- Append-only usage:
  - Time: Usually O(1).
  - Space: O(N).
- Pairwise nested comparisons:
  - Time: O(N²).
  - Space: Often O(1) auxiliary.

TRADE-OFFS:
- Lists are efficient for accumulation and linear scans.
- Algorithms requiring pairwise comparisons quickly become expensive at scale.

---

## queues.py

DATA STRUCTURES USED:
- Array-backed queue
  - Implements FIFO behavior using an underlying array with front index tracking.
  - Chosen for constant-time enqueue and dequeue operations in typical cases.

TIME COMPLEXITY (for N items):
- enqueue(item)
  - Typical: O(1).
  - When resizing occurs: O(N).
- dequeue()
  - O(1).
- is_empty()
  - O(1).

SPACE COMPLEXITY:
- Data structure storage:
  - O(N) for the underlying array.
- Auxiliary space:
  - O(1) for standard operations.
  - O(N) temporarily during resizing.

ALGORITHM COMPARISON:
- Normal enqueue/dequeue:
  - Time: O(1).
  - Space: O(N).
- Enqueue with resize:
  - Time: O(N).
  - Space: O(N) temporary.

TRADE-OFFS:
- Array-backed queues provide fast FIFO operations most of the time.
- Occasional resizing introduces a linear-time and linear-space cost.

---

## searching.py

DATA STRUCTURES USED:
- Python list
  - Stores songs and supports indexed access needed for binary search.

TIME COMPLEXITY (for N items):
- linear_search(...)
  - Best: O(1).
  - Worst: O(N).
- binary_search(...)
  - Best: O(1).
  - Average: O(log N).
  - Worst: O(log N).
- search_by_genre(...)
  - O(N).

SPACE COMPLEXITY:
- Data structure storage:
  - O(N).
- Auxiliary space:
  - O(1) for linear and iterative binary search.
  - O(log N) only applies if a recursive binary search is used.

ALGORITHM COMPARISON:
- Linear Search:
  - Time: Best O(1), Worst O(N).
  - Space: O(1).
- Binary Search:
  - Time: Best O(1), Average/Worst O(log N).
  - Space: O(1) (iterative).

TRADE-OFFS:
- Linear search works on unsorted data but scales poorly.
- Binary search is significantly faster but requires sorted input.

---

## sorting.py

DATA STRUCTURES USED:
- Python list
  - Used as the primary container for in-place and merge-based sorting.

TIME COMPLEXITY (for N items):
- quicksort(...)
  - Best:    O(N log N).
  - Average: O(N log N).
  - Worst:   O(N²).
- merge_sort(...)
  - Best:    O(N log N).
  - Average: O(N log N).
  - Worst:   O(N log N).

SPACE COMPLEXITY:
- quicksort:
  - O(log N) recursion stack in best/average cases.
  - O(N) recursion stack in worst case.
- merge_sort:
  - O(N) extra space for temporary merged lists.

ALGORITHM COMPARISON:
- Quicksort:
  - Time: Best/Average O(N log N), Worst O(N²).
  - Space: O(log N) average, O(N) worst.
- Merge Sort:
  - Time: O(N log N) guaranteed.
  - Space: O(N).

TRADE-OFFS:
- Quicksort is fast and in-place but can degrade with poor pivot choices.
- Merge sort has predictable performance but requires additional memory.
