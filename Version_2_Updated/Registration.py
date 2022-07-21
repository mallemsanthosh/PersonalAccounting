#For checking Matching 
import re
from tkinter import messagebox

#importing the Common Function Which are in  Common_code
from Common_Code import *
from Login import Login

#Server side Imports
from Server import Validation_Server,Building_Server,Update_Authentication_Server

#Registration Class
class Registration:
    #For Checking and Validating the Fields and submiting them to next step..
    def Registration_Submit(entry1,registration_screen,label3):
        # For Checking the username to avoid repitation, checking the Username is present in table or not..
        check_username=Validation_Server.Check_Username(entry1['User Name'].get())

        if entry1['User Name'].get()!= "" and entry1['Password'].get()!="" and entry1['Name'].get()!="" and entry1['Phone'].get()!="" and entry1['Email'].get()!="":
            Email_Pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
            Phone_No_Pattern="[7-9][0-9]{9}"
            Username_Pattren=True
            for i in (str(entry1["User Name"].get())):
                if i==" " or i=="@" or i=="!" or i=="#" or i=="$" or i=="%" or i=="^" or i=="&" or i=="*" or i=="(" or i==")" or i=="-":
                    Username_Pattren=False
                    break
            if re.match(Email_Pattern,entry1['Email'].get()) and re.match(Phone_No_Pattern,entry1['Phone'].get()) and Username_Pattren==True and len(check_username)==0:
                label3.destroy()
                Table_Structure.Table_Structure(entry1,registration_screen)#Open the Table Structure screen to Describe Table Structure..            
            else:
                if re.match(Email_Pattern,entry1['Email'].get()) and not re.match(Phone_No_Pattern,entry1['Phone'].get()) and len(check_username)==0 and Username_Pattren==True:
                    label3['text']="Enter Valid Phone Number"
                    label3['fg']='red'
                elif not re.match(Email_Pattern,entry1['Email'].get()) and re.match(Phone_No_Pattern,entry1['Phone'].get()) and len(check_username)==0 and Username_Pattren==True:
                    label3['text']="Enter Valid Email"
                    label3['fg']='red'
                elif not re.match(Email_Pattern,entry1['Email'].get()) and not re.match(Phone_No_Pattern,entry1['Phone'].get()) and len(check_username)==0 and Username_Pattren==True:
                    label3['text']="Enter Valid Email and Phone"
                    label3['fg']='red'
                elif  re.match(Email_Pattern,entry1['Email'].get()) and re.match(Phone_No_Pattern,entry1['Phone'].get()) and (len(check_username)!=0 or Username_Pattren==False):
                    label3['text']="Try Another User Name \n User Name Should Not Contain Spaces"
                    label3['fg']='red'
                elif  re.match(Email_Pattern,entry1['Email'].get()) and not re.match(Phone_No_Pattern,entry1['Phone'].get()) and (len(check_username)!=0 or Username_Pattren==False):
                    label3['text']="Try Another User Name \n User Name Should Not Contain Spaces \n Valid Phone Number"
                    label3['fg']='red'
                elif  not re.match(Email_Pattern,entry1['Email'].get()) and re.match(Phone_No_Pattern,entry1['Phone'].get()) and (len(check_username)!=0 or  Username_Pattren==False):
                    label3['text']="Try Another User Name \n User Name Should Not Contain Spaces \n Valid Email "
                    label3['fg']='red'
                else:
                    label3['text']="Try another User Name \n User Name Should Not Contain Spaces \nEnter Valid Email and Phone Number"
                    label3['fg']='red'
        else:
            label3['text']="Enter All Fields"
            label3['fg']='red'

    #This Function Will create the Layout for following Fields
    def MainView(register_screen,field,c_font):
        registration_entries={}
        for fields in field:
            row = tk.Frame(register_screen,background='#FFFACD')
            lab = tk.Label(row, width=15, text=fields , anchor='w',font=c_font,background='#FFFACD')
            lab2=  tk.Label(row, width=1, text=":" , anchor='w',font=c_font,background='#FFFACD')
            ent = tk.Entry(row,width=20,font=c_font)
            ent.insert(0,"")
            row.pack(side=tk.TOP,anchor=CENTER,
                    padx=5,
                    pady=5)
            lab.pack(side=tk.LEFT)
            lab2.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT,
                        expand=tk.YES,
                        fill=tk.X)
            registration_entries[fields] = ent
        return registration_entries

    #For Registration
    def Register_Screen(screen):
        screen.destroy()
        register_screen=tk.Tk()
        #setting tkinter window size as maximized
        register_screen.state('zoomed')
        
        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(register_screen,"Registration Form",'Registration Form','')    
       
        #Fonts
        c_font = TkFont.Font(family='Times New Roman', size = 14)
      
        #The Required Fields are..
        registration_field=['User Name','Password','Name','Phone','Email']
        
        #For Creating Layout..
        registration_entries=Registration.MainView(register_screen,registration_field,c_font)

        #For Alert
        label3=Label(register_screen,text='',background="#FFFACD")
        label3['font']=c_font
        label3.pack()
        
        #For link to Login
        row2=tk.Frame(register_screen,background="#FFFACD")
        row2.pack(side=tk.TOP,
                    padx=10,
                    pady=10,
                    anchor=CENTER)
        Label(row2,text="For Login",fg='#0000cd',background="#FFFACD",font=('TimeNewRoman 13')).pack(side=LEFT)
        reg=Button(row2,text="Login", font=('TimeNewRoman 13'),width=10,command= (lambda  : Login.User_Login(register_screen) ))
        reg.pack(side=RIGHT,padx=20)          
     
        #For Submit and Exit Components
        row3=tk.Frame(register_screen,background="#FFFACD")
        row3.pack(side=tk.TOP,
                    padx=50,
                    pady=20,
                    anchor=CENTER)
        b1=Button(row3,text="Submit",font=('TimeNewRoman 13'),width=10,command= (lambda e1=registration_entries : Registration.Registration_Submit(e1,register_screen,label3) ))#Calls Registration Submit
        b1.pack(side=LEFT,padx=20)
        b2=Button(row3,text="Exit",font=('TimeNewRoman 13'),width=10,command= lambda : Exit.Exit(register_screen))#Exit the Screen.
        b2.pack(side=RIGHT,padx=20)

        #For Exicuting the Screen
        register_screen.mainloop()

