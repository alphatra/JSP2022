#I = 1
#V = 5
#X = 10
#L = 50
#C = 100
#D = 500
#M = 1 000
txt = input("Wprowadź liczbę uzywajac cyfr rzysmkich").upper()
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
print(groups,sep="\t",end="asd")