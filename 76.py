print("Merge two lists and remove duplicates. ")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
merged_list = list1 + list2
unique_merged_list = []
for n in merged_list:
    if n not in unique_merged_list:
        unique_merged_list.append(n)
print(unique_merged_list)