#!/usr/bin/env python3
from tkinter import *

def select_all(event=None):
    # first set the focus to the entry widget
    blank2.focus()

    # use the selection_range method from the entry widget
    blank2.selection_range(0, END)
    
def daCopy(event=None):
    blank2.clipboard_clear()
    blank2.clipboard_append(blank2.selection_get())

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
# Creating Menubar
menubar = Menu(main)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
#edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = daCopy)
#edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command=select_all)

Label(main, text=" add or remove underscore ").grid(row=0, columnspan=3, sticky=W, pady=1)

blank = Entry(main)
blank2 = Entry(main)

blank.grid(row=1, column=0, columnspan=2, sticky=W)
blank2.grid(row=2, column=0, columnspan=2, sticky=W)

Button(main, text='Show answer', command=getDaText).grid(row=3, column=0, sticky=W, pady=1)
Button(main, text='Clear', command=clear_answer).grid(row=3, column=1, sticky=W, pady=1)

# display Menu
main.config(menu = menubar)
mainloop()