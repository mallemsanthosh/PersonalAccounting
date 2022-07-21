#Tkinter Library and Packages Imports
import tkinter as tk
from tkinter import *
from sqlalchemy import null
from tkcalendar import Calendar, DateEntry

#Excel Related Imports
import csv
import pandas as pa
from tkinter.filedialog import asksaveasfile

#For Calling the Class and Functions These Local Files are imported
from commoncode import *
from CreatingTable import *
from ownenanddecode import *


def Bal_SubmitEntry(entries,bal_fields,fields,row,username,row2,cfont,b1):
    Bal_fields_list=[]
    
    for b in bal_fields:
        if b=="Bal_Date":
            Bal_fields_list.append(str(entries['Date'].get_date()))
        elif b!="Bal_Total":
            Bal_fields_list.append(str(entries[b].get()))
    
    bal_total=0
    for i in range(1,len(Bal_fields_list)):
        bal_total=round(bal_total+float(Bal_fields_list[i]),2)

    Bal_fields_list.append(str(bal_total))      

    CreateTable.BalanceEntry(Bal_fields_list,fields,username)
    
    data,cr_data,deb_data=CreateTable.CheckBalance(username,str(entries['Date'].get_date()))

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

def BalanceCheck_Submit(username,date,fields,row,cfont,b1,row123):
    data,cr_data,deb_data=CreateTable.CheckBalance(username,date.get())
    row1 = tk.Frame(row,background="#FFFACD")
    row1.pack(side=tk.TOP,
                    fill=tk.X,
                        padx=5,
                        pady=5)
    if(str(data[-1][0]))==str(date.get()):
        Label(row1,text="Balances on "+str(date.get()),font=cfont,fg='purple2').pack(anchor=CENTER)
        for i in range (0,len(fields)):
            row11 = tk.Frame(row1,background="#FFFACD")
            row11.pack(side=tk.TOP,
                    fill=tk.X,
                        padx=5,
                        pady=5)    
            if i==0:
                Label(row11,text=fields[i]+'\t:\t'+str(data[-1][i]),font=cfont,background="#FFFACD").pack(side=tk.LEFT)
            else:
                Label(row11,text=fields[i]+'\t:\t'+Decodess.Decodes(data[-1][i]),font=cfont,background="#FFFACD").pack(side=tk.LEFT)
        
        cr_total=0
        deb_total=0
        for i in cr_data:
            if i[0]==str(date.get()):
                cr_total=cr_total+round(float(Decodess.Decodes(i[-1])),2)
        for i in deb_data:
            if i[0]==str(date.get()):
                deb_total=deb_total+round(float(Decodess.Decodes(i[-1])),2)

        if cr_total!=0:
            Label(row1,text="Total Credit"+'\t:\t'+str(cr_total),font=cfont,background="#FFFACD").pack()
        else:
            Label(row1,text="Total Credit"+'\t:\t'+'0',font=cfont,background="#FFFACD").pack()
        if deb_total!=0:
            Label(row1,text="Total Debit"+'\t:\t'+str(deb_total),font=cfont,background="#FFFACD").pack()
        else:
            Label(row1,text="Total Debit"+'\t:\t'+'0',font=cfont,background="#FFFACD").pack()        
   
    else:
        Label(row,text="No Record On this date "+str(date.get()),font=cfont,fg='purple2').pack(anchor=CENTER)
    b1.destroy()
    row123.destroy()

