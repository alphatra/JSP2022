liczby = {"jeden":1,"dwa":2,"trzy":3,"cztery":4,"pięć":5,"sześć":6,"siedem":7,"osiem":8,"dziewięć":9,"dziesięć":10,"ąt":10,"ści":10}
txt = "sześćdziesiąt trzy"
i=0
while i < len(txt):
    txt.split()
    if i+1<len(txt) and txt[i:i+2] in liczby:
        print(i)