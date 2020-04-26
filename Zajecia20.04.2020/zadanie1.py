class Material():
    def __init__(self,nazwa,rodzaj,dzlugosc,szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
        self.nazwa=nazwa
    def wyswietl_nazwe(self):
        return print(self.nazwa)
class Ubrania(Material):
    def __init__(self,rodzaj,dlugosc,szerokosc,nazwa,rozmiar,kolor,dla_kogo):
        self.rodzaj=rodzaj 
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
        self.nazwa=nazwa
        self.rozmiar=rozmiar
        self.kolor=kolor
        self.dla_kogo=dla_kogo
    def wyswietl_dane(self):
        return print(self.rodzaj,self.dlugosc,self.szerokosc,self.nazwa,self.rozmiar,self.kolor,self.dla_kogo)
class Sweter(Ubrania):
    def wys_dane(self):
        return print(self.rodzaj)
sweter_rozpinany=Sweter("sweter_rozpinany","bawelniany",30,40,"czarny","kobieta","L")
sweter_rozpinany.wyswietl_nazwe()
sweter_rozpinany.wyswietl_dane()
sweter_rozpinany.wys_dane()