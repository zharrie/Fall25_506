from Gradebook import Gradebook
from CourseGradebook import CourseGradebook

class TestUtility:
    # Populates a CourseGradebook from a list of rows. Each row is a list of
    # strings. Row 0 must be the header row. Column 0 must be the student ID
    # column.
    @staticmethod
    def populate_gradebook_from_rows(gradebook, rows):
        # Iterate through non-header rows
        for row_index in range(1, len(rows)):
            row = rows[row_index]
            
            # Parse out student ID first
            student_ID = int(row[0])
            
            # Call set_score for each non-empty entry
            for col_index in range(1, len(row)):
                entry = row[col_index]
                if len(entry) > 0:
                    # Get the assignment name from the header row
                    assignment_name = rows[0][col_index]
                    
                    # Convert score from string to float
                    score = float(entry)
                    
                    # Add to gradebook
                    gradebook.set_score(assignment_name, student_ID, score)
    
    # Returns a sample gradebook to use for testing purposes.
    @staticmethod
    def make_sample_gradebook():
        rows = []
        rows.append([ "Student ID", "Homework 1", "Homework 2", "Midterm", "Homework 3", "Homework 4", "Course project", "Final exam" ])
        rows.append([ "11111",      "92",         "89",         "91",      "100",         "100",        "100",           "95" ])
        rows.append([ "22222",      "",           "75",         "77.5",    "80.5",        "81",         "60",            "54" ])
        rows.append([ "33333",      "100",        "100",        "88",      "100",         "100",        "90",            "77.5" ])
        rows.append([ "44444",      "60",         "50",         "40",      "30",          "",           "",              "" ])
        rows.append([ "55555",      "73.5",       "76.5",       "64.5",    "71.5",        "77.5",       "87",            "63.5" ])
        rows.append([ "66666",      "82.5",       "84.5",       "91",      "92.5",        "86",         "0",             "97" ])
        rows.append([ "77777",      "77",         "76",         "75",      "74",          "73",         "72",            "71" ])
        rows.append([ "88888",      "64.5",       "74.5",       "88",      "84",          "84",         "85.5",          "81.5" ])
        rows.append([ "99999",      "100",        "100",        "88",      "100",         "100",        "80",            "79" ])
        rows.append([ "10000",      "88",         "90",         "92",      "87",          "88.5",       "77.5",          "90" ])
        rows.append([ "90000",      "80",         "85",         "90",      "95",          "100",        "85",            "94.5" ])
        
        gradebook = CourseGradebook()
        TestUtility.populate_gradebook_from_rows(gradebook, rows)
        return gradebook