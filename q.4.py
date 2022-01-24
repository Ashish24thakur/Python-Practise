#l1=[100,500,600,3]
#l2=[100,4,600]
#o/p=[500,3] ,l1-l2
l1=[100,500,600,3]
l2=[100,4,600]
l3=[]
for i in range(len(l1)):
    f=0
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            f=f+1
    if f==0:
        l3.append(l1[i])
print(l3)