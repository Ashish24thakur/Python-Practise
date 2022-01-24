s=input()
l=[]
for i in range(len(s)):
    r=""
    for j in range(i+1,len(s)):
        r=r+s[i]
        if s[i]!=s[j]:
            #sum=sum+1 
            r=r+s[j]
            l.append(r)
        else:
            pass
            break
print(l)
        