class Triangle:
    def __init__(self, obj_id, point1, point2, point3):
        self.id = obj_id
        self.points = [point1, point2, point3]

    def move(self, dx, dy):
        """Перемещает треугольник на dx по x и dy по y"""
        self.points = [(x + dx, y + dy) for x, y in self.points]

    def area(self):
        """Вычисляет площадь треугольника по координатам вершин"""
        (x1, y1), (x2, y2), (x3, y3) = self.points
        return abs(0.5 * ((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)))

class Rectangle:
    def __init__(self, obj_id, x, y, width, height):
        self.id = obj_id
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, dx, dy):
        """Перемещает прямоугольник на dx по x и dy по y"""
        self.x += dx
        self.y += dy

    def area(self):
        """Вычисляет площадь прямоугольника"""
        return self.width * self.height

def compare(t1, t2):
    """Сравнивает площади двух фигур и возвращает результат"""
    area1 = t1.area()
    area2 = t2.area()
    if area1 > area2:
        return f"{t1.id} больше {t2.id}"
    elif area1 < area2:
        return f"{t1.id} меньше {t2.id}"
    else:
        return "Фигуры равны по площади"

# Демонстрация работы
# Создаем объекты
triangle = Triangle("T1", (0, 0), (2, 0), (0, 2))
rectangle = Rectangle("R1", 1, 1, 3, 2)

print(f"Площадь треугольника {triangle.id}: {triangle.area():.1f}")
print(f"Площадь прямоугольника {rectangle.id}: {rectangle.area()}")

# Перемещаем фигуры
triangle.move(1, 1)
rectangle.move(-1, 0)

print("\nПосле перемещения:")
print(f"Координаты треугольника: {triangle.points}")
print(f"Координаты прямоугольника: ({rectangle.x}, {rectangle.y})")

# Сравниваем площади
print("\nСравнение площадей:")
print(compare(triangle, rectangle))