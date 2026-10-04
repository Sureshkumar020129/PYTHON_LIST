print("Move all negative numbers to the beginning of a list. ")
numbers = [-1, 2, -3, 4, -5]
numbers = [x for x in numbers if x < 0] + [x for x in numbers if x >= 0]
print(numbers)