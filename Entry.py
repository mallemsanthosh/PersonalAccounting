import tkinter as tk
from tkinter import *
from commoncode import *
from CreatingTable import *
from ownenanddecode import *

#Credit and Debit Submit
def SubmitEntry(entries1,entries2,cr_fields,de_fields,fields,row,username,row1,row2,cfont,b1):
    cr_fields_list=[]
    de_fields_list=[]
    for c in cr_fields:
        if c=="Cr_Date":
            cr_fields_list.append(str(entries1['Date'].get()))
        elif c!="Cr_Total":
            cr_fields_list.append(str(entries1[c].get()))
    
    for d in de_fields:
        if d=="Deb_Date":
            de_fields_list.append(str(entries1['Date'].get()))
        elif d!="Deb_Total":
            de_fields_list.append(str(entries2[d].get()))
    
    cr_total=0
    de_total=0
    for i in range(1,len(cr_fields_list)):
        cr_total=round(cr_total+float(cr_fields_list[i]),2)
        de_total=round(de_total+float(de_fields_list[i]),2)

    cr_fields_list.append(str(cr_total))
    de_fields_list.append(str(de_total))      

    CreateTable.CreditEntry(cr_fields_list,fields,username)  
    CreateTable.DebitEntry(de_fields_list,fields,username)
    
    data,cr,de=CreateTable.CheckBalance(username,str(entries1['Date'].get()))

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
    
    Label(row,text="Present Credit and Debit Totals",font=cfont,fg='purple2').pack(anchor=CENTER)
    Label(row,text="The total Credit is\t :\t "+str(cr_total),background="#FFFACD",font=cfont).pack()
    Label(row,text="The total Debit is \t:\t "+str(de_total),background="#FFFACD",font=cfont).pack()
    
    row1.destroy()
    row2.destroy()
    b1.destroy()

#Credit Submit
def Cr_SubmitEntry(entries1,cr_fields,fields,row,username,row1,cfont,b1):
    cr_fields_list=[]
    for c in cr_fields:
        if c=="Cr_Date":
            cr_fields_list.append(str(entries1['Date'].get()))
        elif c!="Cr_Total":
            cr_fields_list.append(str(entries1[c].get()))

    cr_total=0
    for i in range(1,len(cr_fields_list)):
        cr_total=round(cr_total+float(cr_fields_list[i]),2)

    cr_fields_list.append(str(cr_total))

    CreateTable.CreditEntry(cr_fields_list,fields,username)  
    
    data,cr,deb=CreateTable.CheckBalance(username,str(entries1['Date'].get()))

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
    
    Label(row,text="Present Credit Totals",font=cfont,fg='purple2').pack(anchor=CENTER)
    Label(row,text="The total Credit is\t :\t "+str(cr_total),background="#FFFACD",font=cfont).pack()
    
    row1.destroy()
    b1.destroy()

#Debit Submit
def De_SubmitEntry(entries2,de_fields,fields,row,username,row2,cfont,b1):
    de_fields_list=[]
    
    for d in de_fields:
        if d=="Deb_Date":
            de_fields_list.append(str(entries2['Date'].get()))
        elif d!="Deb_Total":
            de_fields_list.append(str(entries2[d].get()))
    
    de_total=0
    for i in range(1,len(de_fields_list)):
        de_total=round(de_total+float(de_fields_list[i]),2)

    de_fields_list.append(str(de_total))      

    CreateTable.DebitEntry(de_fields_list,fields,username)
    
    data,cr,deb=CreateTable.CheckBalance(username,str(entries2['Date'].get()))

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
    
    Label(row,text="Present Debit Totals",font=cfont,fg='purple2').pack(anchor=CENTER)
    Label(row,text="The total Debit is \t:\t "+str(de_total),background="#FFFACD",font=cfont).pack()
    
    row2.destroy()
    b1.destroy()


    

def MainView(field,credit,cfont,l=0):
    entries={}
    for fields in field:
        if fields=='Cr_Date' or (fields=='Deb_Date' and l=="debit"):
            fields="Date"
        if fields!='Deb_Date' and fields!='Deb_Total' and fields!='Cr_Total' :
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

#Credit and Debit Entry Screen
def AllEntrytLoop(username):
    credit=tk.Tk()
    cfont = TkFont.Font(family='Times New Roman', size = 12)

    Commonscreen(credit,"Credit/Debit Entry Table",'Credit/Debit Entry Table')
    
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
                    pady=5,anchor=CENTER)

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

#Credit Entry Screen
def CreditEntry(username):
    credit=tk.Tk()
    cfont = TkFont.Font(family='Times New Roman', size = 12)

    Commonscreen(credit,"Credit Entry Table",'Credit Entry Table')
    
    cr_fields,de_fields,bal_fields,fields=CreateTable.Fields(username)
    
    row1 = tk.Frame(credit,background="#FFFACD")
    row1.pack(side=tk.TOP,
                    padx=5,
                    pady=5)
    
    l1 = Label(row1, text="Credit data Entry Fields",background="#FFFACD",fg='green')
    l1['font']=TkFont.Font(family='Times New Roman',weight = 'bold', size = 14)
    l1.pack()
    ent1=MainView(cr_fields,row1,cfont)
        
    row = tk.Frame(credit,background="#FFFACD")
    row.pack(side=tk.TOP,
                    padx=5,
                    pady=5,anchor=CENTER)

    row3=tk.Frame(credit,background="#FFFACD")
    row3.pack(side=tk.TOP,
                    padx=50,
                    pady=20,
                    anchor=CENTER)
        
    b1=Button(row3,text="Submit",command= (lambda e1=ent1 : Cr_SubmitEntry(e1,cr_fields,fields,row,username,row1,cfont,b1) ))
    b1.pack(side=LEFT,padx=20)
    b2=Button(row3,text="Exit",command= lambda : Exit.Exit(credit))
    b2.pack(padx=20,side=RIGHT)
    credit.mainloop()

#Debit Entry Screen
def DebitEntry(username):
    credit=tk.Tk()
    cfont = TkFont.Font(family='Times New Roman', size = 12)
 
    Commonscreen(credit,"Debit Entry Table",'Credit/Debit Entry Table')
    
    cr_fields,de_fields,bal_fields,fields=CreateTable.Fields(username)
    
    row2 = tk.Frame(credit,background="#FFFACD")
    row2.pack(side=tk.TOP,
                    padx=5,
                    pady=5)
    
    l2 = Label(row2, text="Debit Data Entry Fields",background="#FFFACD",font=cfont,fg='green')
    l2['font']=TkFont.Font(family='Times New Roman',weight = 'bold', size = 14)
    l2.pack()
    ent2=MainView(de_fields,row2,cfont,'debit')
    
    row = tk.Frame(credit,background="#FFFACD")
    row.pack(side=tk.TOP,
                    padx=5,
                    pady=5,anchor=CENTER)

    row3=tk.Frame(credit,background="#FFFACD")
    row3.pack(side=tk.TOP,
                    padx=50,
                    pady=20,
                    anchor=CENTER)
        
    b1=Button(row3,text="Submit",command= (lambda e2=ent2 : De_SubmitEntry(e2,de_fields,fields,row,username,row2,cfont,b1) ))
    b1.pack(side=LEFT,padx=20)
    b2=Button(row3,text="Exit",command= lambda : Exit.Exit(credit))
    b2.pack(padx=20,side=RIGHT)
    credit.mainloop()



#AllEntrytLoop('Ram')