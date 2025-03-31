#task2
import sys
import math

circle_path = sys.argv[1]
points_path = sys.argv[2]

# Читаем параметры окружности
with open(circle_path, 'r') as f:
    x0, y0 = map(float, f.readline().split())
    radius = float(f.readline())

# Читаем и обрабатываем точки
with open(points_path, 'r') as f:
    lines = f.readlines()

# Перебираем каждую точку из списка
for line in lines:
    line = line.strip()  
    if not line:         
        continue
# Вычисляем расстояние от текущей точки до центра окружности
    x, y = map(float, line.split())

# вычисляем расстояние от текущей точки до центра окружности
    dx = x - x0
    dy = y - y0
    distance = math.sqrt(dx**2 + dy**2)
# Определяем положение точки относительно окружности:
    if math.isclose(distance, radius):
        print(0)
    elif distance < radius:             # если точка находится внутри окружности
        print(1)
    else:                               # если точка находится снаружи окружности
        print(2)

