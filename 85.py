print("Find all triplets whose sum equals a given number")
numbers = [1, 2, 3, 4, 5]
target = 9
triplets = [(x, y, z) for x in numbers for y in numbers for z in numbers if x < y < z and x + y + z == target]
print(triplets)