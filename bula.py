import math
imie = input("Witaj przybyszu, jak się nazywasz?: ")
print("Witaj", imie) 
menu_options = {
    1: 'Szansa na królika',
    2: 'Zanieczyszczone buły',
    3: 'Szansa na WS',
    4: 'Wyjście',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def szansa_na_krolika():
    a = float(input("Wprowadz szanse na krolika: "))
    b = float(math.sqrt(10))
    c = a * b
    d = c
    if d > 100:
        d = 100
    f = round(d,2)
    print("Szanse na krolika wynosza: ", a,"%","natomiast szansa na kota przy grzałce wynosi",d,"%")
    return szansa_na_krolika
    szansa_na_krolika()
    

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
    a = float(input("Wprowadz szanse na krolika: "))
    b = float(math.sqrt(10))
    c = a * b
    d = c
    if d > 100:
        d = 100
    f = round(d,2)
    Szansa_na_WS = float((d - a) * b)
    if Szansa_na_WS < 1:
        print("Szansa na wiadomo co wiadomo co nie może zostać oszacowana")
    else:
        print("Szansza na wiadomo co wiadomo co wynosi:",Szansa_na_WS, end="%\n")
    return szansa_na_WS
    szansa_na_WS()

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Wybierz działanie: '))
        except:
            print('Złe dane. Proszę wprowadzić numer ...')
        if option == 1:
            szansa_na_krolika()
        elif option == 2:
            zanieczyszczone_buly()
        elif option == 3:
            szansa_na_WS()
        elif option == 4:
            print('Dzięki. Zapraszam ponownie')
            exit()
        else:
            print('Zła opcja. Proszę wybrać numer między 1 a 4.')
