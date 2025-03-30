#task2
import math

# Указываем путь к файлам с данными окружности и точек
circle_path = "circle.txt"  
points_path = "points.txt"  

# Читаем координаты центра окружности и радиус из файла circle.txt
with open(circle_path, 'r') as f:
    x0, y0 = map(float, f.readline().split())
    radius = float(f.readline())

# Читаем координаты точек из файла points.txt
with open(points_path, 'r') as f:
    lines = f.readlines()  

# Перебираем каждую точку из списка
for line in lines:
    line = line.strip()  # убираем лишние пробелы и переносы строк
    if not line:         # если строка пустая, пропускаем её
        continue

    # Получаем координаты текущей точки (x, y)
    x, y = map(float, line.split())

    # Вычисляем расстояние от текущей точки до центра окружности
    dx = x - x0
    dy = y - y0
    distance = math.sqrt(dx**2 + dy**2)

    # Определяем положение точки относительно окружности:
    if math.isclose(distance, radius):  # если точка лежит точно на окружности
        print(0)
    elif distance < radius:             # если точка находится внутри окружности
        print(1)
    else:                               # если точка находится снаружи окружности
        print(2)

