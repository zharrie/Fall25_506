from UndoCommand import UndoCommand
from RemoveLastCommand import RemoveLastCommand
from InsertAtCommand import InsertAtCommand
from SwapCommand import SwapCommand

class GroceryList:
    def __init__(self):
        self.list_items = []
        self.undo_stack = []
    
    def add_with_undo(self, new_item_name):
        # Add the new list item
        self.list_items.append(new_item_name)
        
        # Make an undo command that removes the last item and push onto stack
        self.undo_stack.append(RemoveLastCommand(self.list_items))
    
    def remove_at_with_undo(self, removal_index):
        removed_item = self.list_items.pop(removal_index)
        self.undo_stack.append(InsertAtCommand(self.list_items, removal_index, removed_item))
    
    def swap_with_undo(self, index1, index2):
        #The method swaps list items at specified indices, then
        #pushes a SwapCommand to undo that swap onto the undo stack.
        self.list_items[index1], self.list_items[index2] = self.list_items[index2], self.list_items[index1]
        self.undo_stack.append(SwapCommand(self.list_items, index1, index2))
        

    
    # Pops and executes the undo command at the top of the undo stack
    def execute_undo(self):
        #Step 1: Pop an UndoCommand off the undo stack
        #Step 2: Execute the popped undo command
        most_recent_command = self.undo_stack.pop()
        most_recent_command.execute()
    
    def get_list_length(self):
        return len(self.list_items)
    
    def get_undo_stack_length(self):
        return len(self.undo_stack)
    
    def get_list_copy(self):
        return list(self.list_items)
    
    def __str__(self):
        result = ""
        for i in range(len(self.list_items)):
            result += f"{i}. {self.list_items[i]}\n"