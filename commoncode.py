import tkinter as tk
from tkinter import *
from CreatingTable import *
import tableui

def Exit1(screen,conformation,tablefile):
        conformation.destroy()
        if(tablefile!="Table Error"):
            screen.destroy()
        if(tablefile==True):
            CreateTable.Drop()
        elif(tablefile=="Drop"):
            CreateTable.Drop()
            tableui.Tablemain.Mainloop()
        
class Exit():
    def Exit(screen,tablefile=FALSE):
        conformation=tk.Tk()
        conformation.title("Conformation")
        conformation.configure(bg="white")
        if(tablefile==FALSE or tablefile==True):
            l1=Label(conformation,text="\nAre you really Want to exit",bg="white")
        elif(tablefile=="Drop"):
            l1=Label(conformation,text="\nAre you really Want to Delete Account",bg="white")
        b1=Button(conformation,text="OK",bg="gold",command= lambda : Exit1(screen,conformation,tablefile))
        l1.pack()
        b1.pack_configure(padx=50,pady=10,side=LEFT)
        b2=Button(conformation,text="Cancle",bg="gold",command=conformation.destroy)
        b2.pack(padx=50,pady=10,side=LEFT)

    def Error(screen,tablefile=FALSE):
        conformation=tk.Tk()
        conformation.title("Error")
        conformation.configure(bg="red")
        if(tablefile==FALSE or tablefile==True):
            l1=Label(conformation,text="\nAre you really Want to exit",bg="red")
        elif(tablefile=="Table Error"):
            l1=Label(conformation,text="\nPlease Enter Values in the All Fields",bg="red")
        b1=Button(conformation,text="OK",bg="gold",command= lambda : Exit1(screen,conformation,tablefile))
        l1.pack()
        b1.pack_configure(padx=50,pady=10,side=LEFT)
        b2=Button(conformation,text="Cancle",bg="gold",command=conformation.destroy)
        b2.pack(padx=50,pady=10,side=LEFT) 