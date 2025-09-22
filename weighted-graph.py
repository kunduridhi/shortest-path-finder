G = nx.Graph()
edges = [('A','B',2), ('A','C',4), ('B','C',1), ('B','D',7), ('C','E',3), ('D','E',2)]
G.add_weighted_edges_from(edges)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_size=12)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Weighted Graph - Dijkstra Example")
plt.show()
