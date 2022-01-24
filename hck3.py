n=int(input())
print("0")
print("1")
a=0
b=1
for i in range(3,n+1):
    c=a+b 
    print(c)
    a=b 
    b=c
    