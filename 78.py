print("Find the union of two lists without using set(). ")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
union = list1 + [x for x in list2 if x not in list1]
print(union)