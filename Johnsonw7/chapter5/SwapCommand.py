from UndoCommand import UndoCommand

class SwapCommand(UndoCommand):
    def __init__(self, target_list, index1, index2):
        self.target_list = target_list
        self.index1 = index1
        self.index2 = index2
    
    def execute(self):
        lst = self.target_list
        lst[self.index1], lst[self.index2] = lst[self.index2], lst[self.index1]