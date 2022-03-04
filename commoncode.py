import tkinter as tk
from tkinter import *
from CreatingTable import *

def Exit1(screen,conformation,tablefile):
        conformation.destroy()
        if(tablefile):
            CreateTable.Drop()
        screen.destroy()

class Exit():
    def Exit(screen,tablefile=FALSE):
        conformation=tk.Tk()
        conformation.title("Conformation")
        conformation.configure(bg="white")
        l1=Label(conformation,text="\nAre you really Want to exit",bg="white")
        l1.pack()
        b1=Button(conformation,text="OK",bg="gold",command= lambda : Exit1(screen,conformation,tablefile))
        b1.pack_configure(padx=50,pady=10,side=LEFT)
        b2=Button(conformation,text="Cancle",bg="gold",command=conformation.destroy)
        b2.pack(padx=50,pady=10,side=LEFT)