#Tkinter is Windows Frame Creating Package.
import tkinter as tk
from tkinter import *
import tkinter.font as TkFont

#For checking Matching 
import re

#For Calling the Class and Functions These Local Files are imported
from commoncode import *
import tableui
from CreatingTable import CreateTable 

#For Checking and Validating the Fields and submiting them to next step..
def RegistrationSubmit(entry1,screen,label3):
    # For Checking the username to avoid repitation, checking the Username is present in table or not..
    chechdata=CreateTable.CheckUsername(entry1['User Name'].get())

    if entry1['User Name'].get()!= "" and entry1['Password'].get()!="" and entry1['Name'].get()!="" and entry1['Phone'].get()!="" and entry1['Email'].get()!="":
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        pat2="[7-9][0-9]{9}"
        usepat=True
        for i in (str(entry1["User Name"].get())):
            if i==" " or i=="@" or i=="!" or i=="#" or i=="$" or i=="%" or i=="^" or i=="&" or i=="*" or i=="(" or i==")" or i=="-":
                usepat=False
                break
        if re.match(pat,entry1['Email'].get()) and re.match(pat2,entry1['Phone'].get()) and usepat==True and len(chechdata)==0:
            label3.destroy()
            tableui.Tablemain.Mainloop(entry1,screen)#Open the Table Structure screen to Describe Table Structure..            
        else:
            if re.match(pat,entry1['Email'].get()) and not re.match(pat2,entry1['Phone'].get()) and len(chechdata)==0 and usepat==True:
                label3['text']="Enter Valid Phone Number"
                label3['fg']='red'
            elif not re.match(pat,entry1['Email'].get()) and re.match(pat2,entry1['Phone'].get()) and len(chechdata)==0 and usepat==True:
                label3['text']="Enter Valid Email"
                label3['fg']='red'
            elif not re.match(pat,entry1['Email'].get()) and not re.match(pat2,entry1['Phone'].get()) and len(chechdata)==0 and usepat==True:
                label3['text']="Enter Valid Email and Phone"
                label3['fg']='red'
            elif  re.match(pat,entry1['Email'].get()) and re.match(pat2,entry1['Phone'].get()) and (len(chechdata)!=0 or usepat==False):
                label3['text']="Try Another User Name \n User Name Should Not Contain Spaces"
                label3['fg']='red'
            elif  re.match(pat,entry1['Email'].get()) and not re.match(pat2,entry1['Phone'].get()) and (len(chechdata)!=0 or usepat==False):
                label3['text']="Try Another User Name \n User Name Should Not Contain Spaces \n Valid Phone Number"
                label3['fg']='red'
            elif  not re.match(pat,entry1['Email'].get()) and re.match(pat2,entry1['Phone'].get()) and (len(chechdata)!=0 or  usepat==False):
                label3['text']="Try Another User Name \n User Name Should Not Contain Spaces \n Valid Email "
                label3['fg']='red'
            else:
                label3['text']="Try another User Name \n User Name Should Not Contain Spaces \nEnter Valid Email and Phone Number"
                label3['fg']='red'
    else:
        label3['text']="Enter All Fields"
        label3['fg']='red'
    
#This Function Will create the Layout for following Fields
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


#For Registration
class Registration():
    def RegisterScreen():
        registerscreen=tk.Tk()

        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(registerscreen,"Registration Form",'Registration Form')    
        cfont = TkFont.Font(family='Times New Roman', size = 12)
      
        #The Required Fields are..
        field=['User Name','Password','Name','Phone','Email']
        
        #For Creating Layout..
        ent=MainView(registerscreen,field,cfont)

        #For Alert
        label3=Label(registerscreen,text='',background="#FFFACD")
        label3['font']=cfont
        label3.pack()
        
        #For link to Login
        row2=tk.Frame(registerscreen,background="#FFFACD")
        row2.pack(side=tk.TOP,
                    padx=50,
                    pady=10,
                    anchor=CENTER)
        Label(row2,text="For Login",fg='#0000cd',background="#FFFACD",font=('TimeNewRoman 13')).pack(side=LEFT)
        reg=Button(row2,text="Login",width=10,command= (lambda  : registerscreen.destroy() ))
        reg.pack(side=RIGHT,padx=20)          
     
        #For Submit and Exit Components
        row3=tk.Frame(registerscreen,background="#FFFACD")
        row3.pack(side=tk.TOP,
                    padx=50,
                    pady=20,
                    anchor=CENTER)
        b1=Button(row3,text="Submit",command= (lambda e1=ent : RegistrationSubmit(e1,registerscreen,label3) ))#Calls Registration Submit
        b1.pack(side=LEFT,padx=20)
        b2=Button(row3,text="Exit",command= lambda : Exit.Exit(registerscreen))#Exit the Screen.
        b2.pack(side=RIGHT,padx=20)

        #For Exicuting the Screen
        registerscreen.mainloop()
    
#Checking Purpose:-
#Registration.RegisterScreen()
