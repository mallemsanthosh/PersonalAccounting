import tkinter as tk
from tkinter import *
import tkinter.font as TkFont
from commoncode import *
from Registration import *

import tableui
#def Validationlogic(username,password):




class StartApp():
    def Validation():
        validatee=tk.Tk()
        validatee.title("Login Screen")
        validatee.configure(background='#FFFACD')

        bfont = TkFont.Font(family='Times New Roman', weight = 'bold', size = 25)
        afont = TkFont.Font(family='Times New Roman', weight = 'bold', size = 15)
        cfont = TkFont.Font(family='Times New Roman', size = 13)
       
        Titel=Label(validatee,text='\nWELCOME\nTO\nPERSONAL ACCOUNTING',fg='red',background='#FFFACD')
        Titel['font']=bfont
        Titel.pack(anchor='center')
        Titel=Label(validatee,text='\nLogin Form',fg='blue',background="#FFFACD")
        Titel['font']=afont
        Titel.pack(anchor='center')
       
        row=tk.Frame(validatee,background='#FFFACD')
        row.pack(side=tk.TOP,
                fill=tk.X,
                    padx=5,
                    pady=5)
        label1=Label(row,text='\nEnter the User Name :',background="#FFFACD")
        label1['font']=cfont
        label1.pack()

        username = tk.Entry(row,width=25)
        username.insert(0, "")
        username['font']=cfont
        username.pack()
        
        label2=Label(row,text='\nEnter the Password :',background="#FFFACD")
        label2['font']=cfont
        label2.pack()

        password= tk.Entry(row,show='*',width=25)
        password.insert(0, "")
        password['font']=cfont
        password.pack()
        
        row2=tk.Frame(validatee,background="#FFFACD")
        row2.pack(side=tk.TOP,
                    padx=50,
                    pady=10,
                    anchor=CENTER)          
        Label(row2,text="For New Account/Registration",fg='#0000cd',background="#FFFACD",font=('TimeNewRoman 13')).pack(side=LEFT)
        reg=Button(row2,text="Register",width=10,command= (lambda  : Registration.RegisterScreen() ))
        reg.pack(side=RIGHT,padx=20)

        row3=tk.Frame(validatee,background="#FFFACD")
        row3.pack(side=tk.TOP,
                    padx=50,
                    pady=20,
                    anchor=CENTER)
        b1=Button(row3,text="Submit",command= (lambda e1=username,e2=password : StartApp.Main() ))
        b1.pack(side=LEFT,padx=20)
        b2=Button(row3,text="Exit",command= lambda : Exit.Exit(validatee))
        b2.pack(side=RIGHT,padx=20)

        validatee.mainloop()
    def Main():
        tableui.Tablemain.Mainloop()

StartApp.Validation()
