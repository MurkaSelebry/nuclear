import sys

import numpy as np
import json


class Point:
    def __init__(self, x, y, attributes=None):
        self.x = x
        self.y = y
        self.red = False
        self.attributes = attributes


class Node:
    def __init__(self, x_low_border, x_high_border, y_low_border, y_high_border):
        self.x_low_border = x_low_border
        self.x_high_border = x_high_border
        self.y_low_border = y_low_border
        self.y_high_border = y_high_border
        self.points = []
        self.children = []

    def get_border(self):
        return [[self.x_low_border, self.x_high_border], [self.y_low_border, self.y_high_border]]


class QTree:

    def __init__(self, max_points=7):
        self.root = Node(-180, 180, -90, 90)
        self.root.children = [Node(-180, 0, 0, 90),
                              Node(0, 180, 0, 90),
                              Node(-180, 0, -90, 0),
                              Node(0, 180, -90, 0)]
        self.max_points = max_points
        self.g_count = 0

    def insert(self, point):
        self._insert(self.root, point)

    def _insert(self, node, point):
        # Check if the point is within the node's borders
        if not (node.x_low_border <= point.x <= node.x_high_border and
                node.y_low_border <= point.y <= node.y_high_border):
            return False

        # If the node is a leaf and has space for more points, add the point
        if not node.children and len(node.points) < self.max_points:
            node.points.append(point)
            return True

        # If the node is a leaf but has reached its max_points limit, subdivide it
        if not node.children:
            self._subdivide(node)

        # Insert the point into the appropriate child
        for child in node.children:
            if self._insert(child, point):
                return True

        return False

    def _subdivide(self, node):
        # Subdivide the node into four children
        x_mid = (node.x_low_border + node.x_high_border) / 2
        y_mid = (node.y_low_border + node.y_high_border) / 2

        # node.points = ['-', '-', '-', '-']

        node.children = [
            Node(node.x_low_border, x_mid, node.y_low_border, y_mid),
            Node(x_mid, node.x_high_border, node.y_low_border, y_mid),
            Node(node.x_low_border, x_mid, y_mid, node.y_high_border),
            Node(x_mid, node.x_high_border, y_mid, node.y_high_border)
        ]

        # Move the points from the node to its children
        for point in node.points:
            for child in node.children:
                if self._insert(child, point):
                    break

    def output(self, node=None, level=0):
        if node is None:
            node = self.root

        # Print the node's borders and level
        print(
            ' ' * level + f'Node: {node.x_low_border}, {node.x_high_border}, {node.y_low_border}, {node.y_high_border}')

        # Print the points contained in the node
        if node.points:
            print(' ' * (level + 1) + 'Points:')
            for point in node.points:
                print(' ' * (level + 2) + f'({point.x}, {point.y}, {point.red})')
                print(point.attributes)

        # Recursively output the children of the node
        if node.children:
            for child in node.children:
                self.output(child, level + 1)

    def clear_points_in_tree(self):
        self._clear_points_in_tree(self.root)

    def _clear_points_in_tree(self, node):
        if node.children:
            node.points = []
            for child in node.children:
                self._clear_points_in_tree(child)

    def distance(self, pt_1, pt_2):
        pt_1 = np.array((pt_1.x, pt_1.y))
        pt_2 = np.array((pt_2.x, pt_2.y))
        return np.linalg.norm(pt_1 - pt_2)

    def dfs(self, point):
        return self._dfs(self.root, point, 0)

    def _dfs(self, node, point, depth):
        if not (node.x_low_border <= point.x <= node.x_high_border and
                node.y_low_border <= point.y <= node.y_high_border):
            return 0

        if not node.children:
            '''
            min_distance = [float('inf'), 0]
            for number in range(len(node.points)):
                if min_distance[0] < self.distance(point, node.points[number]):
                    min_distance[0] = self.distance(point, node.points[number])
                    min_distance[1] = number
            if node.points:
                node.points[min_distance[1]].red = True
                self.g_count += 1
                print("Исходная - ", point.x, point.y)
                print("Ближайшая - ", node.points[min_distance[1]].x, node.points[min_distance[1]].y)
            '''
            return depth

        for child in node.children:
            status = self._dfs(child, point, depth + 1)
            if 1 <= status - depth <= 3:
                # print("xyi")
                self.g_count += 1
                if self.find(node, point):
                    return True
                return status
            elif status > 0:
                return status

        return False

    def find(self, node, point):
        path = []
        min_distance = float('inf')
        for i in range(len(node.children)):
            if node.children[i].points:
                for ii in range(len(node.children[i].points)):
                    if self.distance(node.children[i].points[ii], point) < min_distance:
                        min_distance = self.distance(node.children[i].points[ii], point)
                        path = [i, ii]
            for j in range(len(node.children[i].children)):
                if node.children[i].children[j].points:
                    for jj in range(len(node.children[i].children[j].points)):
                        if self.distance(node.children[i].children[j].points[jj], point) < min_distance:
                            min_distance = self.distance(node.children[i].children[j].points[jj], point)
                            path = [i, j, jj]
                for k in range(len(node.children[i].children[j].children)):
                    if node.children[i].children[j].children[k].points:
                        for kk in range(len(node.children[i].children[j].children[k].points)):
                            if self.distance(node.children[i].children[j].children[k].points[kk], point) < min_distance:
                                min_distance = self.distance(node.children[i].children[j].children[k].points[kk], point)
                                path = [i, j, k, kk]
        if len(path) == 2:
            node.children[path[0]].points[path[1]].red = True
            node.children[path[0]].points[path[1]].attributes = point.attributes
            return True
        elif len(path) == 3:
            node.children[path[0]].children[path[1]].points[path[2]].red = True
            node.children[path[0]].children[path[1]].points[path[2]].attributes = point.attributes
            return True
        elif len(path) == 4:
            node.children[path[0]].children[path[1]].children[path[2]].points[path[3]].red = True
            node.children[path[0]].children[path[1]].children[path[2]].points[path[3]].attributes = point.attributes
            return True

    def find_with_dfs(self, node, point):
        if not (node.x_low_border <= point.x <= node.x_high_border and
                node.y_low_border <= point.y <= node.y_high_border):
            return None

        if node.children:
            for child in node.children:
                status = self.find_with_dfs(child, point)
                if status:
                    return status
        else:
            for elem in node.points:
                if elem.x == point.x and elem.y == point.y:
                    return elem.attributes
        return None


tree = QTree()
with open('../j/blue.geojson', 'r', encoding='utf-8') as file:
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

with open('red.geojson', 'r', encoding='utf-8') as file:
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

with open('../j/green.geojson', 'w', encoding='utf-8') as file:
    json.dump(green, file)
