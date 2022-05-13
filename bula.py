import math
a = float(input("Wprowadz szanse na krolika: "))
b = float(math.sqrt(10))
c = a * b
d = c
if d > 100:
    d = 100
f = round(d,2)

opakowanie = ["bula1", "bula2", "bula3", "bula4", "bula6", "bula5"]
for i in range (len(opakowanie)):
    if i % 3 == 0:
        print("Matt Wood zrzucił grzyba na bułę")
    else:
        print("Buła jest czysta")

T = "" #okres polowicznego rozpadu szympansa NIE DZIALA#
Szansa_na_WS = float((d - a) * b)
if Szansa_na_WS < 1:
    print("Szansa na wiadomo co wiadomo co nie może zostać oszacowana")
else:
    print("Szansza na wiadomo co wiadomo co wynosi:",Szansa_na_WS, end="%\n")
    

print("Szanse na krolika wynosza: ", a,"%","natomiast szansa na kota przy grzałce wynosi",d,"%")




