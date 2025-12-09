import csv

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.friend_ids = []
    
    def __str__(self):
        return f"[{self.id}: {self.name}, {len(self.friend_ids)} friends]"

class UserMap:
    def __init__(self):
        self.__map = {}
        self.__next_id = 0
    
    def __str__(self):
        return "\n".join(map(lambda u: str(u), self.__map.values()))

    def add_new_user(self, name):
        id = self.__next_id
        self.__next_id += 1
        self.__map[id] = User(id, name)
    
    def overwrite_user(self, user):
        self.__map[user.id] = user
        if self.__next_id <= user.id:
            self.__next_id = user.id + 1

    def get_user_by_id(self, id):
        return self.__map.get(id)

    def load_network_from_csv(self, csv_path):
        try:
            with open(csv_path, mode ='r') as file:
                people = csv.reader(file)
                for p in people:
                    self.overwrite_user(User(int(p[0]), p[1]))
        except ValueError as err:
            return (False, err)
        return (True, "Success")
