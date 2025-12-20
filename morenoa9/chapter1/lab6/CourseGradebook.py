import math
from Gradebook import Gradebook

class CourseGradebook(Gradebook):
    def __init__(self):
        # TODO: Type your code here
        pass
    
    # get_assignment_scores() takes a string for the assignment name and
    # returns a dictionary that maps a student ID to the student's
    # corresponding score for the assignment
    def get_assignment_scores(self, assignment_name):
        # TODO: Type your code here
        return dict()
    
    def get_score(self, assignment_name, student_ID):
        # TODO: Type your code here
        return math.nan
    
    # get_sorted_assignment_names() returns a list with all distinct assignment
    # names, sorted in ascending order
    def get_sorted_assignment_names(self):
        # TODO: Type your code here
        return []
    
    # get_sorted_student_IDs() returns a list with all distinct student IDs,
    # sorted in ascending order.
    def get_sorted_student_IDs(self):
        # TODO: Type your code here
        return []
    
    # get_student_scores() gets all scores that exist in the gradebook for the
    # student whose ID equals the student_ID parameter. Scores are returned as
    # a dictionary that maps an assignment name to the student's corresponding
    # score for that assignment.
    def get_student_scores(self, student_ID):
        # TODO: Type your code here
        return dict()
    
    def set_score(self, assignment_name, student_ID, score):
        # TODO: Type your code here
        pass