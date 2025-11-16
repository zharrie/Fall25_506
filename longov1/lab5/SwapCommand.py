from UndoCommand import UndoCommand

class SwapCommand(UndoCommand):
    # TODO: Type your __init__() method code here
    def __init__(self, target_list, index1, index2):
        self.target_list = target_list
        self.index1 = index1
        self.index2 = index2

    def execute(self):
        # TODO: Type your code here
        temp = self.target_list[self.index1]
        self.target_list[self.index1] = self.target_list[self.index2]
        self.target_list[self.index2] = temp
        #pass