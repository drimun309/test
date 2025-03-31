#task1
import sys

# Ввод данных  вместе с запуском основного файла
n = sys.argv[1]  
m = sys.argv[2]   

#создаем пустой список для пути и задаем начальный индекс
path = []            
start_index = 0  

while True:
    #доблавление в path начальных элементов полученных интервалов. 
    path.append(start_index + 1)
    
    # Вычисляем индекс последнего элемента текущего интервала:
    last_index = (start_index + m - 1) % n
    start_index = last_index
    
    # Если новый старт равен индексу 0, значит мы вернулись к  числу 1, то брейк
    if start_index == 0:
        break

print("Путь:", path)