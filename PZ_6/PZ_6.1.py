# вариант 24
# Дан список ненулевых целых чисел размера N .
# Проверить образуют ли его элементы геометрическую прогрессию.
# Если образуют, то вывести знаменатель прогрессии, если нет - вывести 0
def check_geometric_progression(arr):
    if len(arr) < 2:
        return 0

    ratio = arr[1] / arr[0]

    for i in range(1, len(arr)):
        if arr[i] / arr[i - 1] != ratio:
            return 0

    return ratio


# Пример :
arr = [2, 4, 8, 16, 32]
result = check_geometric_progression(arr)
if result:
    print(f"Элементы образуют геометрическую прогрессию с знаменателем {result}")
else:
    print("Элементы не образуют геометрическую прогрессию")
