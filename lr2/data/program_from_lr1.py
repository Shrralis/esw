# coding=UTF-8

from tkinter import *
from tkinter import filedialog


def calculate():
    info = []
    fldlg = filedialog.askopenfilename()
    f = open(fldlg, 'r')
    array = [row.split('#')[0].strip() for row in f]
    f.close()
    q = float(array[0])
    C = float(array[1])
    Tpo = float(array[2])
    K = float(array[3])
    Td = float(array[4])

    Q = abs(q * C)
    info.append(Q)
    f2 = open('results.txt', 'a')
    f2.write("Кількість команд вихідного коду = " + str('%d' % Q) + " (команд)")

    nTBK = Q / 1000
    info.append(nTBK)
    t = 3.6 * pow(nTBK, 1.2)
    f2.write("\n" + "Трудомісткість = " + str('%d' % t) + " (люд.-міс.)")

    T = 2.5 * pow(t, 0.32)

    PL = t / T
    info.append(PL)
    f2.write("\n" + "Середня кількість виконавців = " + str('%.3f' % PL) + " (людей)")

    Pp = abs((1000 * nTBK) / t)
    info.append(Pp)
    f2.write("\n" + "Продуктивність праці = " + str('%.2f' % Pp) + " (вих.ком./люд.-міс.)")

    To = (Q * 1.2) / (50 * K)
    Ta = Q / (50 * K)
    Th = (Q * 1.5) / (50 * K)
    Tht = (Q * 4.2) / (50 * K)
    Tzag = Tpo + To + Ta + Th + Tht + Td
    info.append(Tzag)
    f2.write("\n" + "Час потрібний для створення програмного продукту = " + str('%.2f' % Tzag) + " (міс.)")
    f2.close()

    fldlg = filedialog.askopenfilename()
    f = open(fldlg, 'r')
    array = [row.split('#')[0].strip() for row in f]
    f.close()
    Kt = float(array[0])
    Trd = float(array[1])
    P = float(array[2])
    D = float(array[3])
    Z = float(array[4])
    Peom = float(array[5])
    Pocb = float(array[6])
    Bb = float(array[7])
    Np = float(array[8])

    ZPosn = ((1600 * Kt * Tzag) / (22 * Trd)) * (1 + (P / 1))
    info.append(ZPosn)
    f2 = open('results.txt', 'a')
    f2.write("\n" + "Основна заробітня платня = " + str('%.2f' % ZPosn) + " (грн.)")

    ZPdod = ZPosn * (D / 1)
    info.append(ZPdod)
    f2.write("\n" + "Додаткова заробітна плата = " + str('%.2f' % ZPdod) + " (грн.)")

    Zzag = ZPosn + ZPdod

    Becb = (Zzag * 0.347) / 1

    # Витрати на електроенергію
    Bpk = 2112 * Z * Peom
    Bocb = 2112 * Z * Pocb
    Beh = Bpk + Bocb

    # Витрати на витратні матеріали
    Bm = Bb * 0.02

    # Витрати на профілактику
    Bprof = Bb * 0.03

    # Амортизаційні відрахування
    A = Bb / Np

    # Витрати на оплату праці
    ZPobsl_osn = ((1600 * Kt) / 1) * (1 + (P / 1)) * 12
    ZPobsl_dod = ZPobsl_osn * (D / 1)
    Bobsl_ecb = ((ZPobsl_osn + ZPobsl_dod) * 0.347) / 1

    Bsum = Beh + Bm + Bprof + A + ZPobsl_osn + ZPobsl_dod + Bobsl_ecb

    C_m_god = Bsum / (2112 * 0.9)

    # Витрати на утримання та експлуатацію ПЕОМ
    Bpp = C_m_god * Tzag
    info.append(Bpp)
    f2.write("\n" + "Витрати на утримання та експлуатацію ПЕОМ = " + str('%.2f' % Bpp) + " (грн.)")

    # Собівартість
    Cpp = ZPosn + ZPobsl_dod + Becb + Bpp
    info.append(Cpp)
    f2.write("\n" + "Собівартість програмного продукту = " + str('%.2f' % Cpp) + " (грн.)")

    # Ціна
    Price = Cpp * (1 + (0.4 / 1))
    info.append(Price)
    f2.write("\n" + "Вартість готового програмного продукту = " + str('%.2f' % Price) + " (грн.)")
    f2.close()
    show_ui_results(info)


def show_ui_results(info):
    global txt
    txt.delete('1.0', END)
    txt.insert(END, "Кількість команд вихідного коду = " + str('%d' % info[0]) + " (команд)\n"
                                                                                 "\n" + "Трудомісткість = " + str(
        '%d' % info[1]) + " (люд.-міс.)"
                          "\n" + "Середня кількість виконавців = " + str('%.3f' % info[2]) + " (людей)"
                                                                                             "\n" + "Продуктивність праці = " + str(
        '%.2f' % info[3]) + " (вих.ком./люд.-міс.)"
                            "\n" + "Час потрібний для створення програмного продукту = " + str(
        '%.2f' % info[4]) + " (міс.)"
                            "\n" + "Основна заробітня платня = " + str('%.2f' % info[5]) + " (грн.)"
                                                                                           "\n" + "Додаткова заробітна плата = " + str(
        '%.2f' % info[6]) + " (грн.)"
                            "\n" + "Витрати на утримання та експлуатацію ПЕОМ = " + str('%.2f' % info[7]) + " (грн.)"
                                                                                                            "\n" + "Собівартість програмного продукту = " + str(
        '%.2f' % info[8]) + " (грн.)"
                            "\n" + "Вартість готового програмного продукту = " + str('%.2f' % info[9]) + " (грн.)")


global txt

root = Tk()
root.title("Лабораторна робота 1")
root.geometry("500x250")
txt = Text(root, height=13, padx=4, pady=4)
txt.pack(side=TOP)
btn = Button(text="Порахувати", pady="8", command=calculate).pack(side=BOTTOM)
root.mainloop()
