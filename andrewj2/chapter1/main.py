from LabPrinter import LabPrinter

def call_method_named(printer, name):
    if name in ["print_2_plus_2","print_secret"]:
        getattr(printer, name)()
        return
    print(f"Unknown method: {name}")

printer = LabPrinter("abc")

call_method_named(printer, "print_2_plus_2")
call_method_named(printer, "print_plus_2")
call_method_named(printer, "print_secret")