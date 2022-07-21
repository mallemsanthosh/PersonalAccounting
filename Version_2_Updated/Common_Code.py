#importing Tkinter and Required packages
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as TkFont

#For Logo
from PIL import ImageTk, Image

#Comman Data,Available Banks is Common for all Users.
Bank_List=['SBI','AXIS','Union_Bank','ICICI','Yes_Bank','APGVB','Karanataka_Bank','Punjab_National','Bank_of_Baroda']

#Creating Common Code for Creating Title and Common Head Lines for all Screens.
class Commonscreen:
    
    def Commonscreen(screen,screen_title,windows_title,username):
        screen.title(screen_title)#For Title
        screen.iconbitmap('./Assests/Icons_Images/icon1.ico')#For Icon
        screen.configure(background='#FFFACD')#For BackGround Color
        from Server import All_delete
        All_delete.All_Delete()
        #Fonts
        b_font = TkFont.Font(family='Times New Roman', weight = 'bold', size = 25)
        a_font = TkFont.Font(family='Times New Roman', weight = 'bold', size = 15)

        #Title
        Title=Label(screen,text='PERSONAL ACCOUNTING',fg='red',background='#FFFACD')
        Title['font']=b_font
        Title.pack(anchor='center',pady=10,padx=20)
        Title=Label(screen,text=windows_title,fg='blue',background="#FFFACD")
        Title['font']=a_font
        Title.pack(anchor='center')
        if(username!=''):
            from Server import Get_Data 
            name=Get_Data.Get_Name(username)
            Label(screen,text="Name : "+name[-1][0]+';  User_Name : '+username,font=('TimeNewRoman 16 bold'),background="#FFFACD",fg='#FF9933').pack(anchor='e',padx=20,pady=5)

#Exit(Terminate) Function.
def Exit_Conformation(screen,conformation):
        screen.destroy()
        conformation.destroy()
    
#Exit(Terminate) Function.
def Exit_Conformation2(screen,conformation,username):
        conformation.destroy()
        from Index import Index
        Index.Index_Screen(username,screen)

        
        
#Exit Function conformation screen..        
class Exit():
    def Exit(screen):
        conformation=tk.Tk()
        conformation.title("Conformation")
        conformation.configure(bg="white")
        l1=Label(conformation,text="\nAre you really Want to exit",bg="white")
        b1=Button(conformation,text="OK",bg="gold",command= lambda: Exit_Conformation(screen,conformation))
        l1.pack()
        b1.pack_configure(padx=50,pady=10,side=LEFT)
        b2=Button(conformation,text="Cancle",bg="gold",command=conformation.destroy)
        b2.pack(padx=50,pady=10,side=LEFT)

    def Exit2(username,screen):
        conformation=tk.Tk()
        conformation.title("Conformation")
        conformation.configure(bg="white")
        l1=Label(conformation,text="\nAre you really Want to exit",bg="white")
        b1=Button(conformation,text="OK",bg="gold",command= lambda: Exit_Conformation2(screen,conformation,username))
        l1.pack()
        b1.pack_configure(padx=50,pady=10,side=LEFT)
        b2=Button(conformation,text="Cancle",bg="gold",command=conformation.destroy)
        b2.pack(padx=50,pady=10,side=LEFT)