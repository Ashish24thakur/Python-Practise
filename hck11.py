l=list(map(int,input().split()))
if (l[0]>=1 and l[0]<=7) and (l[1]>=1 and l[1]<=1000):
    l1=[]
    g=0
    h=0
    sum=0
    for i in range(l[0]):
        l2=[]
        l2=list(map(int,input().split()))
        l1.append(l2)
    for i in range(len(l1)):
        if (len(l1[i])>=1 and len(l1[i])<=7):
            f=0 
        else:
            g=1 
    if f==0 and g==0:
        for i in range(len(l1)):
            for j in range(len(l1[i])):
                if (l1[i][j]>=1 and l1[i][j]<=1000000000):
                    m=0 
                else:
                    h=h+1 
    if m==0 and h==0:
        for i in range(len(l1)):
            max=l1[i][0]
            for j in range(len(l1[i])):
                if l1[i][j]>max:
                    max=l1[i][j]
                else:
                    max=max 
            sum=sum + max**2
        result=sum%l[1]
        print(result)
