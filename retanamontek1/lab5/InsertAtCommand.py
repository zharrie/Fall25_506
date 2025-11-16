from UndoCommand import UndoCommand

class InsertAtCommand(UndoCommand):
    # TODO: Type your __init__() method code here
    
    def __init__(self, target_list, item, index):
        self.target_list = target_list
        self.item = item
        self.index = index

    def execute(self):
        # TODO: Type your code here
        self.target_list.insert(self.index, self.item)

        pass