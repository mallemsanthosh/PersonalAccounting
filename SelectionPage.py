#All Imports

import tkinter as tk
from tkinter import *
from commoncode import *
from Entry import *

#null function
def null():
    print("Hello")

def Mainfields(screen):
    selectframe=[{"label":"This is for All entry sheet",
                  "button":"ALL Entry sheet",
                  "ram":(lambda: AllEntrytLoop(screen))},
                  {"label":"This is for Balance Update",
                  "button":"Balance_Update",
                  "ram":(lambda: null())},
                  {"label":"This is for Credit Update",
                  "button":"Credit_Update",
                  "ram":(lambda: null())},
                  {"label":"This is for Debit Update",
                  "button":"Debit_Update",
                  "ram":(lambda: null())},
                  {"label":"This is for Balance Check ",
                  "button":"Balance_Checking",
                  "ram":(lambda: null())},
                  {"label":"This is for Montlysheet",
                  "button":"Montly_Sheet",
                  "ram":(lambda: null())},
                  {"label":"This is for Yearly_Sheet",
                  "button":"Yearly_Sheet",
                  "ram":(lambda: null())},
                  {"label":"This is for Day_Sheet",
                  "button":"Day_Sheet",
                  "ram":(lambda: null())},
                  {"label":"This is for creating excel sheet",
                  "button":"To Excel Sheet",
                  "ram":(lambda: null())},
                  {"label":"This is for To Delete Your Account",
                  "button":"Delete Account",
                  "ram":lambda: Exit.Exit(screen,tablefile="Drop")},
                  {"label":"This is for Logout",
                  "button":"Logout",
                  "ram":lambda : Exit.Exit(screen)},
                  {"label":"This is for Exit",
                  "button":"Exit",
                  "ram":lambda : Exit.Exit(screen)}]
    
    for a in range (len(selectframe)):
        row = tk.Frame(screen,background='#FFFACD')
        l0 = Label(row,text=selectframe[a]['label'], width=40,bg="#FFFACD")
        b0 = Button(row, text=selectframe[a]['button'],width=15,command=selectframe[a]['ram'])
        row.pack(side=tk.TOP,anchor=CENTER,
                padx=5,
                pady=5)
        l0.pack(side=RIGHT, pady=5)
        b0.pack(side=LEFT, pady=5, padx=10)

class SelectionPage():
    def Main(screen1=0):
        screen1.destroy()

        screen=tk.Tk()
        screen.title("Main Screen")
        #screen.geometry('500x500')
        screen.configure(bg="#FFFACD")
        Commonscreen(screen,"Selection Screen",'Select Your Option')
        row2=tk.Frame(screen,background="#FFFACD")
        row2.pack(side=tk.TOP,
                    padx=50,
                    pady=10,
                    anchor=CENTER)
        
        Mainfields(row2)
        screen.mainloop()

#SelectionPage.Main()