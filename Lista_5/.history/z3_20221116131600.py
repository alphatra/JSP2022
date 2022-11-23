txt = input("Wprowadź liczbę uzywajac cyfr rzysmkich")
NE=""
groups = []
tmp=txt[0]
for x in range(len(txt)):
    print(f"{txt[x]} wystepuje: {txt.count(txt[x])}")
    if txt[x] == tmp:
        groups.extend(txt[x])
    else:
        tmp = txt[x]
        groups+=" "
        groups.extend(txt[x])
groups.split()
print(groups)