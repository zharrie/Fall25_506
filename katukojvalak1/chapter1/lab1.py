#lab
from LabPrinter import LabPrinter

def call_method_named(printer, method_name):
    if method_name == "print_2_plus_2":
        printer.print_2_plus_2()
    elif method_name == "print_secret":
        printer.print_secret()
    else:
        print(f"Unknown method: {method_name}")
    pass

# Main program code follows
printer = LabPrinter("abc")

call_method_named(printer, "print_2_plus_2")
call_method_named(printer, "print_plus_2")
call_method_named(printer, "print_secret")