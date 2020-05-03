import numpy as np
def funkcja(n):
    b = np.arange(n*n).reshape((n,n))
    return b
n=input("Podaj liczbe: ")
n=int(n)
print(funkcja(n))