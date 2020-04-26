class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "Kształty ogólne"
class kwadrat(Ksztalty):
    def __init__(self,x):
        self.x=x
        self.y=x
    def __str__(self):
        return "kwadrat o boku {}".format(self.x)
    #obsulugje operator <
    def __lt__(self,other):
        return other.x
    #obsulugje operator >=
    def __ge__(self,other):
        return self.x
    #obsluguje operator  >
    def __gt__(self,other):
        return self.x
    #obsulugje operator <=
    def __le__(self,other):
        return self.x

kw1=kwadrat(10)
kw2=kwadrat(17)
print(kw1)
print(kw2)
print(kw1<kw2)
print(kw1>kw2)
print(kw1>=kw2)
print(kw1<=kw2)