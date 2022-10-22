napis = input("podaj napis")
pierw_litera = napis[0]
nowy_napis = [i for i in napis if i==pierw_litera]
napis = "".join(nowy_napis)
print(nowy_napis)