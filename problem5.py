nums = [2, 4, 6, 8, 10]

n = 2

print("Original list:", nums)

print("Given number:", n)

powered_num = list(map(lambda x: x ** n, nums))

print(f"Numbers raised to the power of {n}: {powered_num}")