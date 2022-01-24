l=list(map(eval,input().split()))
if l[0]%5==0:
    if l[0]<l[1]:
        s = l[1]-l[0]
        s1 = s-0.50
        print('%.2f'%s1)
    else:
        print(l[1])
else:
    print(l[1])