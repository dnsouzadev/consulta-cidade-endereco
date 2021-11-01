from geopy.geocoders import Nominatim
from functools import partial
import os
import time
import sys

try:
    os.system('cls')
except:
    os.system('clear')

geolocator = Nominatim(user_agent="bueroficial")

#ENDEREÇO
def endereco(address):
    location = geolocator.geocode(f"{address}")
    l = location.raw
    lat = l['lat']
    lon = l['lon']
    display = l['display_name']
    classe = l['class']
    return f'{display} -> latitude: {lat} -> longitude: {lon} -> classe: {classe}'

#CIDADE
def cidade(city):
    geocode = partial(geolocator.geocode, language="pt")
    cit = geocode(f"{city}")
    c = cit.raw
    lat = c['lat']
    lon = c['lon']
    display = c['display_name']
    classe = c['class']
    importancia = c['importance']
    importancia = round(importancia, 2)
    return f'{display} -> latitude: {lat} -> longitude: {lon} -> classe: {classe} -> importancia: {importancia}'

#POR LATITUDE E LOGINTUDE
def coordenadas(lat, log):
    reverse = partial(geolocator.reverse, language="es")
    return reverse(f"{lat}, {log}")


while True:
    print("""..######...#######..##....##..######..##.....##.##.......########....###.......##.....##...#####..........##..
.##....##.##.....##.###...##.##....##.##.....##.##..........##......##.##......##.....##..##...##.......####..
.##.......##.....##.####..##.##.......##.....##.##..........##.....##...##.....##.....##.##.....##........##..
.##.......##.....##.##.##.##..######..##.....##.##..........##....##.....##....##.....##.##.....##........##..
.##.......##.....##.##..####.......##.##.....##.##..........##....#########.....##...##..##.....##........##..
.##....##.##.....##.##...###.##....##.##.....##.##..........##....##.....##......##.##....##...##..###....##..
..######...#######..##....##..######...#######..########....##....##.....##.......###......#####...###..######
developed by: github.com/buerofical""")
    res = input("""
    [1] - Buscar um endereço
    [2] - Buscar uma cidade
    [3] - Buscar por latitude e longitude
    * DIGITE QUALQUER OUTRA TECLA PARA FECHAR O APLICATIVO
    >>> """)
    if res == '1':
        time.sleep(1)
        end = input('Digite o endereço por favor: ')
        print()
        print(endereco(end))
        time.sleep(5)
        print()
    elif res == '2':
        time.sleep(1)
        end = input('Digite o nome da cidade por favor: ')
        print()
        print(cidade(end))
        time.sleep(5)
        print()
    elif res == '3':
        time.sleep(1)
        end = input('Digite a latitude por favor: ')
        start = input('Digite a longitude por favor: ')
        print()
        print(coordenadas(end, start))
        time.sleep(5)
        print()
    else:
        print('Encerrando...')
        time.sleep(2)
        sys.exit()


