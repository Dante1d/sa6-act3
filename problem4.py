def find_intersection(list1, list2):
    result = list(filter(lambda x: x in list1, list2))
    return result

list1 = [1, 2, 3, 4, 5]
list2 = [2, 5, 1, 6, 7]

result = find_intersection(list1, list2)
print("Intersection of the two list is:", result)