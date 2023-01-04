# Import biblioteki random do generowania losowych liczb
import random

# Inicjalizacja grafu sąsiedztwa
graph = {
    "Warszawa": ["Kraków", "Gdańsk", "Łódź", "Wrocław"],
    "Kraków": ["Warszawa", "Gdańsk", "Łódź", "Wrocław"],
    "Gdańsk": ["Warszawa", "Kraków", "Łódź", "Wrocław"],
    "Łódź": ["Warszawa", "Kraków", "Gdańsk", "Wrocław"],
    "Wrocław": ["Warszawa", "Kraków", "Gdańsk", "Łódź"]
}

# Wypisanie połączeń między miastami oraz dystansu pomiędzy nimi
for city, neighbors in graph.items():
    for neighbor in neighbors:
        # Generowanie losowego dystansu pomiędzy miastami
        distance = random.randint(100, 1000)
        print(f"Miasto {city} połączone jest z miastem {neighbor} dystansem {distance} km.")
