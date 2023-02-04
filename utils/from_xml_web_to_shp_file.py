# on importe les libs
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import shapely.wkt
from shapely.geometry import mapping
import fiona

# on définit la province d'intérêt
filter = "QC"
# la liste des stations
url = "https://dd.meteo.gc.ca/citypage_weather/xml/siteList.xml"
# on fait la requête
response = requests.get(url = url)
# on analyse la réponse
doc = BeautifulSoup( response.text, 'xml')
# extraction de tous les sites
allsites = doc.findAll('site')
# une liste qui contiendra les valeurs
data = []

# on parcourt les sites XML
for node in allsites:
    # on récupère la province
    codeProvince = node.find('provinceCode').text
    # si c'est la province recherchée
    if codeProvince == filter:
        # on récupère le nom du lieu
        name = node.find('nameFr').text
        # on récupère le code de la station
        code = node['code']
        # on va faire une requête sur le fichier de la station
        dataurl = f'https://dd.meteo.gc.ca/citypage_weather/xml/{filter}/{code}_f.xml'
        
        response = requests.get(url = dataurl)
        # on analyse
        datadoc = BeautifulSoup( response.content, 'xml', from_encoding="latin-1")
        # on s'intéresse aux conditions actuelles
        currentConditions = datadoc.find('currentConditions')
        # on peut récupérer la date
        xmldateTime = currentConditions.find('dateTime', {'zone':'UTC'})
        # si jamais il n'y a pas d'observation, on ne fait rien
        if xmldateTime:
            # on va récupérer la date de l'observation
            timestamp = xmldateTime.find('timeStamp').text
            # on forme une date
            obsdate = f'{timestamp[:4]}/{timestamp[4:6]}/{timestamp[6:8]} {timestamp[8:10]}:{timestamp[12:]}'
            # on récupère les infos de la station
            station = currentConditions.find('station')
            # le nom
            name = station.text
            # la position
            lat = station['lat']
            lon = station['lon']
            # on convertit en float
            if 'O' in lon:
                lon = float(lon.replace('O','')) * -1.0
            elif 'E' in lon:
                lon = float(lon.replace('E',''))
            if 'N' in lat:
                lat = float(lat.replace('N',''))
            elif 'S' in lat:
                lat = float(lat.replace('S','')) * -1.0
            # on fait un point
            point = shapely.wkt.loads(f'POINT({lon} {lat})')
            #on va récupérer toutes les infos
            temperature = dewpoint = windChill = pressure = relativeHumidity = None
            # on vérifie si la balise existe et contient des infos
            if currentConditions.find('temperature') and currentConditions.find('temperature').text != '':
                temperature = float(currentConditions.find('temperature').text)
            if currentConditions.find('dewpoint') and currentConditions.find('dewpoint').text != '':
                dewpoint = float(currentConditions.find('dewpoint').text)
            if currentConditions.find('windChill') and currentConditions.find('windChill').text != '':
                windChill = float(currentConditions.find('windChill').text)
            if currentConditions.find('pressure') and currentConditions.find('pressure').text != '':
                pressure = float(currentConditions.find('pressure').text)
            if currentConditions.find('relativeHumidity') and currentConditions.find('relativeHumidity').text != '':              
                relativeHumidity = float(currentConditions.find('relativeHumidity').text)
            # on alimente notre liste
            data.append(
                {'geom': point, 'properties': {'code': code,'date': obsdate, 'name': name, 'lon': lon,
                'lat': lat, 'temp': temperature, 'dew': dewpoint, 'wind': windChill, 'pressure': pressure, 'humidity': relativeHumidity}}
            )

# on va créer le fichier SHP
# voici le schéma
schema = {
    'geometry': 'Point',
    'properties': {
        'code':'str','date': 'str', 'name': 'str', 
        'lon': 'float', 'lat': 'float', 'temp': 'float', 
        'dew': 'float', 'wind': 'float', 
        'pressure': 'float', 'humidity': 'float'
        }
}
# on forme le fichier SHP
with fiona.open('observations.shp', 'w', crs='EPSG:4326', driver="ESRI Shapefile", schema=schema) as src:
    for d in data:
        src.write(
            {'geometry': mapping(d['geom']), 'properties': d['properties']}
        )