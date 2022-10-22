napis = input("podaj napis: ")
napis = napis[0]+napis[1:].replace(napis[0], "$")
napis = napis.replace(napis[0], "$",1)
print(napis)