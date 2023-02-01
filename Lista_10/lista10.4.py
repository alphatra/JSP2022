from urllib.request import urlopen, Request
from itertools import combinations
from xml.etree.ElementTree import parse, fromstring

class Kantor():
    tab_kurs = []

    def __init__(self, link):
        self.url = urlopen(Request(link)).read()
        self.xml = fromstring(self.url)

    def dost_kursy(self):
        for item in self.xml.findall('pozycja'):
            waluta = [item.findtext('nazwa_waluty'), item.findtext('przelicznik'), item.findtext('kurs_sredni').replace(",", ".")]
            self.tab_kurs.append(waluta)
        print("Waluta\tKod waluty\tKurs sredni")
        for i in self.tab_kurs:
            print(i[0], "\t", i[1], "\t", i[2])

    def przelicz_pl(self, waluta, val, tryb):
        for i in self.tab_kurs:
            if waluta in i:
                if tryb == "napl":
                    wart = float(i[2])*val
                    print("Przelicz: ", val, waluta, " => ", round(wart, 2), "zlotych")
                elif tryb == "zpl":
                    wart = val/float(i[2])
                    print("Przelicz: ", val, "zlotych => ", round(wart, 2), waluta)

    def przelicz(self, waluta, waluta2, val):
        wartF, wartS = 0, 0
        for i in self.tab_kurs:
            if waluta in i:
                wartF = val*float(i[2])
            if waluta2 in i:
                wartS = float(i[2])
        print("Przelicz: ", val, waluta, " => ", round(wartF/wartS, 2), waluta2)


kant = Kantor("https://www.nbp.pl/kursy/xml/a012z210120.xml")
kant.dost_kursy()
print()
kant.przelicz_pl('euro', 50, "zpl")
kant.przelicz_pl('euro', 1, "napl")
kant.przelicz("euro", "dolar australijski", 50)
