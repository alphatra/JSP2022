# Inicjalizacja grafu
graph = {}

# Lista połączeń (sąsiedztwa)
# Każde połączenie składa się z dwóch wierzchołków: (A, B)
# oznaczającego połączenie wierzchołka A z wierzchołkiem B
connections = [("A", "B"), ("B", "C"), ("A", "C"), ("C", "D")]

# Dodanie połączeń do grafu
for A, B in connections:
    if A not in graph:
        graph[A] = []
    graph[A].append(B)

# Wypisanie grafu
for node, neighbors in graph.items():
    print(f"Sąsiedzi wierzchołka {node}: {neighbors}")
