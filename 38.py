print("38. Insert an element after every occurrence of a particular value. ")
l1=[1,2,3,4,5,6,7,8,9,10]
value_to_insert=99
value_to_find=5
l1=[x if x!=value_to_find else [x, value_to_insert] for x in l1]
l1=[item for sublist in l1 for item in (sublist if isinstance(sublist, list) else [sublist])]
print(l1)