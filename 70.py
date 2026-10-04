print("Create a list of numbers whose square is greater than 100.")
numbers = [5, 10, 15, 20]
squared_numbers = [n**2 for n in numbers if n**2 > 100]
print(squared_numbers)