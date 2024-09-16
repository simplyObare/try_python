weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (kg or lb): ")

if unit == "kg":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "lb":
    weight = weight / 2.205
    unit = "kgs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid!")

