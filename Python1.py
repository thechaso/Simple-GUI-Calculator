from tkinter import *
from math import *
import math

root = Tk()
root.title("Simple_Calculator@Chaso")
# Input
e = Entry(root, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)


def click(fnum):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(fnum))


def clear():
    e.delete(0, END)


def add():
    global op
    op = "addition"
    global num1
    num1 = int(e.get())
    e.delete(0, END)


def subtract():
    global op
    op = "subtraction"
    global num1
    num1 = int(e.get())
    e.delete(0, END)


def multiply():
    global op
    op = "multiplication"
    global num1
    num1 = int(e.get())
    e.delete(0, END)


def divide():
    global op
    op = "division"
    global num1
    num1 = int(e.get())
    e.delete(0, END)


def mod():
    global op
    op = "mod"
    global num1
    num1 = int(e.get())
    e.delete(0, END)


def exponent():
    global op
    op = "exponent"
    global num1
    num1 = int(e.get())
    e.delete(0, END)


def choose():
    global op
    op = "choose"
    global num1
    num1 = int(e.get())
    e.delete(0, END)


def log():
    global op
    op = "log"
    global num1
    num1 = int(e.get())
    e.delete(0, END)


def equal():
    num2 = int(e.get())
    e.delete(0, END)
    if op == "addition":
        e.insert(0, str(num1 + num2))
    if op == "subtraction":
        e.insert(0, str(num1 - num2))
    if op == "multiplication":
        e.insert(0, str(num1 * num2))
    if op == "division":
        e.insert(0, str(num1 / num2))
    if op == "mod":
        e.insert(0, str(num1 % num2))
    if op == "exponent":
        e.insert(0, str(num1 ** num2))
    if op == "choose":
        e.insert(0, str(int(factorial(num1) / (factorial(num1 - num2) * factorial(num2)))))
    if op == "log":
        e.insert(0, str(math.log(num1, num2)))


button_clear = Button(root, text="AC", command=clear, padx=20)
button_log = Button(root, text="log", command=log, padx=20)
button_mod = Button(root, text="mod", command=mod, padx=20)
button_divide = Button(root, text="/", command=divide, padx=20)
button_seven = Button(root, text="7", command=lambda: click(7), padx=20)
button_eight = Button(root, text="8", command=lambda: click(8), padx=20)
button_nine = Button(root, text="9", command=lambda: click(9), padx=20)
button_multiply = Button(root, text="x", command=multiply, padx=20)
button_four = Button(root, text="4", command=lambda: click(4), padx=20)
button_five = Button(root, text="5", command=lambda: click(5), padx=20)
button_six = Button(root, text="6", command=lambda: click(6), padx=20)
button_subtract = Button(root, text="-", command=subtract, padx=20)
button_one = Button(root, text="1", command=lambda: click(1), padx=20)
button_two = Button(root, text="2", command=lambda: click(2), padx=20)
button_three = Button(root, text="3", command=lambda: click(3), padx=20)
button_add = Button(root, text="+", command=add, padx=20)
button_zero = Button(root, text="0", command=lambda: click(0), padx=20)
button_exponent = Button(root, text="^", command=exponent, padx=20)
button_choose = Button(root, text="C", command=choose, padx=20)
button_equal = Button(root, text="=", command=equal, padx=20)

button_clear.grid(row=1, column=0)
button_log.grid(row=1, column=1)
button_mod.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_seven.grid(row=2, column=0)
button_eight.grid(row=2, column=1)
button_nine.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_four.grid(row=3, column=0)
button_five.grid(row=3, column=1)
button_six.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_one.grid(row=4, column=0)
button_two.grid(row=4, column=1)
button_three.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_zero.grid(row=5, column=0)
button_exponent.grid(row=5, column=1)
button_choose.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

root.mainloop()
