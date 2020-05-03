import numpy as np
macierz=np.arange(25)
macierz[0]=1
macierz[1]=1
for i in range(2,25):
    macierz[i]=macierz[i-1]+macierz[i-2] 
macierz=macierz.reshape((5,5))
print(macierz)