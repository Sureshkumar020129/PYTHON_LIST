print("Remove duplicate elements from a list without using set(). ")
numbers = [1, 2, 2, 3, 3, 4, 5]
unique_numbers = []
for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)
print(unique_numbers)