from tkinter import *

root = Tk()
root.title("GIVE ME MORE LOVE")

root.geometry("600x600")


def foo(console):

    print(console.insert_into_table('services', console.inner,
                                    [atr_first.get(), atr_sec.get(), atr_third.get(), atr_forth.get()]))


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


send = Button(root, text='send more data, even more data!')
send.grid(row=60, column=60, columnspan=60, pady=10, padx=10, ipadx=10)

root.mainloop()


