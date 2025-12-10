import math
import csv

class User:
    def __init__(self, id, name, friends=None):
        self.id = id
        self.name = name
        self.friends = set() if not friends else friends
    
    def __str__(self):
        return f"<User id={self.id}, name={self.name}, len(friends)={len(self.friends)}>"

    def copy(self):
        return User(self.id, self.name, set(self.friends))

class Network:
    def __init__(self):
        self.__map = {}
        self.__next_id = 0
        self.__d_matrix = None
    
    def __str__(self):
        return f"<Network len(__map)={len(self.__map)}>"
        
    def get_all_users(self):
        return sorted(self.__map.values(), key=lambda u: u.id)

    def get_all_ids(self):
        return list(map(lambda u: u.id, self.get_all_users()))
    
    def get_all_connections(self):
        connections = set()
        for u in self.get_all_users():
            for fid in u.friends:
                connections.add((u.id, fid))
        
        return connections

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
        if id1 == id2: return
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

    def bfs_traverse(self, start_id, visit_fn=None, end_id=None, end_dist=math.inf):
        frontier = []
        next_frontier = [] # so that we can keep track of distance
        discovered = set()
        distances = {}

        frontier.append(start_id)
        discovered.add(start_id)
        distances[start_id] = 0

        dist = 0
        while len(frontier) > 0 and dist <= end_dist:
            id = frontier.pop()
            user = self.get_user_by_id(id)
            if not user: continue # error?

            if visit_fn: visit_fn(user.copy())
            if id == end_id: break

            for fid in user.friends:
                if fid not in discovered:
                    next_frontier.insert(0,fid)
                    discovered.add(fid)
                    distances[fid] = distances[id]+1
            
            if len(frontier) == 0: # move to next distance frontier
                frontier = next_frontier
                next_frontier = []
                dist += 1
        
        if end_dist:
            return dict((k,v) for k,v in distances.items() if v <= end_dist)

        return distances

    def dfs_traverse(self, start_id, visit_fn=None, end_id=None):
        v_stack = []
        visited = set()

        while len(v_stack) > 0:
            id = v_stack.pop()
            user = self.get_user_by_id(id)
            if not user: continue # error?

            if id not in visited:
                if visit_fn: visit_fn(user.copy())
                if id == end_id: break
                visited.add(id)
                
                for fid in user.friends:
                    v_stack.append(fid)

    def build_distance_matrix(self):
        if self.__d_matrix: return self.__d_matrix

        v_list = self.get_all_ids()
        n = len(v_list)
        e_list = self.get_all_connections()
        
        d_matrix = []
        for i in range(0, n):
            d_matrix.append([math.inf] * n)
            d_matrix[i][i] = 0
        
        for e in e_list:
            d_matrix[v_list.index(e[0])][v_list.index(e[1])] = 1
        
        for i in range(0, n):
            for to in range(0, n):
                for fm in range(0, n):
                    new_len = d_matrix[fm][i] + d_matrix[i][to]
                    if new_len < d_matrix[fm][to]:
                        d_matrix[fm][to] = new_len

        self.__d_matrix = d_matrix
        return d_matrix

    def get_path(self, start_id, end_id):
        d_matrix = self.build_distance_matrix()

        v_list = self.get_all_ids()
        e_list = self.get_all_connections()
        start = v_list.index(start_id)
        path = []

        cur = v_list.index(end_id)
        while cur != start:
            cur_e_list = set(filter(lambda e: e[1] == v_list[cur], e_list))
            found_next = False
            for e in cur_e_list:
                expect = d_matrix[start][cur] - 1
                actual = d_matrix[start][v_list.index(e[0])]
                if expect == actual:
                    cur = v_list.index(e[0])
                    path = [e] + path
                    found_next = True
                    break
            if not found_next:
                return None
        
        return path

