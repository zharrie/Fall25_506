import math
from Gradebook import Gradebook

class CourseGradebook(Gradebook):
    def __init__(self):
        self.students = {}
    
    # get_assignment_scores() takes a string for the assignment name and
    # returns a dictionary that maps a student ID to the student's
    # corresponding score for the assignment
    def get_assignment_scores(self, assign_id):
        # create a list of student ids that have the assignment
        s_ids = list(filter(lambda id: assign_id in self.students[id], self.students.keys()))
        # return a new map with all the ids of those students and their score on the assignment
        return {id: self.students[id][assign_id] for id in s_ids}
    
    def get_score(self, assign_id, stu_id):
        if stu_id not in self.students or assign_id not in self.students[stu_id]:
            return math.nan
        return self.students[stu_id][assign_id]
    
    # get_sorted_assignment_names() returns a list with all distinct assignment
    # names, sorted in ascending order
    def get_sorted_assignment_names(self):
        return sorted( # sort the list
            list( # convert to list for sorting
                set( # convert to set to remove duplicates
                    sum( # trick to flatten a list of lists - add them all together
                        map(lambda v: list(v.keys()), self.students.values()) # map the list of assignment lists to a list of the assignment names
                        , []
                        )
                    )
                )
            )
    
    # get_sorted_student_IDs() returns a list with all distinct student IDs,
    # sorted in ascending order.
    def get_sorted_student_IDs(self):
        return sorted(self.students.keys())
    
    # get_student_scores() gets all scores that exist in the gradebook for the
    # student whose ID equals the stu_id parameter. Scores are returned as
    # a dictionary that maps an assignment name to the student's corresponding
    # score for that assignment.
    def get_student_scores(self, stu_id):
        return self.students[stu_id]
    
    def set_score(self, assign_id, stu_id, score):
        if stu_id not in self.students:
            self.students[stu_id] = {}
        self.students[stu_id][assign_id] = score