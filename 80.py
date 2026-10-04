print("Find the first non-repeating element in a list. ")
numbers = [1, 2, 2, 3, 3, 4, 5]
for n in numbers:
    if numbers.count(n) == 1:
        print(n)
        break
else:
    print("No non-repeating element found.")