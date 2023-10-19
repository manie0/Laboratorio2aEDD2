#import pandas as pd
import networkx as nx
#import matplotlib.pyplot as plt


def dataandpaths(Code, G):
    aeropuerto_seleccionado = Code

    # Calcula los caminos mínimos desde el aeropuerto seleccionado y obtén los 10 caminos más largos
    longest_paths = nx.single_source_dijkstra_path_length(
        G, source=aeropuerto_seleccionado, weight='weight')
    longest_paths = sorted(longest_paths.items(),
                        key=lambda x: x[1], reverse=True)[:10]

    # Muestra la información del aeropuerto seleccionado
    print("Información del aeropuerto seleccionado:")
    selected_airport_info = G.nodes[aeropuerto_seleccionado]
    for key, value in selected_airport_info.items():
        print(f"{key}: {value}")
    print()

    # Muestra los 10 aeropuertos con los caminos mínimos más largos y sus distancias
    print("Los 10 aeropuertos con los caminos mínimos más largos desde el aeropuerto seleccionado:")
    for airport, distance in longest_paths:
        airport_info = G.nodes[airport]
        print(f"Código: {airport}, Nombre: {airport_info['name']}, Ciudad: {airport_info['city']}, País: {airport_info['country']}, Latitud: {airport_info['latitude']}, Longitud: {airport_info['longitude']}, Distancia desde el aeropuerto seleccionado: {distance}\n")


"""
# Visualización del grafo
pos = nx.spring_layout(G)
labels = {node: G.nodes[node]['name'] for node in G.nodes()}

nx.draw(G, pos, with_labels=True, labels=labels, node_size=100, font_size=8, node_color='lightblue')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
"""