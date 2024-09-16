# format specifiers = {value: flags} format a value based on what flags are inserted

price1 = 3.1456721
price2 = -2212.23
price3 = 12.23

# to specify decimal place
print(f"value is: {price1:.2f}")
print(f"value is: {price2:.1f}")
print(f"value is: {price3:.4f}")


dollars = 3000000.35666
print(f"dollars $: {dollars:,.2f}")