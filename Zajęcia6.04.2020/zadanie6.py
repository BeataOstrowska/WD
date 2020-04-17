#Utwórz klasę Slowa, która będzie zarządzać różnymi grami słownymi. Klasa powinna przechowywać przynajmniej dwa słowa i metody:
#sprawdz_czy_palindrom – metoda sprawdza czy dany wyraz jest palindromem (czytany od początku czy wspak jest taki sam np. kajak)
#sprawdz_czy_metagramy – metoda sprawdza czy wyrazy różnią się jedną litera a poza tym są takie same np. mata, tata
#sprawdz_czy_anagramy – metoda sprawdza czy wyrazy maja ten sam zestaw liter. Np. mata i tama
#wyświetl_wyrazy – wyświetla podane wyrazy
#Stwórz instancję klasy i sprawdź działanie wszystkich metod.
class slowa:
    def __init__(self,x,y):
        self.wyraz1=x
        self.wyraz2=y
    def sprawdz_czy_palindrom(self):
        if (len(self.wyraz1)%2==0):
            for i in range(0,int(len(self.wyraz1)/2-1)):
                if(self.wyraz1[i]!=self.wyraz1[len(self.wyraz1)-i-1]):
                    return print('Wyraz nie jest palindromem')
        else:
             for i in range(0,int((len(self.wyraz1)-1)/2)):
                    if(self.wyraz1[i]!=self.wyraz1[len(self.wyraz1)-i-1]):
                        return print('Wyraz nie jest palindromem')
        return print("Wyraz1 jest palindromem.")
    def sprawdz_czy_metagramy(self):
        if(len(self.wyraz1)!=len(self.wyraz2)):
            return print("Wyrazy nie sa metagramami")
        else:
            count=0
            for i in range(0,len(self.wyraz1)-1):
                if (self.wyraz1[i]!=self.wyraz2[i]):
                    count+=1
                    if (count>1):
                        return print ("Wyrazy nie sa metagramami")
            if(count!=1):
                return print("Wyrazy nie sa metagramami")
        
        return print("Wyrazy są metagramami")
    def sprawdz_czy_anagramy(self):
        if(len(self.wyraz1)!=len(self.wyraz2)):
            return print("Wyrazy nie sa anagramami")
        else:
            for i in range(0,len(self.wyraz1)):
                if (self.wyraz1.count(self.wyraz1[i])!=self.wyraz2.count(self.wyraz1[i])):
                    return print("Wyrazy nie są anagramami")
        return print("Wyrazy są anagramami")
    def wyswietl_wyraz(self):
       print(self.wyraz1 )
       print(self.wyraz2)
    
wyrazy=slowa('mata','tama')
wyrazy.sprawdz_czy_palindrom()
wyrazy.sprawdz_czy_metagramy()
wyrazy.sprawdz_czy_anagramy()
wyrazy.wyswietl_wyraz()