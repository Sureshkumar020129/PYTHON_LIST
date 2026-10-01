print(" Copy one list into another list without using copy().")
l1=[1,2,3,4,5,6,7,8,9,10]
l2=[]
for i in l1:
    l2.append(i)
print("Original list:", l1)
print("Copied list:", l2)