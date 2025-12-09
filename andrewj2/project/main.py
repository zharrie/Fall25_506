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
        if self.__next_id < user.id:
            self.__next_id = user.id + 1

    def get_user_by_id(self, id):
        return self.__map.get(id)

class N:
    def __init__(self):
        self.n = 0
    
    def pp(self):
        r = self.n
        self.n += 1
        return r

def menu():
    n = N()
    menu_str = f"""[MAIN MENU]
    {n.pp()}. Print this menu again
    {n.pp()}. Find connection path
    {n.pp()}. Friends within N degrees
    {n.pp()}. Most connected users
    {n.pp()}. Mutual friends
    {n.pp()}. Friend suggestions
    {n.pp()}. Network statistics
    {n.pp()}. Exit
"""
    print(menu_str)

    while True:
        choice = input("Select: ")
        c = -1
        
        try:
            c = int(choice)
        except ValueError:
            pass

        if c < 0 or c > n.n-1:
            print("Invalid selection: " + choice)
            continue

        if c == 0:
            print(menu_str)
        if c == 6:
            break

        print()


users = UserMap()

import csv
with open('people.csv', mode ='r') as file:
    people = csv.reader(file)
    for p in people:
        users.overwrite_user(User(int(p[0]), p[1]))

print(users)

# menu()