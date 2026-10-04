print("Extract words having more than 5 characters.")
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = [word for word in words if len(word) > 5]
print(long_words)