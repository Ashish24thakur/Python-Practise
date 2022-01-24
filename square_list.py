l=[4,3.4,"hello",9]
l1=[]
l3=[]
for i in l:
    if(type(i)!=str):
        l1.append(i)
for j in l1:
    sqr=1
    sqr=j**2
    l3.append(sqr)
print(l3)
    