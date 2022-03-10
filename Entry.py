import tkinter as tk
from tkinter import *
from commoncode import *
from CreatingTable import *

def MainView(field,credit):
    entries={}
    for fields in field:
        if fields=='Cr_Date':
            fields="Date"
        if fields!='Del_Date':
            row = tk.Frame(credit)
            lab = tk.Label(row, width=15, text=fields + "\t: ", anchor='w')
            ent = tk.Entry(row,width=10)
            ent.insert(0, "0")
            row.pack(side=tk.TOP,
                    fill=tk.X,
                    padx=5,
                    pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT,
                    expand=tk.YES,
                    fill=tk.X)
            entries[fields] = ent
    return entries



def AllEntrytLoop(screen=0):
    credit=tk.Tk()
    credit.title("Credit Table")
    cr_fields,de_fields,bal_fields=CreateTable.Fields()
    
    l1 = Label(credit, text="\nCredit data Entry Fields")
    l1.pack()
    ent1=MainView(cr_fields,credit)
    l2 = Label(credit, text="\nDebit Data Entry Fields")
    l2.pack()
    ent1=MainView(de_fields,credit)
    b1=Button(credit,text="Submit",command= (lambda: Exit.Exit(credit) ))
    b1.pack(padx=50,pady=10,side=LEFT)
    b2=Button(credit,text="Exit",command= lambda : Exit.Exit(credit))
    b2.pack(padx=50,pady=10,side=LEFT)
    credit.mainloop()


#AllEntrytLoop()