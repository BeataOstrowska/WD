#Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.
with open("dane.txt","r") as plik:
    for linia in plik:
        print(linia, end=" dodaje napis \n nowa linia \n kolejna")