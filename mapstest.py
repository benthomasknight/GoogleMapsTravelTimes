import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='')

origins = ['Address 1', 'Address 2']
destinations = ['Address 3','Address 4']
res = gmaps.distance_matrix(origins, destinations)

for originIdx, row in enumerate(res['rows']):
  for destIdx, el in enumerate(row['elements']):
    print(origins[originIdx] + ' to ' + destinations[destIdx] + ' - ' + el['duration']['text'])
