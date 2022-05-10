#Import tkinter library
from re import L
from tkinter import *
import tkinter as tk
from tkcalendar import Calendar, DateEntry

def print_sel(e,l1):
        da=e.get_date().strftime("%d-%m-%Y")
        print(type(str(e.get_date())))
        #dt2=da.strftime("%d-%m-%Y")
        print(da)
        #print(dt2) 
        l1.config(text=e.get_date())
top = tk.Tk()

Label(top, text='Choose date').pack(padx=10, pady=10)
cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
cal.pack(padx=10, pady=10)

l1=Label(top,text="")
l1.pack()

Button(top,text="Submit",command=lambda: print_sel(cal,l1)).pack()

top.mainloop()