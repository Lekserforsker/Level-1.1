def print_staircase(size):
    for i in range(1, size + 1):

        print(' ' * (size - i), end='')
        # Print staircase
        print('*' * i)

def print_double_staircase(size):
    for i in range(1, size + 1):
        # Print leading spaces
        print(' ' * (size - i), end='')
        # Print left side of the staircase
        print('*' * i, end=' ')
        # Print right side of the staircase
        print('*' * i)


size = int(input("Enter the size of the staircase: "))


print("Single-sided staircase:")
print_staircase(size)


print("\nDouble-sided staircase:")
print_double_staircase(size)

