def mprint(x):
    print(f"> {x}")

def mquit():
    mprint("Exiting...")
    quit()

def minput(s=""):
    return input(f"{s}>> ").strip()

def build_menu_str(name: str, cfg: list):
    menu = [f"[{name.upper()} MENU]"]
    menu.append(f"  [x] Exit this menu")
    menu.append(f"  [m] Print this menu again")
    n = 1
    for item in cfg:
        idx,title,_ = item
        if idx == "x": menu[1] = f"  [x] {title}"
        if idx == "m": menu[2] = f"  [m] {title}"
        if idx == "n":
            menu.append(f"  [{n}] {title}")
            n += 1
    return "\n".join(menu)


def run_menu(name: str, cfg: list):
    menu = build_menu_str(name, cfg)
    cfg = list(map(lambda n: (n[1],n[2]), filter(lambda n: n[0] == 'n', cfg)))

    print(menu)

    while True:
        opt = minput().lower()
        if not opt: continue
        elif opt == 'xx': mquit() # exit the program
        elif opt == 'x': break # exit menu loop
        elif opt == 'm': print(menu)
        else:
            i = 0
            try: i = int(opt)
            except: pass
            i -= 1

            if i < 0 or i >= len(cfg):
                mprint(f"Invalid selection: {opt}")
                continue

            if type(cfg[i][1]) is tuple:
                sub_cfg = cfg[i][1]
                run_menu(sub_cfg[0], sub_cfg[1])
                print(menu)
            else:
                try: cfg[i][1]()
                except Exception as e:
                    mprint(f"Error: {e}")
