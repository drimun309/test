#task2
import os
import math

# Путь к файлам (в той же папке)
circle_path = "circle.txt"
points_path = "points.txt"

# Читаем параметры окружности
with open(circle_path, 'r') as file:
    x0, y0 = map(float, file.readline().split())
    radius = float(file.readline())

# Читаем и обрабатываем точки
with open(points_path, 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    if not line:
        continue

    x, y = map(float, line.split())
    dx = x - x0
    dy = y - y0
    distance = math.sqrt(dx**2 + dy**2)

    if math.isclose(distance, radius):
        print(0)
    elif distance < radius:
        print(1)
    else:
        print(2)
