print(" Find elements present in the first list but not the second. ")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
elements_in_first_not_second = [x for x in list1 if x not in list2]
print(elements_in_first_not_second)