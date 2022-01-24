n=list(map(eval,input().split(',')))
n2=[]
for i in n:
    if i not in n2:
        n2.append(i) 
print(n2)
print(n)
print("-------------------------------")
for i in n2:
    s=0
    for j in n:
        if i==j:
            s=s+1
    if s%2!=0:
        r='"'+i+'"'
        print(r)
        break 
        

#l=list(map(eval,input().split()))
#print(l)