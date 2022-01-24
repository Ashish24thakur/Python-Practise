import numpy as np 
from matplotlib import pyplot as plt
graph={'Total cases': 24.7,'Total death': 0.27,'Total recovered': 20.8,'Active Case': 3.63}
detail=list(graph.keys())
person=list(graph.values())
print(detail)
print(person)
plt.bar(detail,person)
plt.title("Corona virus update(India till today) ")
plt.xlabel("Details")
plt.ylabel("Number of Persons (IN MILLION)")
print(plt.show())