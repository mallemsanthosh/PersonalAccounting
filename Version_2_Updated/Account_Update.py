#Importing Common Data like Bank_Names, code for title and exit etc.
import random
from Common_Code import *
from Server import Get_Data,Update_Bank_Tables
from tkcalendar import DateEntry
import tkinter as tk
from tkinter import *
import tkinter.font as TkFont



#Comman Functions which is used in Updating Pages
class Common_Elements:
    #Entry Layout
    def MainView(view_screen,field,c_font):
        Update_entries={}
        for fields in field:
            if fields!="Total":
                row = tk.Frame(view_screen,background='#FFFACD')
                lab = tk.Label(row, width=15, text=fields , anchor='w',font=c_font,background='#FFFACD')
                lab2=  tk.Label(row, width=1, text=":" , anchor='w',font=c_font,background='#FFFACD')
                if fields == "Date":
                    ent = DateEntry(row, width=17,font=c_font, background='darkblue',
                        foreground='white',borderwidth=2)
                else:
                    ent = tk.Entry(row,width=20,font=c_font)
                    ent.insert(0,"0")
                row.pack(side=tk.TOP,anchor=CENTER,
                        padx=5,
                        pady=5)
                lab.pack(side=tk.LEFT)
                lab2.pack(side=tk.LEFT)
                ent.pack(side=tk.RIGHT,
                            expand=tk.YES,
                            fill=tk.X)
                Update_entries[fields] = ent
        return Update_entries

    def Transaction_Id():
        Transaction_Number="TN"+str(random.randrange(10,99))+chr(random.randint(65,90))+chr(random.randint(65,90))+str(random.randint(1000,9999))
        return (Transaction_Number)

