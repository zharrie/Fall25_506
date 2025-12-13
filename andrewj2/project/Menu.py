def mprint(x):
    print(f"> {x}")

def mquit():
    mprint("Exiting...")
    quit()

def minput(s=""):
    return input(f"{s}>> ").strip()

class Menu:
    EXIT_ALL = "qq"
    EXIT = "q"
    MENU = "w"

    def __init__(self, name: str, cfg: list):
        self.name = name
        self.cfg = cfg
        self.menu_str = self.build_menu_str(name, cfg)

    def build_menu_str(self, name: str, cfg: list):
        s = [f"[{name.upper()} MENU]"]
        s.append(f"  [{self.EXIT}] Exit this menu")
        s.append(f"  [{self.MENU}] Print this menu again")
        n = 1
        for item in cfg:
            idx,title,_ = item
            if idx == self.EXIT: s[1] = f"  [{self.EXIT}] {title}"
            if idx == self.MENU: s[2] = f"  [{self.MENU}] {title}"
            if idx == "n":
                s.append(f"  [{n}] {title}")
                n += 1
        return "\n".join(s)

    def run(self):
        cfg = list(map(lambda n: (n[1],n[2]), filter(lambda n: n[0] == 'n', self.cfg)))

        print(self.menu_str)

        while True:
            opt = minput().lower()
            if not opt: continue
            elif opt == self.EXIT_ALL: mquit() # exit the program
            elif opt == self.EXIT: break # exit menu loop
            elif opt == self.MENU: print(self.menu_str)
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
                    Menu(sub_cfg[0], sub_cfg[1]).run()
                    print(self.menu_str)
                else:
                    try: cfg[i][1]()
                    except Exception as e:
                        mprint(f"Error: {e}")
