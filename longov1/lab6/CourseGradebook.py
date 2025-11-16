import math
from Gradebook import Gradebook

class CourseGradebook(Gradebook):
    def __init__(self):
        # TODO: Type your code here
        self.grades = {}
        pass
    
    # get_assignment_scores() takes a string for the assignment name and
    # returns a dictionary that maps a student ID to the student's
    # corresponding score for the assignment
    def get_assignment_scores(self, assignment_name):
        # TODO: Type your code here
        #return dict()
        return self.grades.get(assignment_name, {})
    
    def get_score(self, assignment_name, student_ID):
        # TODO: Type your code here
        if assignment_name not in self.grades:
            return math.nan

        if student_ID not in self.grades[assignment_name]:
            return math.nan
        
        #return math.nan
        return self.grades[assignment_name][student_ID]
    
    # get_sorted_assignment_names() returns a list with all distinct assignment
    # names, sorted in ascending order
    def get_sorted_assignment_names(self):
        # TODO: Type your code here
        return sorted(self.grades.keys())
        #return []
    
    # get_sorted_student_IDs() returns a list with all distinct student IDs,
    # sorted in ascending order.
    def get_sorted_student_IDs(self):
        # TODO: Type your code here
        student_ids = set()

        for assignment_scores in self.grades.values():
            for student_ID in assignment_scores.keys():
                student_ids.add(student_ID)
        #return []
        return sorted(student_ids)
    
    # get_student_scores() gets all scores that exist in the gradebook for the
    # student whose ID equals the student_ID parameter. Scores are returned as
    # a dictionary that maps an assignment name to the student's corresponding
    # score for that assignment.
    def get_student_scores(self, student_ID):
        # TODO: Type your code here
        student_scores = {}

        for assignment_name in self.grades:
            if student_ID in self.grades[assignment_name]:
                student_scores[assignment_name] = self.grades[assignment_name][student_ID]
        #return dict()
        return student_scores
    
    def set_score(self, assignment_name, student_ID, score):
        # TODO: Type your code here
        if assignment_name not in self.grades:
            self.grades[assignment_name] = {}
        
        self.grades[assignment_name][student_ID] = score
        pass