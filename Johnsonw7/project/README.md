Organizational Training Recommendation System
=============================================
by Evelyn Dishaw & Wesley Johnson

This code is intended to allow a member of an organization to view employee profiles including their skills, analyze skill gaps for their ideal role, get training recommendations to address those gaps, compare algorithms for class purposes, list all courses, and show a graph-based training path for individual missing skills. If implemented for an actual organization, these data structures and algorithms would allow any employee to set a path with recommendations for them to achieve their dream position. 

# Modules & Their Key Functions
  1. **models.py:** creates classes/methods for Employee, Course, and  Role
  2. **data_loader.py:** converts raw data from the .json data files listed below into employee, course, and role objects
  3. **algorithms.py:** creates algorithms to compute skill gaps, build a skill index, make course recommendations, and sort course recommendations
  3. **main.py:** prints/displays information and is the "entry point" for the interactive main menu
  5. **recommender.py** creates a class for TrainingRecommender and runs the algorithms from algorithms.py
  6. **training_graph.py** creates a Graph class and creates graph-building and breadth-first search algorithms

# Data Files
  1. courses.json
  2. employees.json
  3. roles.json

# Instructions
  Run the main.py file to access the main menu. The user will select a menu option and follow the prompts.


# Main Menu Functionality Overview:
  1. View employee profile
  2. Analyze skill gaps for a target role
  3. Get training recommendations
  4. Compare recommendation algorithms (naive vs indexed)
  5. Compare sorting algorithms (built-in vs selection sort)
  6. List all courses
  7. Show graph-based training paths for missing skills
  8. Exit



# Presentation Overview:

Wes - Introduction to coding approach
Evelyn - Introduction to project and file layout
Evelyn - Demonstration of first 3 features connecting it to code
Wes - Demonstration of algorithm comparisons and considerations
Wes - Demonstration of graph Functionality




## Extending the Python Techniques Learned in Class - Detailed Walkthrough

This project builds directly on the Python concepts and algorithmic patterns introduced in class (for example, list-based algorithms such as selection sort), and then extends them to support a larger, more realistic application. Rather than replacing what was learned, the code demonstrates how the same core ideas—loops, comparisons, swapping, and conditionals—can be adapted and combined with additional Python features to improve clarity, efficiency, and scalability as program complexity increases.


### Data Representation: Explicit Domain Objects

In class, many examples operate on lists of values such as numbers in order to clearly illustrate algorithm mechanics. This project applies the same logic to real-world entities by representing them as structured objects: `Employee`, `Course`, and `Role`.

These entities are implemented using Python’s `@dataclass` decorator. Dataclasses provide a concise way to define objects whose primary purpose is to store data, while automatically generating common methods such as constructors, readable string representations, and equality checks. This allows the program to work with meaningful objects (for example, `course.title` or `employee.skills`) rather than relying on index positions or loosely structured dictionaries, while still using the same looping and comparison techniques learned in class.


### Function Interfaces and Type Hints

In this project, functions include type hints to document what kinds of inputs they expect and what they return. For example, annotating a function to return  -> `Set[str]` communicates that the output is a collection of skill names and supports reasoning about how that output can be used elsewhere.

Type hints do not change how the program runs, but they make the code easier to follow across multiple files and help clarify how different parts of the system fit together. This is especially useful in a project that includes multiple algorithms and data transformations.

### Applying Sorting Algorithms to Structured Data

Selection sort is introduced in class using lists of numbers to highlight the algorithm’s mechanics: scanning for a minimum or maximum value and swapping elements. This project applies the same algorithmic structure to a more complex case: sorting recommendations that pair a course with a relevance score.

Rather than comparing numbers directly, the code compares scores and applies a secondary tie-breaking rule using course titles. Swapping is still required, but Python’s tuple unpacking syntax allows the swap to be expressed clearly and safely in a single line. This preserves the logic of selection sort while adapting it to work with structured records instead of simple numeric values.

### Modular Program Structure

This project organizes code into multiple files, each with a specific responsibility: data models, data loading, algorithms, graph logic, and user interaction.

This modular structure makes it easier to extend the program without rewriting existing logic. For example, new algorithms can be added without changing the menu system, and data formats can evolve independently of the recommendation logic. The underlying control structures—loops, conditionals, and function calls—remain the same as those learned in class, but are applied within a larger system.

---

### Algorithm Variants and Efficiency

The project includes both a straightforward recommendation algorithm and an optimized version that uses an index to reduce repeated work. This mirrors a common progression in computer science: starting with a clear baseline approach and then improving it by reorganizing data.

