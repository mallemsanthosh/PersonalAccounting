import tkinter as tk
from tkinter import *
from commoncode import *
from CreatingTable import *
from ownenanddecode import *

def Bal_SubmitEntry(entries,bal_fields,fields,row,username,row2,cfont,b1):
    Bal_fields_list=[]
    
    for b in bal_fields:
        if b=="Bal_Date":
            Bal_fields_list.append(str(entries['Date'].get()))
        elif b!="Bal_Total":
            Bal_fields_list.append(str(entries[b].get()))
    
    bal_total=0
    for i in range(1,len(Bal_fields_list)):
        bal_total=round(bal_total+float(Bal_fields_list[i]),2)

    Bal_fields_list.append(str(bal_total))      

    CreateTable.BalanceEntry(Bal_fields_list,fields,username)
    
    data=CreateTable.CheckBalance(username,str(entries['Date'].get()))

    Label(row,text="Current Balances",font=cfont,fg='purple2').pack(anchor=CENTER)
    for i in range (0,len(fields)):
        row11 = tk.Frame(row,background="#FFFACD")
        row11.pack(side=tk.TOP,
                   fill=tk.X,
                    padx=5,
                    pady=5)
            
        if i==0:
            Label(row11,text=fields[i]+'\t:\t'+str(data[-1][i]),font=cfont,background="#FFFACD").pack(side=tk.LEFT)
        else:
            Label(row11,text=fields[i]+'\t:\t'+Decodess.Decodes(data[-1][i]),font=cfont,background="#FFFACD").pack(side=tk.LEFT)
    
    Label(row,text="Present Balance",font=cfont,fg='purple2').pack(anchor=CENTER)
    Label(row,text="The total Updated Balance is \t:\t "+str(bal_total),background="#FFFACD",font=cfont).pack()
    
    row2.destroy()
    b1.destroy()


class BalanceEntry:
    def BalanceUpdate(username):
        balance=tk.Tk()
        cfont = TkFont.Font(family='Times New Roman', size = 12)
        Commonscreen(balance,"Balance Update Table",'Balance Update Table')
        cr_fields,de_fields,bal_fields,fields=CreateTable.Fields(username)

        row1=tk.Frame(balance,background="#FFFACD")
        row1.pack(side=tk.TOP,
                        padx=50,
                        pady=20,
                        anchor=CENTER)    
        entries={}
        for field in (bal_fields):
            row=tk.Frame(row1,background="#FFFACD" )
            if field=='Bal_Date':
                    field='Date'
            if field!='Bal_Total':    
                lab1 = tk.Label(row, width=15, text=field, anchor='w',background="#FFFACD",font=cfont)
                lab2 = tk.Label(row, text=": ", anchor='w',background="#FFFACD",font=cfont)
                ent = tk.Entry(row,width=20)
                ent.insert(0,"0")
                row.pack(side=tk.TOP,
                        fill=tk.X,
                        padx=5,
                        pady=5)
                lab1.pack(side=tk.LEFT)
                lab2.pack(side=tk.LEFT)
                ent.pack(side=tk.RIGHT,
                        expand=tk.YES,
                        fill=tk.X)
                entries[field] = ent

        row2=tk.Frame(balance,background="#FFFACD")
        row2.pack(side=tk.TOP,
                        padx=50,
                        pady=20,
                        anchor=CENTER)
        
        row3=tk.Frame(balance,background="#FFFACD")
        row3.pack(side=tk.TOP,
                        padx=50,
                        pady=20,
                        anchor=CENTER)
        b1=Button(row3,text="Submit",command= (lambda e1=entries : Bal_SubmitEntry(e1,bal_fields,fields,row2,username,row1,cfont,b1) ))
        b1.pack(side=LEFT,padx=20)
        b2=Button(row3,text="Exit",command= lambda : Exit.Exit(balance))
        b2.pack(padx=20,side=RIGHT)
        balance.mainloop()

#BalanceEntry.BalanceUpdate('Sai')