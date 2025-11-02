from Comparer import Comparer

# Comparer for a list sorted in descending order
class DescendingComparer(Comparer):
    def compare(self, a, b):
        if a < b:
            return 1
        elif a > b:
            return -1
        return 0