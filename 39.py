print("39. Find the frequency of every element in a list. ")
l1=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]
frequency={}
for element in l1:
    frequency[element] = frequency.get(element, 0) + 1
print(frequency)