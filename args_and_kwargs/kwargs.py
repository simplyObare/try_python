# **kwargs = allows you to pass multiple keyword arguments.
# Arguments are placed in a dictionary and can be operated as dictionary

def print_address(**kwargs):
    for value in kwargs.values():
        print(value)

    for key in kwargs.keys():
        print(key)

    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(print_address(street="123", city="Detroit", state="MI", zip="54321"))