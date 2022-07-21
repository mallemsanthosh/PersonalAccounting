#Tkinter Library and Packages Imports
import tkinter as tk
from tkinter import *

#For Calling the Class and Functions These Local Files are imported
from commoncode import *
from Balance import *
from Entry import *
from Logout import *
from DeleteAccount import *

#It will Create Layout of the Selection Page Screen
def Mainfields(screen,screen1,username):
    selectframe=[{"label":"This is for Updating Credit and Debit",
                  "button":"ALL Entry sheet",
                  "condition":(lambda: Entrys.AllEntrytLoop(username))},#For Entring Credit and Debit
                  {"label":"This is for Updating Balance",
                  "button":"Balance_Update",
                  "condition":(lambda: BalanceEntry.BalanceUpdate(username))},#For Balance Entry
                  {"label":"This is for Updating Credit",
                  "button":"Credit_Update",
                  "condition":(lambda: Entrys.CreditEntry(username))},#For Credit Entry
                  {"label":"This is for Updating Debit",
                  "button":"Debit_Update",
                  "condition":(lambda: Entrys.DebitEntry(username))},#For Debit Entry
                  {"label":"This is for Checking Current Balance ",
                  "button":"Balance_Checking",
                  "condition":(lambda: BalanceEntry.Bal_Check_Current(username))},#For Balance Check, For Current Date.
                  {"label":"This is for Checking Balance for Particular Month",
                  "button":"Montly_Sheet",
                  "condition":(lambda: BalanceEntry.BalanceCheck_Month(username))},#For Balance Check for Particular Month.
                  {"label":"This is for Checking Balance for Particular Year",
                  "button":"Yearly_Sheet",
                  "condition":(lambda: BalanceEntry.BalanceCheck_Year(username))},#Balance Check for Particular Year.
                  {"label":"This is for Checking Balance for Particular Date",
                  "button":"Day_Sheet",
                  "condition":(lambda: BalanceEntry.BalanceCheck(username))},#Balance Check for Particualar Date.
                  {"label":"This is for Creating Excel Sheet",
                  "button":"To Excel Sheet",
                  "condition":(lambda: To_Excel.To_Excel(username))},#To Create Excel with all Transaction Details.
                  {"label":"This is for To Delete Your Account",
                  "button":"Delete Account",
                  "condition":lambda: DeleteAccount.Delete_Account(username)},#Delete User Account.
                  {"label":"This is for Logout",
                  "button":"Logout",
                  "condition":lambda : Logout.Logout()},#For Logout the User.
                  {"label":"This is for Exit/Close Application",
                  "button":"Exit",
                  "condition":lambda : Exit.Exit(screen1)}]#For Exit the Current Screen (It will Close the Application.)
    
    for a in range (len(selectframe)):
        row = tk.Frame(screen,background='#FFFACD')
        l0 = Label(row,text=selectframe[a]['label'], width=40,bg="#FFFACD")
        b0 = Button(row, text=selectframe[a]['button'],width=20,height=1,command=selectframe[a]['condition'])
        row.pack(side=tk.TOP,anchor=CENTER,
                padx=2,
                pady=2)
        l0.pack(side=RIGHT, pady=2)
        b0.pack(side=LEFT, pady=2, padx=5)

#Selection Page Function
class SelectionPage():
    def Main(username,screen1=0):
        screen1.destroy()
        screen=tk.Tk()
        screen.title("Main Screen")
        #screen.geometry('500x500')
        screen.configure(bg="#FFFACD")
        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(screen,"Selection Screen",'Select Your Option')
        row2=tk.Frame(screen,background="#FFFACD")
        row2.pack(side=tk.TOP,
                    padx=50,
                    pady=10,
                    anchor=CENTER)
        #For Creating Layout..
        Mainfields(row2,screen,username)
        screen.mainloop()

#For Checking:-
#SelectionPage.Main()