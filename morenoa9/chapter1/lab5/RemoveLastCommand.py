from UndoCommand import UndoCommand

class RemoveLastCommand(UndoCommand):
    def __init__(self, target_list):
        self.target_list = target_list
    
    def execute(self):
        if len(self.target_list)> 0:
            self.target_list.pop()