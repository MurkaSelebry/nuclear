'''def _find_nearest_point(self, node, point):
     # Инициализация переменных для хранения ближайшей точки и минимальной дистанции



     # Функция для расчета евклидовой дистанции


     # Обход детей родителя
     for child in node.children:
         # Обход точек в каждом дочернем узле
         print(child.points)
         for child_point in child.points:

             dist = distance(point, child_point)
             #print(dist)
             if dist < min_distance:
                 min_distance = dist
                 nearest_point = child_point

     """
     # Проверка, нет ли среди детей 2-го родителя точек, которые ближе
     if node.parent and node.parent.parent:
         for grandchild in node.parent.parent.children:
             for grandchild_point in grandchild.points:
                 dist = distance(point, grandchild_point)
                 if dist < min_distance:
                     min_distance = dist
                     nearest_point = grandchild_point
     """

     return nearest_point



def dfs(self, nod, point):
    nearest_point = None
    min_distance = float('inf')
    if nod.points:
        for i in nod.points:
            dist = self.distance(point, i)
            # print(dist)
            if dist < min_distance:
                min_distance = dist
                nearest_point = i
        return nearest_point
    for i in nod.children:
        if i.x_low_border <= point.x <= i.x_high_border and i.y_low_border <= point.y <= i.y_high_border:
            self.dfs(i, point)

'''