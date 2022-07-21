#All Imports
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
def Submit(entries,screen,entries1,screenreg):
    entereiesdata =[]
    fields='Date'
    for j in entries:
        fields=fields+','+str(entries[j].get())
        entereiesdata.append(str(entries[j].get())+" varchar(100)")
    fields=fields+','+'Total'
    CreateTable.CreateTab(entereiesdata,str(entries1['User Name'].get()))    #Create Table
    CreateTable.Remeber(fields,entries1) #Rember the Fields for Future Use
    screen.destroy()
    screenreg.destroy()            #Destroy the Screen

def destroy1(e1,r):
    r.destroy()
    global entries
    entries.pop(e1)
    
#Defining the Frame
def Mainview(firstsheet,cfont):
    global entries
    global i
    i= i+1
    row = tk.Frame(firstsheet,background='#FFFACD')
    lab = tk.Label(row, width=15, text=("Enter"+str(i)) + "\t: ", anchor='w',background='#FFFACD')
    ent = tk.Entry(row, width=15,font=cfont)
    ent.insert(0, "")
    if(i!=1):
        button=Button(row, width=15,text="Delete",bg="gold",command= lambda e1=i,r=row : destroy1(e1,r))
    row.pack(side=tk.TOP,
                 fill=tk.X,
                 padx=100,
                 pady=10)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.LEFT,
                 fill=tk.X)
    if(i!=1):
        button.pack(side=tk.LEFT,padx=5)
    entries[i]= ent
    return ()

# Conformation Screen
def Conformation(screen,conformation,entries1,screenreg):
        conformation.destroy()
        Submit(entries,screen,entries1,screenreg)      

#For Checking All fields are Entered or Not..
def ConformationScreen(screen,entries1,screenreg,row1):
    error=False
    for j in entries:
        if str(entries[j].get())=="" or str(entries[j].get())==" ":
            row1['text']="Enter ALl Fields"
            error=True
            break
    if error==False:
        #For Conforming to Submit
        conformation=tk.Tk()
        conformation.title("Conformation")
        conformation.configure(bg="white")
        l1=Label(conformation,text="\nAre you really Want to Submit The Fields",bg="white")
        l1.pack()
        b1=Button(conformation,text="OK",bg="gold",command=lambda: Conformation(screen,conformation,entries1,screenreg))
        b1.pack_configure(padx=50,pady=10,side=LEFT)
        b2=Button(conformation,text="Cancle",bg="gold",command=conformation.destroy)
        b2.pack(padx=50,pady=10,side=LEFT)

#Main Frame
def FirstSheet(entries1,screenreg):
    firstsheet=tk.Tk()
    #firstsheet.geometry('500x500')
    cfont = TkFont.Font(family='Times New Roman', size = 12)

    #Creating the Title
    Commonscreen.Commonscreen(firstsheet,"Table or Accounting Stucture",'Create Your Fields Structure')
    
    #Global Variables
    global i 
    i = 0   

    #For layout
    Mainview(firstsheet,cfont)  

    #For Submit and Exit Components 
    row3 = tk.Frame(firstsheet,background='#FFFACD')
    b1=tk.Button(row3,text="Submit",command=lambda: ConformationScreen(firstsheet,entries1,screenreg,labeler))
    b1.pack(side=tk.LEFT)
    b2=tk.Button(row3,text="Exit", command= lambda : Exit.Exit(firstsheet))
    b2.pack(side=tk.LEFT,padx=50)
    row3.pack(side=tk.BOTTOM,
            fill=tk.X,
                 padx=150,
                 pady=10,anchor=CENTER)

    #For adding extra field to Enter Our Response
    row2 = tk.Frame(firstsheet,background='#FFFACD')
    btn = tk.Button(row2, width=15,text="ADD", command = (lambda  : Mainview(firstsheet,cfont)))
    btn.pack(side=tk.LEFT, padx=10)
    #For Alert
    labeler=Label(row2,text="",background='#FFFACD',fg='red').pack()
    row2.pack(side=tk.BOTTOM,
            fill=tk.X,
                 padx=150,
                 pady=10,anchor=CENTER)             
    
    firstsheet.mainloop()

#Execution Start From Here...
class Tablemain():
    def Mainloop(entriess,screenreg):
        FirstSheet(entriess,screenreg)

#For Checking:-
#tablemain.mainloop()