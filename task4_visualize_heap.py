import uuid
import heapq

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_heap_tree(heap_list):
    """Створює дерево з масиву купи"""
    if not heap_list:
        return None

    nodes = [Node(val) for val in heap_list]

    for i in range(len(heap_list)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(heap_list):
            nodes[i].left = nodes[left_index]
        if right_index < len(heap_list):
            nodes[i].right = nodes[right_index]

    return nodes[0]  # корінь дерева

def assign_colors_by_level(node, level=0):
    if node:
        palette = ["skyblue", "lightgreen", "salmon", "plum", "khaki"]
        node.color = palette[level % len(palette)]
        assign_colors_by_level(node.left, level + 1)
        assign_colors_by_level(node.right, level + 1)

def demo_heap_visualization():
    """Демонстрація побудови та візуалізації бінарної купи"""

    heap_list = [1, 3, 5, 7, 9, 2, 8, 12, 10, 5, 4, 6, 11]
    heapq.heapify(heap_list)
    print(heap_list)

    heap_root = build_heap_tree(heap_list)
    assign_colors_by_level(heap_root)
    draw_tree(heap_root)

