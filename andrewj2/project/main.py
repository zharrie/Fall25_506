import sys
from SocialNetwork import User, Network

# ============================
#         MENU LOGIC
# ----------------------------

def mprint(x):
    print(f"> {x}")

def mquit():
    mprint("Exiting...")
    quit()

def minput(s):
    return input(f"{s}>> ").strip()

def run_menu(menu: dict, name: str):
    menu_str = f"[{name.upper()} MENU]"
    menu_str += f"\n  [x] {menu["x"][0]}" if "x" in menu.keys() else f"\n  [x] Exit this menu"
    menu_str += f"\n  [m] {menu["m"][0]}" if "m" in menu.keys() else f"\n  [m] Print this menu again"
    for k,v in menu.items():
        if k in ["x","m"]: continue
        menu_str += f"\n  [{k}] {v[0]}"

    print(menu_str)

    while True:
        opt = input(">> ").strip().lower()
        if not opt: continue
        elif opt == 'xx': mquit() # exit the program
        elif opt == 'x': break # exit menu loop
        elif opt == 'm': print(menu_str)
        elif opt in menu.keys():
            if type(menu[opt][1]) is tuple:
                submenu = menu[opt][1]
                run_menu(submenu[0], submenu[1])
                print(menu_str)
            else:
                try: menu[opt][1]()
                except Exception as e:
                    mprint(f"Error: {e}")
        else: mprint(f"Invalid selection: {opt}")


# ============================
#        NETWORK LOGIC
# ----------------------------

network = Network()
runtime = {
    "user": None
}

def fmt_user(u):
    return f"{str(u.id).zfill(4)}: {u.name} ({len(u.friends)} friends)"

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


# === Stats Menu ===

def graph_stats():
    distances = network.bfs_traverse(0)
    mprint(f"Graph diameter: {sorted(distances.values(), reverse=True)[0]}")
    mprint(f"Graph connectivity: {"Connected" if len(distances) == network.get_total_users() else "Disconnected"}")


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

user_menu = {
    "1": ("Search users", user_search),
    "2": ("Select user", select_user),
    "3": ("Display current user", display_cur_user),
    "4": ("Connection path", todo),
    "5": ("Friends within N degrees", todo),
    "6": ("Mutual friends", todo),
    "7": ("Friend suggestions", todo),
}

stats_menu = {
    "1": ("Graph statistics", graph_stats),
    "2": ("User statistics", user_stats),
    "3": ("Most-connected users", most_connected),
    "4": ("Least-connected users", least_connected),
}

main_menu = {
    "x": ("Exit the program", None),
    "1": ("User menu", (user_menu, "user")),
    "2": ("Statistics menu", (stats_menu, "stats")),
}


# ============================
#        RUN PROGRAM
# ----------------------------

if len(sys.argv) < 2:
    print("This program reads a social network graph stored in")
    print("a CSV file and provides tools to analyze the data\n")
    print(f"Usage: python3 {sys.argv[0]} <CSV-PATH>")
    quit()

print("\n=== Social Network Analyzer ===\n")

loaded, msg = network.load_network_from_csv(sys.argv[1])
if loaded:
    mprint(f"Network load: {msg}")
    print()
else:
    mprint(f"Network load error: {msg}")
    mquit()

run_menu(main_menu, "main")
mquit()