from sys import argv
from Menu import *
from SocialNetwork import *

# ============================
#        NETWORK LOGIC
# ----------------------------

network = Network()
runtime = {
    "user": None
}

def fmt_user(u):
    return f"{str(u.id).zfill(4)}: {u.name} ({len(u.friends)} friends)"

# credit: https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement
def ordinal(n: int):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

def todo():
    mprint("TODO")

# === User Menu ===

def user_search():
    term = minput("Enter search term")
    for user in network.search_users_by_name(term):
        mprint(fmt_user(user))

def select_user():
    display_cur_user()
    
    id = minput("Enter user ID")
    if id == 'x': return
    if id == 'xx': mquit()

    u = network.get_user_by_id(int(id))
    if not u:
        mprint(f"No user with ID '{id}' found")
    else:
        mprint(f"Selected user {u.id}: {u.name}")
    runtime["user"] = u

def display_cur_user():
    u = runtime["user"]
    if not u:
        mprint("No user selected")
    else:
        mprint(f"Current user: {u.name} ({u.id}), {len(u.friends)} friends")

def users_n_degrees():
    u = runtime["user"]
    if not u:
        mprint("No user selected")
        return
    
    n = int(minput("Enter value for N"))
    
    users = sorted(network.bfs_traverse(u.id, end_dist=n).items(), key=lambda it: it[1])
    mprint(f"Selected: {u.name}")
    for deg in range(1,n+1):
        deg_ids = sorted(list(map(lambda it: it[0], filter(lambda it: it[1] == deg, users))),
            key=lambda it: len(network.get_user_by_id(it).friends), reverse=True)
        mprint(f"{ordinal(deg)}-degree connections ({len(deg_ids)})")
        i = 1
        for id in deg_ids:
            c = network.get_user_by_id(id)
            if not c: continue
            mprint(f"\t{c.name} ({len(c.friends)})")
            if i >= 5:
                mprint(f"\t...{len(deg_ids)-i} more...")
                break
            i += 1


# === Stats Menu ===

def graph_stats():
    total = network.get_total_users()
    visited = set()
    islands = 0
    diameter = 0
    while len(visited) < network.get_total_users():
        i = 0
        while i in visited or not network.get_user_by_id(i):
            i += 1
            continue

        distances = network.bfs_traverse(i, visit_fn=lambda u: visited.add(u.id))
        islands += 1

        d = sorted(distances.values(), reverse=True)[0]
        if diameter < d: diameter = d

    conn = "Fully connected" if islands == 1 else "Empty (no connections)" if islands == total else f"Disconnected ({islands} islands)"

    mprint(f"Graph diameter: {diameter}")
    mprint(f"Graph connectivity: {conn}")

def user_stats():
    n_users = network.get_total_users()
    n_conns = network.get_total_connections()
    mprint(f"Total Users: {n_users}")
    mprint(f"Total Connections: {n_conns}")
    mprint(f"Average Connections Per User: {n_conns / n_users}")

def most_connected(least=False):
    n = int(minput("Enter how many"))
    users = network.get_top_n_users(n, least)
    for u in users:
        mprint(fmt_user(u))

def least_connected():
    most_connected(least=True)


# ============================
#         MENU CONFIG
# ----------------------------

main_menu = [
    ("x", "Exit the program", None),
    ("n", "User menu", ("user", [
        ("n", "Search users", user_search),
        ("n", "Select user", select_user),
        ("n", "Display current user", display_cur_user),
        ("n", "Connection path", todo),
        ("n", "Users within N degrees", users_n_degrees),
        ("n", "Mutual friends", todo),
        ("n", "Friend suggestions", todo),
    ])),
    ("n", "Statistics menu", ("stats", [
        ("n", "Graph statistics", graph_stats),
        ("n", "User statistics", user_stats),
        ("n", "Most-connected users", most_connected),
        ("n", "Least-connected users", least_connected),
    ])),
]


# ============================
#        RUN PROGRAM
# ----------------------------

if len(argv) < 2:
    print("This program reads a social network graph stored in")
    print("a CSV file and provides tools to analyze the data\n")
    print(f"Usage: python3 {sys.argv[0]} <CSV-PATH>")
    quit()

print("\n=== Social Network Analyzer ===\n")

loaded, msg = network.load_network_from_csv(argv[1])
if loaded:
    mprint(f"Network load: {msg}")
    print()
else:
    mprint(f"Network load error: {msg}")
    mquit()

run_menu("main", main_menu)
mquit()