#!/usr/bin/python3

from datetime import date
import subprocess
import os
import math
import urllib.request
import PySimpleGUI as sg



tryb = input("Którego trybu chcesz użyć?\n1.Tekstowy\n2.Graficzny ") # Wybieranie trybu pracy programu

def interfejs_graficzny():
    layout = [[sg.Button('Siema, tutaj buła', size=(50,50))]]
    window = sg.Window('GUI SAMPLE', layout, size=(500,500))
    event, values = window.read() 
    return interfejs_graficzny
       
    
        


def interfejs_tekstowy():

    def menu():

        imie = input("Witaj przybyszu, jak się nazywasz?: ")
        data = date.today()
        print("Witaj", imie + ",", "dzisiejsza data:",data) 
        menu_options = {
            1: 'Szansa na królika',
            2: 'Zanieczyszczone buły',
            3: 'Szansa na WS',
            4: 'Losowa ciekawostka',
            5: 'Wyjście'
        }

        for key in menu_options.keys():
            print (key, '--', menu_options[key])
        return menu
        menu()
        
        

      

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

    def ciekawostki():
        ciekawostka = "python3 ciekawostki.py"
        fileDir = os.path.dirname(os.path.realpath(__file__))
        process = subprocess.check_output(ciekawostka.split(), cwd=fileDir)
        print(process.decode('latin-1'))

    if __name__=='__main__':
        while(True):
            menu()
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
                ciekawostki()
            elif option == 5:
                print('Dzięki. Zapraszam ponownie')
                exit()
            else:
                print('Zła opcja. Proszę wybrać numer między 1 a 5.')
    return interfejs_tekstowy

if tryb == "1" or tryb == "Tekstowy" or tryb == "tekstowy":
    interfejs_tekstowy()
elif tryb == "2" or tryb == "Graficzny" or tryb == "graficzny":
    interfejs_graficzny() 
else:
    print("Wybrałeś nieprawidłową opcję") 
    exit




