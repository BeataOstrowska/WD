#Do klasy z wybranego poprzedniego zadania dołącz funkcję niszczenia obiektu
#skorzystam z zadania 4
class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
    def wyswietl(self):
        print(f"{self.nazwa_produktu}")
        print(f"ilosc: {self.ilosc}")
        print(f"jednostka miary: {self.jednostka_miary}")
        print(f"cena: {self.cena_jed} zlote")
    def ile_produktu(self):
        self.ilosc=str(self.ilosc)
        return print(f"ilosc: {self.ilosc} {self.jednostka_miary} ")
    def ile_kosztuje(self):
        self.ilosc=int(self.ilosc)
        self.koszt=self.ilosc*self.cena_jed
        return print(f"kosztuje: {self.koszt} zlote")
    def __del__(self):
           print ('del!')
marchew=NaZakupy("marchew",3,"kilogramy",3)
sok=NaZakupy("sok",6,"sztuki",2)
#
marchew.wyswietl()
marchew.ile_produktu()
marchew.ile_kosztuje()
#
sok.wyswietl()
sok.ile_produktu()
sok.ile_kosztuje()