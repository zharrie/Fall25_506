import math
from Gradebook import Gradebook

class CourseGradebook(Gradebook):
    def __init__(self):
        # TODO: Type your code here
        self.student_grades = {}
        pass
    
    # get_assignment_scores() takes a string for the assignment name and
    # returns a dictionary that maps a student ID to the student's
    # corresponding score for the assignment
    def get_assignment_scores(self, assignment_name):
        # TODO: Type your code here

        if assignment_name in self.student_grades:
            return self.student_grades[assignment_name]
        
        #return dict()
    
    def get_score(self, assignment_name, student_ID):
        # TODO: Type your code here

        if assignment_name in self.student_grades:
            if student_ID in self.student_grades[assignment_name]:
                return self.student_grades[assignment_name][student_ID]

        return math.nan
    
    # get_sorted_assignment_names() returns a list with all distinct assignment
    # names, sorted in ascending order
    def get_sorted_assignment_names(self):
        # TODO: Type your code here
        assignments = []
        for key in self.student_grades.keys():
            assignments.append(key)
        assignments.sort()

        return assignments

    
    # get_sorted_student_IDs() returns a list with all distinct student IDs,
    # sorted in ascending order.
    def get_sorted_student_IDs(self):
        # TODO: Type your code here

        ids = []
        for a,v in self.student_grades.items():
            for i in v:
                ids.append(i)

        ids = list(set(ids))
        ids.sort()

        return ids
    
    # get_student_scores() gets all scores that exist in the gradebook for the
    # student whose ID equals the student_ID parameter. Scores are returned as
    # a dictionary that maps an assignment name to the student's corresponding
    # score for that assignment.
    def get_student_scores(self, student_ID):
        # TODO: Type your code here
        id_to_grade = {}

        for entry in self.student_grades:
            result = self.student_grades[entry]
            
            for ID in result:
                if ID == student_ID:
                    id_to_grade[entry] = result[ID]

        return id_to_grade
    
    def set_score(self, assignment_name, student_ID, score):
        # TODO: Type your code here
        if assignment_name not in self.student_grades:
            self.student_grades[assignment_name] = {}
        self.student_grades[assignment_name][student_ID] = score

        pass