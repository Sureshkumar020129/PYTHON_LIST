print("Find all pairs whose sum equals a given number. ")
numbers = [1, 2, 3, 4, 5]
target = 6
pairs = [(x, y) for x in numbers for y in numbers if x < y and x + y == target]
print(pairs)