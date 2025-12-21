from sys import argv
from Menu import *
from SocialNetwork import *

# ============================
#        NETWORK LOGIC
# ----------------------------

network = Network()
runtime = {
    "user": None,
    "use_fw": False,
}

# === Helper Functions ===

def digits():
    if not runtime.get("digits"): runtime["digits"] = math.floor(math.log10(network.get_total_users()))
    return runtime["digits"]

def fmt_uid(uid):
    return str(uid).zfill(digits())

def fmt_user(u, pad_uid=True):
    return f"{fmt_uid(u.uid) if pad_uid else u.uid}: {u.name} ({len(u.friends)} friends)"

def ordinal(n: int): # credit: https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement
    if 11 <= (n % 100) <= 13: suffix = 'th'
    else: suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

def todo():
    mprint("TODO")

def sorted_by_friends(u_list, reverse=True):
    return sorted(u_list, key=lambda u: len(u.friends), reverse=reverse)

# === Options Menu ===

def opt_set_use_fw(b):
    runtime["use_fw"] = b
    alg = "Floyd-Warshall" if b else "BFS/Dijkstra"
    mprint(f"Now using {alg} for distance/shortest path")

def use_fw():
    return runtime["use_fw"]

# === Search Menu ===

def search_substr():
    s = minput("Enter search string").lower()
    results = sorted_by_friends(filter(lambda u: s in u.name.lower(), network.get_all_users()))
    if len(results) == 0:
        mprint(f"No results for \"{s}\"")
        return
    mprint(f"Search results for \"{s}\" ({len(results)}):")
    for user in results:
        mprint(f"\t{fmt_user(user)}")

def search_most_connected(least=False):
    n = int(minput("Enter how many"))
    users = sorted_by_friends(network.get_all_users(), reverse=not least)[:n]
    mprint(f"{"Least" if least else "Most"}-connected Users ({n}):")
    for u in users:
        mprint(f"\t{fmt_user(u)}")

def search_least_connected():
    search_most_connected(least=True)

# === User Menu ===

def user_select():
    user_display()
    
    uid = minput("Enter user ID")

    u = network.get_user_by_uid(int(uid))
    if not u:
        mprint(f"No user with ID '{uid}' found")
        return
    
    runtime["user"] = u
    user_display()

def user_display():
    u = runtime["user"]
    if not u:
        mprint("No user selected")
        return
    mprint(f"Current user: {fmt_user(u, pad_uid=False)}")

def n_degrees_list_bfs(u, n):
    users = sorted(network.bfs_traverse(u.uid, end_dist=n).items(), key=lambda it: it[1])
    lst = []
    for deg in range(1,n+1):
        deg_lst = sorted_by_friends(
            list(map(lambda id_deg: network.get_user_by_uid(id_deg[0]),
                filter(lambda id_deg: id_deg[1] == deg,
                    users))))
        if len(deg_lst) > 0:
            lst.append(deg_lst)
    return lst

def n_degrees_list_fw(u, n):
    v_list = network.get_all_uids()
    d_list = network.build_d_matrix_fw()[v_list.index(u.uid)]
    lst = []
    for deg in range(1,n+1):
        deg_lst = []
        for i in range(len(d_list)):
            if d_list[i] == deg:
                deg_lst.append(network.get_user_by_uid(v_list[i]))
        deg_lst = sorted_by_friends(deg_lst)
        if len(deg_lst) > 0:
            lst.append(deg_lst)
    return lst


def user_n_degrees():
    u = runtime["user"]
    if not u:
        mprint("No user selected")
        return
    
    n = int(minput("Enter value for N"))

    lst = n_degrees_list_fw(u, n) if use_fw() else n_degrees_list_bfs(u, n)

    mprint(f"Selected: {u.name}")
    for i in range(len(lst)):
        mprint(f"{ordinal(i+1)}-degree connections ({len(lst[i])})")
        j = 1
        for deg_u in lst[i]:
            mprint(f"\t{fmt_uid(deg_u.uid)}: {deg_u.name} ({len(deg_u.friends)})")
            if j >= 5 and len(lst[i])-j > 1:
                mprint(f"\t...{len(lst[i])-j} more...")
                break
            j += 1

