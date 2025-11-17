from UndoCommand import UndoCommand

class InsertAtCommand(UndoCommand):
    def __init__(self, target_list , index, removed_item):
        self.target_list = target_list
        self.index = index
        self.removed_item = removed_item
    
    def execute(self):
        self.target_list.insert(self.index, self.removed_item)
        pass