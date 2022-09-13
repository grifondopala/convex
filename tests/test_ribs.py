from r2point import R2Point
from convex import Void


class TestRibs:

    def setup_method(self):
        self.trianglePoints = []
        self.trianglePoints.append(R2Point(-3, 1))
        self.trianglePoints.append(R2Point(0, 4))
        self.trianglePoints.append(R2Point(3, 1))

    # Точка лежит внутри треугольника
    def test_1(self):
        assert R2Point(0, 2).is_in_triangle(self.trianglePoints) is True

    # Точка лежит вне треугольника
    def test_2(self):
        assert R2Point(0, -2).is_in_triangle(self.trianglePoints) is False

    # Точка лежит на стороне треугольника
    def test_3(self):
        assert R2Point(0, 1).is_in_triangle(self.trianglePoints) is False

    # Количество ребер точки, внутри треугольника - 0
    def test_4(self):
        f = Void(self.trianglePoints).add(R2Point(0.5, 2))
        assert f.countRibs() == 0

    # Отрезок внутри треугольника
    def test_5(self):
        f = Void(self.trianglePoints).add(R2Point(0.5, 2)).add(R2Point(1, 2))
        assert f.countRibs() == 1

    # Отрезок полностью вне треугольника
    def test_6(self):
        f = Void(self.trianglePoints).add(R2Point(0, -2)).add(R2Point(0, -3))
        assert f.countRibs() == 0

    # Отрезок частично в треугольнике
    def test_6(self):
        f = Void(self.trianglePoints).add(R2Point(0, -2)).add(R2Point(0, 2))
        assert f.countRibs() == 0

    # Треугольник, полностью лежащий внутри
    def test_7(self):
        f = Void(self.trianglePoints).add(R2Point(-2, 1.5)).add(
            R2Point(2, 1.5)).add(R2Point(0, 2.5))
        assert f.countRibs() == 3

    # Добавим к треугольнику точку, лежащую вне заданного треугольника
    def test_8(self):
        f = Void(self.trianglePoints).add(R2Point(-2, 1.5)).add(
            R2Point(2, 1.5)).add(R2Point(0, 2.5)).add(R2Point(0, -1))
        assert f.countRibs() == 2

    # Квадрат вне треугольника
    def test_9(self):
        f = Void(self.trianglePoints).add(R2Point(-4, -1)).add(
            R2Point(-4, 5)).add(R2Point(4, 5)).add(R2Point(4, -1))
        assert f.countRibs() == 0
