import sys
import tkinter as tk
from tkinter import *
import os
import csv
import pandas as pa

from CreatingTable import CreateTable


def Conformation(conformation):
        conformation.destroy()
        python = sys.executable
        os.execl(python, python, * sys.argv)
class Logout:

    def Logout():   
        conformation=tk.Tk()
        conformation.title("Conformation")
        conformation.configure(bg="white")
        l1=Label(conformation,text="\nAre you really Want to Logout",bg="white")
        l1.pack()
        b1=Button(conformation,text="Yes",bg="gold",command=lambda: Conformation(conformation))
        b1.pack_configure(padx=50,pady=10,side=LEFT)
        b2=Button(conformation,text="No",bg="gold",command=conformation.destroy)
        b2.pack(padx=50,pady=10,side=LEFT)


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