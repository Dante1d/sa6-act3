def find_max(numbers, compare):
    max = numbers[0]

    for num in numbers[1:]:
        max = compare(num, max)
    return max

numbers = [3, 8, 4, 9, 10, 2, 12]

compare = lambda a, b: a if a > b else b

max = find_max(numbers, compare)

print("Maximum number in the list:", max)