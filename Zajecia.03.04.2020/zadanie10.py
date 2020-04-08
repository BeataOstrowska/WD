def lista(** rzeczy):     
    suma=0;
    for cos in rzeczy:         
        if (rzeczy[cos])!=0:
            suma+=rzeczy[cos]
        else:
            suma+=1
    return suma
print(lista(czekolada=2,pizza=1) )