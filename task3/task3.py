#task3
import json
import sys

values = sys.argv[1]
tests = sys.argv[2]

with open(values, "r") as f:
    values_d = json.load(f)

with open(tests, "r") as f:
    test_d = json.load(f)


# Создаем словарь, где каждому id соответствует его значение 
value_data = {item['id']: item['value'] for item in values_d['values']}

# Функция рекурсивно проходит по списку тестов и заполняет значения из value_data
def fill_values(tests_list, value_data):
    for test in tests_list:
        test_id = test.get("id")

        if test_id in value_data:
            test["value"] = value_data[test_id]

        # Если у текущего теста есть вложенные тесты, запускаем функцию снова для них (рекурсия)
        if "values" in test:
            fill_values(test["values"], value_data)

fill_values(test_d["tests"], value_data)

#Сохраняем обновленные данные в новый файл report.json
with open("report.json", "w") as f:
    json.dump(test_d, f, indent=2)
