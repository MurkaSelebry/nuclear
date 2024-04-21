from QuadroTree import QTree, Point
from sys import argv
import json
#'C:\\Users\\aleks\PycharmProjects\pythonProject\j\\blue.geojson'
#'C:\\Users\\aleks\PycharmProjects\pythonProject\j\\red.geojson'
#'C:\\Users\\aleks\PycharmProjects\pythonProject\j\\ggg.geojson'
blue_path = argv[1]
red_path = argv[2]
green_path = argv[3]
tree = QTree()
#'../j/blue.geojson'
with open(blue_path, 'r', encoding='utf-8') as file:
    blue = json.load(file)

blue_length = len(blue['features'])

for i in range(blue_length):
    for row in blue['features'][i]['geometry']['coordinates']:
        for el in row:
            tree.insert(Point(float(el[1]), float(el[0])))

'''
test_blue = open('test_blue.txt', 'r')
array = list(str(*test_blue).split(','))
for el in array:
    coords = list(el.split(' '))
    tree.insert(Point(float(coords[0]), float(coords[1])))
'''

tree.clear_points_in_tree()
# tree.output()
#'red.geojson'

with open(red_path, 'r', encoding='utf-8') as file:
    red = json.load(file)

red_length = len(red['features'])

for i in range(red_length):
    for row in red['features'][i]['geometry']['coordinates']:
        for el in row:
            tree.dfs(Point(el[1], el[0], red['features'][i]['properties']))

green = dict()
green['type'] = blue['type']
green['name'] = blue['name']
green['crs'] = blue['crs']
green['features'] = blue['features']
for i in range(blue_length):
    for row in blue['features'][i]['geometry']['coordinates']:
        flag = True
        for el in row:
            new_attributes = tree.find_with_dfs(tree.root, Point(el[1], el[0]))
            if new_attributes:
                print(new_attributes)
                green['features'][i]['properties'] = blue['features'][i]['properties']
                green['features'][i]['properties'].update(new_attributes)
                flag = False
                break
        if not flag:
            break
#'../j/green.geojson'
with open(green_path, 'w', encoding='utf-8') as file:
    json.dump(green, file)