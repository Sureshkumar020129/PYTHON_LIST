print("Find the maximum sum of any two elements in a list.")
numbers = [1, 2, 3, 4, 5]
max_sum = max(x + y for x in numbers for y in numbers if x != y)
print(max_sum)