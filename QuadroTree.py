class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, x_low_border, x_high_border, y_low_border, y_high_border):
        self.x_low_border = x_low_border
        self.x_high_border = x_high_border
        self.y_low_border = y_low_border
        self.y_high_border = y_high_border
        self.points = []
        self.children = []
        self.red = False

    def get_border(self):
        return [[self.x_low_border, self.x_high_border], [self.y_low_border, self.y_high_border]]


class QTree:
    def __init__(self, max_points=4):
        self.root = Node(-90, 90, -180, 180)
        self.root.children = [Node(-90, 0, 0, 180),
                              Node(0, 90, 0, 180),
                              Node(-90, 0, -180, 0),
                              Node(0, 90, -180, 0)]
        self.max_points = max_points

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
                print(' ' * (level + 2) + f'({point.x}, {point.y})')

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


tree = QTree()
test = open('test.txt', 'r')
array = list(str(*test).split(','))
for el in array:
    coords = list(el.split(' '))
    tree.insert(Point(float(coords[0]), float(coords[1])))
tree.clear_points_in_tree()
tree.output()
