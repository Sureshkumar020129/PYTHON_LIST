print("Rotate a list right by 3 positions using slicing. ")
l1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rotated= l1[-3:] + l1[:-3]
print("Original list:", l1)
print("Rotated list:", rotated)