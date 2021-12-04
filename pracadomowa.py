liczbaA = 0
liczbaB = 0
operacja = ''

def dodaj(x, y):
    return x + y

def odejmij(x, y):
    return x - y

def pomnoz(x, y):
    return x * y

def podziel(x, y):
    return x / y


operacja = input("Podaj dzialanie: (* / + -)")  # potrzebujemy string
liczbaA = int(input("Podaj liczbe A: "))
liczbaB = int(input("Podaj liczbe B: "))



def czyLiczbaParzysta(liczbaX)
    return liczbaX % 2




# sprawdzamy
def wykonajDzialanie(operacja):
    if operacja == '*':   # czy jest to samo?
        return pomnoz(liczbaA, liczbaB)

    if operacja == '/':  # czy jest to samo?
        return podziel(liczbaA, liczbaB)

    if operacja == '+':  # czy jest to samo?
        return dodaj(liczbaA, liczbaB)

    if operacja == '-':  # czy jest to samo?
        return odejmij(liczbaA, liczbaB)



#pobierzDane()
wynikDzialania = wykonajDzialanie(operacja)
print(wynikDzialania)
