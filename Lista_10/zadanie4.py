import urllib.request
import xml.etree.ElementTree as ET

class przelicznikWalut():
    def __init__(self,url):
        self.url = url
        self.document = urllib.request.urlopen(url).read()
        self.tree = ET.fromstring(self.document)
        self.file = []
    def czytaj(self):
        for item in self.tree.findall('pozycja'):
            title = item.findtext('nazwa_waluty')
            kod = item.findtext('kod_waluty')
            przelicznik = item.findtext('przelicznik')
            kurs_sredni = item.findtext('kurs_sredni')
            #
            pozycja = [title, przelicznik, kod, kurs_sredni.replace(',', '.')]
            self.file.append(pozycja)
            #
        for name in self.file:
            print(name[0])
    def przelicznik(self):
        przelicz = int(input("\n wpisz 1 jeśli chcesz przeliczyć na złotówki, 2 jeśli na inną walutę "))
        if przelicz == 1:
            przelicz2 = input("podaj nazwe waluty do przeliczenia na ")
            ile = int(input("Podaj ile tej waluty chce przelicz na złotówki"))
            for poz in self.file:
                if przelicz2 in poz[0]:
                    wynik = ile * float(poz[3])
                    print("Wartość ", poz[1], poz[2],"= ", wynik, "PLN")
        elif przelicz == 2:
            przelicz2 = input("podaj nazwe waluty do przeliczenia ")
            przelicz = input("Podaj na jaką walute chcesz przeliczyć walute wcześniej podaną ")
            ile = int(input("Podaj ile tej waluty chce przelicz na złotówki"))
            for poz in self.file:
                if przelicz2 in poz[0]:
                    wynik = ile * float(poz[3])
                    print("Wartość",poz[1],poz[0],"= ", end="")
            for poz in self.file:
                if przelicz in poz[0]:
                    wynik = wynik/float(poz[3])
                    print(wynik, poz[2])

url = 'https://www.nbp.pl/kursy/xml/a012z210120.xml'
url2 = przelicznikWalut(url)
url2.czytaj()
url2.przelicznik()
