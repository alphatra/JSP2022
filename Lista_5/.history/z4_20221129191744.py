klucz = {"a" : "y", "e" : "i", "i" : "o", "o" : "a", "y" : "e"}
txt = "to jest moj tekst"

f=filter(txt,txt.split())
s1="".join(f)
print(s1)