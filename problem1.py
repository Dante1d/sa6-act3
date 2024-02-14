sum_digits = lambda n: sum(int(digit) for digit in str(n))

number = 1234

result = sum_digits(number)

print(f"The sum of digits of {number} is {result}")