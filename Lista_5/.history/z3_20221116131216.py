txt = input("Wprowadź liczbę uzywajac cyfr rzysmkich")
groups = []
tmp=txt[0]
for x in range(len(txt)):
    print(f"{txt[x]} wystepuje: {txt.count(txt[x])}")
    N=[]
    if txt[x] != tmp:
        groups+=txt[0:x]
        tmp = txt[x]
        groups+=" "
        groups.extend(txt[x])
print(groups)