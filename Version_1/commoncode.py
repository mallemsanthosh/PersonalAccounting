#importing Tkinter and Required packages
import tkinter as tk
from tkinter import *
import tkinter.font as TkFont

#Creating Common Code for Creating Title and Common Head Lines for all Screens.
class Commonscreen:
    def Commonscreen(screen,maintitle,titless):
        screen.title(maintitle)#For Title
        screen.configure(background='#FFFACD')

        bfont = TkFont.Font(family='Times New Roman', weight = 'bold', size = 25)
        afont = TkFont.Font(family='Times New Roman', weight = 'bold', size = 15)
        
        Titel=Label(screen,text='\nPERSONAL ACCOUNTING',fg='red',background='#FFFACD')
        Titel['font']=bfont
        Titel.pack(anchor='center')
        Titel=Label(screen,text=titless,fg='blue',background="#FFFACD")
        Titel['font']=afont
        Titel.pack(anchor='center')


#Exit(Terminate) Function.
def Exit1(screen,conformation):
        conformation.destroy()
        screen.destroy()
        
#Exit Function conformation screen..        
class Exit():
    def Exit(screen):
        conformation=tk.Tk()
        conformation.title("Conformation")
        conformation.configure(bg="white")
        l1=Label(conformation,text="\nAre you really Want to exit",bg="white")
        b1=Button(conformation,text="OK",bg="gold",command= lambda : Exit1(screen,conformation))
        l1.pack()
        b1.pack_configure(padx=50,pady=10,side=LEFT)
        b2=Button(conformation,text="Cancle",bg="gold",command=conformation.destroy)
        b2.pack(padx=50,pady=10,side=LEFT)

    