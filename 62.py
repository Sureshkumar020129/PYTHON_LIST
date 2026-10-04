print("Convert a list of strings to uppercase. ")
strings = ["hello", "world", "python"]
uppercase_strings = [s.upper() for s in strings]
print(uppercase_strings)
for i in range(len(uppercase_strings)):
    print(uppercase_strings[i], end=' ')