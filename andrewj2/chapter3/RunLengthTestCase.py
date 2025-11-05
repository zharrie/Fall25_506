from NaturalMergeSorter import NaturalMergeSorter
from FeedbackPrinter import FeedbackPrinter

# RunLengthTestCase represents a test case for the NaturalMergeSorter class's
# get_sorted_run_length() method.
class RunLengthTestCase:
    def __init__(self, target_list, start, expected_ret, test_feedback = FeedbackPrinter()):
        self.target_list = target_list
        self.start_index = start
        self.expected_return_value = expected_ret
        self.test_feedback = test_feedback
    
    # Executes the test case. If the test case passes, a message that starts
    # with "PASS" is printed and True is returned. Otherwise a message that
    # starts with "FAIL" is printed and False is returned.
    def execute(self):
        # Create a NaturalMergeSorter instance
        user_sorter = NaturalMergeSorter()
        
        # Call the get_sorted_run_length() method with the test case parameters
        user_ret_val = user_sorter.get_sorted_run_length(self.target_list,
            self.start_index)
        
        # The test passed only if the actual return value equals the expected
        # return value
        passed = (user_ret_val == self.expected_return_value)
        
        # Show a message about the test case's results
        self.test_feedback.write(("PASS" if passed else "FAIL") +
            ": get_sorted_run_length()\n" +
            f"    List: {self.target_list}\n" +
            f"    Start index:           {self.start_index}\n" +
            f"    Expected return value: {self.expected_return_value}\n" +
            f"    Actual return value:   {user_ret_val}")
        
        return passed