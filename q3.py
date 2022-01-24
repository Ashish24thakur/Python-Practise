import numpy as np 
from matplotlib import pyplot as plt 
x=np.arange(2,11)
y=x
y2=[2,2,2,2,2]
x2=[2,4,6,8,10]
x3=[10,10,10,10,10,10,10,10,10]
y3=[2,3,4,5,6,7,8,9,10]
x4=[2]
y4=[2]
plt.plot(x,y,linewidth=4)
plt.plot(x2,y2,linewidth=4)
plt.plot(x3,y3,linewidth=4)
plt.title("Triangle in frst quadrant of X-Y axis ")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.scatter(x4,y4,color='g')
print(plt.show())