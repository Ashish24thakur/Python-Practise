l=[100,"hello",3.4,"bye"]
sum=0
for i in l:
    #if(type(i)==int or type(i)==float):
    if(type(i)!=str):
        sum=sum+i
print(sum)