#All Imports

import tkinter as tk
from tkinter import *
from commoncode import *
from Balance import *
from Entry import *
from Logout import *
from DeleteAccount import *

#null function
def null():
    print("Hello")

def Mainfields(screen,screen1,username):
    selectframe=[{"label":"This is for All entry sheet",
                  "button":"ALL Entry sheet",
                  "condition":(lambda: AllEntrytLoop(username))},
                  {"label":"This is for Balance Update",
                  "button":"Balance_Update",
                  "condition":(lambda: BalanceEntry.BalanceUpdate(username))},
                  {"label":"This is for Credit Update",
                  "button":"Credit_Update",
                  "condition":(lambda: CreditEntry(username))},
                  {"label":"This is for Debit Update",
                  "button":"Debit_Update",
                  "condition":(lambda: DebitEntry(username))},
                  {"label":"This is for Checking Current Balance ",
                  "button":"Balance_Checking",
                  "condition":(lambda: BalanceEntry.Bal_Check_Current(username))},
                  {"label":"This is for Montlysheet",
                  "button":"Montly_Sheet",
                  "condition":(lambda: BalanceEntry.BalanceCheck_Month(username))},
                  {"label":"This is for Yearly_Sheet",
                  "button":"Yearly_Sheet",
                  "condition":(lambda: BalanceEntry.BalanceCheck_Year(username))},
                  {"label":"This is for Day_Sheet",
                  "button":"Day_Sheet",
                  "condition":(lambda: BalanceEntry.BalanceCheck(username))},
                  {"label":"This is for creating excel sheet",
                  "button":"To Excel Sheet",
                  "condition":(lambda: To_Excel.To_Excel(username))},
                  {"label":"This is for To Delete Your Account",
                  "button":"Delete Account",
                  "condition":lambda: DeleteAccount.Delete_Account(username)},
                  {"label":"This is for Logout",
                  "button":"Logout",
                  "condition":lambda : Logout.Logout()},
                  {"label":"This is for Exit",
                  "button":"Exit",
                  "condition":lambda : Exit.Exit(screen1)}]
    
    for a in range (len(selectframe)):
        row = tk.Frame(screen,background='#FFFACD')
        l0 = Label(row,text=selectframe[a]['label'], width=40,bg="#FFFACD")
        b0 = Button(row, text=selectframe[a]['button'],width=20,height=1,command=selectframe[a]['condition'])
        row.pack(side=tk.TOP,anchor=CENTER,
                padx=2,
                pady=2)
        l0.pack(side=RIGHT, pady=2)
        b0.pack(side=LEFT, pady=2, padx=5)

class SelectionPage():
    def Main(username,screen1=0):
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
        
        Mainfields(row2,screen,username)
        screen.mainloop()

#SelectionPage.Main()