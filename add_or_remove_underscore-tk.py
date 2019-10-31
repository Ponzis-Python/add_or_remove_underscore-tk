from tkinter import *
from tkinter.messagebox import *

def getDaText():
    src = blank.get()

    if '_' in src:
        dst = src.replace("_", " ")
    else:
        dst = src.replace(" ", "_")

    blank2.insert(0, dst)

def clear_answer():

    blank.delete('0', END)
    blank2.delete('0', END)

main = Tk()
Label(main, text=" add or remove underscore ").grid(row=0, columnspan=3, sticky=W, pady=1)

blank = Entry(main)
blank2 = Entry(main)

blank.grid(row=1, column=0, columnspan=2, sticky=W)
blank2.grid(row=2, column=0, columnspan=2, sticky=W)

Button(main, text='Show answer', command=getDaText).grid(row=3, column=0, sticky=W, pady=1)
Button(main, text='Clear', command=clear_answer).grid(row=3, column=1, sticky=W, pady=1)

mainloop()