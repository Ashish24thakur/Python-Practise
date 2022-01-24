l=[100,200,100,4,"hello",100,4,100]
l1=[]
for i in l:
    if(type(i)!=str):
        l1.append(i)
sum=0
for j in l1:
    if j==-1:
        sum=sum+1
if sum>0:
    print("-1 is present in list for",sum,"times")
for j in l1:
    if j!=-1:
        sum=0
        for i in range(len(l1)):
            if j==l1[i]:
                sum=sum+1
                l[i]=-1
    print(j,"is present in the list",sum,"times")


    