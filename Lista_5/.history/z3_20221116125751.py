txt = input("Wprowadź liczbę uzywajac cyfr rzysmkich")
"".join(txt.upper())
for x in txt:
    tmp=x
    groups = []
    print(f"{x} wystepuje: {txt.count(x)}")
    if x == tmp:
        groups.append(x)
    else:
        groups+=" "