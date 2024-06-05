# 24 вариант
# Задание 3.
# Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
# оформленный согласно требованиям. Все задания выполняются c использованием модуля
# OS:
#  перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
# вложенных подкаталогов выводить не нужно.
#  перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
# test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
# Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
# файлов в папке test.
#  перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
# консоль. Использовать функцию basename () (os.path.basename()).
#  перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
# привязанной к нему программе. Использовать функцию os.startfile().
#  удалить файл test.txt
import os
# task 1
print(os.listdir('./PZ_11'))
# task 2
try:
    os.mkdir('./test')
    os.mkdir('./test/test1')
except:
    pass

# task 3
os.rename('./PZ_6/1.txt', './test/1.txt')
os.rename('./PZ_6/2.txt', './test/2.txt')
os.rename('./PZ_7/3.txt', './test/test1/4.txt')

# task 4
path = os.listdir('./test')
for i in path:
    print((os.path.getsize(f'./test/{i}')), 'bytes')

# task 5
path = os.listdir('./PZ_11')
path = min(path, key=len)

print(os.path.basename(f'./PZ_11/{path}'))

# task 6

os.startfile('Reports\Report_17.pdf')

# task 7
open('PZ_17/123.txt', 'w')
os.remove('PZ_17/123.txt')