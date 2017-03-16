import urllib.request, json

url = 'http://localhost:8000/Projects/js/ScrappingLuna/data/bicis_madrid.json'
response = urllib.request.urlopen(url)
response_data = json.loads(response.read().decode('utf-8'))
#response data es un diccionario, u objeto
data_stations_array = response_data['stations']
#data_bici es un array de BICI

#output es un ARRAY
stations = []

print('Creando el for')

indexID = 1
for data_station in data_stations_array:
    #nueva_bici = bici
    nueva_bici = {}
    nueva_bici['id'] = indexID
    indexID = indexID + 1
    nueva_bici['city'] = 'Madrid'
    nueva_bici['latitude'] = data_station['latitude']
    nueva_bici['longitude'] = data_station['longitude']
    nueva_bici['name'] = data_station['name']
    nueva_bici['total_bases'] = data_station['total_bases']
    nueva_bici['dock_bikes'] =  data_station['dock_bikes']
    nueva_bici['free_bases'] =  data_station['free_bases']

    stations.append(nueva_bici)
    #aqui finaliza el for

#creamos el objeto contenedor del array stations
result = {}
result['stations'] = stations

print('Fin del for')


#creamos el fichero de salida
output_file = open('madrid_standard.json', 'w')
#volcamos el json en el fichero
json.dump(result, output_file)
#cerramos el fichero para que se guarde
output_file.close()