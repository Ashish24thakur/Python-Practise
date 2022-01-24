n=int(input())
l=list(map(int,input().split()))
s=set()
s=set(l) 
print(s)
for i in s:
    sum=0
    for j in range(len(l)):
        if i==l[j]:
            sum=sum+1 
        else:
            pass 
    if sum<n:
        print(i)
        break 
    else:
        pass