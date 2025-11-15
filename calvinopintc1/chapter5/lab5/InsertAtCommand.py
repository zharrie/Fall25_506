from UndoCommand import UndoCommand

class InsertAtCommand(UndoCommand):
    def __init__(self, target_list, insert_at_index, item_to_insert):
        self.target_list = target_list
        self.insert_at_index = insert_at_index
        self.item_to_insert = item_to_insert
    
    def execute(self):
        #needs to readd a grocery list item at an arbitray index (an index it was og removed from)
        # print("Attempting to InsertAt", self.insert_at_index)
        self.target_list.append('None') #the list will grow in length so will append something to the end
        #to adjust for the shift
        for i in reversed(range(self.insert_at_index, len(self.target_list)-1)):
            #use reverse list to not overwrite items before shifting
            in_place_item = self.target_list[i]
            self.target_list[i + 1] = self.target_list[i] #shift the items
        
        if len(self.target_list) > self.insert_at_index:
            #if the length of the list is greater than the insert index, overwrite the item at that index
            self.target_list[self.insert_at_index] = self.item_to_insert
        else:
            #otherwise append to the end (mainly when list is empty and want to insert at 0)
            self.target_list.append(self.item_to_insert)
        
        # print(self.target_list)

        