from grafo import crear_grafo
from buscar_ruta import dijkstra
from mostrar_grafo import mostrar_grafo
from analisis_grafo import conexiones_cortas, es_conexo, componentes_conexos, ruta_alternativa

localidades = {
    "Madrid": [("Alcorcón", 13), ("Villaviciosa de Odón", 22), ("Alcalá de Henares", 35)],
    "Villanueva de la Cañada": [("Villaviciosa de Odón", 11), ("Boadilla del Monte", 7)],
    "Alcorcón": [("Madrid", 13), ("Móstoles", 5)],
    "Móstoles": [("Alcorcón", 5), ("Fuenlabrada", 8)],
    "Fuenlabrada": [("Móstoles", 8), ("Getafe", 10)],
    "Getafe": [("Fuenlabrada", 10), ("Madrid", 16)],
    "Villaviciosa de Odón": [("Madrid", 22), ("Villanueva de la Cañada", 11)],
    "Boadilla del Monte": [("Villanueva de la Cañada", 7), ("Madrid", 15)],
    "Alcalá de Henares": [("Madrid", 35), ("Torrejón de Ardoz", 15)],
    "Torrejón de Ardoz": [("Alcalá de Henares", 15), ("Madrid", 20)]
}

def main():
    G = crear_grafo(localidades)
    
    # 1. Ruta más corta entre dos localidades
    inicio, fin = "Alcalá de Henares", "Alcorcón"
    ruta, distancia = dijkstra(G, inicio, fin)
    print(f"Ruta más corta entre {inicio} y {fin}: {' -> '.join(ruta)} con una distancia de {distancia} km")
    mostrar_grafo(G, ruta)
    
    # 2. Conexiones cortas
    conexiones = conexiones_cortas(G, umbral=10)
    print("\nConexiones cortas (distancia < 10 km):")
    for origen, destino, distancia in conexiones:
        print(f"{origen} - {destino}: {distancia} km")
    
    # 3. Conectividad del grafo
    if es_conexo(G):
        print("\nEl grafo es conexo.")
    else:
        print("\nEl grafo no es conexo. Componentes conectados:")
        for i, componente in enumerate(componentes_conexos(G), 1):
            print(f"Componente {i}: {componente}")
    
    # 4. Ruta alternativa
    alternativa, distancia_alt = ruta_alternativa(G, inicio, fin)
    if alternativa:
        print(f"\nRuta alternativa entre {inicio} y {fin}: {' -> '.join(alternativa)} con una distancia de {distancia_alt} km")
    else:
        print("\nNo se encontró una ruta alternativa entre las localidades.")

if __name__ == "__main__":
    main()
