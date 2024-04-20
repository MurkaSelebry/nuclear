import geopandas as gpd
import geojson
import shapely.wkt
# import Geohash
import hashlib
import json

"""
def geo_hash(latitude, longitude, precision=12):
    # Преобразование гео-координат в строку
    coord_str = f"{latitude},{longitude}"

    # Создание хеша из строки с использованием SHA-1
    h = hashlib.sha1(coord_str.encode())

    # Возвращение хеша с указанной точностью
    return h.hexdigest()[:precision]


print((geo_hash(20.25736, 54.94998)))
print((geo_hash(20.25736, 54.94998)))

"""

# df = gpd.read_file('red_test.geojson')
# print(df['geometry'][0])

with open('test_red.geojson', 'r', encoding='utf-8') as file:
    data = json.load(file)

red_length = len(data['features'])

for i in range(red_length):
    for row in data['features'][i]['geometry']['coordinates']:
        for el in row:
            print(el)

# print("DATA:\n", data['features'][0]['geometry']['coordinates'][0])

# for i in range(len(df)):
    # print(df["features"][i]["geometry"]["coordinates"])
