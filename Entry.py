import tkinter as tk
from tkinter import *
from commoncode import *
from CreatingTable import *

def SubmitEntry(entries1,entries2,cr_fields,de_fields,fields,credit):
    cr_fields_list=[]
    de_fields_list=[]
    for c in cr_fields:
        if c=="Cr_Date":
            cr_fields_list.append(str(entries1['Date'].get()))
        else:
            cr_fields_list.append(str(entries1[c].get()))
    
    for d in de_fields:
        if d=="Deb_Date":
            de_fields_list.append(str(entries1['Date'].get()))
        else:
            de_fields_list.append(str(entries2[d].get()))
    
    cr_total=0
    de_total=0
    for i in range(1,len(cr_fields_list)-1):
        cr_total=cr_total+float(cr_fields_list[i])
        de_total=de_total+float(de_fields_list[i])

    cr_fields_list[-1]=str(cr_total)
    de_fields_list[-1]=str(de_total)      

    CreateTable.CreditEntry(cr_fields,cr_fields_list,fields)  
    #creditsql(date,cr_ap,cr_sbi,cr_paytm,cr_dccb,cr_cash,t1)
    #debitsql(date,de_ap,de_sbi,de_paytm,de_dccb,de_cash,t2)

    entries1['Cr_Total'].delete(0, tk.END)
    entries1['Cr_Total'].insert(0, cr_total)
    entries2['Deb_Total'].delete(0, tk.END)
    entries2['Deb_Total'].insert(0, de_total)
    credit.destroy()


def MainView(field,credit):
    entries={}
    for fields in field:
        if fields=='Cr_Date':
            fields="Date"
        if fields!='Deb_Date':
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
    cr_fields,de_fields,bal_fields,fields=CreateTable.Fields()
    
    l1 = Label(credit, text="\nCredit data Entry Fields")
    l1.pack()
    ent1=MainView(cr_fields,credit)
    l2 = Label(credit, text="\nDebit Data Entry Fields")
    l2.pack()
    ent2=MainView(de_fields,credit)
    b1=Button(credit,text="Submit",command= (lambda e1=ent1,e2=ent2 : SubmitEntry(e1,e2,cr_fields,de_fields,fields,credit) ))
    b1.pack(padx=50,pady=10,side=LEFT)
    b2=Button(credit,text="Exit",command= lambda : Exit.Exit(credit))
    b2.pack(padx=50,pady=10,side=LEFT)
    credit.mainloop()


#AllEntrytLoop()