import matplotlib.pyplot as plt
import geopandas as gpd
from sys import argv

blue_path = argv[1]
red_path = argv[2]
green_path = argv[3]
#blue_path = globals().get('blue_path', 'C:\\Users\\aleks\PycharmProjects\pythonProject\j\\blue.geojson')
#red_path = globals().get('red_path', 'C:\\Users\\aleks\PycharmProjects\pythonProject\j\\red.geojson')
#green_path = globals().get('green_path', 'C:\\Users\\aleks\PycharmProjects\pythonProject\j\\green.geojson')
print(blue_path)
df_blue = gpd.read_file(blue_path)
df_blue.plot(color='b')
plt.savefig('static/blue_photo.png')


df_red = gpd.read_file(red_path)
df_red.plot(color='r')
plt.savefig('static/red_photo.png')

df_green = gpd.read_file(green_path)
df_green.plot(color='g')
plt.savefig('static/green_photo.png')
