#Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.
liczby=[x for x in range(0,10000) if x%4==0]
plik = open("zadanie1P.txt","w+")
plik.write(str(liczby))
plik.close()
print(liczby)



    
