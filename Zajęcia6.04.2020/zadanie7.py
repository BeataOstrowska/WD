#Stwórz klasę Robaczek, która będzie sterować ruchami Robaczka. Klasa powinna przechowywać współrzędne x, y, krok (stała wartość kroku dla Robaczka), i powinna mieć następujące metody:
#konstruktor – który nadaje wartość dla x, y i krok
#idz_w_gore(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
#idz_w_dol(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
#idz_w_lewo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
#idz_w_prawo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
#pokaz_gdzie_jestes() – metoda, która wyświetla aktualne współrzędne Robaczka
#Stwórz instancję klasy i sprawdź jak działają wszystkie metody
class Robaczek:
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def idz_w_gore(self,ile_krokow):
        wynik=ile_krokow * self.krok
        self.y=self.y+wynik
        return self.y
    def idz_w_dol(self,ile_krokow):
        wynik=ile_krokow * self.krok
        self.y=self.y-wynik
        return self.y
    def idz_w_lewo(self,ile_krokow):
        wynik=ile_krokow * self.krok
        self.x=self.x-wynik
        return self.x
    def idz_w_prawo(self,ile_krokow):
        wynik=ile_krokow * self.krok
        self.x=self.x + wynik
        return self.x
    def pokaz_gdzie_jestes(self):
        print("twoje wspolrzedne to :") 
        print(self.x)
        print(self.y)
robak=Robaczek(8,1,9)
robak.idz_w_gore(2)
robak.idz_w_dol(4)
robak.idz_w_lewo(3)
robak.idz_w_prawo(6)
robak.pokaz_gdzie_jestes()   