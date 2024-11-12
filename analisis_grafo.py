# analisis_grafo.py
from buscar_ruta import dijkstra
import networkx as nx

def es_conexo(G):
    return nx.is_connected(G)

def componentes_conexos(G):
    return list(nx.connected_components(G))

def conexiones_cortas(G, umbral):
    conexiones = []
    for origen, destino, data in G.edges(data=True):
        if data['weight'] < umbral:
            conexiones.append((origen, destino, data['weight']))
    return conexiones

# analisis_grafo.py

def ruta_alternativa(G, inicio, fin):
    # Primero obtenemos la ruta más corta actual
    ruta_principal, _ = dijkstra(G, inicio, fin)
    
    # Creamos una copia del grafo y eliminamos las aristas de la ruta principal
    G_alternativo = G.copy()
    for i in range(len(ruta_principal) - 1):
        G_alternativo.remove_edge(ruta_principal[i], ruta_principal[i + 1])
    
    # Calculamos la nueva ruta sin la ruta principal
    ruta_alternativa, distancia = dijkstra(G_alternativo, inicio, fin)
    return ruta_alternativa, distancia

