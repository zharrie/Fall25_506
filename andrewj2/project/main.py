from SocialNetwork import User, UserMap

users = UserMap()

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
    raise ValueError("test")
    print("Network statistics")

main_menu = {
    "x": ("Exit the program", None),
    "1": ("Find connection path", find_path),
    "2": ("Friends within N degrees", n_degrees),
    "3": ("Most connected users", most_connected),
    "4": ("Mutual friends", mutual_friends),
    "5": ("Friend suggestions", friend_suggestions),
    "6": ("Network statistics", network_stats),
}

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
            except ValueError as err:
                print(f"[Error encountered: {err}]")
        else: print(f"[Invalid selection: {opt}]")


print("\n=== Social Network Analyzer ===\n")

loaded, msg = users.load_network_from_csv("people.csv")

if loaded:
    print(f"[Network load: {msg}]\n")
else:
    print(f"[Network load error: {msg}]")
    print("\nExiting...")
    quit()

run_menu(main_menu, "main menu")