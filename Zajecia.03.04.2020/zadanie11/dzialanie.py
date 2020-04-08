#dodawanie i odejmowanie liczb rzeczywistych
def dzialanie(rzeczywista1,urojona1,rzeczywista2,urojona2,dzialanko):
    if dzialanko=='+':
        wynikRe=rzeczywista1+rzeczywista2
        wynikIm=urojona1+urojona2
    elif dzialanko=='-':
        wynikRe=rzeczywista1-rzeczywista2
        wynikIm=urojona1-urojona2
    else:
        print('Wybrano dzialanie, ktorego nie mam opracowanego.')
    return wynikRe,wynikIm