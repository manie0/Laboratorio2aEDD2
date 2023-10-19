#h import pandas as pd
import folium







def generatemap(airport_coordinates, lista_source, lista_destino, popup = None):
    m = folium.Map(location=[0, 0], zoom_start=12)
    # Añadir aeropuertos (marcadores) al objeto mapa
    for airport, lat, lon in airport_coordinates:
        if popup == None:
            popup_text = f"Codigo: {airport}"
        else:
            popup_text = f"Codigo: {airport}"
        marker = folium.Marker(location=[lat,lon], popup=popup_text)
        marker.add_to(m)

    # Añadir aristas al objeto mapa
    for i, j in zip(lista_source, lista_destino):
        folium.PolyLine(locations=[i, j], weight=1, color='blue', opacity=0.5).add_to(m)
    m.save('mapa.html')


