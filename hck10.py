# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l1=[]
for i in range(n+1):
    l=[]
    l=list(input().split())
    l1.append(l)
a=1
for i in range(len(l[1][0])):
    if l1[0][i]=='MARKS':
        a=i 
sum=0
for j in range(1,len(l1)):
    sum=sum+ float(l1[j][a])
avg=sum/n
#print(avg)
print('%.2f'%avg)
    
        