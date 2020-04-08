from zadanie11.dzialanie import *
from zadanie11.zwracanie import *
#
liczbaRe=input('podaj czesc rzeczywista :')
liczbaIm=input('podaj czesc zespolona :')
print(zwracanie1(liczbaRe,liczbaIm))
print(zwracanie2(liczbaRe,liczbaIm))
#
print('PIERWSZA LICZBA')
rzeczywista1=input('czesc rzeczywista: ')
rzeczywista1=int(rzeczywista1)
urojona1=input('czesc urojona: ')
urojona1=int(urojona1)
print('DRUGA LICZBA')
rzeczywista2=input('czesc rzeczywista: ')
rzeczywista2=int(rzeczywista2)
urojona2=input('czesc urojona: ')
urojona2=int(urojona2)
dzialanko=input("WYBIERZ DZIALANIE: + lub -")
print(dzialanie(rzeczywista1,urojona1,rzeczywista2,urojona2,dzialanko))