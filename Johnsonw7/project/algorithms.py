# Algorithms.py

from typing import Dict, List, Set, Tuple
#Typing module helps "hint" the expected types of variables and function return values for better code readability and maintainability.
from models import Employee, Course, Role
"""
Typing - helpers for type annotations (tuple is like a cluster of ordered objects)
Models - Importing our key data structures
"""

def compute_skill_gaps(employee: Employee, role: Role) -> Set[str]:
    """
    Return the set of skills that the employee is missing for the given role.
    """
    # This subtracts the set of skills the employee has from the set of skills required by the role,
    # resulting in the set of skills that the employee is missing.
    return role.required_skills - employee.skills


# This function builds a dict that maps skills to the list of course IDs that teach those skills.
def build_skill_index(courses: Dict[str, Course]) -> Dict[str, List[str]]:
    """
    Build a mapping from skill -> list of course IDs that teach that skill.
    """
    # Initialize an empty index
    index: Dict[str, List[str]] = {}
    # Iterate through all courses and their skills to populate the index
    for course in courses.values():
        # For each skill taught by the course, add the course ID to the index
        for skill in course.skills:
            # Use setdefault to initialize the list if the skill is not already in the index
            # Use append to add the course ID to the list for this skill
            index.setdefault(skill, []).append(course.id)
            # This ensures that each skill maps to a list of course IDs that teach it
    return index
    # The resulting index allows for quick way to find courses by skill.


def recommend_courses_naive(
    # Naive recommendation algorithm. This means it checks every course for every missing skill.
    # It does not use any indexing or optimization.
    missing_skills: Set[str],
    # A set of skills that the employee is missing.
    courses: Dict[str, Course],
    # A dictionary of all available courses, keyed by course ID.
    top_n: int = 5,
    # The number of top course recommendations to return. Here, it defaults to 5.
) -> List[Tuple[Course, int]]:
    # Returns a list of tuples, each containing a Course object and its score (aka, the number of missing skills it covers).
    """
    Naive recommendation algorithm:
    For each course, count how many missing skills it covers.
    Return top_n courses with highest coverage.
    """
    # Initialize scores for each course
    # These scores will count how many missing skills each course can help with
    scores: Dict[str, int] = {course_id: 0 for course_id in courses.keys()}
    # Count how many missing skills each course covers
    for skill in missing_skills:
        # Iterate through all courses to see if they cover the skill
        for course_id, course in courses.items():
            # If the course teaches the missing skill, increment its score
            if skill in course.skills:
                # Increment the score for this course
                scores[course_id] += 1
                # This counts how many of the missing skills each course can help with

    # Filter courses that cover at least one missing skill
    candidates = [(courses[cid], score) for cid, score in scores.items() if score > 0]
    # Create a list of (Course, score) tuples for courses that have a non-zero score
    
    # Sort course candidates found above by score descending (-x[1]),
    # then if tied, it orders by ascending titles (x[0].title.lower)
    # key = lambda x means we define an anonymous function that takes one argument x (which is a tuple of (Course, score))
    #title.lower() is used to ensure the sorting is case-insensitive
    candidates.sort(key=lambda x: (-x[1], x[0].title.lower()))
    return candidates[:top_n]
    #Return the top_n courses from the sorted list

