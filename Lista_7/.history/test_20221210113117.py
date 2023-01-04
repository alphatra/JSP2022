# Inicjalizacja macierzy sąsiedztwa
matrix = [    [0, 200, 300, 100, 0],
    [0, 0, 100, 0, 400],
    [0, 0, 0, 200, 0],
    [0, 0, 0, 0, 300],
    [0, 0, 0, 0, 0]
]

# Wypisanie macierzy sąsiedztwa
for i in range(5):
    for j in range(5):
        print(matrix[i][j], end=" ")
    print()
