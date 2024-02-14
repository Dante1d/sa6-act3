myList = ["apple", "grape", "orange", "pear", "pineapple"]

sorted_strings = sorted(myList, key=lambda x: (len(x), x))

print(sorted_strings)
for string in sorted_strings:
    print(string)