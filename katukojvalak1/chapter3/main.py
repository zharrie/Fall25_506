from NaturalMergeSorter import NaturalMergeSorter
from RunLengthTestCase import RunLengthTestCase

def is_list_sorted(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True

# Main program code follows

# Test case 1: A completely sorted list
list1 = [ 15, 23, 23, 23, 31, 64, 77, 87, 88, 91 ]

# Test case 2: Sorted run of 3 followed by sorted run of 6
list2 = [ 64, 88, 91, 12, 21, 34, 43, 56, 65 ]

# Test case 3: 5 elements in descending order, so 5 runs of length 1
list3 = [ -10, -20, -30, -40, -50 ]

# Test case array: 8 equal elements, so 1 run of 8
list4 = [ -99, -99, -99, -99, -99, -99, -99, -99 ]

# Test cases:
test_cases = [
    # First test case uses an out-of-bounds starting index. Remaining test
    # cases do not.
    RunLengthTestCase(list1, len(list1), 0),

    RunLengthTestCase(list1, 0, len(list1)),
    RunLengthTestCase(list1, 3, len(list1) - 3),
    RunLengthTestCase(list2, 0, 3),
    RunLengthTestCase(list2, 2, 1),
    RunLengthTestCase(list2, 3, 6),
    RunLengthTestCase(list3, 0, 1),
    RunLengthTestCase(list3, 3, 1),
    RunLengthTestCase(list4, 0, len(list4)),
    RunLengthTestCase(list4, 4, len(list4) - 4),
    RunLengthTestCase(list4, 5, len(list4) - 5)
]

# Execute each test case
for test_case in test_cases:
    test_case.execute()

# Test case list for sorting
list5 = [ 92, 71, 18, 26, 54, 73, 89, 10, 39, 99, 64, 22 ]
list5_copy = list(list5)

sorter = NaturalMergeSorter()
sorter.natural_merge_sort(list5_copy)
print(f'\n{"PASS" if is_list_sorted(list5_copy) else "FAIL"}' +
    ": natural_merge_sort()\n" +
    f"    List before calling natural_merge_sort(): {list5}\n" +
    f"    List after calling natural_merge_sort():  {list5_copy}")