# 24 вариант
# Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16' ,
# отражающая продажи продукции по дням в кг.
# Преобразить информацию из строки в словари , с использованием функции найти
# минимальные продажи по каждому виду продукции, результаты вывести на экран

def convert_string_to_dict(data_string):
    data_list = data_string.split()
    sales_dict = {}
    current_key = ''
    current_values = []

    for item in data_list:
        if item.isnumeric():
            current_values.append(int(item))
        else:
            if current_key != '':
                sales_dict[current_key] = current_values
                current_key = item
                current_values = []
            else:
                current_key = item

    sales_dict[current_key] = current_values
    return sales_dict


def find_minimum_sales(sales_dict):
    result = {}
    for key, values in sales_dict.items():
        result[key] = min(values)
    return result


data_string = 'груши 45 991 63 100 12 морковь 13 47 26 0 16'
sales_dict = convert_string_to_dict(data_string)
min_sales = find_minimum_sales(sales_dict)
print(min_sales)

Результат:{'груши': 12, 'морковь': 0}