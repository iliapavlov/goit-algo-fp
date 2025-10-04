import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import time

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, pause=0.5):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [tree.nodes[n]['color'] for n in tree.nodes]
    labels = {n: tree.nodes[n]['label'] for n in tree.nodes}

    plt.clf()
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.pause(pause) # Пауза для анімації

def generate_gradient_colors(n, start_color="#000080", end_color="#ADD8E6"):
    """ Повертає список кольорів від start_color до end_color """
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(rgb):
        return "#{:02X}{:02X}{:02X}".format(*rgb)

    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)

    gradient = []
    for i in range(n):
        ratio = i / max(n - 1, 1)
        rgb = tuple(int(start_rgb[j] + (end_rgb[j] - start_rgb[j]) * ratio) for j in range(3))
        gradient.append(rgb_to_hex(rgb))
    return gradient

def visualize_dfs(root):
    stack = [root]
    visited = []
    seen = set()

    while stack:
        node = stack.pop()
        if node and node.id not in seen:
            visited.append(node)
            seen.add(node.id)
            stack.append(node.right)
            stack.append(node.left)

    colors = generate_gradient_colors(len(visited))
    for i, node in enumerate(visited):
        node.color = colors[i] # Оновлення кольору вузла
        draw_tree(root)

def visualize_bfs(root):
    queue = deque([root])
    visited = []
    seen = set()

    while queue:
        node = queue.popleft()
        if node and node.id not in seen:
            visited.append(node)
            seen.add(node.id)
            queue.append(node.left)
            queue.append(node.right)

    colors = generate_gradient_colors(len(visited))
    for i, node in enumerate(visited):
        node.color = colors[i] # Оновлення кольору вузла
        draw_tree(root)

def build_heap_tree(heap_list):
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
    return nodes[0]

def demo_traversal_visualization():
    heap_list = [1, 3, 5, 7, 9, 2, 8, 12, 10, 5, 4, 6, 11]
    heapq.heapify(heap_list)
    heap_root = build_heap_tree(heap_list)

    print("🔍 DFS Visualization")
    plt.figure(figsize=(8, 5))
    visualize_dfs(heap_root)

    heap_root = build_heap_tree(heap_list)
    print("🌐 BFS Visualization")
    plt.figure(figsize=(8, 5))
    visualize_bfs(heap_root)

    plt.show()

if __name__ == "__main__":
    demo_traversal_visualization()