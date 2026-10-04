print("Find the longest consecutive sequence of integers.")
numbers = [1, 2, 3, 10, 11, 12, 13, 20, 21]
numbers.sort()
longest_sequence = []
current_sequence = [numbers[0]]

for i in range(1, len(numbers)):
    if numbers[i] == numbers[i-1] + 1:
        current_sequence.append(numbers[i])
    else:
        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence
        current_sequence = [numbers[i]]

if len(current_sequence) > len(longest_sequence):
    longest_sequence = current_sequence

print("Longest consecutive sequence:", longest_sequence)