from UndoCommand import UndoCommand

class SwapCommand(UndoCommand):
    # TODO: Type your __init__() method code here
    def __init__(self, target_list, item1, item2):
        self.target_list = target_list
        self.item1 = item1
        self.item2 = item2
    
    def execute(self):
        # TODO: Type your code here
        self.target_list[self.item1] , self.target_list[self.item2] = self.target_list[self.item2] , self.target_list[self.item1]
        pass