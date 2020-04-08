import random
macierz=[[random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]for i in range(4)]
print(macierz)
lista=[macierz[i][i] for i in[0,1,2,3]]
print(lista)