def geo1(a,q,n):
    An=a*q**(n-1)
    return An
def geo2(a,q,n):
    if q == 1:
        Sm=a*n
    else:
        Sm=a*1-q**n/1-q