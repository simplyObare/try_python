# indexing - accessing elements of a sequence using [] (indexing operator

# [star: end : step]

credit_number = "1231-4562-7883-2344"

print(credit_number[0])
print(credit_number[:4])
print(credit_number[5:])
print(credit_number[3:6])
print(credit_number[5:9])
print(credit_number[:-2])
print(credit_number[::2]) # prints every second character within our string
print(credit_number[::3]) # prints every third character within our string

# credit card digit example
credit_num = "5321-4575-0988-7105"

last_digits = credit_num[-4:]
print(f"XXXX-XXXX-XXX-{last_digits}")

# reverse credit_num
reverse_credit_num = credit_num[::-1]
print(reverse_credit_num)