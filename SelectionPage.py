#All Imports

import tkinter as tk
from tkinter import *
from commoncode import *
from CreatingTable import *
#null function
def null():
    print("Hello")

def Mainfields(screen):
    i=1
    l0 = Label(text="This is for All entry sheet", width=40, bg="white")
    l0.grid(row=i, column=2, pady=5)
    b0 = Button(screen, text="ALL Entry sheet", command=lambda: null(),width=15)
    b0.grid_configure(row=i, column=1, pady=5, padx=10)
    i = i + 1
    l15 = Label(text="This is for Balance Update", width=40, bg="white")
    l15.grid(row=i, column=2, pady=5)
    b15 = Button(screen, text="Balance_Update", command=lambda: null(), width=15)
    b15.grid_configure(row=i, column=1, pady=5, padx=10)

    i=i+1
    l1=Label(text="This is for Credit Update",width=40,bg="white")
    l1.grid(row=i,column=2,pady=5)
    b1=Button(screen,text="Credit_Update",command=lambda : null(),width=15)
    b1.grid_configure(row=i,column=1,pady=5,padx=10)
    i = i + 1
    l2 = Label(text="This is for Debit Update", width=40, bg="white")
    l2.grid(row=i, column=2,pady=5)
    b2 = Button(screen, text="Debit_Update", command=lambda : null(),width=15)
    b2.grid_configure(row=i, column=1,padx=10)
    i = i + 1
    l3 = Label(text="This is for Balance Check ", width=40, bg="white")
    l3.grid(row=i, column=2,pady=5)
    b3 = Button(screen, text="Balance_Checking", command=lambda : null(),width=15)
    b3.grid_configure(row=i, column=1,padx=10)
    i = i + 1
    l4 = Label(text="This is for Montlysheet", width=40, bg="white")
    l4.grid(row=i, column=2, pady=5)
    b4 = Button(screen, text="Montly_Sheet", command=lambda : null(),width=15)
    b4.grid_configure(row=i, column=1,padx=10)
    i = i + 1
    l5 = Label(text="This is for Yearly_Sheet", width=40, bg="white")
    l5.grid(row=i, column=2, pady=5)
    b5 = Button(screen, text="Yearly_Sheet", command=lambda : null(),width=15)
    b5.grid_configure(row=i, column=1,padx=10)
    i = i + 1
    l6 = Label(text="This is for Day_Sheet", width=40, bg="white")
    l6.grid(row=i, column=2, pady=5)
    b6 = Button(screen, text="Day_Sheet", command=lambda : null(),width=15)
    b6.grid_configure(row=i, column=1,padx=10)
    i = i + 1
    l7 = Label(text="This is for Day to Day sheet", width=40, bg="white")
    l7.grid(row=i, column=2, pady=5)
    b7 = Button(screen, text="Date_to_date Sheet", command=lambda : null(),width=15)
    b7.grid_configure(row=i, column=1,padx=10)
    i = i + 1
    l9 = Label(text="This is for creating excel sheet", width=40, bg="white")
    l9.grid(row=i, column=2, pady=5)
    b9 = Button(screen, text="To Excel Sheet", command=lambda: null(), width=15)
    b9.grid_configure(row=i, column=1, padx=10)
    i = i + 1
    l10 = Label(text="This is for To Delete Your Account", width=40, bg="white")
    l10.grid(row=i, column=2, pady=5)
    b10 = Button(screen, text="Delete Account", command=lambda: Exit.Exit(screen,tablefile="Drop"), width=15)
    b10.grid_configure(row=i, column=1, padx=10)
    i = i + 1

    l8 = Label(text="This is for Exit", width=40, bg="white")
    l8.grid(row=i, column=2, pady=5)
    b8 = Button(screen, text="Exit", command= lambda : Exit.Exit(screen),width=15)
    b8.grid_configure(row=i, column=1,padx=10)

class SelectionPage():
    def Main(screen=0):
        screen=tk.Tk()
        screen.title("Main Screen")
        #screen.geometry('500x500')
        screen.configure(bg="white")
        Mainfields(screen)
        screen.mainloop()

#SelectionPage.main()