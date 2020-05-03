import numpy as np
a=input("Podaj liczbe: ")
a=int(a)
b=input("Podaj ilosc wyswietlen: ")
b=int(b)
def generuj(a,b):
    y=np.logspace(a-1,b,num=b,base=a,dtype='int64')
    return y
n=generuj(a,b)
print(n)