The optimized version does not change the fundamental logic of matching skills to courses; instead, it applies additional data structures (dictionaries) to make those operations more efficient. This allows for direct comparison between approaches and illustrates how performance considerations can influence implementation choices.


### Use of Graphs to Extend Core Ideas

This project introduces a graph structure to represent relationships between skills, courses, and roles. The graph is traversed using breadth-first search.

This feature extends the same foundational ideas taught in class—systematic exploration and condition-based traversal—into a richer data structure that supports explainable training paths.


### Overall Perspective

The intent of this project is to demonstrate how the Python techniques and algorithms learned in class can be extended and combined with additional language features to solve more complex problems, relevant to Industrial/Organizational Psychology. Dataclasses and type hints are used in addition to fundamental course methods in ways that improve clarity, efficiency, and maintainability as the scope of the program increases.

In this way, the project reflects a natural progression from instructional examples to a more complete and practical application, while remaining grounded in the same core algorithmic principles introduced in coursework.

## How `dataclasses` and `typing` Add Utility

### dataclasses - simplified definitions and attribute notation

In class, structured data is often represented using dictionaries or parallel lists. For example, a course might be stored as a dictionary with fixed keys, and the program must consistently remember and reference those keys correctly throughout the code.

course = {"id": "C010", "title": "Patient Education Strategies", "skills": ["patient_education", "communication"]}
print(course["title"])

In this project, the same idea is expressed using a dataclass, which defines the structure of the data once and makes it explicit everywhere it is used.

@dataclass
class Course:
    id: str
    title: str
    skills: Set[str]
    difficulty: str = "unspecified"

A course can then be created and accessed using attribute notation:

course = Course(id="C010", title="Patient Education Strategies", skills={"patient_education", "communication"})
print(course.title)

Added value of dataclasses:
	•	Provide a clear, centralized definition of each domain entity.
	•	Automatically generate common methods such as __init__, __repr__, and __eq__, reducing boilerplate code.
	•	Improve readability and debugging by working with named attributes instead of dictionary keys.
	•	Make it easier to pass structured data consistently across multiple modules.


Methods Automatically Added by @dataclass (Beyond __init__)

In addition to generating the __init__ constructor, Python’s @dataclass decorator automatically creates two important methods that are used throughout this project: __repr__ and __eq__.

__repr__ (string representation)
The __repr__ method defines how an object is displayed when it is printed or inspected. With @dataclass, objects are shown in a clear, readable format that includes their field names and values. For example, printing a Course object will display its ID, title, and skills instead of a generic memory address. This greatly improves debugging and makes intermediate outputs easier to interpret when objects appear inside lists or tuples.

__eq__ (equality comparison)
The __eq__ method defines how two objects are compared for equality using ==. With @dataclass, two objects are considered equal if all of their fields are equal. This enables value-based comparisons rather than default memory-based comparisons, which is especially useful when testing logic, checking results across algorithm runs, or reasoning about whether two domain objects represent the same underlying data.


### typing

In class, function behavior is often inferred from context or comments rather than being explicitly documented in the function definition.

def compute_skill_gaps(employee, role):
    return role["required_skills"] - employee["skills"]

In this project, type hints are used to make function expectations and outputs explicit:

def compute_skill_gaps(employee: Employee, role: Role) -> Set[str]:
    return role.required_skills - employee.skills

This annotation clearly communicates that the function expects an Employee and a Role object and returns a set of strings representing missing skills.

Added value of typing:
- Helps ensure multiple coders are on the same page about what input/output is expected where

## Algorithm Comparisons

compute_skill_gaps
TC: O(1) per lookup
SC: O(N) N = number of missing skills

build_skill_index
TC: O(C*K) C = Courses, K = Skills
SC: O(C*K)
This has relatively high up-front cost but enables efficient comparisons down the line once it is loaded

recommend_courses_naive
If course.skills is a set:
TC: O(M*C) + O(P log P)
SC: O(C) + O(P)
M = number of missing skills, C = number of courses, P = number of candidate courses with score > 0
This approach “full scans” all courses for each missing skill, then sorts the candidates. It is simple and readable, but scales poorly as the course catalog grows.

If course.skills is a list/tuple:
TC: O(MCK) + O(P log P)
SC: O(C) + O(P)
K = avg skills per course
Membership checks become linear in K, which can materially increase runtime.

