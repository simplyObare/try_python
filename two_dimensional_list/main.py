# one dimensional lists
fruits = ["apple", "orange", "banana"]
vegetables = ["carrots", "tomatoes", "potatoes"]
meats = ["chicken", "pork", "harm"]

# two-dimensional list
groceries = [fruits, vegetables, meats]
print(groceries[0][2])
print(groceries[1][2])
print(groceries[2][2])

for collection in groceries:
    print(collection)
    for food in collection:
        print(food)