#For Table Structure
class Table_Structure:
    #Global variables
    global entry_number
    entry_number=0
    global table_entries
    table_entries={}
    
    #Table_structure start exicution from here
    def Table_Structure(registration_entries,registration_screen):
        table_ui_screen=tk.Tk()
        c_font = TkFont.Font(family='Times New Roman', size = 12)

        #setting tkinter window size as maximized
        table_ui_screen.state('zoomed')
        
        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(table_ui_screen,"Table or Accounting Stucture",'Create Your Fields Structure','')
        
        #Global Variables
        global entry_number 
        entry_number = 0   
        
        #For layout
        row_1 = tk.Frame(table_ui_screen,background='#FFFACD')
        row_1.pack(anchor="center")
        
        Table_Structure.Mainview(row_1,c_font)#Create the Entry Layout  

        #For adding extra field to Enter Our Response
        row2 = tk.Frame(table_ui_screen,background='#FFFACD')
        row2.pack(anchor=CENTER)
        btn = tk.Button(row2, width=15,text="ADD", font=('TimeNewRoman 13'),command = (lambda  : Table_Structure.Mainview(row_1,c_font)))
        btn.pack(side=tk.LEFT, padx=10)
        #For Alert
        display_lable=Label(row2,text="",background='#FFFACD',fg='red').pack()
        
        #For Submit and Exit Components 
        row3 = tk.Frame(table_ui_screen,background='#FFFACD')
        row3.pack(anchor=CENTER)
        #Submiting the Table_Ui
        b1=tk.Button(row3,text="Submit",font=('TimeNewRoman 13'),command=lambda: Table_Structure.Table_Ui_ConformationScreen(table_ui_screen,registration_entries,registration_screen,display_lable))
        b1.pack(side=tk.LEFT,pady=10)
        b2=tk.Button(row3,text="Exit",font=('TimeNewRoman 13'), command= lambda : Exit.Exit(table_ui_screen))
        b2.pack(side=tk.LEFT,padx=50,pady=10)

        table_ui_screen.mainloop()

    #Defining the Frame
    def Mainview(table_ui_screen,c_font):
        #Global variables
        global table_entries
        global entry_number
        entry_number= entry_number+1
        
        row = tk.Frame(table_ui_screen,background='#FFFACD')
        lab = tk.Label(row, width=15, text=("Enter"+str(entry_number)) + "\t: ", anchor='w',font=c_font,background='#FFFACD')
        ent1=ttk.Combobox(row,state="readonly",values=Bank_List,font=c_font)
        if(entry_number!=1):
            #Below button will destroy the entry field
            button=Button(row, width=15,text="Delete",bg="gold",font=('TimeNewRoman 13'),command= lambda e1=entry_number,r=row : Table_Structure.Destroy_Entry_row(e1,r))
        row.pack(side=tk.TOP,
                    fill=tk.X,
                    padx=100,
                    pady=10)
        lab.pack(side=tk.LEFT)
        ent1.pack(side=tk.LEFT,
                    fill=tk.X)
        if(entry_number!=1):
            button.pack(side=tk.LEFT,padx=5)
        table_entries[entry_number]= ent1
        return ()

    #For the destory unused Entry Field in Table_Ui
    def Destroy_Entry_row(entry_number,row):
        row.destroy()
        global table_entries
        table_entries.pop(entry_number)

    #For Checking All fields are Entered or Not..
    def Table_Ui_ConformationScreen(table_screen,registration_entries,registration_screen,row1):
        Field_empty=False
        for j in table_entries:
            if str(table_entries[j].get())=="" or str(table_entries[j].get())==" ":
                row1['text']="Enter ALl Fields"
                Field_empty=True
                break
        if Field_empty==False:
            #For Conforming to Submit
            conformation_screen=tk.Tk()
            conformation_screen.title("Conformation")
            conformation_screen.configure(bg="white")
            l1=Label(conformation_screen,text="\nAre you really Want to Submit The Fields",bg="white")
            l1.pack()
            b1=Button(conformation_screen,text="OK",bg="gold",command=lambda: Table_Structure.Table_Ui_Conformation(table_screen,conformation_screen,registration_entries,registration_screen))
            b1.pack_configure(padx=50,pady=10,side=LEFT)
            b2=Button(conformation_screen,text="Cancle",bg="gold",command=conformation_screen.destroy)
            b2.pack(padx=50,pady=10,side=LEFT)
    
    # After Conformation, the Form will be submitted and adding the Columns in Database
    def Table_Ui_Conformation(table_ui_screen,conformation_screen,registration_entries,registration_screen):
        conformation_screen.destroy()
        entries_data_queary =[]
        fields='Date'
        for j in table_entries:
            fields=fields+','+str(table_entries[j].get())
            entries_data_queary.append(str(table_entries[j].get())+" varchar(100)")
        fields=fields+','+'Total'
        

        Update_Authentication_Server.Update_Fields(fields,registration_entries) #Rember the Fields for Future Use
        
        table_ui_screen.destroy()               #Destroy the table_ui Screen
        registration_screen.destroy()            #Destroy the Screen

        #This is display Conformation message and ask for What next
        After_Registration_screen=tk.Tk()
        #Windows Screen Configuration
        After_Registration_screen.configure(background='#FFFACD')
        #setting tkinter window size as maximized
        After_Registration_screen.state("zoomed")
        
        #Fonts
        c_font = TkFont.Font(family='Times New Roman', size = 15,weight='bold')
        
        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(After_Registration_screen,"Registration Submitted","Registration Submitted Conformaition",'')    
       
        #Button Layout
        #Login
        row_1=tk.Frame(After_Registration_screen,background='#FFFACD')
        row_1.pack(pady=10,padx=20)
        reg=Button(row_1,text="LOGIN",width=15,font=c_font,foreground="navy",command= (lambda  : Login.User_Login(After_Registration_screen) ))#Calls the Login Screen
        reg.pack(anchor='center',pady=10)
        
        #Register
        reg=Button(row_1,text="REGISTER\nANOTHER USER",width=15,font=c_font,foreground="navy",command= (lambda  : Registration.Register_Screen(After_Registration_screen)))#Calls the Registration Screen
        reg.pack(anchor='center',pady=10)

        #Exit Layout
        b2=Button(row_1,text="EXIT",width=15,font=c_font,foreground="navy",command= lambda : Exit.Exit(After_Registration_screen))#Exit the Screen.
        b2.pack(anchor='center',pady=10)
        
        #For Opening the window.
        After_Registration_screen.mainloop()        