recommend_courses_indexed
TC: O(T) + O(U log U)
SC: O(U)
T = total index hits across all missing skills (sum of list lengths in skill_index for each missing skill), U = unique courses that matched at least one missing skill
This approach avoids scanning irrelevant courses by using the skill index. It typically performs much better than the naive approach when skills are sparse across the catalog. Worst case, if every skill maps to almost every course, T approaches M*C and the advantage shrinks.

selection_sort_recommendations
TC: O(N^2)
SC: O(N) (due to the copied list)
N = number of recommendations being sorted
Selection Sort repeatedly searches the remaining unsorted portion to find the next best item, which makes it quadratic. This is useful for demonstrating manual sorting and tie-breaking logic, but it is not competitive with Python’s built-in sorting for large N.

Built-in sorting used in both recommenders (candidates.sort(...))
TC: O(N log N)
SC: O(N) (typical auxiliary space behavior)
N = number of candidate courses being sorted
Python’s built-in sort is highly optimized (Timsort) and will generally outperform manual quadratic sorts. It also cleanly supports multi-key ordering (score descending, then title ascending) via the key function.


## Graph Implementation 
Added Utility: 
- Training Recommendations provides a list of the missing skills then asks how many recommendations you would like, providing a recommendation for courses without an easy exploration course/skill exploration feature. 
- Graph shows the missing skills and specifies a course that would provide each missing skill - showing more transparency than just "this course solves 2 gaps"


Future Considerations:
- Using a topological sort for implementing mandatory course sequences in the future
- Adding weights for the length of time or effort for each class (Getting an MD should be labeled as very intensive)
- Adding roles themselves as necessary paths to other roles, reflecting a realistic work scenario

## Data Structures Used (and Why)

### Dictionaries 
Where it appears
- `employees: Dict[str, Employee]`, `courses: Dict[str, Course]`, `roles: Dict[str, Role]` (loaded from JSON in `data_loader.py`)
- `scores: Dict[str, int]` in both recommendation algorithms (`algorithms.py`)
- `skill_index: Dict[str, List[str]]` built in `build_skill_index()` (`algorithms.py`)
- `graph.adj: Dict[str, List[str]]` adjacency list in `training_graph.py`
- `parent: Dict[str, Optional[str]]` in BFS path reconstruction (`training_graph.py`)

Why it was used
- Fast lookups by ID or key (employee ID, course ID, role ID, skill name) are central to the system’s workflow.
- Dictionaries make it easy to model “mappings” that show up naturally in this domain:
  - course_id - Course object  
  - skill - courses that teach it  
  - node - neighbors (graph adjacency list)  
  - node - parent (for shortest path reconstruction)

What was considered instead
- Lists for storing employees/courses/roles: would require O(n) searches to find a specific ID, which becomes inefficient and adds extra code complexity.
- Tuples or custom classes for indexing: less direct than a dict and typically still need a mapping structure for retrieval.


### Sets 
Where it appears
- `Employee.skills: Set[str]` (`models.py`)
- `Role.required_skills: Set[str]` (`models.py`)
- `Course.skills: Set[str]` (`models.py`)
- `missing_skills: Set[str]` outputs from `compute_skill_gaps()` (`algorithms.py`)
- `visited: Set[str]` in BFS (`training_graph.py`)

Why it was used
- Sets enforce uniqueness automatically (skills should not duplicate).
- They support efficient membership testing (`skill in course.skills`) and set operations:
  - `compute_skill_gaps()` uses set difference: `role.required_skills - employee.skills`, which is both clean and efficient.
- BFS requires a `visited` structure to avoid cycles and repeated exploration; a set provides fast “have we seen this?” checks.

What was considered instead
- Lists for skills: would allow duplicates and make membership checks slower (O(n)), which matters because membership testing is repeated inside nested loops in the naive algorithm.
- Tuples for skills: immutable and still O(n) membership checks; also not ideal when you want set operations like difference.


### Lists
Where it appears
- Recommendations output: `List[Tuple[Course, int]]` (both recommenders)
- `skill_index` values: `List[str]` of course IDs (`build_skill_index()`)
- Graph adjacency: `Dict[str, List[str]]` (neighbors list per node)
- BFS path output: `List[str]` of node IDs
- Internal workflow lists like `candidates` in recommendation functions

Why it was used
- Lists preserve ordering, which is important for:
  - returning “top N” recommendations in ranked order
  - storing graph neighbors (iterable traversal order)
  - representing a path as an ordered sequence of nodes from start to goal
- Lists work smoothly with sorting (`candidates.sort(...)`, `sorted(...)`) and slicing (`[:top_n]`).

