#All Imports
from distutils import command
import sqlite3
import tkinter as tk
from tkinter import *
from commoncode import *
from CreatingTable import *

#Global Varibles
global i
global entries 
i =0
entries={}

#Submitting the Form and adding the Columns in Database
def submit(entries):
    entereiesdata =[]
    for j in entries:
        print (entries[j].get())
        entereiesdata.append(str(entries[j].get())+" float")
    print (entereiesdata)
    createtable.createtab(entereiesdata)

#Defining the Frame
def mainview(firstsheet):
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

#Main Frame
def firstsheet(screen=0):
    firstsheet=tk.Tk()
    firstsheet.geometry('500x500')
    firstsheet.title("Create Your Table or Accounting Stucture")
    mainview(firstsheet)
    
    row2 = tk.Frame(firstsheet)
    btn = tk.Button(row2, width=15,text="ADD", command = (lambda  : mainview(firstsheet)))
    btn.pack(side=tk.LEFT, padx=10)
    row2.pack(side=tk.TOP,
            fill=tk.X,
                 padx=150,
                 pady=10)
               
    row3 = tk.Frame(firstsheet)
    b1=tk.Button(row3,text="Submit", command=(lambda e=entries : submit(e)))
    b1.pack(side=tk.LEFT)
    b2=tk.Button(row3,text="Exit", command= lambda : exit.Exit(firstsheet))
    b2.pack(side=tk.LEFT,padx=50)
    row3.pack(side=tk.BOTTOM,
            fill=tk.X,
                 padx=150,
                 pady=10)
    firstsheet.mainloop()

#Checking Whether Table is created or Not.
def mainloop():
    try:
        createtable.dummytab()
        firstsheet()
    except sqlite3.OperationalError as ram:
        print(ram,"Test is exist")

mainloop()