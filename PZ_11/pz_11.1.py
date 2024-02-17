import random


def generate_data_and_write_to_files():
    data1 = [random.randint(-100, 100) for _ in range(10)]
    data2 = [random.randint(-100, 100) for _ in range(10)]

    with open('file1.txt', 'w', encoding='utf-8') as file1:
        for num in data1: \
    file1.write(str(num) + '\n')

    with open('file2.txt', 'w', encoding='utf-8') as file2:
        for num in data2: \
        file2.write(str(num) + '\n')


def process_data_and_write_output():
    with open('file1.txt', 'r') as file1, open('file2.txt', 'r', encoding='utf-8') as file2, open('output.txt', 'w', encoding='utf-8') as output:
        data1 = [int(line.strip()) for line in file1.readlines()]
        data2 = [int(line.strip()) for line in file2.readlines()]

        data1_mul = 1
        data1_min = min(data1) if len(data1) > 0 else None

        output.write('Содержимое первого файла:\n')
        output.write('Элементы кратные 3:\n')
        for num in data1:
            if num % 3 == 0:
                output.write(str(num) + '\n')
                data1_mul *= num

        output.write('Произведение элементов:\n')
        output.write(str(data1_mul) + '\n')

        output.write('Минимальный элемент:\n')
        output.write(str(data1_min) + '\n')

        data2_count = 0
        data2_sum = 0
        data2_avg = 0

        output.write('\nСодержимое второго файла:\n')
        output.write('Элементы кратные 5:\n')
        for num in data2:
            if num % 5 == 0:
                output.write(str(num) + '\n')
                data2_count += 1
                data2_sum += num

        output.write('Количество элементов:\n')
        output.write(str(data2_count) + '\n')

        output.write('Среднее арифметическое элементов:\n')
        if data2_count > 0:
            data2_avg = data2_sum / data2_count
        output.write(str(data2_avg) + '\n')


# Генерация данных и запись в файлы
generate_data_and_write_to_files()

# Обработка данных и запись результатов в output.txt
process_data_and_write_output()
