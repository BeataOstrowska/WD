import numpy as np
def podziel(tablica,kierunek):
    x,y=tablica.shape
    mat=tablica
    if(kierunek in (4,6)):
        if(y%2!=0):
            return("Ilosc kolumn nie pozwala na operacje")
        else:
            if(kierunek==6):
                mat=tablica[:,int(y/2):]
            else:
                mat=tablica[:,:int(y/2)]

    else:
        if(x%2!=0):
            return("Ilosc wierszy nie pozwala na operacje")
        else:
            if(kierunek==2):
                mat=tablica[int(x/2):]
            else:
                mat=tablica[:int(x/2)]

    return mat
def kierunek():
    n=input("Wybierz jak podzielic:\n8-gora,\n2-dol,\n4-lewo,\n6-prawo\n")
    print(n)
    if(int(n) in (2,4,6,8)):
        return int(n)
    else:
        print("Zly wybor. ")
        kierunek()

x=input("Podaj wysokosc: ")
x=int(x)
y=input("Podaj szerokosc: ")
y=int(y)
tab=np.arange((x*y))
tab=tab.reshape((x,y))
print(tab)
n=kierunek()
print(podziel(tab,n))