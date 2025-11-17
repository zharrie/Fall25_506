from UndoCommand import UndoCommand

class InsertAtCommand(UndoCommand):
    def __init__(self,target_list,index,item):
        self.target_list= target_list
        self.index= index
        self.item= item
    
    def execute(self):
        self.target_list.insert(self.index, self.item)