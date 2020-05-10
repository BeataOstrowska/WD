import numpy as np
import math
macierz=np.array([6,1,5,2,4,3]) .reshape(2,3)
a=np.zeros((2,3))
print(a)
print(macierz)
for i in range(2):
    for j in range(3):
        a[i,j]=a[i,j]+math.sin(macierz[i,j])
print(a)