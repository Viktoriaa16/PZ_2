# 24 вариант
# составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры
# число символов
def print_python_string(num_characters):
    result = "^_^  " * num_characters
    print(result)

# Получаем ввод от пользователя
num = int(input("Введите число символов: "))

# Вызов функции для вывода строки
print_python_string(num)

