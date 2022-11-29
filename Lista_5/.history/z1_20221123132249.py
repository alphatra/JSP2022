liczby = {"jeden":1,"dwa":2,"trzy":3,"cztery":4,"pięć":5,"sześć":6,"siedem":7,"osiem":8,"dziewięć":9,"dziesięć":10,"ąt":10,"ści":10}
txt = "sześćdziesiąt trzy"
i,n=0
for x in liczby:
    if x in txt:
        print(liczby[x],i)
        i+=1
        while(n<len(txt)):
            print("asda")
            n+=1
        n=0
    