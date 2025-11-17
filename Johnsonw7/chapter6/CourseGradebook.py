import math
from Gradebook import Gradebook

class CourseGradebook(Gradebook):
    def __init__(self):
        self._scores = {}
    
    # get_assignment_scores() takes a string for the assignment name and
    # returns a dictionary that maps a student ID to the student's
    # corresponding score for the assignment
    def get_assignment_scores(self, assignment_name):
        if assignment_name not in self._scores:
            return{}
        return dict(self._scores[assignment_name])
    
    def get_score(self, assignment_name, student_ID):
        # Returning math.nan if no assignment yet
        if assignment_name not in self._scores:
            return math.nan

        assignment_scores = self._scores[assignment_name]

        # Returning math.nan if no student score
        if student_ID not in assignment_scores:
            return math.nan

        # If they both exist, return the score
        return assignment_scores[student_ID]


    
    # get_sorted_assignment_names() returns a list with all distinct assignment
    # names, sorted in ascending order
    def get_sorted_assignment_names(self):
        return sorted(self._scores.keys())
    
    # get_sorted_student_IDs() returns a list with all distinct student IDs,
    # sorted in ascending order.
    def get_sorted_student_IDs(self):
        student_ids = set()
        for assignment_scores in self._scores.values():
            for student_ID in assignment_scores.keys():
                student_ids.add(student_ID)
        return sorted(student_ids)
    
    # get_student_scores() gets all scores that exist in the gradebook for the
    # student whose ID equals the student_ID parameter. Scores are returned as
    # a dictionary that maps an assignment name to the student's corresponding
    # score for that assignment.
    def get_student_scores(self, student_ID):
        result = {}
        for assignment_name, assignment_scores in self._scores.items():
            if student_ID in assignment_scores:
                result[assignment_name] = assignment_scores[student_ID]

        return result
    
    def set_score(self, assignment_name, student_ID, score):
        if assignment_name not in self._scores:
            self._scores[assignment_name] = {}

        self._scores[assignment_name][student_ID] = score