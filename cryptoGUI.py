from tkinter import Tk, Label, Canvas, Button
from random import randint as rint
from math import fabs

root1 = Tk()
root1.geometry("530x420")
root1.resizable(False, False)


body = Canvas(root1, width=540, height=500, bg="#8090a0")
body.pack()


body.create_line(170, 0, 170, 270-10, fill="#0f0", width=5)
body.create_line(0, 53-10, 550, 53-10, fill="#0f0", width=5)
body.create_line(174+175, 0, 174+175, 270, fill="#0f0", width=5)
body.create_line(0, 160-10, 550, 160-10, fill="#0f0", width=5)
body.create_line(0, 160+110-10, 550, 160+110-10, fill="#0f0", width=5)
body.create_line(0, 270+43-5, 540, 270+43-5, fill="#0f0", width=5)#
body.create_line(349, 270, 349, 550, fill="#0f0", width=5)
body.create_line(0, 420-42, 540, 420-42, fill="#0f0", width=5)
body.create_line(170, 378, 170, 420, fill="#0f0", width=5)


def buy_bitc():
	print("Биткоин куплен")


def buy_ether():
	print("Эфир куплен")




currency_label = Label(text="Валюта", bg="#0f0", font="Areal 14")
currency_label.place(x=10, y=10)

price_label = Label(text="Цена", bg="#0f0", font="Areal 14")
price_label.place(x=185, y=10)

change_label = Label(text="Курс", bg="#0f0", font="Areal 14")
change_label.place(x=361, y=10)


bitc_label = Label(text="Биткоин", bg="#0f0", font="Areal 14")
bitc_label.place(x=10, y=55)

btn_buy_bitc = Button(root1, text="Купить", bg="#0f0", font="Areal 9")
btn_buy_bitc.bind("<Button-1>", lambda event: buy_bitc())
btn_buy_bitc.place(x=10, y=94)


ether_label = Label(text="Эфир", bg="#0f0", font="Areal 14")
ether_label.place(x=10, y=163)

btn_buy_ether = Button(root1, text="Купить", bg="#0f0", font="Areal 9")
btn_buy_ether.bind("<Button-1>", lambda event: buy_ether())
btn_buy_ether.place(x=10, y=202)


status_label = Label(text="Статус", bg="#0f0", font="Areal 14")
status_label.place(y=273, x=135)


cash_label = Label(text="Деньги:", bg="#0f0", font="Areal 14")
cash_label.place(x=10, y=388)


goal_label = Label(text="Цель:", bg="#0f0", font="Areal 14")
goal_label.place(x=182, y=388)

person_status_label = Label(text="Вы:", bg="#0f0", font="Areal 14")
person_status_label.place(x=361, y=388)

history_label = Label(text="История", bg="#0f0", font="Areal 14")
history_label.place(x=361, y=273)

root1.mainloop()