#I = 1
#V = 5
#X = 10
#L = 50
#C = 100
#D = 500
#M = 1 000
txt = input("Wprowadź liczbę uzywajac cyfr rzysmkich").upper()
roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
def romanToInt(txt):
    while i < len(txt):
        if i+1<len(txt) and txt[i:i+2] in roman:
            num+=roman[txt[i:i+2]]
            i+=2
        else:
            #print(i)
            num+=roman[txt[i]]
            i+=1
    print(f"{num}")
romanToInt("III")