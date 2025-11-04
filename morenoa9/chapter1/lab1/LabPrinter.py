class LabPrinter:
    def __init__(self, secret_string_value):
        self.secret = secret_string_value

    def print_2_plus_2(self):
        print("2 + 2 = 4")
    
    def print_secret(self):
        print(f"Secret string: \"{self.secret}\"")
