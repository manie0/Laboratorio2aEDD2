import networkx as nx
import folium
from eo import *

def MPbetweeenairports(cod1, cod2, G):
    # Supongamos que tienes dos aeropuertos seleccionados por sus códigos
    aeropuerto_origen = cod1
    aeropuerto_destino = cod2

    # Calcula el camino mínimo entre el aeropuerto de origen y el de destino
    shortest_path = nx.shortest_path(
        G, source=aeropuerto_origen, target=aeropuerto_destino, weight='weight')

    # Inicializa la lista "Points" para almacenar los pares de latitud y longitud
    Points = []
    latitudes = []
    longitudes = []
    LLsource = []
    LLdestination = []
    pesos_aristas = []
    # Obtiene los pares de latitud y longitud de cada aeropuerto en el camino mínimo
    for i in range(len(shortest_path)):
        airport_code = shortest_path[i]
        airport_info = G.nodes[airport_code]
        airport = airport_code
        latitude = airport_info['latitude']
        latitudes.append(latitude)
        longitude = airport_info['longitude']
        longitudes.append(longitude)
        Points.append((airport, latitude, longitude))
            # Obtiene el peso de la arista entre el aeropuerto actual y el siguiente
        if i < len(shortest_path) - 1:
            next_airport_code = shortest_path[i + 1]
            weight = G[airport_code][next_airport_code]['weight']
            pesos_aristas.append(weight)



    # Muestra la información de los aeropuertos en el camino mínimo
    popup = []
    print("Información de los aeropuertos en el camino mínimo:")
    for airport_code in shortest_path:
        airport_info = G.nodes[airport_code]
        print(f"Código: {airport_code}")
        print(f"Nombre: {airport_info['name']}")
        popup.append(airport_info['name'])
        print(f"Ciudad: {airport_info['city']}")
        popup.append(airport_info['city'])
        print(f"País: {airport_info['country']}")
        popup.append(airport_info['country'])
        print(f"Latitud: {airport_info['latitude']}")
        print(f"Longitud: {airport_info['longitude']}\n")

    # Recorre la lista de latitudes
    index = 0
    for i in range(len(latitudes)-1):
        LLsource.append([latitudes[i], longitudes[i]])
        LLdestination.append([latitudes[i+1], longitudes[i+1]])
        index += 1

    #result = {"airport_coordinates": Points, "lista_source": LLsource, "lista_destino": LLdestination}
    m = folium.Map(location=[0, 0], zoom_start=12)
    # Añadir aeropuertos (marcadores) al objeto mapa
    for airport, lat, lon in Points:
        if popup == None:
            popup_text = f"Codigo: {airport}"
        else:
            popup_text = f"Codigo: {airport} \nNombre: {popup[0]} \nCiudad: {popup[1]}\nPais: {popup[2]}\nLatitud: {lat}\nLongitud:{lon}"
        marker = folium.Marker(location=[lat,lon], popup=popup_text)
        marker.add_to(m)

    # Añadir aristas al objeto mapa
    index=0
    for i, j in zip(LLsource, LLdestination):
        folium.PolyLine(locations=[i, j], weight=1, color='blue', opacity=0.5, popup=pesos_aristas[index]).add_to(m)
        index += 1

    m.save('mapaP2.html')

