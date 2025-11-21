import math

class Gradebook:
    # get_score() returns the specified student's score for the specified
    # assignment. math.nan is returned if either:
    # - the assignment does not exist in the gradebook, or
    # - the assignment exists but no score exists for the specified student.
    def get_score(self, assignment_name, student_ID):
        pass
    
    # set_score() adds or updates a score in the gradebook.
    def set_score(self, assignment_name, student_ID, score):
        pass
    
    # get_assignment_scores() returns an unordered_map that maps a student ID
    # to the student's corresponding score for the specified assignment. An
    # entry exists in the returned map only if a score has been entered with
    # the set_score() method.
    def get_assignment_scores(self, assignment_name):
        pass
    
    # get_sorted_assignment_names() returns a list with all distinct assignment
    # names, sorted in ascending order.
    def get_sorted_assignment_names(self):
        pass
    
    # get_sorted_student_IDs() returns a list with all distinct student IDs,
    # sorted in ascending order.
    def get_sorted_student_IDs(self):
        pass
    
    # get_student_scores() gets all scores that exist in the gradebook for the
    # student whose ID matches the function parameter. get_student_scores()
    # returns a dictionary that maps an assignment name to the student's
    # corresponding score for that assignment.
    def get_student_scores(self, student_ID):
        pass