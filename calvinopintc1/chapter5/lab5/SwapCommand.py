from UndoCommand import UndoCommand

class SwapCommand(UndoCommand):
    def __init__(self, target_list, index1, index2):
        self.target_list = target_list
        self.index1 = index1
        self.index2 = index2
    
    def execute(self):
        #swap list items at specified indices
        # print("Attempting to swap at", self.index1, self.index2)
        item1 = self.target_list[self.index1]
        item2 = self.target_list[self.index2]
        self.target_list[self.index1] = item2
        self.target_list[self.index2] = item1
        # print(self.target_list)