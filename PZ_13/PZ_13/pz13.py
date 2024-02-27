# 24 вариант
# В матрице найти отрицательные элементы, сформировать из них новый массив.
# Вывести размер полученного массива.
# Для каждой строки матрицы с нечётным номером найти среднее арифметическое ее элементов

# Создаем матрицу с использованием библиотеки NumPy
import numpy as np

# Создание матрицы
matrix = np.array([[1, -2, 3],
                   [4, -5, 6],
                   [-7, 8, -9],
                   [10, 11, -12]])


negative_elements = matrix[matrix < 0]
print("Отрицательные элементы:", negative_elements)
print("Размер полученного массива:", negative_elements.size)


rows, cols = matrix.shape
for i in range(1, rows, 2):
    row_mean = np.mean(matrix[i])
    print(f"Среднее арифметическое элементов в строке {i}: {row_mean}")