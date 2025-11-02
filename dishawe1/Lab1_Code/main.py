from LabPrinter import LabPrinter

def call_method_named(printer, method_name):
    # TODO: Implement this function after completing step 1
    if method_name == "print_2_plus_2":
        printer.print_2_plus_2()
    elif method_name == "print_secret":
        printer.print_secret()
    else : 
        print("Unknown method:", method_name)

# Main program code follows
printer = LabPrinter("abc")
   
# TODO: Step 1:
# Uncomment the lines below and submit code for grading. Note that the
# submission passes the "Compare output" test, but fails each unit test.

    
# TODO: After completing step 1:
# Remove lines of code from step 1 and implement the call_method_named() 
# function above the main program code
call_method_named(printer, "print_2_plus_2")
call_method_named(printer, "print_plus_2")
call_method_named(printer, "print_secret")