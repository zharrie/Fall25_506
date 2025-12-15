# recommender.py

import time
#imports Python’s built-in time module, which provides functions related to time
from typing import Dict, List, Tuple, Set, Optional
#imports several type hinting constructs from Python's built-in typing module; used for readability and maintainability of the code
# Dict, List, Tuple, Set, and Optional are used to specify the expected types of variables and function return values throughout the code.  

# Importing our data models
from models import Employee, Course, Role
#imports three classes (Employee, Course, Role) from models.py; these classes represent the core entities in the training recommendation system.
from algorithms import (
    # Functions imported from algorithms.py to be used in the TrainingRecommender class.
    compute_skill_gaps,
    build_skill_index,
    recommend_courses_naive,
    recommend_courses_indexed,
    selection_sort_recommendations,
)
from training_graph import build_training_graph, bfs_shortest_path, Graph
# Imports functions and a type (Graph) from training_graph.py to handle graph-based training paths.

# For building and using the training graph
from training_graph import build_training_graph, bfs_shortest_path, Graph

# Build training recommender service object
class TrainingRecommender:
    # Main class for recommending training courses based on skill gaps.
    def __init__(
        self,
        employees: Dict[str, Employee],
        courses: Dict[str, Course],
        roles: Dict[str, Role],
    ):
        self.employees = employees
        self.courses = courses
        self.roles = roles

        # Hash-based index for fast recommendation
        self.skill_index = build_skill_index(courses)

        # Graph structure for training paths: skill -> course -> role
        self.graph: Graph = build_training_graph(courses, roles)

    # --- Basic lookup and listing ---
    # This function retrieves an Employee object by its ID. 
    def get_employee(self, emp_id: str) -> Optional[Employee]:
        return self.employees.get(emp_id)
    #This function retrieves a Role object by its ID.
    def get_role(self, role_id: str) -> Optional[Role]:
        return self.roles.get(role_id)
    #This function retrieves a Course object by its ID.
    def list_employees(self) -> List[Employee]:
        return sorted(self.employees.values(), key=lambda e: e.id)
    #This function retrieves a list of all Role objects, sorted by their IDs.
    def list_roles(self) -> List[Role]:
        return sorted(self.roles.values(), key=lambda r: r.id)
    #This function retrieves a list of all Course objects, sorted by their IDs.
    def list_courses(self) -> List[Course]:
        return sorted(self.courses.values(), key=lambda c: c.id)

    # --- Skill gap analysis ---
    # This function returns the skill gaps for a given employee and role.
    # emp: Employee object representing the employee whose skill gaps are to be analyzed. This is in the .py file named algorithms.py
    # role: Role object representing the target role for which skill gaps are to be determined. This is in the .py file named algorithms.py
    # compute_skill_gaps: This function is imported from algorithms.py 
    def analyze_gaps(self, emp: Employee, role: Role) -> Set[str]:
        return compute_skill_gaps(emp, role)

    # --- Recommendation algorithms ---


    def recommend(
        self,
        missing_skills: Set[str],
        top_n: int = 5
    ) -> Dict[str, List[Tuple[Course, int]]]:
        """
        Run both naive and indexed recommendation algorithms and return their results.
        """
        naive_recs = recommend_courses_naive(missing_skills, self.courses, top_n=top_n)
        indexed_recs = recommend_courses_indexed(
            missing_skills, self.courses, self.skill_index, top_n=top_n
        )
        return {
            "naive": naive_recs,
            "indexed": indexed_recs,
        }

    # --- Algorithm comparison (time) ---

    # This function compares the average run time of naive vs indexed recommendation algorithms.
    # It runs each algorithm a specified number of times (repeats) and calculates the average execution time for each.
    # The results are returned in a dictionary format, showing the average time taken by each algorithm in seconds.
    # This comparison is useful for evaluating the performance of the two recommendation approaches.
    # missing_skills: A set of skills that the employee is missing, found in algorithms.py
    # repeats: The number of times to repeat each algorithm for averaging the run time. Defaults to 100.
    # Returns a dictionary with average run times for both algorithms.
    def compare_algorithms(self, missing_skills: Set[str], repeats: int = 100) -> dict:
        """
        Compare average run time of naive vs indexed recommendation over a number of repeats.
        This is for educational / experimental purposes.
        """
        # Warm up
        # We run each algorithm once before timing to ensure any initial setup costs are excluded from the timing.
        # This helps in getting a more accurate measurement of the average execution time.
        recommend_courses_naive(missing_skills, self.courses)
        recommend_courses_indexed(missing_skills, self.courses, self.skill_index)

        # Timing
        start = time.perf_counter()
        # We use time.perf_counter() to get a high-resolution timer for measuring the execution time.
        # It provides a more precise measurement compared to other time functions.
        # We run the naive recommendation algorithm the specified number of times (repeats)
        # and measure the total time taken for all runs.
        # This total time is then used to calculate the average time per run (lower down in code, avg_naive).
       
        for _ in range(repeats):
            recommend_courses_naive(missing_skills, self.courses)
        # Save the difference in time after operation
        naive_time = time.perf_counter() - start

        # The same process is repeated for the indexed recommendation algorithm.
        # This allows us to compare the performance of both algorithms under the same conditions.
        # Finally, we calculate the average time taken by each algorithm and return the results in a dictionary.
        start = time.perf_counter()
        for _ in range(repeats):
            recommend_courses_indexed(missing_skills, self.courses, self.skill_index)
        indexed_time = time.perf_counter() - start

        # Calculate averages
        avg_naive = naive_time / repeats
        avg_indexed = indexed_time / repeats

        # Return results
        return {
            "avg_naive_seconds": avg_naive,
            "avg_indexed_seconds": avg_indexed,
        }

    # --- Algorithm comparison (sorting) ---
    # This function compares the average run time of Python's built-in sort vs a custom selection sort on the same recommendation list.
    # It runs each sorting method a specified number of times (repeats) and calculates the average execution time for each.
    # The results are returned in a dictionary format, showing the average time taken by each sorting method in seconds.
    # This comparison is useful for evaluating the performance of the two sorting approaches.
    # missing_skills: A set of skills that the employee is missing, found in algorithms.py
    # top_n: The number of top recommendations to consider for sorting. Defaults to 10.
    # repeats: The number of times to repeat each sorting method for averaging the run time. Defaults to 100.
   
    def compare_sorts(self, missing_skills: Set[str], top_n: int = 10, repeats: int = 100) -> dict:
        """
        Compare built-in sort vs selection sort on the same recommendation list.
        """
        # Get base recommendations using indexed algorithm
        # We first obtain the output from recommend_courses_indexed function, which is defined in algorithms.py.
        # This list is then used as the input for both sorting methods being compared.
        # This ensures that both sorting methods are tested on the same data set.
        # The base_recs variable holds the list of recommended courses along with their scores. 

        base_recs = recommend_courses_indexed(
            missing_skills, self.courses, self.skill_index, top_n=top_n
        )

        # Timing built-in sort
        # We measure the time taken by Python's built-in sort method to sort the list of recommendations.
        # The sorting is done based on the score (in descending order) and then by course title (in ascending order, case-insensitive).
        # This is repeated the specified number of times (repeats) to get an average time.
        # The total time taken for all runs is recorded and used to calculate the average time per run.
        start = time.perf_counter()
        for _ in range(repeats):
            _ = sorted(
                base_recs,
                key=lambda x: (-x[1], x[0].title.lower()),
            )
        builtin_time = time.perf_counter() - start

        # Timing selection sort
        # We measure the time taken by the custom selection sort function to sort the same list of recommendations.
        # Similar to the built-in sort timing, this is also repeated the specified number of times (repeats).
        # The total time taken for all runs is recorded and used to calculate the average time per run.
        # This allows us to directly compare the performance of the two sorting methods.
        start = time.perf_counter()
        for _ in range(repeats):
            _ = selection_sort_recommendations(base_recs)
        selection_time = time.perf_counter() - start
        # Return averages
        # The average times for both sorting methods are calculated by dividing the total time by the number of repeats.
        # These averages are then returned in a dictionary format for easy comparison.
        # This provides insights into the efficiency of each sorting method.
        return {
            "avg_builtin_seconds": builtin_time / repeats,
            "avg_selection_seconds": selection_time / repeats,
        }

    # --- Graph-based training paths ---
    #This function finds the shortest path from a missing skill to a target role using the training graph.
    # It returns a list of node IDs representing the path, or None if no path is found.
    # The path typically includes the skill node, course node, and role node.
    # This is useful for visualizing how taking certain courses can help an employee acquire the skills needed for a specific role.
    def get_training_path_for_skill(
        self,
        skill_name: str,
        role: Role,
    ) -> Optional[List[str]]:
        """
        Use the graph to find a shortest path from a missing skill to the target role.

        Returns a list of node IDs, e.g.:
            ["skill:conflict_resolution", "course:C01", "role:R01"]
        or None if no path is found.
        """
        # Clean skill name by taking out extra spaces and converting to lowercase
        skill_name_clean = skill_name.strip().lower()
        # Define start and goal nodes in the graph
        start = f"skill:{skill_name_clean}"
        goal = f"role:{role.id}"
        #bfs_shortest_path is imported from training_graph.py
        # It performs a breadth-first search on the graph to find the shortest path from start to goal.
        return bfs_shortest_path(self.graph, start, goal)