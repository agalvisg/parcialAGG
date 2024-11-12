# grafo.py
import networkx as nx

# Función para construir el grafo
def crear_grafo(localidades):
    G = nx.Graph()
    for origen, destinos in localidades.items():
        for destino, distancia in destinos:
            G.add_edge(origen, destino, weight=distancia)
    return G
