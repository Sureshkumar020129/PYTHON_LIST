print("Find the element that occurs least frequently. ")
numbers = [1, 2, 2, 3, 3, 3, 4, 5]
element = min(set(numbers), key=numbers.count)
print(element)