from UndoCommand import UndoCommand

class InsertAtCommand(UndoCommand):
    # TODO: Type your __init__() method code here
    def __init__(self, target_list, index, item):
        self.target_list = target_list
        self.index = index
        self.item = item

    def execute(self):
        # TODO: Type your code here
        self.target_list.insert(self.index, self.item)
        pass