def BalanceCheck_Year_Submit(username,date,fields,row,cfont,b1,row123):
    data,cr_data,deb_data=CreateTable.For_YearBalance(username,date.get())
    row1 = tk.Frame(row,background="#FFFACD")
    row1.pack(side=tk.TOP,
                    fill=tk.X,
                        padx=5,
                        pady=5)
    if(data!=[]):
        Label(row1,text="Balances For the Year: "+str(date.get()),font=cfont,fg='purple2').pack(anchor=CENTER)
        for i in range (0,len(fields)):
            row11 = tk.Frame(row1,background="#FFFACD")
            row11.pack(side=tk.TOP,
                    fill=tk.X,
                        padx=5,
                        pady=5)    
            Label(row11,text=fields[i]+'\t:\t'+str(data[-1][i]),font=cfont,background="#FFFACD").pack(side=tk.LEFT)
        if cr_data!=0:
            Label(row1,text="Total Credit"+'\t:\t'+str(cr_data),font=cfont,background="#FFFACD").pack()
        else:
            Label(row1,text="Total Credit"+'\t:\t'+'0',font=cfont,background="#FFFACD").pack()
        if deb_data!=0:
            Label(row1,text="Total Debit"+'\t:\t'+str(deb_data),font=cfont,background="#FFFACD").pack()
        else:
            Label(row1,text="Total Debit"+'\t:\t'+'0',font=cfont,background="#FFFACD").pack()        
   
    else:
        Label(row,text="No Record On this Year "+str(date.get()),font=cfont,fg='purple2').pack(anchor=CENTER)
    b1.destroy()
    row123.destroy()

def BalanceCheck_Month_Submit(username,date,fields,row,cfont,b1,row123,year,row1234):
    data,cr_data,deb_data=CreateTable.For_MonthBalance(username,date.get(),year.get())
    row1 = tk.Frame(row,background="#FFFACD")
    row1.pack(side=tk.TOP,
                    fill=tk.X,
                        padx=5,
                        pady=5)
    if(data!=[]):
        Label(row1,text="Balances For the Month: "+str(date.get())+" in Year "+str(year.get()),font=cfont,fg='purple2').pack(anchor=CENTER)
        for i in range (0,len(fields)):
            row11 = tk.Frame(row1,background="#FFFACD")
            row11.pack(side=tk.TOP,
                    fill=tk.X,
                        padx=5,
                        pady=5)    
            Label(row11,text=fields[i]+'\t:\t'+str(data[-1][i]),font=cfont,background="#FFFACD").pack(side=tk.LEFT)
        if cr_data!=0:
            Label(row1,text="Total Credit"+'\t:\t'+str(cr_data),font=cfont,background="#FFFACD").pack()
        else:
            Label(row1,text="Total Credit"+'\t:\t'+'0',font=cfont,background="#FFFACD").pack()
        if deb_data!=0:
            Label(row1,text="Total Debit"+'\t:\t'+str(deb_data),font=cfont,background="#FFFACD").pack()
        else:
            Label(row1,text="Total Debit"+'\t:\t'+'0',font=cfont,background="#FFFACD").pack()        
   
    else:
        Label(row,text="No Record On this Month "+str(date.get())+" in Year "+str(year.get()),font=cfont,fg='purple2').pack(anchor=CENTER)
    b1.destroy()
    row123.destroy()
    row1234.destroy()


