print(" Move all zeros to the end of a list while maintaining the order of other elements.")
numbers = [0, 1, 0, 3, 12]
numbers = [x for x in numbers if x != 0] + [x for x in numbers if x == 0]
print(numbers)