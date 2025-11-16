from UndoCommand import UndoCommand
'''
The RemoveLastCommand class derives from UndoCommand and is declared in RemoveLastCommand.py. 
When a RemoveLastCommand object is executed, the string list's last element is removed. 
So when the user appends a new item to the grocery list, a RemoveLastCommand is pushed onto the stack of undo commands. 
Popping and executing the RemoveLastCommand then removes the item most recently added by the user.

RemoveLastCommand's target_list attribute and __init__() method are already declared:

target_list is a reference to a GroceryList object's list of strings.

__init__() takes a string list as an argument and assigns target_list with the list.

Implement RemoveLastCommand's execute() method to remove target_list's last element.
'''

class RemoveLastCommand(UndoCommand):
    def __init__(self, target_list):
        self.target_list = target_list
    
    def execute(self):
        if len(self.target_list) > 0:
            self.target_list.pop()
        pass