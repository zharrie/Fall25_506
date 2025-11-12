from UndoCommand import UndoCommand
from RemoveLastCommand import RemoveLastCommand
from InsertAtCommand import InsertAtCommand
from SwapCommand import SwapCommand

class GroceryList:
    def __init__(self):
        self.lst = []
        self.undo_stack = []
    
    def add_with_undo(self, item_name):
        self.lst.append(item_name)
        self.undo_stack.append(RemoveLastCommand(self.lst))
    
    def remove_at_with_undo(self, idx):
        self.undo_stack.append(InsertAtCommand(self.lst, idx, self.lst[idx]))
        del self.lst[idx]
    
    def swap_with_undo(self, idx1, idx2):
        tmp = self.lst[idx1]
        self.lst[idx1] = self.lst[idx2]
        self.lst[idx2] = tmp
        self.undo_stack.append(SwapCommand(self.lst, idx1, idx2))
    
    # Pops and executes the undo command at the top of the undo stack
    def execute_undo(self):
        cmd = self.undo_stack.pop()
        cmd.execute()
    
    def get_list_length(self):
        return len(self.lst)
    
    def get_undo_stack_length(self):
        return len(self.undo_stack)
    
    def get_list_copy(self):
        return list(self.lst)
    
    def __str__(self):
        result = ""
        for i in range(len(self.lst)):
            result += f"{i}. {self.lst[i]}\n"