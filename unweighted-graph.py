import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
edges = [('A','B'), ('A','C'), ('B','D'), ('B','E'), ('C','F'), ('E','F')]
G.add_edges_from(edges)
nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=12)
plt.title("Unweighted Graph - BFS Example")
plt.show()
