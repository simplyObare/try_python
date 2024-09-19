try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter a number please")
except Exception:
    print("Something went wrong")
finally:
    print("Do some clean up")