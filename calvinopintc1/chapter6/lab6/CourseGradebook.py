import math
from Gradebook import Gradebook

class CourseGradebook(Gradebook):
    def __init__(self):
        # TODO: Type your code here
        #initialize a dictionary
        self.course_grades = {}
    
    
    # get_assignment_scores() takes a string for the assignment name and
    # returns a dictionary that maps a student ID to the student's
    # corresponding score for the assignment
    def get_assignment_scores(self, assignment_name):
        # TODO: Type your code here
        if assignment_name in self.course_grades:
            return self.course_grades[assignment_name]
        
        return dict()
    
    def get_score(self, assignment_name, student_ID):
        # TODO: Type your code here
        if assignment_name in self.course_grades and student_ID in self.course_grades[assignment_name]:
            return self.course_grades[assignment_name][student_ID]
        return math.nan
    
    # get_sorted_assignment_names() returns a list with all distinct assignment
    # names, sorted in ascending order
    def get_sorted_assignment_names(self):
        # TODO: Type your code here
        sorted_assignment_list = []
        
        for i in self.course_grades:
            sorted_assignment_list.append(i)
        
        sorted_assignment_list.sort()
        return sorted_assignment_list


    # get_sorted_student_IDs() returns a list with all distinct student IDs,
    # sorted in ascending order.
    def get_sorted_student_IDs(self):
        # TODO: Type your code here
        sorted_ID_list = []
        
        for i in self.course_grades:
            assignment_name_values = self.course_grades[i]
            for j in assignment_name_values:
                if j not in sorted_ID_list:
                    sorted_ID_list.append(j)
        
        sorted_ID_list.sort()
        return sorted_ID_list
    
    # get_student_scores() gets all scores that exist in the gradebook for the
    # student whose ID equals the student_ID parameter. Scores are returned as
    # a dictionary that maps an assignment name to the student's corresponding
    # score for that assignment.
    def get_student_scores(self, student_ID):
        # TODO: Type your code here
        students_grades = {}

        for i in self.course_grades:
            assignment_name_values = self.course_grades[i]
            for j in assignment_name_values:
                if j == student_ID:
                    students_grades[i] = assignment_name_values[j]

        return students_grades
    
    def set_score(self, assignment_name, student_ID, score):
        # TODO: Type your code here
        if assignment_name not in self.course_grades:
            self.course_grades[assignment_name] = {}

        self.course_grades[assignment_name][student_ID] = score        



        
        
