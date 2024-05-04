def shift_right(lst, num_shifts):
    length = len(lst)
    num_shifts %= length  # To handle cases where num_shifts > length
    return lst[-num_shifts:] + lst[:-num_shifts]

# Get list from the user
my_list = input("Enter elements of the list separated by space: ").split()

# Convert input elements to integers
my_list = [int(x) for x in my_list]

# Get number of shifts from the user
num_shifts = int(input("Enter the number of shifts: "))

# Perform the shift and print the result
shifted_list = shift_right(my_list, num_shifts)
print("Shifted list:", shifted_list)