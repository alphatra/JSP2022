klucz = {"a" : "y", "e" : "i", "i" : "o", "o" : "a", "y" : "e"}
txt = "to jest moj tekst"

print(txt)
def szyfrator(txt):
    txt = txt.translate(str.maketrans(klucz))
    return txt
def deszyfrator(txt):
    kluczd = {y: x for x, y in klucz.items()}
    txt = txt.translate(str.maketrans(kluczd))
    return txt
print(szyfrator(txt))
txt =szyfrator(txt)
print(deszyfrator(txt))