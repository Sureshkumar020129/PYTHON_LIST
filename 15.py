print(" Count positive, negative, and zero values. ")
l1=[1,2,3,4,5,6,7,8,9,10]
positive=0
negative=0
zero=0
for i in l1:
    if i>0:
        positive+=1
    elif i<0:
        negative+=1
    else:
        zero+=1
print("Positive values:", positive)
print("Negative values:", negative)
print("Zero values:", zero)