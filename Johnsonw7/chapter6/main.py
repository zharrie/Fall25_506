import math
from Gradebook import Gradebook
from CourseGradebook import CourseGradebook
from TestUtility import TestUtility

def test_get_score_and_set_score():
    print("\n---- test_get_score_and_set_score() ----")
    
    # Create a gradebook with sample data for testing
    gradebook = TestUtility.make_sample_gradebook()
    
    # Each test case is a (assignmentName, studentID, expectedScore) tuple
    test_cases = [
        ("Midterm", 11111, 91.0),
        ("Homework 1", 22222, math.nan), # no entry
        ("Homework 3", 55555, 71.5),
        ("Course project", 66666, 0.0),
        ("Homework 2", 10000, 90.0),
        ("Homework 4", 55555, 77.5),
        ("Homework 5", 33333, math.nan), # no such assignment
        ("Final exam", 44444, math.nan), # no entry
        ("Homework 2", 77777, 76.0),
        ("Homework 1", 88888, 64.5)
    ]
    
    # Iterate through test cases
    for test_case in test_cases:
        assignment_name = test_case[0]
        student_ID = test_case[1]
        expected = test_case[2]
        actual = gradebook.get_score(assignment_name, student_ID)
        
        # Reminder: Can't compare NaN with ==, so a special case is needed
        are_equal = False
        if math.isnan(expected):
            are_equal = math.isnan(actual)
        else:
            are_equal = (actual == expected)
        
        if are_equal:
            print(f'PASS: get_score("{assignment_name}", ', end="")
            print(f"{student_ID}) returned {actual}")
        else:
            print(f'FAIL: get_score("{assignment_name}", ', end="")
            print(f"{student_ID}) returned {actual}, ", end="")
            print(f"but expected is {expected}")
            return False
    
    return True

def test_get_assignment_scores():
    print("\n---- test_get_assignment_scores() ----")
    
    # Create a gradebook with sample data for testing
    gradebook = TestUtility.make_sample_gradebook()
    
    hw2_scores = {
        11111: 89.0,
        22222: 75.0,
        33333: 100.0,
        44444: 50.0,
        55555: 76.5,
        66666: 84.5,
        77777: 76.0,
        88888: 74.5,
        99999: 100.0,
        10000: 90.0,
        90000: 85.0
    }
    midterm_scores = {
        11111: 91.0,
        22222: 77.5,
        33333: 88.0,
        44444: 40.0,
        55555: 64.5,
        66666: 91.0,
        77777: 75.0,
        88888: 88.0,
        99999: 88.0,
        10000: 92.0,
        90000: 90.0
    }
    project_scores = {
        11111: 100.0,
        22222: 60.0,
        33333: 90.0,
        #44444: 80.0, # no entry for student 44444
        55555: 87.0,
        66666: 0.0,
        77777: 72.0,
        88888: 85.5,
        99999: 80.0,
        10000: 77.5,
        90000: 85.0
    }
    
    # Each test case is a (assignment_name, expected_scores_dictionary) pair
    test_cases = [
        ("Homework 2", hw2_scores),
        ("Midterm", midterm_scores),
        ("Course project", project_scores)
    ]
    
    # Iterate through all test cases
    for test_case in test_cases:
        assignment_name = test_case[0]
        expected_dictionary = test_case[1]
        
        # Get the actual dictionary from the gradebook
        print(f'Calling get_assignment_scores("{assignment_name}")')
        actual_dictionary = gradebook.get_assignment_scores(assignment_name)
        
        # Compare lengths first
        if len(expected_dictionary) != len(actual_dictionary):
            print(f'FAIL: get_assignment_scores("{assignment_name}")', end="")
            print(" returned a dictionary with ", end="")
            if 1 == len(actual_dictionary):
                print("1 score, ", end="")
            else:
                print(f"{len(actual_dictionary)} scores, ", end="")
            print(f"but the expected dictionary has " +
                f"{len(expected_dictionary)} scores")
            return False
        
        # Sizes are equal, so now compare each ID/score pair
        for student_ID in expected_dictionary:
            if student_ID not in actual_dictionary:
                print(f'FAIL: get_assignment_scores("{assignment_name}")', end="")
                print(f" returned a dictionary that is missing an entry ", end="")
                print(f"for student ID {student_ID}")
                return False
            
            # actual_dictionary has student ID, so now compare corresponding
            # score
            expected_score = expected_dictionary[student_ID]
            actual_score = actual_dictionary[student_ID]
            are_equal = False
            if math.isnan(expected_score):
                are_equal = math.isnan(actual_score)
            else:
                are_equal = (actual_score == expected_score)
            if not are_equal:
                print(f'FAIL: get_assignment_scores("{assignment_name}") ' +
                    f"returned a dictionary that has a score of " +
                    f"{actual_score} for student ID {student_ID}, but the " +
                    f"expected score is {expected_score}")
                return False
        
        # All entries match
        print(f'PASS: get_assignment_scores("{assignment_name}") returned ' +
            f"a dictionary with {len(actual_dictionary)} correct scores")
    
    return True

