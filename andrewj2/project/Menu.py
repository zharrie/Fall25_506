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

    def __init__(self, name: str, cfg: list, root=True):
        self.name = name
        self.cfg = cfg
        self.root = root
        self.menu_str = self.build_menu_str()

    def build_menu_str(self):
        s = [f"[{self.name.upper()} MENU]"]
        s.append(f"  [{self.EXIT}] {"Exit program" if self.root else "Previous menu"}")
        s.append(f"  [{self.MENU}] Print current menu")
        for i in range(len(self.cfg)):
            s.append(f"  [{i+1}] {self.cfg[i][0]}")
        return "\n".join(s)

    def run(self):
        print(self.menu_str)
        while True:
            opt = minput().lower()
            if not opt: continue
            elif opt == self.EXIT_ALL: mquit() # exit the program
            elif opt == self.EXIT: break # exit menu loop
            elif opt == self.MENU: print(self.menu_str)
            else:
                i = -1
                try: i = int(opt)-1
                except: pass

                if i < 0 or i >= len(self.cfg):
                    mprint(f"Invalid selection: {opt}")
                    continue

                if type(self.cfg[i][1]) is tuple:
                    sub_cfg = self.cfg[i][1]
                    Menu(sub_cfg[0], sub_cfg[1], root=False).run()
                    print(self.menu_str)
                else:
                    try: self.cfg[i][1]()
                    except Exception as e:
                        mprint(f"Error: {e}")
