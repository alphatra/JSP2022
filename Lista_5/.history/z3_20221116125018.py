txt = input("Wprowadź liczbę uzywajac cyfr rzysmkich")
"".join(txt.upper())
for x in txt:
    print(f"{x} wystepuje: {txt.count(x)}")