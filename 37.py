print("37. Replace all occurrences of one value with another. ")
l1=[1,2,3,4,5,6,7,8,9,10]
old_value=5
new_value=50
l1=[new_value if x==old_value else x for x in l1]
print(l1)