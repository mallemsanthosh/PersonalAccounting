
import tkinter as tk
from tkinter import *
import tkinter.font as TkFont
import re
from commoncode import *
import tableui

def RegistrationSubmit(entry1,screen,label3):
    if entry1['User Name'].get()!= "" and entry1['Password'].get()!="" and entry1['Name'].get()!="" and entry1['Phone'].get()!="" and entry1['Email'].get()!="":
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        pat2="[7-9][0-9]{9}"
        if re.match(pat,entry1['Email'].get()) and re.match(pat2,entry1['Phone'].get()):
            tableui.Tablemain.Mainloop(entry1,screen)            
        else:
            if re.match(pat,entry1['Email'].get()) and not re.match(pat2,entry1['Phone'].get()):
                label3['text']="Enter Valid Phone Number"
                label3['fg']='red'
            elif not re.match(pat,entry1['Email'].get()) and re.match(pat2,entry1['Phone'].get()):
                label3['text']="Enter Valid Email"
                label3['fg']='red'
            else:
                label3['text']="Enter Valid Email and Valid Phone Number"
                label3['fg']='red'
    else:
        label3['text']="Enter All Fields"
        label3['fg']='red'
    
def MainView(registerscreen,field,cfont):
    entries={}
    for fields in field:
        row = tk.Frame(registerscreen,background='#FFFACD')
        lab = tk.Label(row, width=15, text=fields , anchor='w',font=cfont,background='#FFFACD')
        lab2=  tk.Label(row, width=1, text=":" , anchor='w',font=cfont,background='#FFFACD')
        ent = tk.Entry(row,width=20,font=cfont)
        ent.insert(0,"")
        row.pack(side=tk.TOP,anchor=CENTER,
                padx=5,
                pady=5)
        lab.pack(side=tk.LEFT)
        lab2.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT,
                    expand=tk.YES,
                    fill=tk.X)
        entries[fields] = ent
    return entries

class Registration():
    def RegisterScreen():
        registerscreen=tk.Tk()

        Commonscreen(registerscreen,"Registration Form",'Registration Form')    
        cfont = TkFont.Font(family='Times New Roman', size = 12)
      
        field=['User Name','Password','Name','Phone','Email']
        
        ent=MainView(registerscreen,field,cfont)

        label3=Label(registerscreen,text='',background="#FFFACD")
        label3['font']=cfont
        label3.pack()
        
        row2=tk.Frame(registerscreen,background="#FFFACD")
        row2.pack(side=tk.TOP,
                    padx=50,
                    pady=10,
                    anchor=CENTER)
        Label(row2,text="For Login",fg='#0000cd',background="#FFFACD",font=('TimeNewRoman 13')).pack(side=LEFT)
        reg=Button(row2,text="Login",width=10,command= (lambda  : registerscreen.destroy() ))
        reg.pack(side=RIGHT,padx=20)          
     
        row3=tk.Frame(registerscreen,background="#FFFACD")
        row3.pack(side=tk.TOP,
                    padx=50,
                    pady=20,
                    anchor=CENTER)
        b1=Button(row3,text="Submit",command= (lambda e1=ent : RegistrationSubmit(e1,registerscreen,label3) ))
        b1.pack(side=LEFT,padx=20)
        b2=Button(row3,text="Exit",command= lambda : Exit.Exit(registerscreen))
        b2.pack(side=RIGHT,padx=20)

        registerscreen.mainloop()
    
#Registration.RegisterScreen()
