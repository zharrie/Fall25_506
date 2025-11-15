from UndoCommand import UndoCommand

class RemoveLastCommand(UndoCommand):
    def __init__(self, target_list):
        self.target_list = target_list
    
    def execute(self):
        #we want to remove the last element in target_list
        #find the last element in target_list
        # print("Attempting to removelast")
        self.target_list.remove(self.target_list[-1])
        # print(self.target_list)
        
    
        