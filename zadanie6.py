import numpy as np
import math
macierz=np.array([1,6,4,5,3,2]) .reshape(2,3)
b=np.zeros((2,3))
print(b)
print(macierz)
for i in range(2):
    for j in range(3):
        b[i,j]=b[i,j]+math.cos(macierz[i,j])
print(b)