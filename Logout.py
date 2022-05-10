#Tkinter Library and Packages Imports
import tkinter as tk
from tkinter import *

#System and OS related Imports
import sys
import os

#Logout Function
def Conformation(conformation):
        conformation.destroy()
        python = sys.executable
        os.execl(python, python, * sys.argv)

#Logout Class and Logout Conformation Screen..
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