import sys
import tkinter as tk
from tkinter import *
import os

def Conformation(conformation):
        conformation.destroy()
        python = sys.executable
        os.execl(python, python, * sys.argv)
class Logout:

    def Logout():   
        conformation=tk.Tk()
        conformation.title("Conformation")
        conformation.configure(bg="white")
        l1=Label(conformation,text="\nAre you really Want to Logout",bg="white")
        l1.pack()
        b1=Button(conformation,text="Yes",bg="gold",command=lambda: Conformation(conformation))
        b1.pack_configure(padx=50,pady=10,side=LEFT)
        b2=Button(conformation,text="No",bg="gold",command=conformation.destroy)
        b2.pack(padx=50,pady=10,side=LEFT)
        