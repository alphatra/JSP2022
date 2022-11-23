txt = input("Wprowadź liczbę uzywajac cyfr rzysmkich")
"".join(txt.upper())
groups = []
for x in range(len(txt)):
    tmp=txt[0]
    print(f"{txt[x]} wystepuje: {txt.count(txt[x])}")
    if txt[x] == tmp:
        groups.append(txt[x])
    else:
        groups+=" "
        tmp = txt[x]
print(groups)