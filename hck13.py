# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=list(map(int,input().split()))
sum=0
for i in l:
    if i>0:
        pass 
    else:
        sum=sum+1 
if sum==0:
    sum2=0
    for i in range(len(l)):
        a=l[i]
        b=l[i]
        sum=0
        #print(a)
        #print(b)
        #print("----------------")
        while a>0:
            rem=a%10 
            #print(rem)
            #print("*******************")
            sum=sum*10 + rem 
            a=a//10
        #print(sum)
        #print("------------------") 
        if sum==b:
            sum2=sum2+1 
    if sum2>0:
        print("True")
    else:
        print("False")
else:
    print("False")
        
            
        