import urllib.request, json

url = 'http://barcelonaapi.marcpous.com/bicing/stations.json'
response = urllib.request.urlopen(url)
response_data = json.loads(response.read().decode('utf-8'))
data_bici = response_data['data']['bici']

output = []

for bici in data_bici:
    nueva_bici = bici
    nueva_bici['ciudad'] = 'Barcelona'
    output.append(nueva_bici)

output_file = open('barcelona.json', 'w')
json.dump(output, output_file)
output_file.close()