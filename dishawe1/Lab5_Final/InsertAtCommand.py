from UndoCommand import UndoCommand

class InsertAtCommand(UndoCommand):
    def __init__(self, target_list, index, new_item):
        self.target_list = target_list
        self.index = index
        self.new_item = new_item
  
    def execute(self):
        self.target_list.insert(self.index, self.new_item)