 # Enter your code here. Read input from STDIN. Print output to STDOUT
l1=list(map(int,input().split()))
l3=[]
for i in range(l1[0]):
    l2=[]
    l2=list(map(int,input().split()))
    l3.append(l2)
print(l3)
j=1
sum=0
for i in range(l1[0]):
    if j< len(l3[i]):
        a=l3[i][j]
        print(a)
        print("--------------------------")
        b=a**2 
        print(b)
        print("--------------------------")
        sum=sum+b
        j=j+2
print(sum)
result=sum%l1[1]
print(result)
