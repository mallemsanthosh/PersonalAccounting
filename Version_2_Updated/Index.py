#importing the Common Function Which are in  Common_code
from Common_Code import *
from Account_Update import Balance_Update,Credit_Update,Debit_Update
from Account_Balance_Check import Current_Balance,Date_Sheet,Year_Sheet,Month_Sheet,Date_to_Date_Sheet
from Server import Get_Data

class Index():
    def Index_Screen(username,login_screen):
        login_screen.destroy()
        index_screen=tk.Tk()
        
        #setting tkinter window size as maximized
        index_screen.state('zoomed')
        
        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(index_screen,"Index Form",'Index/Selection Form',username)    
       
        index_screen.configure(bg="#FFFACD")

        #For Button Layout Space       
        row2=tk.Frame(index_screen,background="#FFFACD")
        row2.pack(side=tk.TOP,
                    padx=50,
                    pady=10,
                    anchor=CENTER)
        
        #For Creating Layout..
        Index.Mainfields(row2,index_screen,username)
        index_screen.mainloop()

    #It will Create Layout of the Index/Selection Page Screen
    def Mainfields(index_row,index_screen,username):
        from Login import Login
        selectframe_update=[
                    {"label":"This is for Updating Balance",
                    "button":"Balance_Update",
                    "condition":(lambda: Balance_Update.Balance_Update_Screen(index_screen,username))},#For Balance Entry
                    {"label":"This is for Updating Credit",
                    "button":"Credit_Update",
                    "condition":(lambda: Credit_Update.Credit_Update_Screen(index_screen,username))},#For Credit Entry
                    {"label":"This is for Updating Debit",
                    "button":"Debit_Update",
                    "condition":(lambda: Debit_Update.Debit_Update_Screen(index_screen,username))}]#For Debit Entry
        selectframe_View=[{"label":"This is for Checking Current Balance ",
                    "button":"Balance_Checking",
                    "condition":(lambda: Current_Balance.Current_Balance_Screen(index_screen,username))},#For Balance Check, For Current Date.
                    {"label":"This is for Checking Balance for Particular Date",
                    "button":"Date_Sheet",
                    "condition":(lambda: Date_Sheet.Date_Sheet_Screen(index_screen,username))},#Balance Check for Particualar Date.
                    {"label":"This is for Checking Balance In between two Dates",
                    "button":"Date_to_Date_Sheet",
                    "condition":(lambda: Date_to_Date_Sheet.Date_to_Date_Sheet_Screen(index_screen,username))},#Balance Check in between two Dates.
                    {"label":"This is for Checking Balance for Particular Month",
                    "button":"Montly_Sheet",
                    "condition":(lambda: Month_Sheet.Month_Sheet_Screen(index_screen,username))},#For Balance Check for Particular Month.
                    {"label":"This is for Checking Balance for Particular Year",
                    "button":"Yearly_Sheet",
                    "condition":(lambda: Year_Sheet.Year_Sheet_Screen(index_screen,username))},#Balance Check for Particular Year.
                    ]
        from Registration import Account_Delete,Update_User_Details    
        selectframe_operations=[{"label":"To Updating Your User Details(Password,username etc.)",
                    "button":"Update Account",
                    "condition":lambda: Update_User_Details.Update_User_Details_Screen(username,index_screen)},#For Updating the User details like Password, User_Name,Phone_No,E_Mail.
                    {"label":"This is for To Delete Your Account",
                    "button":"Delete Account",
                    "condition":lambda: Account_Delete.Delete_Account(username,index_screen)},#Delete User Account.
                    {"label":"This is for Logout",
                    "button":"Logout",
                    "condition":lambda : Login.User_Login(index_screen)},#For Logout the User.
                    {"label":"This is for Exit/Close Application",
                    "button":"Exit",
                    "condition":lambda : Exit.Exit(index_screen)}]#For Exit the Current Screen (It will Close the Application.)
        row_main=tk.Frame(index_row,tk.Frame(index_row,background='#FFFACD'))
        row_main.pack(side=tk.TOP,anchor=CENTER,
                    padx=2,
                    pady=2)
        Label(row_main,text="For Updating Accounts",font=('TimeNewRoman 16 bold'), width=40,bg="#FFFACD",fg='#2D0064').pack(anchor='center')   
        Balance_Check=True
        Banks_fields=Get_Data.For_Fields(username)
        for bank in Banks_fields:
            if bank!="Date" and bank!='Total':
                query="select Date from "+bank+"_Table where User_Name='"+username+"'"
                data=Get_Data.Get_Balance_For_Display(query)
                if data==[]:
                    Balance_Check=True
                    break
                else:
                    Balance_Check=False
        for a in range (len(selectframe_update)):
            if Balance_Check==False and selectframe_update[a]['button']=='Balance_Update':
                pass
            else:
                row = tk.Frame(row_main,background='#FFFACD')
                l0 = Label(row,text=selectframe_update[a]['label'],font=('TimeNewRoman 13'),width=50,bg="#FFFACD")
                b0 = Button(row, text=selectframe_update[a]['button'],font=('TimeNewRoman 13'),width=20,height=1,command=selectframe_update[a]['condition'])
                row.pack(side=tk.TOP,anchor=CENTER,
                        padx=2,
                        pady=2)
                l0.pack(side=RIGHT, pady=2,anchor='w')
                b0.pack(side=LEFT, pady=2, padx=5)
        
        Label(row_main,text="For Checking of Viewing Accounts",font=('TimeNewRoman 16 bold'), width=40,bg="#FFFACD",fg='#8B0000').pack(anchor='center')   
        for a in range (len(selectframe_View)):
            row = tk.Frame(row_main,background='#FFFACD')
            l0 = Label(row,text=selectframe_View[a]['label'],font=('TimeNewRoman 13'), width=50,bg="#FFFACD")
            b0 = Button(row, text=selectframe_View[a]['button'],font=('TimeNewRoman 13'),width=20,height=1,command=selectframe_View[a]['condition'])
            row.pack(side=tk.TOP,anchor=CENTER,
                    padx=2,
                    pady=2)
            l0.pack(side=RIGHT, pady=2,anchor='w')
            b0.pack(side=LEFT, pady=2, padx=5)

        Label(row_main,text="For Managing User Account",font=('TimeNewRoman 16 bold'), width=40,bg="#FFFACD",fg='#FF4932').pack(anchor='center')   
        for a in range (len(selectframe_operations)):
            row = tk.Frame(row_main,background='#FFFACD')
            l0 = Label(row,text=selectframe_operations[a]['label'],font=('TimeNewRoman 13'), width=50,bg="#FFFACD")
            b0 = Button(row, text=selectframe_operations[a]['button'],font=('TimeNewRoman 13'),width=20,height=1,command=selectframe_operations[a]['condition'])
            row.pack(side=tk.TOP,anchor=CENTER,
                    padx=2,
                    pady=2)
            l0.pack(side=RIGHT, pady=2,anchor='nw')
            b0.pack(side=LEFT, pady=2, padx=5)
