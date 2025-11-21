from GroceryList import GroceryList
from GroceryListTest import GroceryListTest

# Test 1 tests insertion and undo of insertion only
def test1(test_feedback):
    test = GroceryListTest([
        "add carrots",
        "verify carrots",
        "undo",   # undo addition of carrots
        "verify", # verify empty list
        "add potatoes",
        "verify potatoes",
        "add carrots",
        "verify potatoes,carrots",
        "add lettuce",
        "verify potatoes,carrots,lettuce",
        "add rice",
        "verify potatoes,carrots,lettuce,rice",
        "add cilantro",
        "verify potatoes,carrots,lettuce,rice,cilantro",
        "undo",  # undo addition of cilantro
        "verify potatoes,carrots,lettuce,rice",
        "undo",  # undo addition of rice
        "verify potatoes,carrots,lettuce",
        "undo",  # undo addition of lettuce
        "verify potatoes,carrots",
        "undo",  # undo addition of carrots
        "verify potatoes",
        "undo",  # undo addition of potatoes
        "verify",
        "add basil",
        "verify basil",
        "add onions",
        "verify basil,onions",
        "add spinach",
        "verify basil,onions,spinach",
        "undo",  # undo addition of spinach
        "verify basil,onions",
        "undo",  # undo addition of onions
        "verify basil",
        "undo",  # undo addition of basil
        "verify"
    ], test_feedback)
    return test.execute()

# Test 2 tests insertion and swapping and the undo of each
def test2(test_feedback):
    test = GroceryListTest([
        "add chips",
        "add cookies",
        "add waffles",
        "add syrup",
        "add ice cream",
        "add lettuce",
        "verify chips,cookies,waffles,syrup,ice cream,lettuce",
        "swap 1 4", # swap cookies and ice cream
        "verify chips,ice cream,waffles,syrup,cookies,lettuce",
        "undo", # undo the swap
        "verify chips,cookies,waffles,syrup,ice cream,lettuce"
    ], test_feedback)
    return test.execute()

# Test 3 tests all commands
def test3(test_feedback):
    test = GroceryListTest([
        "add orange juice",
        "add apple juice",
        "verify orange juice,apple juice",
        "undo", # undo add apple juice
        "verify orange juice",
        "removeat 0",
        "verify",
        "undo", # undo remove orange juice
        "verify orange juice",
        "undo", # undo add orange juice
        "verify",
        "add mango juice",
        "verify mango juice",
        "add grapefruit juice",
        "add grape juice",
        "verify mango juice,grapefruit juice,grape juice",
        "swap 0 1",
        "verify grapefruit juice,mango juice,grape juice",
        "add strawberry smoothie",
        "verify grapefruit juice,mango juice,grape juice,strawberry smoothie",
        "swap 2 3",
        "verify grapefruit juice,mango juice,strawberry smoothie,grape juice",
        "removeat 3",
        "verify grapefruit juice,mango juice,strawberry smoothie",
        "removeat 1",
        "verify grapefruit juice,strawberry smoothie",
        "swap 0 1",
        "verify strawberry smoothie,grapefruit juice",
        "undo", # undo swap 0 1
        "undo", # undo removal of mango juice
        "undo", # undo removal of grape juice
        "undo", # undo swap 2 3
        "undo", # undo add strawberry smoothie
        "verify grapefruit juice,mango juice,grape juice",
        "undo", # undo swap 0 1
        "undo", # undo add grape juice
        "verify mango juice,grapefruit juice",
        "undo", # undo add grapefruit juice
        "verify mango juice",
        "undo", # undo add mango juice
        "verify"
    ], test_feedback)
    return test.execute()

# FeedbackPrinter is used to print feedback when testing locally
class FeedbackPrinter:
    def write(self, text):
        print(text)

# Main program code follows

# Run tests
feedback = FeedbackPrinter()
tests_passed = [test1(feedback)]
print()
#tests_passed.append(test2(feedback))
#print()
#tests_passed.append(test3(feedback))
#print()

# Print summary
for i in range(len(tests_passed)):
    print(f'Test {i + 1}: {"PASS" if tests_passed[i] else "FAIL"}')