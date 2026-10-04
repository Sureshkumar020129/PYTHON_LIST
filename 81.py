print("Find the first repeating element in a list. ")
numbers = [1, 2, 3, 4, 5, 2, 6, 7, 8]
for n in numbers:
    if numbers.count(n) > 1:
        print(n)
        break
else:
    print("No repeating element found.")