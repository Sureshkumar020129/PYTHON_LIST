print("Find all unique elements in a list. ")
numbers = [1, 2, 2, 3, 3, 4, 5]
unique_numbers = [n for n in numbers if numbers.count(n) == 1]
print(unique_numbers)