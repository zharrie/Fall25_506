import math
from Gradebook import Gradebook

class CourseGradebook(Gradebook):
    def __init__(self):
        # TODO: Type your code here
        # Make entries a dictionary like
        # {
        #     ("midterm", 123) = 92.0,
        #     ("final", 456) = 95.0,   
        # }
        self.gradebook_entries = {}
    
    # get_assignment_scores() takes a string for the assignment name and
    # returns a dictionary that maps a student ID to the student's
    # corresponding score for the assignment
    def get_assignment_scores(self, assignment_name):
        # TODO: Type your code here
        #creating an empty dictionary called assignment scores
        assignment_scores = {}
        #default behavior is to loop through keys, not values
        for key in self.gradebook_entries:
            #for each key, assign what is in initial spot in key-tuple as this_assignment_name
            this_assignment_name = key[0]
            #for each key, assign what is in next spot in key-tuple as this_student_ID
            this_student_ID = key[1]
            #check if this_assignment_name equals the assignment name you want to find
            if this_assignment_name == assignment_name:
                #if yes, then look up value associated with that key and assign it to this_score
                this_score = self.gradebook_entries[key]
                #fill in the empty dict, assignment_scores, for this assignment
                #Start by specifying the key for this dict, which is this_student_ID
                #This is what is on left side. Then assign value of this_score 
                assignment_scores[this_student_ID] = this_score
        return assignment_scores
    
    def get_score(self, assignment_name, student_ID):
        # TODO: Type your code here
        gradebook_key = (assignment_name, student_ID)
        if gradebook_key in self.gradebook_entries:
            return self.gradebook_entries[gradebook_key]
        else:
            return math.nan
    
    # get_sorted_assignment_names() returns a list with all distinct assignment
    # names, sorted in ascending order
    def get_sorted_assignment_names(self):
        # TODO: Type your code here
        list_distinct_assignments = []
        for key in self.gradebook_entries:
          #for each key, assign what is in initial spot in key-tuple as this_assignment_name
            this_assignment_name = key[0]
            #for each key, assign what is in next spot in key-tuple as this_student_ID
            this_student_ID = key[1]
            if this_assignment_name not in list_distinct_assignments:
                list_distinct_assignments.append(this_assignment_name)
        return sorted(list_distinct_assignments)
    
    # get_sorted_student_IDs() returns a list with all distinct student IDs,
    # sorted in ascending order.
    def get_sorted_student_IDs(self):
        # TODO: Type your code here
        list_distinct_students = []
        for key in self.gradebook_entries:
          #for each key, assign what is in initial spot in key-tuple as this_assignment_name
            this_assignment_name = key[0]
            #for each key, assign what is in next spot in key-tuple as this_student_ID
            this_student_ID = key[1]
            if this_student_ID not in list_distinct_students:
                list_distinct_students.append(this_student_ID)
        return sorted(list_distinct_students)

    
    # get_student_scores() gets all scores that exist in the gradebook for the
    # student whose ID equals the student_ID parameter. Scores are returned as
    # a dictionary that maps an assignment name to the student's corresponding
    # score for that assignment.
    def get_student_scores(self, student_ID):
        # TODO: Type your code here
        student_scores = {}
        #default behavior is to loop through keys, not values
        for key in self.gradebook_entries:
            #for each key, assign what is in initial spot in key-tuple as this_assignment_name
            this_assignment_name = key[0]
            #for each key, assign what is in next spot in key-tuple as this_student_ID
            this_student_ID = key[1]
            #check if this_student_ID equals the student_ID you want to find
            if this_student_ID == student_ID:
                #if yes, then look up value associated with that key and assign it to this_score
                this_score = self.gradebook_entries[key]
                #fill in the empty dict, student_scores, for this assignment
                #Start by specifying the key for this dict, which is this_student_ID
                #This is what is on left side. Then assign value of this_score 
                student_scores[this_assignment_name] = this_score
        return student_scores
    
    def set_score(self, assignment_name, student_ID, score):
        self.gradebook_entries[(assignment_name, student_ID)] = score