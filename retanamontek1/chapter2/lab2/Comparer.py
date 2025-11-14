# Comparer is a base class that can compare two items with the compare()
# method. compare() compares items a and b and returns an integer:
# - greater than 0 if a > b,
# - less than 0 if a < b, or
# - equal to 0 if a == b
class Comparer:
    def compare(self, a, b):
        if a > b:
            return 1
        elif a < b:
            return -1
        return 0