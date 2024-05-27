# 24 вариант
# Создайте класс "Компьютер" с атрибутами "марка"  "процессор " и "Оперативная память"
# Напишите метод , который выводит информацию  о компьютере в формате
# "Марка:марка, Процессор: процессор, Оперативная память: оперативная память"

class Computer:
    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram

    def display_info(self):
        print(f"Марка: {self.brand}, Процессор: {self.processor}, Оперативная память: {self.ram}")


my_computer = Computer("HP", "Intel i5", "16GB")
my_computer.display_info()
