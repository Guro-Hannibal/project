from tkinter import *



root = Tk()
root.title("2.24")

root.geometry("1200x1200")



def submit():
    atr_first.delete(0, END)
    atr_sec.delete(0, END)
    atr_third.delete(0, END)
    atr_forth.delete(0, END)


atr_first = Entry(root, width=50)
atr_first.grid(row=3, column=1)
atr_sec = Entry(root, width=50)
atr_sec.grid(row=8, column=1)
atr_third = Entry(root, width=50)
atr_third.grid(row=13, column=1)
atr_forth = Entry(root, width=50)
atr_forth.grid(row=18, column=1)


atr_f1 = Label(root, text='Come to me')
atr_f1.grid(row=0, column=1)
atr_f3 = Label(root, text='Be initiative already')
atr_f3.grid(row=5, column=1)
atr_f6 = Label(root, text='Note to myself, need more sex')
atr_f6.grid(row=10, column=1)
atr_fo7 = Label(root, text='and finish this project')
atr_fo7.grid(row=15, column=1)


var_first = Entry(root, width=50)
var_first.grid(row=3, column=24)
var_sec = Entry(root, width=50)
var_sec.grid(row=8, column=24)
var_third = Entry(root, width=50)
var_third.grid(row=13, column=24)
var_forth = Entry(root, width=50)
var_forth.grid(row=18, column=24)


var_f1 = Label(root, text='Come to me')
var_f1.grid(row=0, column=24)
var_f3 = Label(root, text='Be initiative already')
var_f3.grid(row=5, column=24)
var_f6 = Label(root, text='Note to myself, need more sex')
var_f6.grid(row=10, column=24)
var_fo7 = Label(root, text='and finish this project')
var_fo7.grid(row=15, column=24)


arg_first = Entry(root, width=50)
arg_first.grid(row=3, column=12)
arg_sec = Entry(root, width=50)
arg_sec.grid(row=8, column=12)
arg_third = Entry(root, width=50)
arg_third.grid(row=13, column=12)
arg_forth = Entry(root, width=50)
arg_forth.grid(row=18, column=12)


arg_f1 = Label(root, text='Come to me')
arg_f1.grid(row=0, column=12)
arg_f3 = Label(root, text='Be initiative already')
arg_f3.grid(row=5, column=12)
arg_f6 = Label(root, text='Note to myself, need more sex')
arg_f6.grid(row=10, column=12)
arg_fo7 = Label(root, text='and finish this project')
arg_fo7.grid(row=15, column=12)

el_first = Entry(root, width=50)
el_first.grid(row=42, column=11)
el_sec = Entry(root, width=50)
el_sec.grid(row=44, column=11)
el_third = Entry(root, width=50)
el_third.grid(row=46, column=11)
el_forth = Entry(root, width=50)
el_forth.grid(row=48, column=11)


el_f1 = Label(root, text='Come to me')
el_f1.grid(row=41, column=11)
el_f3 = Label(root, text='Be initiative already')
el_f3.grid(row=43, column=11)
el_f6 = Label(root, text='Note to myself, need more sex')
el_f6.grid(row=45, column=11)
el_fo7 = Label(root, text='and finish this project')
el_fo7.grid(row=47, column=11)


item_first = Entry(root, width=50)
item_first.grid(row=42, column=24)
item_sec = Entry(root, width=50)
item_sec.grid(row=44, column=24)
item_third = Entry(root, width=50)
item_third.grid(row=46, column=24)
item_forth = Entry(root, width=50)
item_forth.grid(row=48, column=24)


item_f1 = Label(root, text='Come to me')
item_f1.grid(row=41, column=24)
item_f3 = Label(root, text='Be initiative already')
item_f3.grid(row=43, column=24)
item_f6 = Label(root, text='Note to myself, need more sex')
item_f6.grid(row=45, column=24)
item_fo7 = Label(root, text='and finish this project')
item_fo7.grid(row=47, column=24)


send = Button(root, text='send more data, even more data!')
send.grid(row=420, column=1, columnspan=100, pady=420, padx=1, ipadx=1)

root.mainloop()
