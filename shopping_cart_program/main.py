foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want to buy ( enter q to Quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the food you want to buy: $"))
        foods.append(food)
        prices.append(price)

print("--------- YOUR CART ---------")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"Your total price is: ${total:.2f}")