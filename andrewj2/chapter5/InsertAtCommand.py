from UndoCommand import UndoCommand

class InsertAtCommand(UndoCommand):
    def __init__(self, lst, idx, item):
        self.lst = lst
        self.idx = idx
        self.item = item
    
    def execute(self):
        self.lst.insert(self.idx, self.item)