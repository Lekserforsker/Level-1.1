def print_staircase(size):
    for i in range(1, size + 1):
        print(" " * (size - i) + "*" * i)

def print_double_sided_staircase(size):
    for i in range(1, size + 1):
        print(" " * (size - i) + "*" * i + " " * (size - i) + "*" * i)

size = int(input("Enter the size of the staircase: "))
print("Single-sided staircase:")
print_staircase(size)
print("\nDouble-sided staircase:")
print_double_sided_staircase(size)
