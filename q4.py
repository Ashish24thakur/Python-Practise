import numpy as np 
from matplotlib import pyplot as plt 
x=[4,4,4,4,4,4,4]
y=[1,2,3,4,5,6,7]
x2=[1,2,3,4,5,6,7,8,9,10]
y2=[5,5,5,5,5,5,5,5,5,5]
x3=[7,7,7,7,7,7,7]
y3=[1,2,3,4,5,6,7]
x4=[1,2,3,4,5,6,7,8,9,10]
y4=[3,3,3,3,3,3,3,3,3,3]
a1=[2.5,2.5,8.5,5.5]
b1=[6,2,6,4]
a2=[5.5,5.5,8.5,2.5,8.5]
b2=[6,2,2,4,4]
p1=[2.5,4,7,8.5]
q1=[2,3,5,6]
p2=[2.5,2.5,2.5,2.5]
q2=[2,3,5,6]
p3=[2.5,4,6,8,8.5]
q3=[6,6,6,6,6]
#p1=[,,2.5,2.5,4,7,8,8.5]
#q1=[,6.3,1.6,2,3,4,5,6,6,6,6,6,6]
plt.scatter(a1,b1,marker="*",c='g',s=700)
plt.scatter(a2,b2,c='r',s=700)
#qd=['Ist','2nd','3rd','4th']
#vl=[90,90,90,90]
plt.plot(x,y,color='y')
plt.plot(x2,y2,color='y')
plt.plot(x3,y3,color='y')
plt.plot(x4,y4,color='y')
ang1=[3.3,3.3,2.5,3.3]
ang2=[6,5.4,5.4,5.4]
plt.plot(p1,q1,color='b')
plt.plot(p2,q2,color='b')
plt.plot(p3,q3,color='b')
plt.plot(ang1,ang2,color='r')
#plt.pie(vl,labels=qd)
print(plt.show())