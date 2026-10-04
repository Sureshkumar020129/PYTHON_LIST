print(" Find the element that occurs most frequently")
numbers = [1, 2, 2, 3, 3, 3, 4, 5]
element = max(set(numbers), key=numbers.count)
print(element)