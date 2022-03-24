a=input()
f=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            f=1 
if f==0:
    print(len(a))
else:
    max_s = ""
    s1=""
    for i in range(len(a)):
        s1=a[i]
        for j in range(i+1,len(a)):
            if a[j] not in s1:
                s1 = s1 + a[j] 
            else:
                if len(max_s)<len(s1):
                    max_s = s1
                    s1=""
                elif len(max_s) == len(s1):
                    if max_s>s1:
                        max_s = s1
                    s1=""
            if len(s1)>len(max_s) or (s1<max_s and len(s1) == len(max_s)):
                max_s = s1
    print(max_s,len(max_s))