def user_connection_path():
    u = runtime["user"]
    if not u:
        mprint("No user selected")
        return
    
    fid = int(minput("Enter target user ID"))

    path = network.get_path_fw(u.uid, fid) if use_fw() else network.get_path_dijkstra(u.uid, fid)
    if not path:
        mprint("No connection path found")
        return
    path.pop(0)
    mprint(f"Connection path found ({len(path)} steps):")

    def fmt(u): return f"{fmt_uid(u.uid)}: {u.name}"

    mprint(f"\t{fmt(u)}")
    for uid in path:
        next_u = network.get_user_by_uid(uid)
        mprint("\t ↓")
        mprint(f"\t{fmt(next_u)}")

def user_mutual_friends():
    u = runtime["user"]
    if not u:
        mprint("No user selected")
        return
    
    fid = int(minput("Enter target user ID"))

    f = network.get_user_by_uid(fid)
    mutuals = network.get_mutual_connections(u.uid, fid)
    if len(mutuals) == 0:
        mprint(f"No mutual friends with {f.name}")
        return
    mprint(f"Mutual friends with {f.name} ({len(mutuals)}):")
    for user in sorted_by_friends(network.get_users_by_uids(mutuals)):
        mprint(f"\t{fmt_user(user)}")

def user_friend_suggestions():
    u = runtime["user"]
    if not u:
        mprint("No user selected")
        return

    u_list = []
    for uid in network.get_all_uids():
        if uid == u.uid: continue
        n_mutual = len(network.get_mutual_connections(u.uid, uid))
        if n_mutual > 0: u_list.append((uid, n_mutual))
    
    if len(u_list) == 0:
        mprint("No friend recommendations") # todo: search 2nd-degree?
        return
    
    mprint(f"Friend suggestions for {u.name}:")
    u_list = sorted(
        map(lambda it: (network.get_user_by_uid(it[0]), it[1]), u_list),
            key=lambda it: (it[1], len(it[0].friends)), reverse=True)[:10]
    for user,m in u_list:
        mprint(f"\t{fmt_uid(user.uid)}: {user.name} ({len(user.friends)} friends, {m} mutual friends)")


# === Stats Menu ===

def stats_graph():
    total = network.get_total_users()
    visited = set()
    islands = 0
    diameter = 0
    while len(visited) < network.get_total_users():
        i = 0
        while i in visited or not network.get_user_by_uid(i):
            i += 1
            continue

        distances = network.bfs_traverse(i, visit_fn=lambda u: visited.add(u.uid))
        islands += 1

        d = sorted(distances.values(), reverse=True)[0]
        if diameter < d: diameter = d

    conn = "Fully connected" if islands == 1 else "Empty (no connections)" if islands == total else f"Disconnected ({islands} islands)"

    mprint(f"Graph diameter: {diameter}")
    mprint(f"Graph connectivity: {conn}")

def stats_users():
    n_users = network.get_total_users()
    n_conns = network.get_total_connections()
    mprint(f"Total Users: {n_users}")
    mprint(f"Total Connections: {n_conns}")
    mprint(f"Avg. Friends Per User: {n_conns * 2 / n_users}")


# ============================
#         MENU CONFIG
# ----------------------------

main_menu = [
    ("Options", ("options", [
        ("Distance algorithm -> BFS/Dijkstra", lambda: opt_set_use_fw(False)),
        ("Distance algorithm -> FW", lambda: opt_set_use_fw(True)),
    ])),
    ("Users", ("users", [
        ("Search users", ("search", [
            ("Substring search", search_substr),
            ("Most-connected users", search_most_connected),
            ("Least-connected users", search_least_connected),
        ])),
        ("Select user", user_select),
        ("Display current user", user_display),
        ("Connection path", user_connection_path),
        ("Users within N degrees", user_n_degrees),
        ("Mutual friends", user_mutual_friends),
        ("Friend suggestions", user_friend_suggestions),
    ])),
    ("Statistics", ("stats", [
        ("Graph statistics", stats_graph),
        ("User statistics", stats_users),
    ])),
]


# ============================
#        RUN PROGRAM
# ----------------------------

if len(argv) < 2:
    print("This program reads a social network graph stored in")
    print("a CSV file and provides tools to analyze the data\n")
    print(f"Usage: python3 {argv[0]} <CSV-PATH>")
    quit()

print("\n=== Social Network Analyzer ===\n")

loaded, msg = network.load_network_from_csv(argv[1])
if loaded:
    mprint(f"Network load: {msg}")
    print()
else:
    mprint(f"Network load error: {msg}")
    mquit()

try: Menu("main", main_menu).run()
except KeyboardInterrupt: print()
mquit()