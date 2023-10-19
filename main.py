import pandas as pd
import networkx as nx
#import matplotlib.pyplot as plt
from eo import *
from punto1 import *
from punto2 import *
dataframe = pd.read_csv('datos.csv')
#Verifica conexion entre aeropuertos
def estan_conectados(G,aeropuerto_origen, aeropuerto_destino):
    return nx.has_path(G, source=aeropuerto_origen, target=aeropuerto_destino)
def getlists(dataframe):

    # Crear lista de puntos para aeropuertos de origen
    lista_source = list(zip(dataframe['Source Airport Latitude'], dataframe['Source Airport Longitude']))

    # Crear lista de puntos para aeropuertos de destino
    lista_destino = list(zip(dataframe['Destination Airport Latitude'], dataframe['Destination Airport Longitude']))

    # Crear un diccionario para almacenar los aeropuertos únicos y sus coordenadas
    unique_airports = {}

    # Iterar sobre los registros del dataset
    for index, row in dataframe.iterrows():
        # Obtener el aeropuerto origen y destino de cada registro
        source_airport = row["Source Airport Code"]
        destination_airport = row["Destination Airport Code"]

    # Obtener la latitud y longitud del aeropuerto origen
        source_lat = row["Source Airport Latitude"]
        source_lon = row["Source Airport Longitude"]

        # Obtener la latitud y longitud del aeropuerto destino
        dest_lat = row["Destination Airport Latitude"]
        dest_lon = row["Destination Airport Longitude"]

        # Agregar el aeropuerto origen al diccionario si no existe
        if source_airport not in unique_airports:
            unique_airports[source_airport] = (source_lat, source_lon)

        # Agregar el aeropuerto destino al diccionario si no existe
        if destination_airport not in unique_airports:
            unique_airports[destination_airport] = (dest_lat, dest_lon)

    # Crear una lista de aeropuertos sin repeticiones con sus coordenadas
    airport_coordinates = [(airport, lat, lon) for airport, (lat, lon) in unique_airports.items()]

    result = {"airport_coordinates": airport_coordinates, "lista_source": lista_source, "lista_destino": lista_destino}
    return result

G = nx.Graph()
# Creacion de nodos
for index, row in dataframe.iterrows():
    source_airport = row['Source Airport Code']
    destination_airport = row['Destination Airport Code']
    distance = row['Distancia']

    G.add_node(source_airport, name=row['Source Airport Name'], city=row['Source Airport City'],
               country=row['Source Airport Country'], latitude=row['Source Airport Latitude'], longitude=row['Source Airport Longitude'])
    G.add_node(destination_airport, name=row['Destination Airport Name'], city=row['Destination Airport City'],
               country=row['Destination Airport Country'], latitude=row['Destination Airport Latitude'], longitude=row['Destination Airport Longitude'])
    G.add_edge(source_airport, destination_airport, weight=distance)
cod1 = str(input('Codigo 1er aeropuerto:'))
cod2 = str(input('Codigo 2do aeropuerto:'))
if estan_conectados(G, cod1, cod2):
    print('Los aeropuertos seleccionados estan conectados')
else:
    print('Los aeropuertos seleccionados NO estan conectados')
    
op1 = int(input("Empezar? 1.SI"))
while op1 ==1:
    op2 = int(input('Opciones: \n1.Generar grafo completo\n 2.Info 1er aeropuerto y 10 aeropuertos mas lejanos \n3.Camino minimo entre 2 aeropuertos seleccionados'))
    if op2 == 1:
        info = getlists(dataframe)
        generatemap(info["airport_coordinates"], info["lista_source"], info["lista_destino"])
    elif op2 ==2:
        dataandpaths(cod1, G)
    else:
        MPbetweeenairports(cod1, cod2, G)
    op1 = int(input("Seguir? 1.SI"))








