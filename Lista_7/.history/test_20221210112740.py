# Inicjalizacja grafu sąsiedztwa
graph = {
    "Warszawa": [("Kraków", 200), ("Wrocław", 300), ("Poznań", 100)],
    "Kraków": [("Wrocław", 100), ("Gdańsk", 400)],
    "Wrocław": [("Poznań", 200)],
    "Poznań": [("Gdańsk", 300)],
    "Gdańsk": []
}

# Wypisanie połączeń między miastami i dystansów
for city, neighbors in graph.items():
    print(f"Połączenia z miastem {city}:")
    for neighbor, distance in neighbors:
        print(f" - {neighbor}, dystans: {distance} km")
