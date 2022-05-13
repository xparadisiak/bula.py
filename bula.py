import math
imie = input("Witaj przybyszu, jak się nazywasz?: ")
a = float(input("Wprowadz szanse na krolika: "))
b = float(math.sqrt(10))
c = a * b
d = c
''' do udoskonalenia
def menu(dzialanie): 
    dzialanie = ""
    operacja = input("Witaj",imie, "Jaką operację chciałbyś wykonać?\n1.Obliczenie szansy na królika\n2.Zidentyfikowanie zanieczyszczonych buł\n3.Określenie szansy na WS")
    if operacja == "1":
        operacja = szansa_na_krolika
    elif operacja == "2":
        operacja = "zanieczyszczone_buly"
    elif operacja == "3":
        operacja = "Szansa_na_WS"   
    dzialanie = operacja + "()"
    return dzialanie
 
menu(dzialanie)   '''                    

def szansa_na_krolika():
    if d > 100:
        d = 100
    f = round(d,2)


def zanieczyszczone_buly():
    opakowanie = ["bula1", "bula2", "bula3", "bula4", "bula5", "bula6"]
    for i in range (len(opakowanie)):
        if i % 3 == 0:
            print("Matt Wood zrzucił grzyba na bułę")
        else:
            print("Buła jest czysta")
    return opakowanie
zanieczyszczone_buly()


def szansa_na_WS():
    T = "" #okres polowicznego rozpadu szympansa NIE DZIALA
    Szansa_na_WS = float((d - a) * b)
    if Szansa_na_WS < 1:
        print("Szansa na wiadomo co wiadomo co nie może zostać oszacowana")
    else:
        print("Szansza na wiadomo co wiadomo co wynosi:",Szansa_na_WS, end="%\n")
    return szansa_na_WS
szansa_na_WS()        
    

print("Szanse na krolika wynosza: ", a,"%","natomiast szansa na kota przy grzałce wynosi",d,"%")
