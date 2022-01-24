l=[100,200,100,4,"hello",100,4,100]
l1=[]
for i in l:
    if i in l1:
        pass 
    else:
        l1.append(i)
for j in l1:
    k=l.count(j)
    print(j,"is present",k,"times in the list")