import geopandas as gpd
import geojson
import shapely.wkt
# import Geohash
import hashlib

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

df = gpd.read_file('blue.geojson')
print(df.shape)
print(df.keys())
print(df['geometry'][0])

with open('blue.geojson') as file:
    data = geojson.load(file)

blue_length = len(data['features'])

for i in range(blue_length):
    for row in data['features'][i]['geometry']['coordinates']:
        for el in row:
            print(el)

# print("DATA:\n", data['features'][0]['geometry']['coordinates'][0])

# for i in range(len(df)):
    # print(df["features"][i]["geometry"]["coordinates"])
