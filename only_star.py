import numpy as np 
from matplotlib import pyplot as plt 
a1=[2.5,4,6,8,8.5]
b1=[4,4,4,4,4]
a12=[8.5,7,5.5,4]
b12=[4,3,2,1]
a13=[4,4.3,4.6,4.9,5.2,5.5]
b13=[1,2,3,4,5,6]
a14=[5.5,5.7,5.9,6.1,6.3,6.5,6.7,6.9,7.1,7.3,7.5]
b14=[6,5.5,5,4.5,4,3.5,3,2.5,2,1.5,1]
a15=[7.5,7,6.5,6,5.5,5,4.5,4,3.5,3,2.5]
b15=[1,1.3,1.6,1.9,2.2,2.5,2.8,3.1,3.4,3.7,4]
a16=[3,3.5,4,4.1,4.5,4.8,5,5.3,5.2,5.6,6.7,7.1,7.6,4.3,4.6,4.9,5.2,5.9,6.2,6.5,7.3,7.6,7.9,8.2,4.5]
b16=[4,4,4,1.5,2.5,3.5,4.5,5.5,4,4,4,4,4,1.2,1.4,1.6,1.8,2.3,2.5,2.7,3.2,3.4,3.6,3.8,4]
plt.scatter(a1,b1,marker="*",c='b',s=200)
plt.scatter(a12,b12,marker="*",c='b',s=200)
plt.scatter(a13,b13,marker="*",c='b',s=200)
plt.scatter(a14,b14,marker="*",c='b',s=200)
plt.scatter(a15,b15,marker="*",c='b',s=200)
plt.scatter(a16,b16,marker="*",c='b',s=200)
print(plt.show())