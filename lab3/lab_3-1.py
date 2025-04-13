class InvalidShapeError(Exception):
    """Исключение для некорректных фигур."""
    pass

class Triangle:
    def __init__(self, obj_id, point1, point2, point3):
        self.id = obj_id
        self.points = [self._validate_point(p) for p in (point1, point2, point3)]
        if self._is_degenerate():
            raise InvalidShapeError(f"Треугольник {self.id} вырожден (точки лежат на одной линии)")

    def _validate_point(self, point):
        if not (isinstance(point, tuple) and len(point) == 2 and all(isinstance(c, (int, float)) for c in point)):
            raise ValueError(f"Некорректные координаты точки: {point}")
        return point

    def _is_degenerate(self):
        (x1, y1), (x2, y2), (x3, y3) = self.points
        return (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1)

    def move(self, dx, dy):
        self.points = [(x + dx, y + dy) for x, y in self.points]

    def area(self):
        (x1, y1), (x2, y2), (x3, y3) = self.points
        return abs(0.5 * ((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)))


class Rectangle:
    def __init__(self, obj_id, x, y, width, height):
        self.id = obj_id
        self.x, self.y = self._validate_point((x, y))
        self.width, self.height = self._validate_size(width, height)

    def _validate_point(self, point):
        if not (isinstance(point, tuple) and len(point) == 2 and all(isinstance(c, (int, float)) for c in point)):
            raise ValueError(f"Некорректные координаты точки: {point}")
        return point

    def _validate_size(self, width, height):
        if not all(isinstance(v, (int, float)) and v > 0 for v in (width, height)):
            raise ValueError(f"Ширина и высота должны быть положительными числами: {width}, {height}")
        return width, height

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def area(self):
        return self.width * self.height


def compare(shape1, shape2):
    if not all(isinstance(shape, (Triangle, Rectangle)) for shape in (shape1, shape2)):
        raise TypeError("Оба объекта должны быть фигурами (Triangle или Rectangle)")

    area1, area2 = shape1.area(), shape2.area()
    if area1 > area2:
        return f"{shape1.id} больше {shape2.id}"
    elif area1 < area2:
        return f"{shape1.id} меньше {shape2.id}"
    return "Фигуры равны по площади"


try:
    triangle = Triangle("T1", (0, 0), (2, 0), (0, 2))
    rectangle = Rectangle("R1", 1, 1, 3, 2)

    print(f"Площадь треугольника {triangle.id}: {triangle.area():.1f}")
    print(f"Площадь прямоугольника {rectangle.id}: {rectangle.area()}")

    triangle.move(1, 1)
    rectangle.move(-1, 0)

    print("\nПосле перемещения:")
    print(f"Координаты треугольника: {triangle.points}")
    print(f"Координаты прямоугольника: ({rectangle.x}, {rectangle.y})")

    print("\nСравнение площадей:")
    print(compare(triangle, rectangle))
except (ValueError, InvalidShapeError, TypeError) as e:
    print(f"Ошибка: {e}")
