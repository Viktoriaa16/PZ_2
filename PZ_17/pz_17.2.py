# 24 вариант
# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 2 – 9.
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("PZ")
root.geometry("300x250")
root.resizable(width=False, height=False)


def check_palindrome():
    num = int(entry.get())

    a1 = num // 1000 % 10
    a2 = (num // 100) % 10
    a3 = (num // 10) % 10
    a4 = num % 10

    if a1 == a4 and a2 == a3:
        result_label.config(text="Число читается слева направо")
    else:
        result_label.config(text="Число не читается слева направо")


entry = tk.Entry(root, width=20)

result_label = tk.Label(root, text="", font=("Arial", 12))

check_button = tk.Button(root, text="Проверить", fg="white", bg="Blue", font=("Arial", 12), command=check_palindrome)

lbl1 = tk.Label(root, text="Введите четырёхзначное число:", font=("Arial", 12))

result_label.place(x=10, y=140)
entry.place(x=80, y=40)
check_button.place(x=95, y=75)
lbl1.place(x=41, y=0)

root.mainloop()