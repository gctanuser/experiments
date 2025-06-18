import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_edges_from([("A", "B"), ("A", "C"), ("B", "C"), ("B", "D")])
nx.draw(G, with_labels=True)
plt.show()
