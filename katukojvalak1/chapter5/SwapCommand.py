from UndoCommand import UndoCommand

class SwapCommand(UndoCommand):
    def __init__(self, target_list, i,j):
        self.target_list = target_list
        self.i = i
        self.j = j
    
    def execute(self):
        self.target_list[self.i], self.target_list[self.j] = \
        self.target_list[self.j], self.target_list[self.i]
        pass