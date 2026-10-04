print("Find the minimum sum of any two elements. ")
numbers = [1, 2, 3, 4, 5]
min_sum = min(x + y for x in numbers for y in numbers if x != y)
print(min_sum)