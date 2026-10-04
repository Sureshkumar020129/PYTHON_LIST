print("Replace negative numbers with 0. ")
numbers = [1, -2, 3, -4, 5]
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0
print(numbers)