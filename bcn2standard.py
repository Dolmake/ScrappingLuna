import urllib.request, json

url = 'http://barcelonaapi.marcpous.com/bicing/stations.json'
response = urllib.request.urlopen(url)
response_data = json.loads(response.read().decode('utf-8'))
#response data es un diccionario, u objeto
data_bici = response_data['data']['bici']
#data_bici es un array de BICI

#output es un ARRAY
stations = []

indexID = 1
for bici in data_bici:
    #nueva_bici = bici
    nueva_bici = {}
    nueva_bici['id'] = indexID
    indexID = indexID + 1
    nueva_bici['city'] = 'Barcelona'
    nueva_bici['latitude'] = bici['lat']
    nueva_bici['longitude'] = bici['lon']
    nueva_bici['name'] = bici['name']
    nueva_bici['total_bases'] = 0
    nueva_bici['dock_bikes'] = 0
    nueva_bici['free_bases'] = 0

    stations.append(nueva_bici)
    #aqui finaliza el for

#creamos el objeto contenedor del array stations
result = {}
result['stations'] = stations


#creamos el fichero de salida
output_file = open('barcelona_standard.json', 'w')
#volcamos el json en el fichero
json.dump(result, output_file)
#cerramos el fichero para que se guarde
output_file.close()