#For Deleting User_Account
class Account_Delete:
    #This code will give Conformation Screen where we should give conformation.
    def Delete_Account(username,index_screen):   
        delete_conformation=tk.Tk()
        delete_conformation.title("Delete_Conformation")
        delete_conformation.configure(bg="white")
        l1=Label(delete_conformation,text="\nAre you really Want to Delete Account",bg="white")
        l1.pack()
        b1=Button(delete_conformation,text="Yes",bg="gold",command=lambda: Account_Delete.Delete_Conformation(username,delete_conformation,index_screen))
        b1.pack_configure(padx=50,pady=10,side=LEFT)
        b2=Button(delete_conformation,text="No",bg="gold",command=delete_conformation.destroy)
        b2.pack(padx=50,pady=10,side=LEFT)
    #If we give authentication to Then deletion will be done.
    def Delete_Conformation(username,delete_conformation,index_screen):
        delete_conformation.destroy()
        index_screen.destroy()
        Update_Authentication_Server.Delete_Account(username)#Delete User related Tables and Authentication Details from Database.
        Login.User_Login()#Redirect to Login Page.

#For Updating the User Details
class Update_User_Details:
    def Update_User_Details_Screen(username,screen):
        screen.destroy()
        user_details=Validation_Server.User_Details(username)
        fields={}
        fields['Name']=user_details[0][5]
        fields['User Name']=user_details[0][1]
        fields['Password']=user_details[0][2]
        fields['Phone']=user_details[0][3]
        fields['Email']=user_details[0][4]
        
        update_screen=tk.Tk()
        #setting tkinter window size as maximized
        update_screen.state('zoomed')
        
        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(update_screen,"Update User Details",'Update User Details','')    
       
        #Fonts
        c_font = TkFont.Font(family='Times New Roman', size = 14)
      
        
        #For Creating Layout..
        updated_entries=Update_User_Details.MainView(update_screen,fields,c_font)

        #For Alert
        label3=Label(update_screen,text='',background="#FFFACD")
        label3['font']=c_font
        label3.pack()
        
        #For link to Login
        row2=tk.Frame(update_screen,background="#FFFACD")
        row2.pack(side=tk.TOP,
                    padx=10,
                    pady=10,
                    anchor=CENTER)
        Label(row2,text="For Logout",fg='#0000cd',background="#FFFACD",font=('TimeNewRoman 13')).pack(side=LEFT)
        reg=Button(row2,text="Logout", font=('TimeNewRoman 13'),width=10,command= (lambda  : Login.User_Login(update_screen) ))
        reg.pack(side=RIGHT,padx=20)

        #For link to Index/Selection Page
        row2=tk.Frame(update_screen,background="#FFFACD")
        row2.pack(side=tk.TOP,
                    padx=10,
                    pady=10,
                    anchor=CENTER)
        Label(row2,text="For Exiting From edit Form",fg='#0000cd',background="#FFFACD",font=('TimeNewRoman 13')).pack(side=LEFT)
        from Index import Index# To Avoid the Loop in code inline import was done
        reg=Button(row2,text="Cancle Edit", font=('TimeNewRoman 13'),width=10,command= (lambda  : Index.Index_Screen(username,update_screen) ))
        reg.pack(side=RIGHT,padx=20)          
     
        #For Submit and Exit Components
        row3=tk.Frame(update_screen,background="#FFFACD")
        row3.pack(side=tk.TOP,
                    padx=50,
                    pady=20,
                    anchor=CENTER)
        b1=Button(row3,text="Submit",font=('TimeNewRoman 13'),width=10,command= (lambda e1=updated_entries : Update_User_Details.Update_User_Details_Submit(e1,update_screen,label3)))#Calls Registration Submit
        b1.pack(side=LEFT,padx=20)
        b2=Button(row3,text="Exit",font=('TimeNewRoman 13'),width=10,command= lambda : Exit.Exit(update_screen))#Exit the Screen.
        b2.pack(side=RIGHT,padx=20)

        #For Exicuting the Screen
        update_screen.mainloop()

    #This Function Will create the Layout for following Fields
    def MainView(update_screen,field,c_font):
        update_entries={}
        for fields in field:
            row = tk.Frame(update_screen,background='#FFFACD')
            lab = tk.Label(row, width=15, text=fields , anchor='w',font=c_font,background='#FFFACD')
            lab2=  tk.Label(row, width=1, text=":" , anchor='w',font=c_font,background='#FFFACD')
            if fields=="User Name" or fields=="Name":
                ent = tk.Entry(row,width=20,font=c_font)
                ent.insert(0,field[fields])
                ent['state']='disabled'
            else:
                ent = tk.Entry(row,width=20,font=c_font)
                ent.insert(0,field[fields])
            row.pack(side=tk.TOP,anchor=CENTER,
                    padx=5,
                    pady=5)
            lab.pack(side=tk.LEFT)
            lab2.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT,
                        expand=tk.YES,
                        fill=tk.X)
            update_entries[fields] = ent
        return update_entries

    #For Submitting Edited User Details
    def Update_User_Details_Submit(entry1,update_screen,label3):
        if entry1['User Name'].get()!= "" and entry1['Password'].get()!="" and entry1['Name'].get()!="" and entry1['Phone'].get()!="" and entry1['Email'].get()!="":
            Email_Pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
            Phone_No_Pattern="[7-9][0-9]{9}"
            
            if re.match(Email_Pattern,entry1['Email'].get()) and re.match(Phone_No_Pattern,entry1['Phone'].get()):
                Update_Authentication_Server.Update_User_Details(entry1['User Name'].get(),entry1['Password'].get(),entry1['Phone'].get(),entry1['Email'].get())#Open the Table Structure screen to Describe Table Structure..            
                label3['text']="Successfully Updated the Details"
                label3['fg']="green"
                messagebox.showinfo("Success","User Details Updated Successfully")#Success information Popup.
                Login.User_Login(update_screen)
            else:
                if re.match(Email_Pattern,entry1['Email'].get()) and not re.match(Phone_No_Pattern,entry1['Phone'].get()):
                    label3['text']="Enter Valid Phone Number"
                    label3['fg']='red'
                elif not re.match(Email_Pattern,entry1['Email'].get()) and re.match(Phone_No_Pattern,entry1['Phone'].get()):
                    label3['text']="Enter Valid Email"
                    label3['fg']='red'
                elif not re.match(Email_Pattern,entry1['Email'].get()) and not re.match(Phone_No_Pattern,entry1['Phone'].get()):
                    label3['text']="Enter Valid Email and Phone"
                    label3['fg']='red'
        else:
            label3['text']="Enter All Fields"
            label3['fg']='red'