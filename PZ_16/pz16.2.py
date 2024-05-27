# 24
# Создайте класс "Человек" который содержит информацию о имени, возрасте и поле.
# Создайте классы "Мужчина " и "Женщина" которые наследуются от класса "Человек" .
#  Каждый класс должен иметь метод , который выводит информацию о поле субъекта.

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_gender(self):
        print(f"The person's gender is {self.gender}")


class Man(Person):
    def __init__(self, name, age):
        super().__init__(name, age, "Male")

    def display_gender(self):
        print(f"The man's gender is {self.gender}")


class Woman(Person):
    def __init__(self, name, age):
        super().__init__(name, age, "Female")

    def display_gender(self):
        print(f"The woman's gender is {self.gender}")


john = Man("John", 30)
jane = Woman("Jane", 25)

john.display_gender()
jane.display_gender()
