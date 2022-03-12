from random import randint
import tkinter


def init_nums(): # Функция для генерации нового выражения
    first_n.set(randint(1, 10))
    second_n.set(randint(1, 10))

    oper_n.set("+-"[randint(0, 1)])
    sv_answer.set("")


def scan_answer(n, s, b): #Функция для проверки ответа
    global count_success
    if sv_answer.get():
        if sv_answer.get()[-1] == "r":
            sv_answer.set("")
        elif sv_answer.get()[-1] == "-":
            sv_answer.set("-")
        elif not (sv_answer.get()[-1].isdigit()):
            sv_answer.set(sv_answer.get()[:-1])
        else:
            f, s, o, a = get_nums()
            if a == eval(f"{f} {o} {s}"):
                sv_count_success.set(int(sv_count_success.get()) + 1)
                init_nums()

    if int(sv_count_success.get()) == 10:
        exit()


def get_nums(): # Получить значения всех полей
    return int(first_n.get()), int(second_n.get()), oper_n.get(), float(sv_answer.get())


def btn_click(): # Функция, отвечающая на нажатие клавиши.
    f, s, o, a = get_nums()

    if eval(f"{f} {o} {s}") == a:
        init_nums()



root = tkinter.Tk()
root.geometry("400x200")


my_font = ("Times New Roman", 14) # Создаем свой шрифт

first_n = tkinter.StringVar()
second_n = tkinter.StringVar()
oper_n = tkinter.StringVar()
sv_answer = tkinter.StringVar()
sv_count_success = tkinter.StringVar(value="0")


lbl_success_count = tkinter.Label(root, font=("Times New Roman", 18), textvariable=sv_count_success)
lbl_num_first = tkinter.Label(root, font=my_font, textvariable=first_n)
lbl_oper = tkinter.Label(root, font=my_font, textvariable=oper_n)
lbl_num_second = tkinter.Label(root, font=my_font, textvariable=second_n)

sv_answer.trace_add("write", scan_answer)
answer_entry = tkinter.Entry(root, font=my_font, textvariable=sv_answer)


tkinter.Label(root, text="=", font=my_font).place(x=200, y=50)
lbl_success_count.place(x=50, y=10)
lbl_num_first.place(x=50, y=50)
lbl_oper.place(x=100, y=50)
lbl_num_second.place(x=150, y=50)
answer_entry.place(x=250, y=50, width=50)

btn_scan = tkinter.Button(root, text="Проверка ответа", command=btn_click)
btn_scan.place(x=150, y=100)

init_nums()

answer_entry.focus()

root.mainloop()
