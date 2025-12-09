import csv

class User:
    def __init__(self, id, name, friends=None):
        self.id = id
        self.name = name
        self.friends = set() if not friends else friends
    
    def __str__(self):
        return f"<User id={self.id}, name={self.name}, len(friends)={len(self.friends)}>"

class Network:
    def __init__(self):
        self.__map = {}
        self.__next_id = 0
    
    def __str__(self):
        return "\n".join(map(lambda u: str(u), self.__map.values()))

    def add_new_user(self, name):
        id = self.__next_id
        self.__next_id += 1
        self.__map[id] = User(id, name)
        return id
    
    def overwrite_user(self, user):
        self.__map[user.id] = user
        if self.__next_id <= user.id:
            self.__next_id = user.id + 1

    def get_user_by_id(self, id):
        return self.__map.get(id)

    def add_friend(self, id1, id2):
        u1 = self.get_user_by_id(id1)
        u2 = self.get_user_by_id(id2)
        if not u1 or not u2: return # error?
        u1.friends.add(id2)
        u2.friends.add(id1)

    def un_friend(self, id1, id2):
        u1 = self.get_user_by_id(id1)
        u2 = self.get_user_by_id(id2)
        if u1: u1.friends.discard(id2)
        if u2: u2.friends.discard(id1)

    def load_network_from_csv(self, csv_path):
        try:
            with open(csv_path, mode='r') as file:
                rows = csv.reader(file)
                for row in rows:
                    self.overwrite_user(User(int(row[0]), row[1], set(map(int, row[2].split()))))
        except Exception as e:
            return (False, e)
        return (True, "Success")

    def save_network_to_csv(self, csv_path):
        try:
            with open(csv_path, mode='w') as file:
                writer = csv.writer(file)
                writer.writerows(map(lambda u: [u.id, u.name, " ".join(map(str, u.friends))], self.__map.values()))
        except Exception as e:
            return (False, e)
        return (True, "Success")

    def get_top_n_users(self, n, bottom=False):
        return sorted(self.__map.values(), key=lambda u: len(u.friends), reverse=not bottom)[:n]
    
    def get_total_users(self):
        return len(self.__map)
    
    def get_total_connections(self):
        return sum(map(lambda u: len(u.friends), self.__map.values())) // 2

    def search_users_by_name(self, search):
        return list(filter(lambda u: search.lower() in u.name.lower(), self.__map.values()))
