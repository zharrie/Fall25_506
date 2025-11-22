import math
from Gradebook import Gradebook

class CourseGradebook(Gradebook):
    def __init__(self):
        # Dictionary format:
        # { assignment_name : { student_ID : score } }
        self.data = {}

    # get_assignment_scores() returns a dict mapping student → score
    def get_assignment_scores(self, assignment_name):
        if assignment_name not in self.data:
            return {}
        return dict(self.data[assignment_name])

    def get_score(self, assignment_name, student_ID):
        if assignment_name in self.data:
            if student_ID in self.data[assignment_name]:
                return self.data[assignment_name][student_ID]
        return math.nan

    # sorted list of assignment names
    def get_sorted_assignment_names(self):
        return sorted(self.data.keys())

    # sorted list of all student IDs
    def get_sorted_student_IDs(self):
        all_IDs = set()
        for assignment in self.data:
            for student in self.data[assignment]:
                all_IDs.add(student)
        return sorted(all_IDs)

    # all scores for one student
    def get_student_scores(self, student_ID):
        result = {}
        for assignment in self.data:
            if student_ID in self.data[assignment]:
                result[assignment] = self.data[assignment][student_ID]
        return result

    # Set or update score
    def set_score(self, assignment_name, student_ID, score):
        # If assignment doesn't exist, create it
        if assignment_name not in self.data:
            self.data[assignment_name] = {}

        # Set the score
        self.data[assignment_name][student_ID] = score
        return True
