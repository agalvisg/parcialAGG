# buscar_ruta.py
import heapq

def dijkstra(grafo, inicio, fin):
    # Inicialización
    distancias = {nodo: float('inf') for nodo in grafo.nodes}
    distancias[inicio] = 0
    previo = {nodo: None for nodo in grafo.nodes}
    cola = [(0, inicio)]
    
    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)
        
        if nodo_actual == fin:
            break
            
        for vecino in grafo.neighbors(nodo_actual):
            peso = grafo[nodo_actual][vecino]['weight']
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                previo[vecino] = nodo_actual
                heapq.heappush(cola, (distancia, vecino))
                
    # Reconstruir la ruta más corta
    ruta = []
    nodo = fin
    while nodo:
        ruta.append(nodo)
        nodo = previo[nodo]
    ruta.reverse()
    
    return ruta, distancias[fin]
