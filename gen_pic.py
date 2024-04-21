import matplotlib.pyplot as plt
import geopandas as gpd


blue_path = globals().get('blue_path', 'C:\\Users\\aleks\PycharmProjects\pythonProject\j\\blue.geojson')
red_path = globals().get('red_path', 'C:\\Users\\aleks\PycharmProjects\pythonProject\j\\red.geojson')
green_path = globals().get('green_path', 'C:\\Users\\aleks\PycharmProjects\pythonProject\j\\green.geojson')

df_blue = gpd.read_file(blue_path)
df_blue.plot(color='b')
plt.savefig('')

df_red = gpd.read_file(red_path)
df_red.plot(color='r')
plt.savefig('')

df_green = gpd.read_file(green_path)
df_green.plot(color='g')
plt.savefig('')
