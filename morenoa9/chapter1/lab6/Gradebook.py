import math
from Gradebook import Gradebook

class CourseGradebook(Gradebook):
    def __init__(self):
        self.data ={}
    
    
    def get_assignment_scores(self, assignment_name):
        if assignment_name not in self.data:
            return {}

        return dict(self.data[assignment_name])
    
    def get_score(self, assignment_name, student_ID):
        if assignment_name not in self.data:
            return math.nan
        if student_ID not in self.data[assignment_name]:
            return math.nan
        return self.data[assignment_name][student_ID]
    
    # get_sorted_assignment_names() returns a list with all distinct assignment
    # names, sorted in ascending order
    def get_sorted_assignment_names(self):
        return sorted(self.data.keys())
    
    # get_sorted_student_IDs() returns a list with all distinct student IDs,
    # sorted in ascending order.
    def get_sorted_student_IDs(self):
        student_ids= set()
        for scores_students in self.data.values():
            student_ids.update(scores_students.keys())
        return sorted(student_ids)
    
    # get_student_scores() gets all scores that exist in the gradebook for the
    # student whose ID equals the student_ID parameter. Scores are returned as
    # a dictionary that maps an assignment name to the student's corresponding
    # score for that assignment.
    def get_student_scores(self, student_ID):
        result= {}
        for assignment_name,scores_students in self.data.items():
            if student_ID in scores_students:
                result[assignment_name]= scores_students[student_ID]
        return result
    
    def set_score(self, assignment_name, student_ID, score):
        if assignment_name not in self.data:
            self.data[assignment_name]= {}

        self.data[assignment_name][student_ID]= score