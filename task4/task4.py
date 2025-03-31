#task4
import sys

file_name = sys.argv[1]

with open(file_name, 'r') as f:
    nums = [int(line.strip()) for line in f]

# Сортируем числа, чтобы легко найти медиану
nums_sorted = sorted(nums)

# Если элементов нечётное количество
if len(nums_sorted) % 2 == 1:
    median = nums_sorted[len(nums_sorted) // 2]

# Если элементов чётное количество
else:
    median1 = nums_sorted[len(nums_sorted) // 2 - 1]  
    median2 = nums_sorted[len(nums_sorted) // 2]      

    # считаем количество ходов для каждой медианы
    moves1 = sum(abs(num - median1) for num in nums_sorted)
    moves2 = sum(abs(num - median2) for num in nums_sorted)

    # выбираем медиану с минимальным количеством ходов
    median = median1 if moves1 <= moves2 else median2

# cчитаем общее количество ходов
moves = sum(abs(num - median) for num in nums_sorted)

print(moves)
