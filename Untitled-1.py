print("Hello world!")
def main():
    print("Hello world!")
# Ctrl+/ - ustaw komentarz/usuń komentarz
# Shift+Alt+strzałka(góra/dół)- powiela linie
# """-służy do ciągów wieloliniowych/ciąg znakomy do dokumentacji metody/funkcji
# 
# łańcuch znaków
imie="Ala"
imie='Ala'
imie="""Ala ma
kota a
kot jest głodny"""
print(type(imie))
print(type(5))
print(type(5.6))
print(type(True))
print(type(None))
# isinstance() sprawdzam czy zmienna jest danego typu
print("Ala "+"ma kota.")
print("Ala "+"ma "+str(5)+" kotów.")
# print("Ala "+"ma "+ 5 +" kotów.")błąd
ilosc_kotow = 5
print("Ala "+"ma {} kotów.".format(ilosc_kotow))
print("Ala "+"ma {1} {0} {2} kotów.".format(4, 5, 7))
liczba=6.87759
print(f"Liczba {liczba:.2f}") #2 miejsca dziesiętne
# http://pyformat.info

print(imie[1])
