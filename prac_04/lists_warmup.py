# List play
numbers = [3, 1, 4, 1, 5, 9, 2]

# Change first element to "ten"
numbers[0] = "ten"
# Change the last element of numbers to 1
numbers[-1] = 1
# Get all the elements from numbers except the first two
list_slice = numbers[2:]
# Check i 9 is in numbers
bool_test = 9 in numbers

print(numbers, '\n', list_slice, '\n', bool_test)
