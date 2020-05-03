import numpy as np
def macierz(n):
    mac=np.zeros((n,n))
    for i in range(n):
       mac=mac+np.diag(np.linspace(2*(i+1),2*(i+1),n-i),i)
       if(i!=0):
           mac=mac+np.diag(np.linspace(2*(i+1),2*(i+1),n-i),-i)
    return mac

n=input("Podaj wartosc liczby n: ")
n=int(n)
print(macierz(n))