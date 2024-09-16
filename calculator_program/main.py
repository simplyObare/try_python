operator = input("Enter an operator (+ - / *): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
else:
    input(f"The program does not support this {operator} operator. Enter an operator (+ - / *): ")