# *args = allows you to pass multiple non-key arguments
# the arguments are placed in a tuple and are legible to all tuple functionality

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5))


def display_names(*args):
    for arg in args:
        print(arg, end=" ")

print(display_names("Dr.", "SpongeBob", "SquarePants", "III"))