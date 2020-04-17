#Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli.
plik = open("zadanie1P.txt","r")
znaki=plik.read()
plik.close()
print(znaki)