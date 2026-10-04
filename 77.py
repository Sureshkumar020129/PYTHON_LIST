print(" Find the intersection of three lists. ")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 6, 7, 8, 9]
intersection = [x for x in list1 if x in list2 and x in list3]
print(intersection)