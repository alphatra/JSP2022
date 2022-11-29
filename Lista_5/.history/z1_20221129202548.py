liczby = {"jeden":1,"dwa":2,"trzy":3,"cztery":4,"pięć":5,"sześć":6,"siedem":7,"osiem":8,"dziewięć":9,"dziesięć":10,"jedynaście":11,"dwanaście":12,"trzynaście":13,"czternaście":14,"piętnaście":15,"szesnaście":16,"siedemnaście":17,"osiemnaście":18,"dziewiętnaście":19,"dwadzieścia":20,"ąt":10,"ści":10,}
txt = "pięćdziesiąt dziewięć"
i=0
num = []
for x,y in liczby.items():
    if x in txt:
        num.append(y)
if len(num)<3:
    num.insert(0,0)
z = (num[-1]*num[-2])+num[-3]
z2 = (num[-1]*num[0]+num[1])
if z>99:
    z/10
print(z)
print(z2)