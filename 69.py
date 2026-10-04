print(" Extract vowels from a given string using list comprehension. ")
string = "Hello, World!"
vowels = [char for char in string if char in "aeiouAEIOU"]
print(vowels)