What was considered instead
- Sets for candidates/recommendations: would remove ordering and make “top N” ranking awkward.
- Heaps / priority queues (`heapq`) for top-N selection: could reduce sorting cost for very large candidate lists, but adds complexity and is less aligned with the project’s instructional goals.
- Linked lists: not advantageous here; Python lists already perform well for iteration and sorting, which are the core operations used.


### Tuples
Where it appears
- Recommendation items are `(Course, score)` tuples: `Tuple[Course, int]`
- These tuples are stored in lists: `List[Tuple[Course, int]]`

Why it was used
- A tuple is a lightweight way to bundle two related values that travel together (the course and its coverage score).
- Tuples communicate “pairing” semantics clearly and work naturally with sorting keys like `(-x[1], x[0].title.lower())`.

What was considered instead
- Small custom class / dataclass like `Recommendation(course, score)`: more explicit, but heavier than needed for the project’s scope.
- Dictionaries per recommendation item: more verbose and typically unnecessary for a simple 2-field record.

### Queue  
Where it appears
- BFS uses `deque([start])` and `popleft()` in `bfs_shortest_path()` (`training_graph.py`)

Why it was used
- BFS requires a FIFO queue. `deque.popleft()` is O(1), which is ideal for repeated queue operations.
- This keeps BFS efficient and avoids the performance penalty of removing from the front of a normal list.

What was considered instead
- Python list as a queue: `pop(0)` is O(n), which becomes inefficient as the queue grows.
- Priority queue: not needed because the graph is unweighted and BFS already guarantees a shortest path in terms of number of edges.


### Graph via an Adjacency List 
Where it appears
- `Graph.adj: Dict[str, List[str]]` and `Graph.add_edge()` (`training_graph.py`)
- Nodes are encoded as strings like `"skill:communication"`, `"course:C01"`, `"role:R01"`

Why it was used
- The training relationships are naturally graph-shaped: skill ↔ course ↔ role.
- An adjacency list is a standard, memory-efficient representation for sparse graphs (which this is likely to be).
- It supports BFS cleanly for “shortest path” explanations (a simple training path narrative).

What was considered instead
- Adjacency matrix: simpler conceptually for very small graphs, but memory-inefficient and less practical as nodes grow.
- Edge list only: would require scanning all edges to find neighbors, making traversal slower and more complex.
- Separate bipartite structures (skill→courses and course→roles only): workable, but the explicit graph representation makes pathfinding and explanation output more general and extendable.


### Strings as Node Identifiers  
Where it appears
- Graph nodes are strings with prefixes: `"skill:<name>"`, `"course:<id>"`, `"role:<id>"`

Why it was used
- Node IDs need to be hashable and consistent across the graph, BFS, and pretty-printing.
- Prefixing prevents collisions (e.g., a skill named `"R01"` can’t be confused with role `"R01"`).

What was considered instead
- Tuples like `("skill", "communication")`: more structured, but more verbose to print and explain.
- Custom Node objects: clearer typing, but heavier and unnecessary for the project’s scale and learning objectives



# Minimal example schemas:

## employees.json
[
  {
    "id": "E001",
    "name": "Alice",
    "skills": ["communication", "customer_service", "basic_data_entry"]
  },
  {
    "id": "E002",
    "name": "Bob",
    "skills": ["data_analysis", "python", "report_writing"]
  },
  {
    "id": "E003",
    "name": "Carla",
    "skills": ["communication", "conflict_resolution", "coaching"]
  }
]

## courses.json
[
  {
    "id": "C01",
    "title": "De-escalation and Conflict Resolution",
    "skills": ["communication", "conflict_resolution"],
    "difficulty": "intermediate"
  },
  {
    "id": "C02",
    "title": "Intro to Data Analysis with Python",
    "skills": ["data_analysis", "python"],
    "difficulty": "beginner"
  },
  {
    "id": "C03",
    "title": "Coaching and Feedback for Supervisors",
    "skills": ["coaching", "communication"],
    "difficulty": "intermediate"
  },
  {
    "id": "C04",
    "title": "Applied Decision-Making in Public Service",
    "skills": ["decision_making"],
    "difficulty": "advanced"
  }
]

## roles.json

[
  {
    "id": "R01",
    "name": "Supervisor",
    "required_skills": ["communication", "conflict_resolution", "coaching", "decision_making"]
  },
  {
    "id": "R02",
    "name": "Data Analyst",
    "required_skills": ["data_analysis", "python", "report_writing"]
  }
]


