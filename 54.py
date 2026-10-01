print(" Rotate a list left by 2 positions using slicing.")
l1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rotated= l1[2:] + l1[:2]
print("Original list:", l1)
print("Rotated list:", rotated)