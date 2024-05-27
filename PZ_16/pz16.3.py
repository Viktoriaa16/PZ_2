# 24
# Для задачи из блока 1 (Создайте класс "Компьютер" с атрибутами "марка"  "процессор " и "Оперативная память"
# Напишите метод , который выводит информацию  о компьютере в формате "Марка:марка,
# Процессор: процессор, Оперативная память: оперативная память") создать 2 функции ,
# save_def и load_def , которые позволяют сохранять информацию из экземпляров класса (3шт) в файл
# и загружать ее обратно. Использовать модуль pickle для сериализации и дессериализации объектов python
# в бинарном формате

import pickle


class Computer:
    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram

    def display_info(self):
        print(f"Марка: {self.brand}, Процессор: {self.processor}, Оперативная память: {self.ram}")


def save_def(computers):
    with open('computers.pkl', 'wb') as file:
        pickle.dump(computers, file)


def load_def():
    try:
        with open('computers.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


computer1 = Computer("Lenovo", "Intel Core i5", "8GB")
computer2 = Computer("HP", "Intel Core i5", "16GB")
computer3 = Computer("Dell", "Intel Core i7", "12GB")


computers_list = [computer1, computer2, computer3]
save_def(computers_list)


loaded_computers = load_def()


for computer in loaded_computers:
    computer.display_info()