# Indexed recommendation algorithm. This means it uses a pre-built index to quickly find relevant courses.
def recommend_courses_indexed(
    missing_skills: Set[str],
    # A set of skills that the employee is missing.
    courses: Dict[str, Course],
    # A dictionary of all available courses, keyed by course ID.
    skill_index: Dict[str, List[str]],
    # A pre-built index mapping skills to lists of course IDs that teach those skills.
    top_n: int = 5,
    # The number of top recommendations to return. Here, it defaults to 5.
) -> List[Tuple[Course, int]]:
    # Returns a list of tuples, each containing a Course object and its score (the number of missing skills it covers).
    # This function leverages the skill_index to only consider courses that are relevant to the missing skills.
    # This makes it more efficient than the naive approach.
    # It counts how many missing skills each relevant course covers and returns the top_n courses.
    """
    Indexed recommendation algorithm:
    Use skill_index (skill -> [course_ids]) to only inspect relevant courses.
    """
    # Initialize scores for relevant courses
    #Dict[str, int]: A dictionary mapping course IDs to their scores.
    scores: Dict[str, int] = {}
    # for each missing skill, look up relevant courses in the skill index
    for skill in missing_skills:
        # For each missing skill, get the list of course IDs that teach that skill
        for course_id in skill_index.get(skill, []):
            # Increment the score for this course
            # scores.get(course_id, 0) retrieves the current score for the course_id, defaulting to 0 if it doesn't exist
            scores[course_id] = scores.get(course_id, 0) + 1
            # This counts how many of the missing skills each relevant course can help with
# Filter courses that cover at least one missing skill
    candidates = [(courses[cid], score) for cid, score in scores.items() if score > 0]
    # Create a list of (Course, score) tuples for courses that have a non-zero score
    candidates.sort(key=lambda x: (-x[1], x[0].title.lower()))
# Sort the candidates first by score (in descending order) and then by course title (in ascending order, case-insensitive)
    return candidates[:top_n]
    # Return the top_n courses from the sorted list

# Sorting algorithm using Selection Sort for educational purposes.
# This is because Selection Sort is not efficient for large datasets compared to built-in sorting methods.
# Selection sort's time complexity is O(n^2), making it impractical for large lists
#Whereas Python's built-in sort is implemented using Timsort, which has a time complexity of O(n log n) worst case
def selection_sort_recommendations(
    # A list of (Course, score) tuples to be sorted.
    recs: List[Tuple[Course, int]]
    # The function returns a new list of (Course, score) tuples sorted by score descending, then by title ascending.
) -> List[Tuple[Course, int]]:
# Implements Selection Sort to sort the recommendations.
    """
    Sort recommendations using Selection Sort
    Orders by score descending, then by title ascending
    """
    # Make a copy to avoid mutating the input list of course recommendations
    recs_copy = recs[:]
    # Get the length of the list
    n = len(recs_copy)
    # Perform Selection Sort
    for i in range(n):
        # Find the index of the max element in the remaining unsorted portion
        max_idx = i
        # Iterate through the unsorted portion of the list
        for j in range(i + 1, n):
            # Compare scores and titles for tie-breaking
            score_j = recs_copy[j][1]
            # Acknowledge score of current max
            score_max = recs_copy[max_idx][1]
            # Update max_idx if a higher score is found or if there's a tie with the "dictionary ordering" of a title
            if score_j > score_max:
                max_idx = j
                # Found a new maximum score
            elif score_j == score_max:
                # Tie-break by title
                # If the title of recs_copy[j] comes sooner in "dictionary order" than that of recs_copy[max_idx]
                if recs_copy[j][0].title.lower() < recs_copy[max_idx][0].title.lower():
                    # Update max_idx to the current index j
                    max_idx = j
                    # Found a tie in score, but recs_copy[j] has an earlier title in dictionary order
        # Swap the found max element with the first element of the unsorted portion
        # Only swap if max_idx is different from i
        # This places the highest scoring course at the current position i
        # Swap only if needed
        # This avoids unnecessary swaps when the max element is already in the correct position
        
        if max_idx != i:
            #With a tuple swap, there is no need for a temp variable risking data loss
            recs_copy[i], recs_copy[max_idx] = recs_copy[max_idx], recs_copy[i]
            # Swap the elements at indices i and max_idx
            # This places the highest scoring course at the current position i
            # Swap only if needed
            # This avoids unnecessary swaps when the max element is already in the correct position
            # Swap the elements at indices i and max_idx
    return recs_copy
    # Return the sorted list
