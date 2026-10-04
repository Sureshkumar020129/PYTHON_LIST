print(" Find all duplicate elements in a list. ")
numbers = [1, 2, 2, 3, 3, 4, 5]
duplicates = [n for n in numbers if numbers.count(n) > 1]
print(duplicates)