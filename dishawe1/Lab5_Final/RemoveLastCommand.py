from UndoCommand import UndoCommand

class RemoveLastCommand(UndoCommand):
    def __init__(self, target_list):
        self.target_list = target_list
    
    def execute(self):
        # Remove target_list's last element
        if self.target_list:
            return self.target_list.pop()
