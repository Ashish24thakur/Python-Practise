# Enter your code here. Read input from STDIN. Print output to STDOUT
a=input()
l1=[]
l2=[]
l3=[]
l4=[]
'''r1=""
r2=""
r3=""
r4=""
r=""
'''
for i in range(-1,-(len(a)),-1):
    if (a[i]>='0') and (a[i]<='9'):
        pass 
    else:
        if (a[i]>='A') and (a[i]<='Z'):
            pass 
        else:
            l1.append(a[i]) 
for i in range(len(a)):
    if (a[i]>='A') and (a[i]<='Z'):
        l2.append(a[i])
for i in range(len(a)):
    if (a[i]>='0') and (a[i]<='9'):
        if int(a[i])%2==0:
            pass 
        else:
            l3.append(a[i])
for i in range(len(a)):
    if (a[i]>='0') and (a[i]<='9'):
        if int(a[i])%2==0:
            l4.append(a[i])
        else:
            pass 
l1.sort()
l2.sort()
l3.sort()
l4.sort()
#r=r1+r2+r3+r4
r=""
for i in l1:
    r=r+i 
for i in l2:
    r=r+i 
for i in l3:
    r=r+i 
for i in l4:
    r=r+i
print(r)
    