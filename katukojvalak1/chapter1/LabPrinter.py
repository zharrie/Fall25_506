class LabPrinter:
    def __init__(self, secret):
        self.secret = secret

    def print_2_plus_2(self):
        print("2 + 2 = 4")

    def print_secret(self):
        print(f'Secret string: "{self.secret}"')
