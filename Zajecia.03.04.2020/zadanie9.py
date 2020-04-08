#symbol * oznacza dowolną ilość argumentów przechowywanych w krotce 
 
def ciag(* liczby):     
    #jeżeli nie ma argumentów to     
    if len(liczby) == 0:
        return 0.0     
    else:
        iloczyn = 1.0 
        #mnożymy elementy ciągu
        for i in liczby:
            iloczyn *= i
        #zwracamy wartość iloczynu
        return iloczyn 
#wywołanie gdy brak argumentów 
print(ciag()) 
#podajemy argumenty 
print(ciag(1,2,3,4,5,6,7,8))