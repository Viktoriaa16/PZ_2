# 24 вариант
# составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры
# число символов
def print_string_with_length():
    length = int(input("Введите число символов: "))
    string = "*" * length  # создаем строку, содержащую нужное количество символов
    print(string)

print_string_with_length()