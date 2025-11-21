from GroceryList import GroceryList

# Represents a test case for the user's GroceryList class implementation. Has
# attributes:
#
# "commands":
#   A list of string commands, each of which is one of the five forms:
#   - add item_name
#   - removeat index
#   - swap index1 index2
#   - undo
#   - verify lits_item1,list_item2,...,last_list_item
#
# "show_commands":
#   A Boolean value indicating whether or not executed commands are shown in
#   feedback.
#
# "assert_undo_count":
#   A Boolean value indicating whether or not to the test should assert the
#   number of undo commands on the undo stack.
class GroceryListTest:
    def __init__(self, command_list, test_feedback):
        self.commands = list(command_list)
        self.show_commands = True
        self.assert_undo_count = True
        self.test_feedback = test_feedback
    
    @staticmethod
    def assert_list_content(test_feedback, actual, expected):
        passed = True
        # First ensure that the sizes match
        if len(actual) != len(expected):
            passed = False
        
        if passed:
            # Now compare each element
            for i in range(len(actual)):
                if actual[i] != expected[i]:
                    passed = False
        
        if not passed:
            test_feedback.write("FAIL:\n" +
                f"  Expected list: {expected}\n" +
                f"  Actual list:   {actual}\n")
        
        return passed
    
    def execute(self):
        # Create a GroceryList
        grocery_list = GroceryList()
        
        # Execute each command in the commands list
        for command in self.commands:
            if not self.exec_command(command, grocery_list):
                return False
        
        # All tests passed
        return True
    
    def exec_command(self, command, grocery_list):
        # Record the undo stack length prior to executing the command
        undo_count_before = grocery_list.get_undo_stack_length()
        
        # Store the current undo stack length as the "expected" undo stack
        # length. The expected count is incremented for the add, removeat, and
        # swap commands, and is decremented for the undo command.
        expected_undo_count = undo_count_before
        
        # Check the command string
        if command.startswith("add "):
            item_to_add = command[4:]
            if self.show_commands:
                self.feedback(f"Adding {item_to_add}")
            grocery_list.add_with_undo(item_to_add)
            expected_undo_count += 1
        elif command.startswith("removeat "):
            index = int(command[9:])
            if self.show_commands:
                self.feedback(f"Removing at index {index}")
            grocery_list.remove_at_with_undo(index)
            expected_undo_count += 1
        elif command.startswith("swap "):
            indices = [-1, -1]
            if GroceryListTest.parse_indices(command[5:], indices):
                if self.show_commands:
                    self.feedback(f"Swapping at indices {indices[0]} and " +
                        f"{indices[1]}")
                grocery_list.swap_with_undo(indices[0], indices[1])
            else:
                self.feedback(f"Malformed swap command: {command}")
                return False
            expected_undo_count += 1
        elif command == "undo":
            if self.show_commands:
                self.feedback("Executing undo")
            if 0 == grocery_list.get_undo_stack_length():
                self.feedback("FAIL: Cannot execute undo because undo stack " +
                    "is empty")
            else:
                grocery_list.execute_undo()
                expected_undo_count -= 1
        elif command.startswith("verify "):
            list_str = command[7:]
            expected = list_str.split(",")
            actual = grocery_list.get_list_copy()
            if not GroceryListTest.assert_list_content(self.test_feedback, actual, expected):
                return False
            self.feedback(f"PASS: Verified list content: {list_str}")
        elif command == "verify":
            # Special case for empty list
            actual_length = len(grocery_list.get_list_copy())
            if 0 == actual_length:
                self.feedback("PASS: List is empty")
            else:
                self.feedback("FAIL: List should be empty, but instead has " +
                    f"{actual_length} item{'' if 1 == actual_length else 's'}")
        
        # If the undo stack length should have changed, verify
        if self.assert_undo_count and undo_count_before != expected_undo_count:
            # Get the actual undo command count
            actual_count = grocery_list.get_undo_stack_length()
            
            if expected_undo_count != actual_count:
                self.feedback("FAIL: Expected undo stack length is " +
                    f"{expected_undo_count}, but actual length is " +
                    f"{actual_count}")
                return False
            else:
                self.feedback(f"PASS: Undo stack length is {actual_count}")
        
        return True
    
    def feedback(self, message):
        self.test_feedback.write(message)
    
    @staticmethod
    def parse_indices(string, out_indices):
        space_index = string.find(" ")
        if -1 == space_index:
            return False
        out_indices[0] = int(string[0:space_index])
        out_indices[1] = int(string[space_index + 1:])
        return True