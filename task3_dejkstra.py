import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:

    """Ваговий граф з алгоритмом Дейкстри.
    Використовує бінарну купу (heapq) для ефективного вибору наступної вершини.
    Метод dijkstra має параметр verbose для покрокового виводу."""

    def __init__(self):
        self.edges = {}  # словник: вершина -> список (сусід, вага)

    def add_edge(self, u, v, weight):
        self.edges.setdefault(u, []).append((v, weight))
        self.edges.setdefault(v, []).append((u, weight))

    def dijkstra(self, start, verbose=False):

        distances = {vertex: float('inf') for vertex in self.edges}
        distances[start] = 0

        heap = [(0, start)]
        visited = set()

        if verbose:
            print("\n=== Початок алгоритму Дейкстри ===")
            print(f"[Ініціалізація] Стартова вершина: {start}")
            print(f"[Купа] Початковий стан: {heap}\n")

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)

            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            if verbose:
                print(f"[Вибір] Витягнуто з купи: ({current_distance}, '{current_vertex}')")
                print(f"[Фіксація] Відстань до '{current_vertex}' = {current_distance}")

            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    if verbose:
                        print(f"  [Оновлення] '{neighbor}' через '{current_vertex}' з вагою {weight}")
                        print(f"     Стара відстань: {distances[neighbor]}")
                        print(f"     Нова відстань:  {distance}")
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
                    if verbose:
                        print(f"     Додано до купи: ({distance}, '{neighbor}')")

            if verbose:
                print(f"[Купа] Стан після обробки '{current_vertex}': {heap}\n")

        if verbose:
            print("=== Завершення алгоритму ===\n")

        return distances

def visualize_graph(graph, distances=None, start=None):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()

    # Додаємо ребра
    for u in graph.edges:
        for v, weight in graph.edges[u]:
            G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G, weight='weight', seed=42)

    # Кольори вузлів
    node_colors = []
    for node in G.nodes():
        if node == start:
            node_colors.append("orange")
        else:
            node_colors.append("lightblue")

    # Малюємо вузли, ребра, ваги
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

    # Мітки вузлів — за іменем (ID)
    nx.draw_networkx_labels(G, pos, labels={node: node for node in G.nodes()}, font_size=12)

    # Відстані від стартової вершини
    if distances:
        for node in G.nodes():
            if node != start:
                x, y = pos[node]
                plt.text(x, y - 0.1, f"dist: {distances[node]:.1f}", fontsize=9, color="gray", ha="center")

    plt.title("Граф з іменами вузлів та вагами")
    plt.axis("off")
    plt.show()

def demo_dejkstra():
    print("=== Демонстрація алгоритму Дейкстри ===")

    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'E', 2)
    g.add_edge('D', 'Z', 6)
    g.add_edge('E', 'Z', 3)

    start = input("Введіть стартову вершину (наприклад, A): ").strip()
    if start not in g.edges:
        print(f"Вершина {start} не знайдена у графі.")
        return

    distances = g.dijkstra(start)

    print(f"Найкоротші відстані від вершини {start}:")
    for vertex, distance in distances.items():
        print(f"{start} → {vertex}: {distance}")
    visualize_graph(g, distances, start)