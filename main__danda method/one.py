# What is "'if__name__== '__main__"


def read_file():
    with open("files/text.txt", "r") as f:
        print(f.read())


def is_main():
    print("I am being run directly from my original source file")
    read_file()


def not_main():
    print("I HAVE BEEN IMPORTED HERE")
    read_file()


if __name__ == "__main__":
    is_main()
else:
    not_main()
