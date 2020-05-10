import numpy as np
import math
macierz1=np.array([6,1,5,2,4,3]) .reshape(2,3)
a=np.zeros((2,3))
print(a)
print(macierz1)
for i in range(2):
    for j in range(3):
        a[i,j]=a[i,j]+math.sin(macierz1[i,j])
print(a)
macierz2=np.array([1,6,4,5,3,2]) .reshape(2,3)
b=np.zeros((2,3))
print(b)
print(macierz2)
for i in range(2):
    for j in range(3):
        b[i,j]=b[i,j]+math.cos(macierz2[i,j])
print(b)
print("a+b = ")
print(np.add(a,b))