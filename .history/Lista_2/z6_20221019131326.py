lista = ["Kasia", "Basia", "Marek", "Darek"]
lista.append("Józek")
lista.extend(["Ania","Basia"])
lista = sorted(lista)
print(lista)
print(lista[4])
print(lista[:2])
print(lista[-2:])
lista.remove("Basia")