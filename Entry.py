import tkinter as tk
from tkinter import *
from tkinter import font
from commoncode import *
from CreatingTable import *
from ownenanddecode import *

def SubmitEntry(entries1,entries2,cr_fields,de_fields,fields,credit,username,row1,row2,cfont,b1):
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
        cr_total=round(cr_total+float(cr_fields_list[i]),2)
        de_total=round(de_total+float(de_fields_list[i]),2)

    cr_fields_list[-1]=str(cr_total)
    de_fields_list[-1]=str(de_total)      

    CreateTable.CreditEntry(cr_fields_list,fields,username)  
    CreateTable.DebitEntry(de_fields_list,fields,username)
    entries1['Cr_Total'].delete(0, tk.END)
    entries1['Cr_Total'].insert(0, cr_total)
    entries2['Deb_Total'].delete(0, tk.END)
    entries2['Deb_Total'].insert(0, de_total)
    
    data=CreateTable.CheckBalance(username,str(entries1['Date'].get()))
    for i in range (0,len(fields)):
        if i==0:
            Label(credit,text=fields[i]+'\t:\t'+str(data[-1][i]),font=cfont,background="#FFFACD").pack()
        else:
            Label(credit,text=fields[i]+'\t:\t'+Decodess.Decodes(data[-1][i]),font=cfont,background="#FFFACD").pack()
    Label(credit,text="The total Credit is\t :\t "+str(cr_total),background="#FFFACD",font=cfont).pack()
    Label(credit,text="The total Debit is \t:\t "+str(de_total),background="#FFFACD",font=cfont).pack()
    
    row1.destroy()
    row2.destroy()
    b1.destroy()

    

def MainView(field,credit,cfont):
    entries={}
    for fields in field:
        if fields=='Cr_Date':
            fields="Date"
        if fields!='Deb_Date':
            row = tk.Frame(credit,background="#FFFACD")
            lab1 = tk.Label(row, width=15, text=fields, anchor='w',background="#FFFACD",font=cfont)
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
            entries[fields] = ent
    return entries



def AllEntrytLoop(username,screen=0):
    credit=tk.Tk()
    Commonscreen(credit,"Credit/Debit Entry Table",'Credit/Debit Entry Table')    
    cfont = TkFont.Font(family='Times New Roman', size = 12)

    cr_fields,de_fields,bal_fields,fields=CreateTable.Fields(username)
    
    row1 = tk.Frame(credit,background="#FFFACD")
    row1.pack(side=tk.TOP,
                    padx=5,
                    pady=5)
    
    l1 = Label(row1, text="Credit data Entry Fields",background="#FFFACD",fg='green')
    l1['font']=TkFont.Font(family='Times New Roman',weight = 'bold', size = 14)
    l1.pack()
    ent1=MainView(cr_fields,row1,cfont)
    
    row2 = tk.Frame(credit,background="#FFFACD")
    row2.pack(side=tk.TOP,
                    padx=5,
                    pady=5)
    
    l2 = Label(row2, text="Debit Data Entry Fields",background="#FFFACD",font=cfont,fg='green')
    l2['font']=TkFont.Font(family='Times New Roman',weight = 'bold', size = 14)
    l2.pack()
    ent2=MainView(de_fields,row2,cfont)
    
    row = tk.Frame(credit,background="#FFFACD")
    row.pack(side=tk.TOP,
                    padx=5,
                    pady=5)

    row3=tk.Frame(credit,background="#FFFACD")
    row3.pack(side=tk.TOP,
                    padx=50,
                    pady=20,
                    anchor=CENTER)
        
    b1=Button(row3,text="Submit",command= (lambda e1=ent1,e2=ent2 : SubmitEntry(e1,e2,cr_fields,de_fields,fields,row,username,row1,row2,cfont,b1) ))
    b1.pack(side=LEFT,padx=20)
    b2=Button(row3,text="Exit",command= lambda : Exit.Exit(credit))
    b2.pack(padx=20,side=RIGHT)
    credit.mainloop()


#AllEntrytLoop('SaiRam')