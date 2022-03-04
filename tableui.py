#All Imports

import sqlite3
import tkinter as tk
from tkinter import *
from commoncode import *
from CreatingTable import *
from SelectionPage import *

#Global Varibles
global i
global entries 
i =0
entries={}

#Submitting the Form and adding the Columns in Database
def Submit(entries,screen):
    entereiesdata =[]
    fields='Null'
    for j in entries:
        fields=fields+','+str(entries[j].get())
        entereiesdata.append(str(entries[j].get())+" float")
    CreateTable.CreateTab(entereiesdata)    #Create Table
    CreateTable.Remeber(fields) #Rember the Fields for Future Use
    screen.destroy()            #Destroy the Screen
    SelectionPage.Main()        #Open Selection Menu Page
    

#Defining the Frame
def Mainview(firstsheet):
    global entries
    global i
    i= i+1
    row = tk.Frame(firstsheet)
    lab = tk.Label(row, width=15, text=("Enter"+str(i)) + "\t: ", anchor='w')
    ent = tk.Entry(row, width=15)
    ent.insert(0, " ")
    row.pack(side=tk.TOP,
                 fill=tk.X,
                 padx=100,
                 pady=10)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.LEFT,
                 fill=tk.X)
    entries[i]= ent
    return ()

# Conformation Screen
def Conformation(screen,conformation):
        conformation.destroy()
        Submit(entries,screen)        

def ConformationScreen(screen):
    conformation=tk.Tk()
    conformation.title("Conformation")
    conformation.configure(bg="white")
    l1=Label(conformation,text="\nAre you really Want to Submit The Fields",bg="white")
    l1.pack()
    b1=Button(conformation,text="OK",bg="gold",command=lambda: Conformation(screen,conformation))
    b1.pack_configure(padx=50,pady=10,side=LEFT)
    b2=Button(conformation,text="Cancle",bg="gold",command=conformation.destroy)
    b2.pack(padx=50,pady=10,side=LEFT)

#Main Frame
def FirstSheet(screen=0):
    firstsheet=tk.Tk()
    #firstsheet.geometry('500x500')
    firstsheet.title("Create Your Table or Accounting Stucture")
    Mainview(firstsheet)  
    row3 = tk.Frame(firstsheet)
    b1=tk.Button(row3,text="Submit", command=lambda: ConformationScreen(firstsheet))
    b1.pack(side=tk.LEFT)
    b2=tk.Button(row3,text="Exit", command= lambda : Exit.Exit(firstsheet,tablefile=True))
    b2.pack(side=tk.LEFT,padx=50)
    row3.pack(side=tk.BOTTOM,
            fill=tk.X,
                 padx=150,
                 pady=10)
    row2 = tk.Frame(firstsheet)
    btn = tk.Button(row2, width=15,text="ADD", command = (lambda  : Mainview(firstsheet)))
    btn.pack(side=tk.LEFT, padx=10)
    row2.pack(side=tk.BOTTOM,
            fill=tk.X,
                 padx=150,
                 pady=10)             
    firstsheet.mainloop()

#Checking Whether Table is created or Not.
class Tablemain():
    def Mainloop():
        try:
            CreateTable.DummyTab()
            FirstSheet()
        except sqlite3.OperationalError as ram:
            SelectionPage.Main()

#tablemain.mainloop()