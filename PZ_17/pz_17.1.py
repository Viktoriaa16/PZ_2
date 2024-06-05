# 24 вариант
# . В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу

# Импорт библиотеки
from tkinter import *
import tkinter as tk

# Создание функции для очищения всех полей
def dele():
	entry1.delete(0, END)
	entry2.delete(0, END)
	entry3.delete(0, END)
	entry4.delete(0, END)
	entry5.delete(0, END)
	entry6.delete(0, END)
	entry7.delete(0, END)
	entry8.delete(0, END)
	entry9.delete(0, END)


# Создание главного окна
root = tk.Tk()
root.title("PZ_17")
root.geometry("850x700")
root.resizable(width=False, height=False)

# Создание текста
lbl1 = tk.Label(root, text="Certificate Self Service Portal", font=("Arial", 35))
lbl2 = tk.Label(root, text="Fill out form to get a certificate", font=("Arial", 17))

label1 = tk.Label(root, text="Requester", font=("Arial", 15))
label2 = tk.Label(root, text="Short Name", font=("Arial", 15))
label3 = tk.Label(root, text="Email", font=("Arial", 15))
label4 = tk.Label(root, text="Organization", font=("Arial", 15))
label5 = tk.Label(root, text="Country", font=("Arial", 15))
label6 = tk.Label(root, text="IPv4 Address", font=("Arial", 15))
label7 = tk.Label(root, text="Hostname", font=("Arial", 15))
label8 = tk.Label(root, text="FQND", font=("Arial", 15))
label9 = tk.Label(root, text="Description", font=("Arial", 15),justify="right")

# Создания кнопки
btn1 = Button(root, text="Submit Form", fg ="white" ,bg = "Blue",font=("Arial", 12), command = dele)
btn1.configure(borderwidth=7,
	highlightthickness=11, highlightcolor="Grey")

# Создание поля ввода
entry1 = tk.Entry(root, fg = "Grey", width=45)
entry2 = tk.Entry(root, fg = "Grey", width=45)
entry3 = tk.Entry(root, fg = "Grey", width=45)
entry4 = tk.Entry(root, fg = "Grey", width=45)
entry5 = tk.Entry(root, fg = "Grey", width=45)
entry6 = tk.Entry(root, fg = "Grey", width=45)
entry7 = tk.Entry(root, fg = "Grey", width=45)
entry8 = tk.Entry(root, fg = "Grey", width=45)
entry9 = tk.Entry(root, fg = "Grey", width=45)


# Создание надпись по умолчанию в поле ввода
entry1.insert(0, "firstname lastname")
entry2.insert(0, "asdf")
entry3.insert(0, "mail@mail.com")
entry4.insert(0, "Organization")
entry5.insert(0, "Austria")
entry6.insert(0, "127.0.0.1")
entry7.insert(0, "host")
entry8.insert(0, "host.domain.tld")
entry9.insert(0, "desc")

# Позиционирование элементов в окне
lbl1.place(x=0, y=0)

lbl2.place(x=10, y=60)

label1.place(x=170, y=95)
label2.place(x=158, y=145)
label3.place(x=212, y=195)
label4.place(x=150, y=245)
label5.place(x=190, y=295)
label6.place(x=140, y=345)
label7.place(x=170, y=395)
label8.place(x=200, y=445)
label9.place(x=155, y=495)

entry1.place(x=270, y=100)
entry2.place(x=270, y=150)
entry3.place(x=270, y=200)
entry4.place(x=270, y=250)
entry5.place(x=270, y=300)
entry6.place(x=270, y=350)
entry7.place(x=270, y=400)
entry8.place(x=270, y=450)
entry9.place(x=270, y=500)

btn1.place(x=270, y=550)

# Запуск главного цикла
root.mainloop()