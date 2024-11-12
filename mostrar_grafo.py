
# mostrar_grafo.py
import networkx as nx
import matplotlib.pyplot as plt

# Graficar el grafo y la ruta más corta
def mostrar_grafo(G, ruta=[]):
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    
    # Dibujar nodos y etiquetas
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    # Destacar la ruta más corta si existe
    if ruta:
        ruta_edges = [(ruta[i], ruta[i+1]) for i in range(len(ruta) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=ruta_edges, edge_color="orange", width=3)
    
    plt.show()
