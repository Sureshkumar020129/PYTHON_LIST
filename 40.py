print("40. Compare two lists and check whether they contain the same elements. ")
l1=[1,2,3,4,5]      
l2=[5,4,3,2,1]
if sorted(l1) == sorted(l2):
    print("The lists contain the same elements.")
else:
    print("The lists do not contain the same elements.")
    