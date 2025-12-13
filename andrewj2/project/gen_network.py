import random as r
import math
from SocialNetwork import Network
from names import names

def gen_network(lst):
    net = Network()

    for n in lst:
        net.add_new_user(n)

    def connect_range(a, b, n):
        for _ in range(0, n):
            id1 = r.randint(a, b)
            id2 = r.randint(a, b)
            net.add_friend(id1, id2)

    def connect_user(id1, a, b, n):
        for _ in range(0, n):
            id2 = r.randint(a, b)
            net.add_friend(id1, id2)

    # create 7 islands
    n = math.ceil(len(lst)/7)
    for i in range(7):
        a = i * n
        b = min((i+1)*n-1, len(lst)-1)
        connect_range(a, b, r.randint(n*6, n*7))

        # with a few popular people each
        for j in range(r.randint(n//200, n//100)):
            uid = r.randint(a, b)
            connect_user(uid, a, b, r.randint(n//20, n//5)) # popular in the island
            connect_user(uid, 0, len(lst)-1, r.randint(2,5)) # and a couple connections outside

    # add a few connections across the whole network
    for i in range(len(lst)//100):
        uid = r.randint(0, len(lst)-1)
        connect_user(uid, 0, len(lst)-1, 1)
    
    return net

r.shuffle(names)
N = 100
names = names[:N]
network = Network()
for n in names:
    network.add_new_user(n)
for _ in range(0, 3*N):
    id1 = r.randint(0, N)
    id2 = r.randint(0, N)
    network.add_friend(id1, id2)

# diameter = 0
# while(diameter < 10):
#     network = gen_network(names)

#     total = network.get_total_users()
#     visited = set()
#     islands = 0
#     while len(visited) < network.get_total_users():
#         i = 0
#         while i in visited or not network.get_user_by_id(i):
#             i += 1
#             continue

#         distances = network.bfs_traverse(i, visit_fn=lambda u: visited.add(u.uid))
#         islands += 1

#         d = sorted(distances.values(), reverse=True)[0]
#         if diameter < d: diameter = d
#     n_users = network.get_total_users()
#     n_conns = network.get_total_connections()
#     print(f"Total Users: {n_users}")
#     print(f"Total Connections: {n_conns}")
#     print(f"Average Connections Per User: {n_conns / n_users}")

#     for user in network.get_top_n_users(5):
#         print(user)
#     print()
#     for user in network.get_top_n_users(5, bottom=True):
#         print(user)
#     print()

#     print(f"Graph diameter: {diameter}")
#     conn = "Fully connected" if islands == 1 else "Empty (no connections)" if islands == total else f"Disconnected ({islands} islands)"
#     print(f"Graph connectivity: {conn}")

network.save_network_to_csv("network-small.csv")