def test_get_sorted_assignment_names():
    print("\n---- test_get_sorted_assignment_names() ----")
    gradebook = TestUtility.make_sample_gradebook()
    
    expected = [ "Course project", "Final exam", "Homework 1", "Homework 2",
        "Homework 3", "Homework 4", "Midterm" ]
    actual = gradebook.get_sorted_assignment_names()
    
    are_equal = True
    if len(actual) == len(expected):
        # Compare elements in order
        i = 0
        while are_equal and i < len(expected):
            if actual[i] != expected[i]:
                are_equal = False
            i += 1
    else:
        are_equal = False
    
    # Show pass or fail message along with expected and actual vector contents
    if are_equal:
        print("PASS: get_sorted_assignment_names()")
    else:
        print("FAIL: get_sorted_assignment_names()")
    print(f"  Expected: {expected}")
    print(f"  Actual:   {actual}")
    
    return are_equal

def test_get_sorted_student_IDs():
    print("\n---- test_get_sorted_student_IDs() ----")
    gradebook = TestUtility.make_sample_gradebook()
    
    expected = [
        10000, 11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 90000,
        99999
    ]
    actual = gradebook.get_sorted_student_IDs()
    
    are_equal = True
    if len(actual) == len(expected):
        # Compare elements in order
        i = 0
        while are_equal and i < len(expected):
            if actual[i] != expected[i]:
                are_equal = False
            i += 1
    else:
        are_equal = False
    
    # Show pass or fail message along with expected and actual vector contents
    if are_equal:
        print("PASS: get_sorted_student_IDs()")
    else:
        print("FAIL: get_sorted_student_IDs()")
    print(f"  Expected: {expected}")
    print(f"  Actual:   {actual}")
    return are_equal

def test_get_student_scores():
    print("\n---- test_get_student_scores() ----")
    gradebook = TestUtility.make_sample_gradebook()
    
    student_22222_scores = {
        # Student has no score for "Homework 1"
        "Homework 2": 75.0,
        "Midterm": 77.5,
        "Homework 3": 80.5,
        "Homework 4": 81.0,
        "Course project": 60.0,
        "Final exam": 54.0
    }
    student_44444_scores = {
        "Homework 1": 60.0,
        "Homework 2": 50.0,
        "Midterm": 40.0,
        "Homework 3": 30.0
        # Student has no score for "Homework 4"
        # Student has no score for "Course project"
        # Student has no score for "Final exam"
    }
    student_88888_scores = {
        "Homework 1": 64.5,
        "Homework 2": 74.5,
        "Midterm": 88.0,
        "Homework 3": 84.0,
        "Homework 4": 84.0,
        "Course project": 85.5,
        "Final exam": 81.5
    }
    student_90000_scores = {
        "Homework 1": 80.0,
        "Homework 2": 85.0,
        "Midterm": 90.0,
        "Homework 3": 95.0,
        "Homework 4": 100.0,
        "Course project": 85.0,
        "Final exam": 94.5
    }
    
    # Each test case is a (student_ID, dictionary_of_expected_scores) pair
    test_cases = [
        (22222, student_22222_scores),
        (44444, student_44444_scores),
        (88888, student_88888_scores),
        (90000, student_90000_scores)
    ]
    
    # Iterate through all test cases
    for test_case in test_cases:
        student_ID = test_case[0]
        expected_dictionary = test_case[1]
        
        # Get the actual dictionary from the gradebook
        print(f"Calling get_student_scores({student_ID})")
        actual_dictionary = gradebook.get_student_scores(student_ID)
        
        # Compare lengths first
        if len(expected_dictionary) != len(actual_dictionary):
            print(f"FAIL: get_student_scores({student_ID}) returned a " +
                "dictionary with ", end="")
            if 1 == len(actual_dictionary):
                print("1 score, ", end="")
            else:
                print(f"{len(actual_dictionary)} scores, ", end="")
            print(f"but the expected dictionary has " +
                f"{len(expected_dictionary)} scores")
            return False
        
        # Lengths are equal, so now compare each assignment name/score pair
        for assignment_name in expected_dictionary:
            if assignment_name not in actual_dictionary:
                print(f"FAIL: get_student_scores({student_ID}) returned a " +
                    "dictionary that is missing an entry for assignment " +
                    f'"{assignment_name}"')
                return False
            
            # Actual dictionary has assignment name, so now compare
            # corresponding score
            expected_score = expected_dictionary[assignment_name]
            actual_score = actual_dictionary[assignment_name]
            are_equal = False
            if math.isnan(expected_score):
                are_equal = math.isnan(actual_score)
            else:
                are_equal = (actual_score == expected_score)
            if not are_equal:
                print(f"FAIL: get_student_scores({student_ID}) returned a " +
                    f"dictionary that has a score of {actual_score} for " +
                    f'assignment "{assignment_name}", but the expected ' +
                    f"score is {expected_score}")
                return False
        
        # All entries match
        print(f"PASS: get_student_scores({student_ID}) returned a " +
            f"dictionary with {len(actual_dictionary)} correct scores")
    
    return True

# Main program code follows
result1 = test_get_score_and_set_score()
result2 = test_get_assignment_scores()
result3 = test_get_sorted_assignment_names()
result4 = test_get_sorted_student_IDs()
result5 = test_get_student_scores()
   
print("\nSummary:")
print(f"test_get_score_and_set_score(): {'PASS' if result1 else 'FAIL'}")
print(f"test_get_assignment_scores(): {'PASS' if result2 else 'FAIL'}")
print(f"test_get_sorted_assignment_names(): {'PASS' if result3 else 'FAIL'}")
print(f"test_get_sorted_student_IDs(): {'PASS' if result4 else 'FAIL'}")
print(f"test_get_student_scores(): {'PASS' if result5 else 'FAIL'}")