x = []
for i in range (100,400):
    for x in range(0,2):
        if i[int(x)] % 2 == 0:
            x.append(i[x])
print(x)