#For Updating the Balance
class Balance_Update:
    #This Function Will create the Layout for Given Fields
    def Balance_Update_Screen(index_screen,username):
        index_screen.destroy()
        balance_update_screen=tk.Tk()
        #setting tkinter window size as maximized
        balance_update_screen.state('zoomed')
        
        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(balance_update_screen,"Balance Update Form",'Balance Update Form',username)    
       
        #Fonts
        c_font = TkFont.Font(family='Times New Roman', size = 14)
        #Getting the User Using Banks list from Server
        Banks_fields=tuple(Get_Data.For_Fields(username))
        Banks_fields_updated=list(Banks_fields)
        for bank in Banks_fields:
            if bank!="Date" and bank!='Total':
                query="select Date from "+bank+"_Table where User_Name='"+username+"'"
                data=Get_Data.Get_Balance_For_Display(query)
                if data!=[]:
                    Banks_fields_updated.remove(bank)
        #Creating Data Entry Form for Balance 
        row_1=tk.Frame(balance_update_screen,background="#FFFACD")
        row_1.pack(side=tk.TOP,
                        anchor=CENTER) 
        balance_data=Common_Elements.MainView(row_1,Banks_fields_updated,c_font)

        #For Displaying Udated Result
        row_2=tk.Frame(balance_update_screen,background="#FFFACD")
        row_2.pack(side=tk.TOP,
                        anchor=CENTER) 
        
       #For Submit and Exit Components 
        row3 = tk.Frame(balance_update_screen,background='#FFFACD')
        row3.pack(anchor=CENTER)
        #Submiting the Table_Ui
        b1=tk.Button(row3,text="Submit",font=('TimeNewRoman 13'),command=lambda e1=balance_data: Balance_Update.Bal_SubmitEntry(e1,username,Banks_fields_updated,row_1,row_2,b1))
        b1.pack(side=tk.LEFT,pady=10)
        b2=tk.Button(row3,text="Exit",font=('TimeNewRoman 13'), command= lambda : Exit.Exit2(username,balance_update_screen))
        b2.pack(side=tk.LEFT,padx=50,pady=10)

        balance_update_screen.mainloop()

    def Bal_SubmitEntry(balance_entries,username,Banks_fields,row_1,row_2,b1):
        Balance_Total=0
        Date=balance_entries['Date'].get_date()
        for field in Banks_fields:
            if field!='Date' and field!='Total':
                if balance_entries[field].get()!=0 and balance_entries[field].get()!="" and balance_entries[field].get!="0":
                    query='insert into '+field+'_Table values("'+username+'","'+str(Date)+'","'+str(Common_Elements.Transaction_Id())+'",0,0,'+str(round(float(balance_entries[field].get()),2))+',"")'
                    Update_Bank_Tables.Update_Bank_Tables(query)
                    Balance_Total=round((Balance_Total+float(balance_entries[field].get())),2)
        #For Displaying How much Updated..
        Label(row_2,text="Present Updated Total Balance",font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
        Label(row_2,text=str(Balance_Total),font=('TimeNewRoman 14 bold'),fg='#665500',background="#FFFACD").pack(anchor='center',pady=10)
        #For Displaying Idividual Account Balance
        
        Label(row_2,text="Present Idividual Balance",font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
        row_3=tk.Frame(row_2,background="#FFFACD")
        row_3.pack(side=tk.TOP,
                        anchor=CENTER) 
        row_value=1
        for field in Banks_fields:
            if field!='Date' and field!='Total':
                query='select Balance from '+field+'_Table where Date="'+str(Date)+'" and User_Name="'+username+'"'
                Display_Amount=Get_Data.Get_Balance_For_Display(query)
                Label(row_3,text=field,font=('TimeNewRoman 14 bold'),fg='#665500',background="#FFFACD").grid(row=row_value,column=1,pady=10,sticky='w')
                Label(row_3,text= "\t : \t",font=('TimeNewRoman 14 bold'),fg='#665500',background="#FFFACD").grid(row=row_value,column=2,pady=10,sticky='w')
                Label(row_3,text=str(Display_Amount[-1][0]),font=('TimeNewRoman 14 bold'),fg='#665500',background="#FFFACD").grid(row=row_value,column=3,pady=10,sticky='E')
                row_value=row_value+1
        b1.pack_forget()
        row_1.pack_forget()

#For Updating the Credit
class Credit_Update:
    #This Function Will create the Layout for Given Fields
    def Credit_Update_Screen(index_screen,username):
        index_screen.destroy()
        credit_update_screen=tk.Tk()
        #setting tkinter window size as maximized
        credit_update_screen.state('zoomed')
        
        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(credit_update_screen,"Credit Update Form",'Credit Update Form',username)    
       
        #Fonts
        c_font = TkFont.Font(family='Times New Roman', size = 14)
        #Getting the User Using Banks list from Server
        Banks_fields=Get_Data.For_Fields(username)
        #Creating Data Entry Form for Credit 
        row_1=tk.Frame(credit_update_screen,background="#FFFACD")
        row_1.pack(side=tk.TOP,
                        anchor=CENTER) 
        credit_data=Common_Elements.MainView(row_1,Banks_fields,c_font)

        #For Displaying Udated Result
        row_2=tk.Frame(credit_update_screen,background="#FFFACD")
        row_2.pack(side=tk.TOP,
                        anchor=CENTER) 
        
       #For Submit and Exit Components 
        row3 = tk.Frame(credit_update_screen,background='#FFFACD')
        row3.pack(anchor=CENTER)
        #Submiting the Table_Ui
        b1=tk.Button(row3,text="Submit",font=('TimeNewRoman 13'),command=lambda e1=credit_data: Credit_Update.Credit_SubmitEntry(e1,username,Banks_fields,row_1,row_2,b1))
        b1.pack(side=tk.LEFT,pady=10)
        b2=tk.Button(row3,text="Exit",font=('TimeNewRoman 13'), command= lambda : Exit.Exit2(username,credit_update_screen))
        b2.pack(side=tk.LEFT,padx=50,pady=10)

        credit_update_screen.mainloop()

    def Credit_SubmitEntry(credit_entries,username,Banks_fields,row_1,row_2,b1):
        Credit_Total=0
        Balance_Total=0
        Date=credit_entries['Date'].get_date()
        for field in Banks_fields:
            if field!='Date' and field!='Total':
                if credit_entries[field].get()!=0 or credit_entries[field].get()!="":
                    Balance=Get_Data.Retriving_Balance(username,Date,field)
                    query='insert into '+field+'_Table values("'+username+'","'+str(Date)+'","'+str(Common_Elements.Transaction_Id())+'",'+str(round(float(credit_entries[field].get()),2))+',0,'+str(round((float(credit_entries[field].get())+Balance[-1][0]),2))+',"")'
                    Update_Bank_Tables.Update_Bank_Tables(query)
                    Credit_Total=round(Credit_Total+float(credit_entries[field].get()),2)
        #For Displaying Total Updated Credit
        Label(row_2,text="Present Updated Credit",font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
        Label(row_2,text=str(Credit_Total),font=('TimeNewRoman 14 bold'),fg='#665500',background="#FFFACD").pack(anchor='center',pady=10)
        #For Displaying Idividual Account Balance
        Label(row_2,text="Present Idividual Balance",font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
        row_3=tk.Frame(row_2,background="#FFFACD")
        row_3.pack(side=tk.TOP,
                        anchor=CENTER) 
        row_value=1
        for field in Banks_fields:
            if field!='Date' and field!='Total':
                query='select Balance from '+field+'_Table where Date="'+str(Date)+'" and User_Name="'+username+'"'
                Display_Amount=Get_Data.Get_Balance_For_Display(query)
                Balance_Total=round(Balance_Total+float(Display_Amount[-1][0]),2)
                Label(row_3,text=field,font=('TimeNewRoman 14 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=row_value,column=1)
                Label(row_3,text="\t : \t",font=('TimeNewRoman 14 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=row_value,column=2)
                Label(row_3,text=str(Display_Amount[-1][0]),font=('TimeNewRoman 14 bold'),fg='#665500',background="#FFFACD").grid(sticky='E',pady=10,row=row_value,column=3)
                row_value=row_value+1
        Label(row_2,text="Present Balance After Credit",font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
        Label(row_2,text=str(Balance_Total),font=('TimeNewRoman 14 bold'),fg='#665500',background="#FFFACD").pack(anchor='center',pady=10)
       
        b1.pack_forget()
        row_1.pack_forget()    

#For Updating the Debit
class Debit_Update:
    #This Function Will create the Layout for Given Fields
    def Debit_Update_Screen(index_screen,username):
        index_screen.destroy()
        debit_update_screen=tk.Tk()
        #setting tkinter window size as maximized
        debit_update_screen.state('zoomed')
        
        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(debit_update_screen,"Debit Update Form",'Debit Update Form',username)    
       
        #Fonts
        c_font = TkFont.Font(family='Times New Roman', size = 14)
        #Getting the User Using Banks list from Server
        Banks_fields=Get_Data.For_Fields(username)
        #Creating Data Entry Form for Debit 
        row_1=tk.Frame(debit_update_screen,background="#FFFACD")
        row_1.pack(side=tk.TOP,
                        anchor=CENTER) 
        debit_data=Common_Elements.MainView(row_1,Banks_fields,c_font)

        #For Displaying Udated Result
        row_2=tk.Frame(debit_update_screen,background="#FFFACD")
        row_2.pack(side=tk.TOP,
                        anchor=CENTER) 
        
       #For Submit and Exit Components 
        row3 = tk.Frame(debit_update_screen,background='#FFFACD')
        row3.pack(anchor=CENTER)
        #Submiting the Table_Ui
        b1=tk.Button(row3,text="Submit",font=('TimeNewRoman 13'),command=lambda e1=debit_data: Debit_Update.Debit_SubmitEntry(e1,username,Banks_fields,row_1,row_2,b1))
        b1.pack(side=tk.LEFT,pady=10)
        b2=tk.Button(row3,text="Exit",font=('TimeNewRoman 13'), command= lambda : Exit.Exit2(username,debit_update_screen))
        b2.pack(side=tk.LEFT,padx=50,pady=10)

        debit_update_screen.mainloop()

    def Debit_SubmitEntry(debit_entries,username,Banks_fields,row_1,row_2,b1):
        Debit_Total=0
        Balance_Total=0
        Date=debit_entries['Date'].get_date()
        for field in Banks_fields:
            if field!='Date' and field!='Total':
                if debit_entries[field].get()!=0 or debit_entries[field].get()!="":
                    Balance=Get_Data.Retriving_Balance(username,Date,field)
                    query='insert into '+field+'_Table values("'+username+'","'+str(Date)+'","'+str(Common_Elements.Transaction_Id())+'",0,'+str(round(float(debit_entries[field].get()),2))+','+str(round((-float(debit_entries[field].get())+Balance[-1][0]),2))+',"")'
                    Update_Bank_Tables.Update_Bank_Tables(query)
                    Debit_Total=round(Debit_Total+float(debit_entries[field].get()),2)
        #For Displaying Total Updated Debits
        Label(row_2,text="Present Updated Debit",font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
        Label(row_2,text=str(Debit_Total),font=('TimeNewRoman 14 bold'),fg='#665500',background="#FFFACD").pack(anchor='center',pady=10)
        #For Displaying Idividual Account Balance
        Label(row_2,text="Present Idividual Balance",font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
        row_3=tk.Frame(row_2,background="#FFFACD")
        row_3.pack(side=tk.TOP,
                        anchor=CENTER) 
        row_value=1
        for field in Banks_fields:
            if field!='Date' and field!='Total':
                query='select Balance from '+field+'_Table where Date="'+str(Date)+'" and User_Name="'+username+'"'
                Display_Amount=Get_Data.Get_Balance_For_Display(query)
                Balance_Total=round(Balance_Total+float(Display_Amount[-1][0]),2)
                Label(row_3,text=field,font=('TimeNewRoman 14 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=row_value,column=1)
                Label(row_3,text="\t : \t",font=('TimeNewRoman 14 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=row_value,column=2)
                Label(row_3,text=str(Display_Amount[-1][0]),font=('TimeNewRoman 14 bold'),fg='#665500',background="#FFFACD").grid(sticky='E',pady=10,row=row_value,column=3)
                row_value=row_value+1
        Label(row_2,text="Present Balance After Debit",font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
        Label(row_2,text=str(Balance_Total),font=('TimeNewRoman 14 bold'),fg='#665500',background="#FFFACD").pack(anchor='center',pady=10)
       
        b1.pack_forget()
        row_1.pack_forget()