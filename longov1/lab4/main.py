from SortedNumberList import SortedNumberList

# include_removals = False
include_removals = True

# Numbers to insert during first loop:
numbers_to_insert = [ 77.75, 15.25, -4.25, 63.5, 18.25, -3.5 ]
# numbers_to_insert = [ 4000.75, 105.25, -4444.25, 6143.5, 1448.25, -300.5 ]
# numbers_to_insert = [ 4000.75, 105.25, -4444.25, 6143.5, 1448.25, -300.5 ]
# numbers_to_insert = [ 66, 19, -707, 11.11, -9000, 19.84, 2049, 13 ]

# Insert each number and print sorted list's contents after each insertion
sorted_list = SortedNumberList()
for number in numbers_to_insert:
    print(f"List after inserting {number:.2f}: ", end="")
    sorted_list.insert(number)
    print(sorted_list.to_string(", ", "(", ")"))
   
if include_removals:
    print()
    numbers_to_remove = [
        77.75, # List's last element
        -4.25, # List's first element
        18.25, # Neither first nor last element
         
        # Remaining elements:
        15.25, 63.5, -3.5
    ]
    
    # Remove numbers
    for to_remove in numbers_to_remove:
        print(f"List after removing {to_remove:.2f}: ", end="")
        sorted_list.remove(to_remove)
        print(sorted_list.to_string(", ", "(", ")"))