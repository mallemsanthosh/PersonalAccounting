import tkinter as tk
from tkinter import *
import tkinter.font as TkFont
from turtle import color
import tableui




class StartApp():
    def Validation():
        validatee=tk.Tk()
        validatee.title("Login Screen")
        bfont = TkFont.Font(family='Times New Roman', weight = 'bold', size = 30)
        Titel=Label(validatee,text='\nWELCOME\nTO\nPERSONAL ACCOUNTING',fg='red')
        Titel['font']=bfont
        Titel.pack(anchor='center')
        
        validatee.mainloop()
    def Main():
        tableui.Tablemain.Mainloop()

StartApp.Validation()
