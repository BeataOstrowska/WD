import numpy as np
def wektor(n):
    w=np.linspace(n,1,n)
    mat_diag = np.diag(w)
    return mat_diag
n=input("Podaj liczbe: ")
n=int(n)
print(wektor(n))
