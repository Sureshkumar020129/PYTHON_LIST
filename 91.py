print(" Separate even and odd numbers while maintaining their original order. ")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 != 0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)