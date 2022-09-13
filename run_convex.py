#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void, Segment


try:
    trianglePoints = []
    print('Введите вершины треугольника')
    for i in range(3):
        print(f'{i+1}-я точка треугольника')
        trianglePoints.append(R2Point())
    f = Void(trianglePoints)
    print('Точки выпуклой оболочки')
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}")
        print(f.countRibs())
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
