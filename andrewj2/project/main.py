from sys import argv
from Menu import *
from SocialNetwork import *

# ============================
#        NETWORK LOGIC
# ----------------------------

network = Network()
runtime = {
    "user": None,
    "dist_alg": "bfs",
}

# === Helper Functions ===

def digits():
    if not runtime.get("digits"): runtime["digits"] = math.floor(math.log10(network.get_total_users()))
    return runtime["digits"]

def fmt_uid(uid):
    return str(uid).zfill(digits())

def fmt_user(u):
    return f"{fmt_uid(u.uid)}: {u.name} ({len(u.friends)} friends)"

def ordinal(n: int): # credit: https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement
    if 11 <= (n % 100) <= 13: suffix = 'th'
    else: suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

def todo():
    mprint("TODO")

# === Options Menu ===

def opt_set_dist_alg(s):
    runtime["dist_alg"] = s
    alg = "Floyd-Warshall" if s == "fw" else "BFS/Dijkstra"
    mprint(f"Now using {alg} for distance calculations")

# === User Menu ===

def user_search():
    s = minput("Enter search string").lower()
    for user in filter(lambda u: s in u.name.lower(), network.get_all_users()):
        mprint(fmt_user(user))

def user_select():
    user_display()
    
    uid = minput("Enter user ID")

    u = network.get_user_by_uid(int(uid))
    if not u:
        mprint(f"No user with ID '{uid}' found")
    else:
        mprint(f"Selected user {u.uid}: {u.name}")
    runtime["user"] = u

def user_display():
    u = runtime["user"]
    if not u:
        mprint("No user selected")
    else:
        mprint(f"Current user: {u.name} ({u.uid}), {len(u.friends)} friends")

def user_n_degrees():
    u = runtime["user"]
    if not u:
        mprint("No user selected")
        return
    
    n = int(minput("Enter value for N"))

    def n_degrees_list_bfs(u, n):
        users = sorted(network.bfs_traverse(u.uid, end_dist=n).items(), key=lambda it: it[1])
        lst = []
        for deg in range(1,n+1):
            deg_lst = sorted(
                list(map(lambda id_deg: network.get_user_by_uid(id_deg[0]),
                    filter(lambda id_deg: id_deg[1] == deg,
                        users))),
                key=lambda u: len(u.friends), reverse=True)
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
            deg_lst.sort(key=lambda u: len(u.friends), reverse=True)
            if len(deg_lst) > 0:
                lst.append(deg_lst)
        return lst

    use_fw = runtime["dist_alg"] == "fw"
    lst = n_degrees_list_fw(u, n) if use_fw else n_degrees_list_bfs(u, n)

    mprint(f"Selected: {u.name}")
    for i in range(len(lst)):
        mprint(f"{ordinal(i+1)}-degree connections ({len(lst[i])})")
        j = 1
        for deg_u in lst[i]:
            mprint(f"\t{deg_u.name} ({len(deg_u.friends)})")
            if j >= 5 and len(lst[i])-j > 1:
                mprint(f"\t...{len(lst[i])-j} more...")
                break
            j += 1

def user_connection_path():
    u = runtime["user"]
    if not u:
        mprint("No user selected")
        return
    
    uid = int(minput("Enter target user ID"))

    path = network.get_path_fw(u.uid, uid)
    if not path:
        mprint("No connection path found")
        return
    mprint(f"Connection path found ({len(path)} steps):")

    def fmt(u): return f"{fmt_uid(u.uid)}: {u.name}"

    mprint(f"\t{fmt(u)}")
    for step in path:
        next_u = network.get_user_by_uid(step[1])
        mprint("\t ↓")
        mprint(f"\t{fmt(next_u)}")

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

def stats_most_connected(least=False):
    n = int(minput("Enter how many"))
    users = sorted(network.get_all_users(), key=lambda u: len(u.friends), reverse=not least)[:n]
    for u in users:
        mprint(fmt_user(u))

def stats_least_connected():
    stats_most_connected(least=True)


# ============================
#         MENU CONFIG
# ----------------------------

main_menu = [
    ("Options", ("options", [
        ("Distance algorithm -> BFS", lambda: opt_set_dist_alg("bfs")),
        ("Distance algorithm -> FW", lambda: opt_set_dist_alg("fw")),
    ])),
    ("Users", ("users", [
        ("Search users", user_search),
        ("Select user", user_select),
        ("Display current user", user_display),
        ("Connection path", user_connection_path),
        ("Users within N degrees", user_n_degrees),
        ("Mutual friends", todo),
        ("Friend suggestions", todo),
    ])),
    ("Statistics", ("stats", [
        ("Graph statistics", stats_graph),
        ("User statistics", stats_users),
        ("Most-connected users", stats_most_connected),
        ("Least-connected users", stats_least_connected),
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

Menu("main", main_menu).run()
mquit()