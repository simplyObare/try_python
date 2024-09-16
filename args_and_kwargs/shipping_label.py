from turtledemo.penrose import start


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    for value in kwargs.values():
        print(value, end=" ")

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")


shipping_label("Dr.", "SpongeBob", "SquarePants", "III",
               street="123", city="Detroit", state="MI", zip="54321")