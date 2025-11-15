from UndoCommand import UndoCommand

class SwapCommand(UndoCommand):
    def __init__(self, lst, idx1, idx2):
        self.lst = lst
        self.idx1 = idx1
        self.idx2 = idx2
    
    def execute(self):
        tmp = self.lst[self.idx1]
        self.lst[self.idx1] = self.lst[self.idx2]
        self.lst[self.idx2] = tmp
