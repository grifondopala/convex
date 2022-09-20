#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon


def void_draw(self, tk):
    pass


def point_draw(self, tk, trianglePoints):
    tk.draw_point(self.p)


def segment_draw(self, tk, trianglePoints):
    a = Segment(self.p, self.q, trianglePoints)
    color = "red" if a.countRibs() == 1 else "black"
    tk.draw_line(self.p, self.q, color)


def polygon_draw(self, tk, trianglePoints):
    for n in range(self.points.size()):
        a = Segment(self.points.last(), self.points.first(), trianglePoints)
        color = "red" if a.countRibs() == 1 else "black"
        tk.draw_line(self.points.last(), self.points.first(), color)
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)


tk = TkDrawer()
f = Void()
tk.clean()

try:
    trianglePoints = []
    print('Введите вершины треугольника')
    for i in range(3):
        print(f'{i + 1}-я точка треугольника')
        trianglePoints.append(R2Point())
    f = Void(trianglePoints)
    print('Точки выпуклой оболочки')
    while True:
        f = f.add(R2Point())
        tk.clean()
        tk.create_polygon(trianglePoints[0], trianglePoints[1],
                          trianglePoints[2])
        f.draw(tk, trianglePoints)
        print(f"S = {f.area()}, P = {f.perimeter()}\n")
        print(f"Количество ребер, лежащих в треугольнике: {f.countRibs()}")
except(EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
