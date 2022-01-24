n=int(input())
for i in range(n):
    li=list(map(int,input().split()))
for i in range(n):
    print(li)
for i in range(n):
    if li[0]>li[1]:
        print(">")
    elif li[0]<li[1]:
        print("<")
    elif li[0]==li[1]:
        print("=")