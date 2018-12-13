from tkinter import *
from tkinter import filedialog


def calculate():
    info = []
    fldlg = filedialog.askopenfilename()
    empty = 0
    commentary = 0
    text = len(open(fldlg, 'r').readlines())
    info.append(text)
    print("Загальна кількість рядків: ", text)

    for y in open(fldlg, 'r').readlines():
        if y == "#":
            commentary += 1

    for x in open(fldlg, 'r').readlines():
        if x == "\n":
            empty += 1

    text = text - (commentary + empty)
    info.append(text)
    print("Кількість рядків коду: ", text)

    f2 = open('commentaries.txt', 'w')
    for i in open(fldlg, "r").readlines():
        if "#" in i:
            f2.write(i)
    show_ui_results(info)


def show_ui_results(info):
    global txt
    txt.delete('1.0', END)
    txt.insert(END, "Загальна кількість рядків: " + str('%d' % info[0])
               + "\n" + "Кількість рядків коду: " + str('%d' % info[1]))


global txt

root = Tk()
root.title("Лабораторна робота 2")
root.geometry("500x250")
txt = Text(root, height=13, padx=4, pady=4)
txt.pack(side=TOP)
btn = Button(text="Порахувати", pady="8", command=calculate).pack(side=BOTTOM)
root.mainloop()
