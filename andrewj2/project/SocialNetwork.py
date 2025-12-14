import math
import csv

class User:
    def __init__(self, uid, name, friends=None):
        self.uid = uid
        self.name = name
        self.friends = set() if not friends else friends
    
    def __str__(self):
        return f"<User uid={self.uid}, name={self.name}, len(friends)={len(self.friends)}>"

    def copy(self):
        return User(self.uid, self.name, set(self.friends))

class Network:
    def __init__(self):
        self.__u_dict = {}
        self.__next_uid = 0
        self.__d_matrix = None

    def __str__(self):
        return f"<Network len(__map)={len(self.__u_dict)}>"

    def get_user_by_uid(self, uid):
        return self.__u_dict.get(uid)

    def get_users_by_uids(self, uid_list):
        return list(map(self.get_user_by_uid, uid_list))

    def get_all_users(self):
        return sorted(self.__u_dict.values(), key=lambda u: u.uid)

    def get_all_uids(self):
        return list(map(lambda u: u.uid, self.get_all_users()))

    def get_all_connections(self):
        connections = set()
        for u in self.get_all_users():
            for fid in u.friends:
                connections.add((u.uid, fid))
        
        return connections

    def get_mutual_connections(self, uid1, uid2):
        u1 = self.get_user_by_uid(uid1)
        u2 = self.get_user_by_uid(uid2)
        return list(set(u1.friends) & set(u2.friends))

    def get_total_users(self):
        return len(self.__u_dict)
    
    def get_total_connections(self):
        return sum(map(lambda u: len(u.friends), self.__u_dict.values())) // 2

    def add_new_user(self, name):
        uid = self.__next_uid
        self.__next_uid += 1
        self.__u_dict[uid] = User(uid, name)
        return uid
    
    def overwrite_user(self, user):
        self.__u_dict[user.uid] = user
        if self.__next_uid <= user.uid:
            self.__next_uid = user.uid + 1

    def add_friend(self, uid1, uid2):
        if uid1 == uid2: return
        u1 = self.get_user_by_uid(uid1)
        u2 = self.get_user_by_uid(uid2)
        if not u1 or not u2: return # error?
        u1.friends.add(uid2)
        u2.friends.add(uid1)

    def un_friend(self, uid1, uid2):
        u1 = self.get_user_by_uid(uid1)
        u2 = self.get_user_by_uid(uid2)
        if u1: u1.friends.discard(uid2)
        if u2: u2.friends.discard(uid1)

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
                writer.writerows(map(lambda u: [u.uid, u.name, " ".join(map(str, u.friends))], self.__u_dict.values()))
        except Exception as e:
            return (False, e)
        return (True, "Success")

    def bfs_traverse(self, start_uid, visit_fn=None, end_uid=None, end_dist=math.inf):
        frontier = []
        next_frontier = [] # so that we can keep track of distance
        discovered = set()
        distances = {}

        frontier.append(start_uid)
        discovered.add(start_uid)
        distances[start_uid] = 0

        dist = 0
        while len(frontier) > 0 and dist <= end_dist:
            uid = frontier.pop()
            user = self.get_user_by_uid(uid)
            if not user: continue # error?

            if visit_fn: visit_fn(user.copy())
            if uid == end_uid: break

            for fid in user.friends:
                if fid not in discovered:
                    next_frontier.insert(0,fid)
                    discovered.add(fid)
                    distances[fid] = distances[uid]+1
            
            if len(frontier) == 0: # move to next distance frontier
                frontier = next_frontier
                next_frontier = []
                dist += 1
        
        if end_dist:
            return dict((k,v) for k,v in distances.items() if v <= end_dist)

        return distances

    def dfs_traverse(self, start_uid, visit_fn=None, end_uid=None):
        v_stack = []
        visited = set()

        while len(v_stack) > 0:
            uid = v_stack.pop()
            user = self.get_user_by_uid(uid)
            if not user: continue # error?

            if uid not in visited:
                if visit_fn: visit_fn(user.copy())
                if uid == end_uid: break
                visited.add(uid)
                
                for fid in user.friends:
                    v_stack.append(fid)

    def get_path_dijkstra(self, start_uid, end_uid):
        unvisited = self.get_all_uids()
        # uid: (dist, pred)
        d_dict = {k:v for k,v in map(lambda uid: (uid, (math.inf, None)), unvisited)}
        d_dict[start_uid] = (0, None)

        while len(unvisited) > 0:
            min_i = 0
            for i in range(1, len(unvisited)):
                if d_dict[unvisited[i]][0] < d_dict[min_i][0]: min_i = i
            uid = unvisited.pop(min_i)

            new_dist = d_dict[uid][0] + 1
            for fid in self.get_user_by_uid(uid).friends:
                if new_dist < d_dict[fid][0]: d_dict[fid] = (new_dist, uid)
        
        if d_dict[end_uid][0] == math.inf:
            return None

        path = []
        uid = end_uid
        while uid != start_uid:
            path = [uid] + path
            uid = d_dict[uid][1]
        return [start_uid] + path

    def build_d_matrix_fw(self):
        if self.__d_matrix: return self.__d_matrix

        v_list = self.get_all_uids()
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

    def get_path_fw(self, start_uid, end_uid):
        d_matrix = self.build_d_matrix_fw()

        v_list = self.get_all_uids()
        e_list = self.get_all_connections()
        start = v_list.index(start_uid)
        path = [end_uid]

        cur = v_list.index(end_uid)
        while cur != start:
            cur_e_list = set(filter(lambda e: e[1] == v_list[cur], e_list))
            found_next = False
            for e in cur_e_list:
                expect = d_matrix[start][cur] - 1
                actual = d_matrix[start][v_list.index(e[0])]
                if actual != math.inf and expect == actual:
                    cur = v_list.index(e[0])
                    path = [e[0]] + path
                    found_next = True
                    break
            if not found_next:
                return None
        
        return path
