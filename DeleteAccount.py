import tkinter as tk
from tkinter import *
from CreatingTable import *
import sys
import os


def Conformation(username,conformation):
    conformation.destroy()
    CreateTable.DeleteAccount(username)
    python = sys.executable
    os.execl(python, python, * sys.argv)        


class DeleteAccount:
    def Delete_Account(username):   
        conformation=tk.Tk()
        conformation.title("Conformation")
        conformation.configure(bg="white")
        l1=Label(conformation,text="\nAre you really Want to Delete Account",bg="white")
        l1.pack()
        b1=Button(conformation,text="Yes",bg="gold",command=lambda: Conformation(username,conformation))
        b1.pack_configure(padx=50,pady=10,side=LEFT)
        b2=Button(conformation,text="No",bg="gold",command=conformation.destroy)
        b2.pack(padx=50,pady=10,side=LEFT)    
        

#DeleteAccount.Delete_Account('Ramsai')