txt = input("Wprowadź liczbę uzywajac cyfr rzysmkich")
"".join(txt.upper())
groups = []
for x in txt:
    tmp=x
    print(f"{x} wystepuje: {txt.count(x)}")
    if x == tmp:
        groups.append(x)
    else:
        groups+=" "
print(groups)