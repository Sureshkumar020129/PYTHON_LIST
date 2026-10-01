print(" Split a list into two equal halves")
l1=[1,2,3,4,5,6,7,8,9,10]
half = len(l1) // 2
l2 = l1[:half]
l3 = l1[half:]
print("First half:", l2)
print("Second half:", l3)