litera = input("podaj literę do sprawdzenia: ")
samo = list(['a','e','i','o','u','y','ą','ę'])
spol = list(['b','c','ć','d','f','g','h','j','k','l','ł','m','n','ń','p','t','w','x','z','ź','ż'])
def sprawdz_liter(letter):
    return "podana litera to samogłoska" if letter in samo else "podana litera to spółgłoska" if letter in spol else "podana wartość jest błędna"
print(sprawdz_liter(litera))