class BalanceEntry:
    def BalanceUpdate(username):
        balance=tk.Tk()
        cfont = TkFont.Font(family='Times New Roman', size = 12)
        Commonscreen.Commonscreen(balance,"Balance Update Table",'Balance Update Table')
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
                if field == "Date":
                    ent = DateEntry(row, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
                else:
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

    def BalanceCheck(username):
        balance=tk.Tk()
        cfont = TkFont.Font(family='Times New Roman', size = 12)
        Commonscreen.Commonscreen(balance,"Balance Check Sheet of Date Table",'Balance Check Sheet of Date Table')
        cr_fields,de_fields,bal_fields,fields=CreateTable.Fields(username)

        row1=tk.Frame(balance,background="#FFFACD")
        row1.pack(side=tk.TOP,
                        padx=50,
                        pady=20,
                        anchor=CENTER)
        tk.Label(row1, width=15, text="Date", anchor='w',background="#FFFACD",font=cfont).pack(side=tk.LEFT)
        tk.Label(row1, text=": ", anchor='w',background="#FFFACD",font=cfont).pack(side=tk.LEFT)
        ent = tk.Entry(row1,width=20)
        ent.insert(0,"")
        ent.pack(side=tk.RIGHT,
                expand=tk.YES,
                fill=tk.X)
           

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
        b1=Button(row3,text="Submit",command= (lambda e1=ent : BalanceCheck_Submit(username,e1,fields,row2,cfont,b1,row1) ))
        b1.pack(side=LEFT,padx=20)
        b2=Button(row3,text="Exit",command= lambda : Exit.Exit(balance))
        b2.pack(padx=20,side=RIGHT)
        balance.mainloop()

    def Bal_Check_Current(username):
        balance=tk.Tk()
        cfont = TkFont.Font(family='Times New Roman', size = 12)
        Commonscreen.Commonscreen(balance,"Balance Table",'Balance Table')
        cr_fields,de_fields,bal_fields,fields=CreateTable.Fields(username)   

        row2=tk.Frame(balance,background="#FFFACD")
        row2.pack(side=tk.TOP,
                        padx=50,
                        pady=20,
                        anchor=CENTER)

        data,cr_data,deb_data=CreateTable.CheckBalance(username,null)
        Label(row2,text="Current Balances",font=cfont,fg='purple2').pack(anchor=CENTER)
        for i in range (0,len(fields)):
            row11 = tk.Frame(row2,background="#FFFACD")
            row11.pack(side=tk.TOP,
                    fill=tk.X,
                        padx=5,
                        pady=5)    
            if i==0:
                Label(row11,text=fields[i]+'\t:\t'+str(data[-1][i]),font=cfont,background="#FFFACD").pack(side=tk.LEFT)
            else:
                Label(row11,text=fields[i]+'\t:\t'+Decodess.Decodes(data[-1][i]),font=cfont,background="#FFFACD").pack(side=tk.LEFT)
        row3=tk.Frame(balance,background="#FFFACD")
        row3.pack(side=tk.TOP,
                        padx=50,
                        pady=20,
                        anchor=CENTER)
        b2=Button(row3,text="Exit",command= lambda : Exit.Exit(balance))
        b2.pack(padx=20,side=RIGHT)
        balance.mainloop()

    def BalanceCheck_Year(username):
        balance=tk.Tk()
        cfont = TkFont.Font(family='Times New Roman', size = 12)
        Commonscreen.Commonscreen(balance,"Balance Check Sheet of Year",'Balance Check Sheet Year')
        cr_fields,de_fields,bal_fields,fields=CreateTable.Fields(username)

        row1=tk.Frame(balance,background="#FFFACD")
        row1.pack(side=tk.TOP,
                        padx=50,
                        pady=20,
                        anchor=CENTER)
        tk.Label(row1, width=15, text="Year", anchor='w',background="#FFFACD",font=cfont).pack(side=tk.LEFT)
        tk.Label(row1, text=": ", anchor='w',background="#FFFACD",font=cfont).pack(side=tk.LEFT)
        ent = tk.Entry(row1,width=20)
        ent.insert(0,"")
        ent.pack(side=tk.RIGHT,
                expand=tk.YES,
                fill=tk.X)
           

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
        b1=Button(row3,text="Submit",command= (lambda e1=ent : BalanceCheck_Year_Submit(username,e1,fields,row2,cfont,b1,row1) ))
        b1.pack(side=LEFT,padx=20)
        b2=Button(row3,text="Exit",command= lambda : Exit.Exit(balance))
        b2.pack(padx=20,side=RIGHT)
        balance.mainloop()

    def BalanceCheck_Month(username):
        balance=tk.Tk()
        cfont = TkFont.Font(family='Times New Roman', size = 12)
        Commonscreen.Commonscreen(balance,"Balance Check Sheet of Month",'Balance Check Sheet Month')
        cr_fields,de_fields,bal_fields,fields=CreateTable.Fields(username)

        row1=tk.Frame(balance,background="#FFFACD")
        row1.pack(side=tk.TOP,
                        padx=50,
                        pady=20,
                        anchor=CENTER)
        tk.Label(row1, width=15, text="Month", anchor='w',background="#FFFACD",font=cfont).pack(side=tk.LEFT)
        tk.Label(row1, text=": ", anchor='w',background="#FFFACD",font=cfont).pack(side=tk.LEFT)
        ent1 = tk.Entry(row1,width=20)
        ent1.insert(0,"")
        ent1.pack(side=tk.RIGHT,
                expand=tk.YES,
                fill=tk.X)
        row11=tk.Frame(balance,background="#FFFACD")
        row11.pack(side=tk.TOP,
                        padx=50,
                        pady=20,
                        anchor=CENTER)
        
        tk.Label(row11, width=15, text="Year", anchor='w',background="#FFFACD",font=cfont).pack(side=tk.LEFT)
        tk.Label(row11, text=": ", anchor='w',background="#FFFACD",font=cfont).pack(side=tk.LEFT)
        ent2 = tk.Entry(row11,width=20)
        ent2.insert(0,"")
        ent2.pack(side=tk.RIGHT,
                expand=tk.YES,
                fill=tk.X)
           

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
        b1=Button(row3,text="Submit",command= (lambda e1=ent1,e2=ent2 : BalanceCheck_Month_Submit(username,e1,fields,row2,cfont,b1,row1,e2,row11) ))
        b1.pack(side=LEFT,padx=20)
        b2=Button(row3,text="Exit",command= lambda : Exit.Exit(balance))
        b2.pack(padx=20,side=RIGHT)
        balance.mainloop()

class To_Excel:
    def Excel_Conformation(username,conformation):
        conformation.destroy()
        bal,cr,deb=CreateTable.For_Excel(username)
        cr_fields,de_fields,bal_fields,fields=CreateTable.Fields(username)
        field=[]
        for fiel in range(len(cr_fields)):
            if(cr_fields[fiel]=="Cr_Date"):
                field.append("Date")
            else:
                field.append(cr_fields[fiel])
            if(de_fields[fiel]!="Deb_Date"):
                field.append(de_fields[fiel])
            if(bal_fields[fiel]!="Bal_Date"):
                field.append(bal_fields[fiel])
        data=[]
        for i in range(len(bal)):
            data.append([])
            for j in range(len(bal[i])):
                if j!=0 and len(cr[i])!=1:
                    data[i].append(cr[i][j])
                elif j!=0 and len(cr[i])==1:
                    data[i].append(0)
                if j!=0 and len(deb[i])!=1:
                    data[i].append(deb[i][j])
                elif j!=0 and len(deb[i])==1:
                    data[i].append(0)
                data[i].append(bal[i][j])
        
        with open("Moneyaccount.csv",'w') as files:
            csvwriter=csv.writer(files)
            csvwriter.writerow(field)
            csvwriter.writerows(data)
        files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
        file = asksaveasfile(filetypes = files, defaultextension = files)
        df = pa.read_csv('Moneyaccount.csv')
        df.to_csv('Moneyaccount.csv')

    def To_Excel(username):
        conformation=tk.Tk()
        conformation.title("Conformation")
        conformation.configure(bg="white")
        l1=Label(conformation,text="\nAre you really Want to Create Excel Sheet",bg="white")
        l1.pack()
        b1=Button(conformation,text="Yes",bg="gold",command=lambda: To_Excel.Excel_Conformation(username,conformation))
        b1.pack_configure(padx=50,pady=10,side=LEFT)
        b2=Button(conformation,text="No",bg="gold",command=conformation.destroy)
        b2.pack(padx=50,pady=10,side=LEFT)
        


#To_Excel.To_Excel("Sai")
#BalanceEntry.BalanceUpdate('Sai')
#BalanceEntry.BalanceCheck('Sai')
#BalanceEntry.Bal_Check_Current("Ram")