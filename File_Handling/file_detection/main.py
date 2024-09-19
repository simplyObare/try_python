import os

file_path = "text.txt"
another_path = "Stuff/stuff.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else:
    print("That location doesn't exist")

if os.path.exists(another_path):
    print(f"The location '{another_path}' exists")
else:
    print("That location doesn't exist")