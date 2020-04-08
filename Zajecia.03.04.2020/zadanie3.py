#słownik na produkty
slownik={"jajka": "sztuki",
        "ziemniaki": "kilogramy",
        "woda": "litry",
        "ksiązka": "sztuki"}
print("Lista produktów i jednostka w jakiej się je kupuje")
print(slownik)
sztuki=[key for key in slownik.keys() if slownik[key]=='sztuki']
print("Lista produktów, które kupujemy na sztuki")
print(sztuki)
