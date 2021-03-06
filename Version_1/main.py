#Tkinter is Windows Frame Creating Package.
import tkinter as tk
from tkinter import *
import tkinter.font as TkFont

#From Call the Class and Functions These Local Files are imported
from commoncode import *
from Registration import *
from CreatingTable import *
from SelectionPage import *

#Login Validation Logic
def ValidationLogic(username,password,label3,validate):
    if username.get()=="" and password.get()=="":
        label3['text']="Enter User Name and Password"
        label3['fg']='red'
    elif password.get()=="":
        label3['text']="Enter Password"
        label3['fg']='red'
    elif username.get()=="":
        label3['text']="Enter User Name"
        label3['fg']='red'
    else:
        result=CreateTable.Validate(username.get())#Validate the User and Password From Database
        if result==[] or result[0][1]!=username.get():
            label3['text']="Enter Valid User Name and Password\n or Regiester to Login"
            label3['fg']='red'
        else:
            if result[0][2]==password.get():
                label3['text']="Success"
                label3['fg']='green'
                SelectionPage.Main(username.get(),validate)#After Success FUll Validation, the Selection Page Will be Open.
            else:
                label3['text']="Password Wrong"
                label3['fg']='red'

#It is the Starting Window that will appear while we open the Application.
class StartApp():
    def Validation():
        validatee=tk.Tk()
        validatee.title("Login Screen")
        validatee.configure(background='#FFFACD')

        #Creating Table for Authentication Purpose
        CreateTable.AuthenticationTab()#For New User it will Create DataBase and New Authentication  Table

        #Fonts which are used to Display the Charaters on the Screen
        bfont = TkFont.Font(family='Times New Roman', weight = 'bold', size = 25)
        afont = TkFont.Font(family='Times New Roman', weight = 'bold', size = 15)
        cfont = TkFont.Font(family='Times New Roman', size = 13)
       
        #Titels 
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

        #For Alert
        label3=Label(row,text='',background="#FFFACD")
        label3['font']=cfont
        label3.pack()
        
        #For Registration Command
        row2=tk.Frame(validatee,background="#FFFACD")
        row2.pack(side=tk.TOP,
                    padx=50,
                    pady=10,
                    anchor=CENTER)          
        Label(row2,text="For New Account/Registration",fg='#0000cd',background="#FFFACD",font=('TimeNewRoman 13')).pack(side=LEFT)
        reg=Button(row2,text="Register",width=10,command= (lambda  : Registration.RegisterScreen() ))#Calls the Registration Screen
        reg.pack(side=RIGHT,padx=20)

        #For Submit and Exit Layout
        row3=tk.Frame(validatee,background="#FFFACD")
        row3.pack(side=tk.TOP,
                    padx=50,
                    pady=20,
                    anchor=CENTER)
        b1=Button(row3,text="Login",command= (lambda e1=username,e2=password : ValidationLogic(e1,e2,label3,validatee) ))#Calls the Validation Logic
        b1.pack(side=LEFT,padx=20)
        b2=Button(row3,text="Exit",command= lambda : Exit.Exit(validatee))#Exit the Screen.
        b2.pack(side=RIGHT,padx=20)

        #For Opening the window.
        validatee.mainloop()

#Execution Starts From Here...
StartApp.Validation()
