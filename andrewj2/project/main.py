from SocialNetwork import User, Network

network = Network()

def find_path():
    print("Find connection path")
def n_degrees():
    print("Friends within N degrees")
def most_connected():
    print("Most connected users")
def mutual_friends():
    print("Mutual friends")
def friend_suggestions():
    print("Friend suggestions")
def network_stats():
    n_users = network.get_total_users()
    n_conns = network.get_total_connections()
    mprint(f"Total Users: {n_users}")
    mprint(f"Total Connections: {n_conns}")
    mprint(f"Average Connections Per User: {n_conns / n_users}")
def user_search():
    term = input("Enter search term >> ").strip()
    for u in network.search_users_by_name(term):
        mprint(f"{str(u.id).zfill(4)}: {u.name} ({len(u.friends)} friends)")

main_menu = {
    "x": ("Exit the program", None),
    "1": ("Find connection path", find_path),
    "2": ("Friends within N degrees", n_degrees),
    "3": ("Most connected users", most_connected),
    "4": ("Mutual friends", mutual_friends),
    "5": ("Friend suggestions", friend_suggestions),
    "6": ("Network statistics", network_stats),
    "7": ("User search", user_search),
}

def mprint(x):
    print(f"> {x}")

def run_menu(menu: dict, title: str):
    menu_str = f"[{title.upper()}]"
    menu_str += f"\n  [x] {menu["x"][0]}" if "x" in menu.keys() else f"\n  [x] Exit this menu"
    menu_str += f"\n  [m] {menu["m"][0]}" if "m" in menu.keys() else f"\n  [m] Print this menu again"
    for k,v in menu.items():
        if k in ["x","m"]: continue
        menu_str += f"\n  [{k}] {v[0]}"

    print(menu_str)

    while True:
        opt = input(">> ").strip().lower()
        if not opt: continue
        elif opt == 'x': break # exit menu loop
        elif opt == 'm': print(menu_str)
        elif opt in menu.keys():
            try:
                menu[opt][1]()
            except Exception as e:
                mprint(f"Error: {e}")
        else: mprint(f"Invalid selection: {opt}")


print("\n=== Social Network Analyzer ===\n")

loaded, msg = network.load_network_from_csv("network.csv")
if loaded:
    mprint(f"Network load: {msg}")
    print()
    network_stats()
    print()
else:
    mprint(f"Network load error: {msg}")
    mprint("Exiting...")
    quit()

# for user in network.get_top_n_users(10):
#     print(user)

run_menu(main_menu, "main menu")