from Common_Code import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as TkFont
from tkcalendar import DateEntry
from Server import Get_Data
from datetime import datetime, timedelta


#For Checking and Displaying Current Balance
class Current_Balance:
    def Current_Balance_Screen(index_screen,username):
        index_screen.destroy()
        current_balance_screen=tk.Tk()
        #setting tkinter window size as maximized
        current_balance_screen.state('zoomed')
        
        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(current_balance_screen,"Current Balance",'Current Balance',username)    
       
        #Fonts
        c_font = TkFont.Font(family='Times New Roman', size = 14)
        #Getting the User Using Banks list from Server
        Banks_fields=Get_Data.For_Fields(username)
        #Creating Data Entry Form for Balance 
        Total_balance=0
        row_1=tk.Frame(current_balance_screen,background="#d9ead3")
        row_1.pack(side=tk.TOP,
                    anchor=CENTER) 
        Label(row_1,text="Current Balance In Individual Banks",font="TimeNewRoman 14 bold",fg="#0b0a0a",background="#6fa8dc").pack(anchor='center',pady=10,padx=10)
        row_3=tk.Frame(row_1,background="#d9ead3")
        row_3.pack(side=tk.TOP,
                        anchor=CENTER) 
        row_value=1
        for bank in Banks_fields:
            if bank!="Date" and bank!="Total":
                query="select Balance,Date from "+bank+"_Table where User_Name='"+username+"' order by Date"
                retrieved_balance=Get_Data.Get_Balance_For_Display(query)
                Label(row_3,text=bank,font="TimeNewRoman 14 bold",fg="#df3e1b",background="#d9ead3").grid(sticky='W',pady=10,row=row_value,column=1)
                Label(row_3,text="\t:\t",font="TimeNewRoman 14 bold",fg="#df3e1b",background="#d9ead3").grid(sticky='W',pady=10,row=row_value,column=2)
                Label(row_3,text=str(retrieved_balance[-1][0]),font="TimeNewRoman 14 bold",fg="#df3e1b",
                                                        background="#d9ead3").grid(sticky='E',pady=10,row=row_value,column=3)
                Label(row_3,text=" Last Update on "+str(retrieved_balance[-1][1]),font="TimeNewRoman 14 bold",fg="#df3e1b",
                                                        background="#d9ead3").grid(sticky='E',pady=10,row=row_value,column=4)
                Total_balance=round(Total_balance+float(retrieved_balance[-1][0]),2)
                row_value=row_value+1
        Label(row_1,text="Total Balance In All Banks\n"+str(Total_balance),font="TimeNewRoman 14 bold",fg="#df3e1b",
                                                        background="#A7FC00").pack(anchor='center',pady=10)
       #For Submit and Exit Components 
        row3 = tk.Frame(current_balance_screen,background='#FFFACD')
        row3.pack(anchor=CENTER)
        b2=tk.Button(row3,text="Exit",font=('TimeNewRoman 13'), command= lambda : Exit.Exit2(username,current_balance_screen))
        b2.pack(side=tk.LEFT,padx=50,pady=10)

        current_balance_screen.mainloop()

#For Checking and Displaying accounting details of particular date
class Date_Sheet:
    def Date_Sheet_Screen(index_screen,username):
        index_screen.destroy()
        date_sheet_screen=tk.Tk()
        #setting tkinter window size as maximized
        date_sheet_screen.state('zoomed')
        scrollbar = Scrollbar(date_sheet_screen,orient="vertical")
        scrollbar.pack( side = RIGHT, fill = Y )
      

        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(date_sheet_screen,"Date Wise Balance Check",'Date Wise Balance Check Sheet',username)    
       
        #Fonts
        c_font = TkFont.Font(family='Times New Roman', size = 14)
        #Getting the User Using Banks list from Server
        Banks_fields=Get_Data.For_Fields(username)
        
        #Creating Data Entry Form for Balance
        row_1= tk.Frame(date_sheet_screen,background='#FFFACD')
        lab = tk.Label(row_1, width=15, text="Date" , anchor='w',font=c_font,background='#FFFACD')
        lab2=  tk.Label(row_1, width=1, text=":" , anchor='w',font=c_font,background='#FFFACD')
        date_entry = DateEntry(row_1, width=17,font=c_font, background='darkblue',
                        foreground='white',borderwidth=2)
        row_1.pack(side=tk.TOP,anchor=CENTER,
                        padx=5,
                        pady=5)
        lab.pack(side=tk.LEFT)
        lab2.pack(side=tk.LEFT)
        date_entry.pack(side=tk.RIGHT,expand=tk.YES,fill=tk.X)

        #For Displaying Udated Result
        row_2=tk.Frame(date_sheet_screen,background="#FFFACD")
        row_2.pack(side=tk.TOP,
                        anchor=CENTER) 
        
        #For Submit and Exit Components 
        row3 = tk.Frame(date_sheet_screen,background='#FFFACD')
        row3.pack(anchor=CENTER)
        #Submiting the Table_Ui
        b1=tk.Button(row3,text="Individual_Transaction",font=('TimeNewRoman 13'),command=lambda e1=date_entry: Date_Sheet.Date_Sheet_Submit(e1,username,Banks_fields,row_1,row_2,b1,b2,'individual'))
        b1.pack(side=tk.LEFT,pady=10)
        b2=tk.Button(row3,text="Bank Wise Transaction",font=('TimeNewRoman 13'),command=lambda e1=date_entry: Date_Sheet.Date_Sheet_Submit(e1,username,Banks_fields,row_1,row_2,b1,b2,'bank_wise'))
        b2.pack(side=tk.LEFT,padx=10,pady=10)
        b3=tk.Button(row3,text="Exit",font=('TimeNewRoman 13'), command= lambda : Exit.Exit2(username,date_sheet_screen))
        b3.pack(side=tk.LEFT,padx=50,pady=10)

        date_sheet_screen.mainloop()

    def Date_Sheet_Submit(date,username,Banks_fields,row_1,row_2,b1,b2,print_view):
        date=date.get_date()

        my_canvas= Canvas(row_2,height=600,border=5,width=1000,background='#FFFACD')
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

        scrollbar = Scrollbar(row_2,orient=VERTICAL,command=my_canvas.yview)
        scrollbar.pack( side = RIGHT, fill = Y )
        
        my_canvas.configure(yscrollcommand=scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        row_2_1=Frame(my_canvas,background="#FFFACD")
        my_canvas.create_window((0,0),window=row_2_1,anchor="center")

        Label(row_2_1,text="Accounting Details as of "+str(date),font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
        
        row_3=tk.Frame(row_2_1,background="#FFFACD")
        row_3.pack(side=tk.TOP,
                        anchor=CENTER) 
        
        row_value=1
        Label(row_3,text="Bank_Name",font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',width=20,fg='#665500',background="#FFFACD").grid(row=row_value,column=1)
        Label(row_3,text="Credit",font=('TimeNewRoman 14 bold'),width=10,borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=2)
        Label(row_3,text="Debit",font=('TimeNewRoman 14 bold'),width=10,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(row=row_value,column=3)
        Label(row_3,text="Balance",font=('TimeNewRoman 14 bold'),width=10,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(row=row_value,column=4)
        row_value=row_value+1
        Total_Credit=0
        Total_Debit=0
        Total_Balance=0
        if print_view=="bank_wise": 
            for bank in Banks_fields:
                if bank!="Date" and bank!="Total":
                    query_1="select Sum(Credit),Sum(Debit) from "+bank+"_Table where Date='"+str(date)+"' and User_Name='"+username+"' Group by Date"
                    Cr_De_Balances=Get_Data.Get_Balance_For_Display(query_1)
                    query_2="select Balance from "+bank+"_Table where Date='"+str(date)+"' and User_Name='"+username+"'"
                    balance=Get_Data.Get_Balance_For_Display(query_2)
                    modified_Date=str(date)
                    reminder=1
                    while(balance==[] and reminder<50):
                        modified_Date=datetime.strptime(modified_Date, '%Y-%m-%d')
                        modified_Date=str(modified_Date-timedelta(1))[slice(0,10)]                   
                        query_2="select Balance from "+bank+"_Table where Date='"+str(modified_Date)+"' and User_Name='"+username+"'"
                        balance=Get_Data.Get_Balance_For_Display(query_2)
                        reminder=reminder+1
                    if(balance==[]):
                        query_2="select Balance from "+bank+"_Table where User_Name='"+username+"' order by Date Desc"
                        balance=Get_Data.Get_Balance_For_Display(query_2)
                    Label(row_3,text=bank,font=('TimeNewRoman 14 bold'),width=20,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky='W',row=row_value,column=1)
                    if(Cr_De_Balances!=[]): 
                        Label(row_3,text=str(Cr_De_Balances[-1][0]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=2)
                        Label(row_3,text=str(Cr_De_Balances[-1][1]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                        Total_Credit=round(float(Cr_De_Balances[-1][0])+Total_Credit,2)
                        Total_Debit=round(float(Cr_De_Balances[-1][1])+Total_Debit,2)
                    else:
                        Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=2)
                        Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                    Label(row_3,text=str(balance[-1][0]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=4)
                    Total_Balance=round(float(balance[-1][0])+Total_Balance,2)
                    row_value=row_value+1
        elif print_view=="individual":
            for bank in Banks_fields:
                if bank!="Date" and bank!="Total":
                    query_1="select Credit,Debit,Balance from "+bank+"_Table where Date='"+str(date)+"' and User_Name='"+username+"'"
                    Cr_De_Balances=Get_Data.Get_Balance_For_Display(query_1)
                    query_2="select Balance from "+bank+"_Table where Date='"+str(date)+"' and User_Name='"+username+"'"
                    balance=Get_Data.Get_Balance_For_Display(query_2)
                    modified_Date=str(date)
                    reminder=1
                    while(balance==[]and reminder<50):
                        modified_Date=datetime.strptime(modified_Date, '%Y-%m-%d')
                        modified_Date=str(modified_Date-timedelta(1))[slice(0,10)]                   
                        query_2="select Balance from "+bank+"_Table where Date='"+str(modified_Date)+"' and User_Name='"+username+"'"
                        balance=Get_Data.Get_Balance_For_Display(query_2)
                        reminder=reminder+1
                    if(balance==[]):
                        query_2="select Balance from "+bank+"_Table where User_Name='"+username+"' order by Date Desc"
                        balance=Get_Data.Get_Balance_For_Display(query_2)
                    if(Cr_De_Balances!=[]):
                        for rows in Cr_De_Balances:
                            Label(row_3,text=bank,font=('TimeNewRoman 14 bold'),width=20,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky='W',row=row_value,column=1)
                            Label(row_3,text=str(rows[0]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=2)
                            Label(row_3,text=str(rows[1]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                            Label(row_3,text=str(rows[2]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=4)
                            Total_Credit=round(float(rows[0])+Total_Credit,2)
                            Total_Debit=round(float(rows[1])+Total_Debit,2)
                            row_value=row_value+1
                    else:
                        Label(row_3,text=bank,font=('TimeNewRoman 14 bold'),width=20,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky='W',row=row_value,column=1)
                        Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=2)
                        Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                        Label(row_3,text=str(balance[-1][0]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=4)
                        row_value=row_value+1
                    Total_Balance=round(float(balance[-1][0])+Total_Balance,2)        
        Label(row_2_1,text="Account Summary As on "+str(date),font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
        row_4=tk.Frame(row_2_1,background="#FFFACD")
        row_4.pack(side=tk.TOP,
                        anchor=CENTER) 
        Label(row_4,text="Total Credits of All Banks ",font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=1,column=1)
        Label(row_4,text="\t:\t"+str(Total_Credit),font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=1,column=2)
        Label(row_4,text="Total Debits of All Banks ",font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=2,column=1)
        Label(row_4,text="\t:\t"+str(Total_Debit),font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=2,column=2)
        Label(row_4,text="Total Balance of All Banks ",font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=3,column=1)
        Label(row_4,text="\t:\t"+str(Total_Balance),font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=3,column=2)

        b1.pack_forget()
        b2.pack_forget()
        row_1.pack_forget()

#For Checking and Displaying accounting details of particular Year
class Year_Sheet:
    def Year_Sheet_Screen(index_screen,username):
        index_screen.destroy()
        year_sheet_screen=tk.Tk()
        #setting tkinter window size as maximized
        year_sheet_screen.state('zoomed')
        
        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(year_sheet_screen,"Year Wise Balance Check",'Year Wise Balance Check Sheet',username)    
       
        #Fonts
        c_font = TkFont.Font(family='Times New Roman', size = 14)
        #Getting the User Using Banks list from Server
        Banks_fields=Get_Data.For_Fields(username)
        year_List=[]
        for year in range(2000,2100):
            year_List.append(year)
        
        #Creating Year Entry Form for Balance
        row_1= tk.Frame(year_sheet_screen,background='#FFFACD')
        lab = tk.Label(row_1, width=15, text="Year" , anchor='w',font=c_font,background='#FFFACD')
        lab2=  tk.Label(row_1, width=1, text=":" , anchor='w',font=c_font,background='#FFFACD')
        year_entry = ttk.Combobox(row_1,state="readonly",values=year_List,font=c_font)
        year_entry.current((datetime.now().year)%100)
        row_1.pack(side=tk.TOP,anchor=CENTER,
                        padx=5,
                        pady=5)
        lab.pack(side=tk.LEFT)
        lab2.pack(side=tk.LEFT)
        year_entry.pack(side=tk.RIGHT,expand=tk.YES,fill=tk.X)

        #For Displaying Udated Result
        row_2=tk.Frame(year_sheet_screen,background="#FFFACD")
        row_2.pack(side=tk.TOP,
                        anchor=CENTER) 
        
        #For Submit and Exit Components 
        row3 = tk.Frame(year_sheet_screen,background='#FFFACD')
        row3.pack(anchor=CENTER)
        #Submiting the Table_Ui
        b1=tk.Button(row3,text="For Individual Transaction",font=('TimeNewRoman 13'),command=lambda e1=year_entry: Year_Sheet.Year_Sheet_Submit(e1,username,Banks_fields,row_1,row_2,b1,b2,'individual'))
        b1.pack(side=tk.LEFT,pady=10)
        b2=tk.Button(row3,text="For Date Wise Transaction",font=('TimeNewRoman 13'),command=lambda e1=year_entry: Year_Sheet.Year_Sheet_Submit(e1,username,Banks_fields,row_1,row_2,b1,b2,'date_wise'))
        b2.pack(side=tk.LEFT,padx=10,pady=10)
        b3=tk.Button(row3,text="Exit",font=('TimeNewRoman 13'), command= lambda : Exit.Exit2(username,year_sheet_screen))
        b3.pack(side=tk.LEFT,padx=50,pady=10)

        year_sheet_screen.mainloop()

    def Year_Sheet_Submit(year,username,Banks_fields,row_1,row_2,b1,b2,Individual_date):
        year=year.get()

        
        my_canvas= Canvas(row_2,height=600,border=5,width=1000,background='#FFFACD')
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

        scrollbar = Scrollbar(row_2,orient=VERTICAL,command=my_canvas.yview)
        scrollbar.pack( side = RIGHT, fill = Y )
        
        my_canvas.configure(yscrollcommand=scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        row_2_1=Frame(my_canvas,background="#FFFACD",width=900)
        my_canvas.create_window((0,0),window=row_2_1,anchor="center")
        
        Label(row_2_1,text="Accounting Details as of "+str(year),font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
        
        row_3=tk.Frame(row_2_1,background="#FFFACD")
        row_3.pack(side=tk.TOP,
                        anchor=CENTER) 
    
        
        dates_Getting_Data=[]
        for bank in Banks_fields:
            if bank!="Date" and bank!="Total":
                query_for_date='select Date from '+bank+"_Table where Date like '"+year+"%' and User_Name='"+username+"' Group by Date" 
                Dates=Get_Data.Get_Balance_For_Display(query_for_date)
                for date_count in range(len(Dates)):
                    if Dates[date_count][0] not in dates_Getting_Data:
                        dates_Getting_Data.append(Dates[date_count][0])
        if dates_Getting_Data!=[]:
            row_value=1
            Label(row_3,text="Date",font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',width=15,fg='#665500',background="#FFFACD").grid(row=row_value,column=1)
            Label(row_3,text="Bank_Name",font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',width=20,fg='#665500',background="#FFFACD").grid(row=row_value,column=2)
            Label(row_3,text="Credit",font=('TimeNewRoman 14 bold'),width=10,borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
            Label(row_3,text="Debit",font=('TimeNewRoman 14 bold'),width=10,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(row=row_value,column=4)
            Label(row_3,text="Balance",font=('TimeNewRoman 14 bold'),width=10,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(row=row_value,column=5)
            row_value=row_value+1
            Total_Credit=0
            Total_Debit=0
            Total_Balance=0
            if Individual_date=="date_wise":
                for date in dates_Getting_Data:
                    Label(row_3,text=str(date),font=('TimeNewRoman 14 bold'),width=15,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky=tk.S+tk.N,row=row_value,rowspan=len(Banks_fields),column=1)
                    for bank in Banks_fields:
                        if bank!="Date" and bank!="Total":
                            query_1="select Sum(Credit),Sum(Debit) from "+bank+"_Table where Date='"+str(date)+"' and User_Name='"+username+"' Group by Date"
                            Cr_De_Balances=Get_Data.Get_Balance_For_Display(query_1)
                            query_2="select Balance from "+bank+"_Table where Date='"+str(date)+"' and User_Name='"+username+"'"
                            balance=Get_Data.Get_Balance_For_Display(query_2)
                            modified_Date=str(date)
                            while(balance==[]):
                                modified_Date=datetime.strptime(modified_Date, '%Y-%m-%d')
                                modified_Date=str(modified_Date-timedelta(1))[slice(0,10)]                   
                                query_2="select Balance from "+bank+"_Table where Date='"+str(modified_Date)+"' and User_Name='"+username+"'"
                                balance=Get_Data.Get_Balance_For_Display(query_2)
                            Label(row_3,text=bank,font=('TimeNewRoman 14 bold'),width=20,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky='W',row=row_value,column=2)
                            if(Cr_De_Balances!=[]): 
                                Label(row_3,text=str(Cr_De_Balances[-1][0]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                                Label(row_3,text=str(Cr_De_Balances[-1][1]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=4)
                                Total_Credit=round(float(Cr_De_Balances[-1][0])+Total_Credit,2)
                                Total_Debit=round(float(Cr_De_Balances[-1][1])+Total_Debit,2)
                            else:
                                Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                                Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=4)
                            Label(row_3,text=str(balance[-1][0]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=5)
                            Total_Balance=round(float(balance[-1][0])+Total_Balance,2)
                            row_value=row_value+1
          #Should See From Here
            elif Individual_date=="individual":
                for date in dates_Getting_Data:
                    for bank in Banks_fields:
                        if bank!="Date" and bank!="Total":
                            query_1="select Credit,Debit,Balance from "+bank+"_Table where Date='"+str(date)+"' and User_Name='"+username+"'"
                            Cr_De_Balances=Get_Data.Get_Balance_For_Display(query_1)
                            
                            if(Cr_De_Balances!=[]):
                                for rows in Cr_De_Balances:
                                    Label(row_3,text=str(date),font=('TimeNewRoman 14 bold'),width=15,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky="W",row=row_value,column=1)
                                    Label(row_3,text=bank,font=('TimeNewRoman 14 bold'),width=20,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky="W",row=row_value,column=2)
                                    Label(row_3,text=str(rows[0]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                                    Label(row_3,text=str(rows[1]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=4)
                                    Label(row_3,text=str(rows[2]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=5)
                                    Total_Credit=round(float(rows[0])+Total_Credit,2)
                                    Total_Debit=round(float(rows[1])+Total_Debit,2)
                                    row_value=row_value+1
                            else:
                                Label(row_3,text=str(date),font=('TimeNewRoman 14 bold'),width=15,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky="W",row=row_value,column=1)
                                Label(row_3,text=bank,font=('TimeNewRoman 14 bold'),width=20,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky="W".N,row=row_value,column=2)
                                Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                                Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=4)
                                Label(row_3,text=str(Cr_De_Balances[-1][2]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=5)
                                row_value=row_value+1

                            Total_Balance=round(float(Cr_De_Balances[-1][2])+Total_Balance,2)
                                            

            Label(row_2_1,text="Account Summary As of "+str(year),font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
            row_4=tk.Frame(row_2_1,background="#FFFACD")
            row_4.pack(side=tk.TOP,
                            anchor=CENTER) 
            Label(row_4,text="Total Credits of All Banks ",font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=1,column=1)
            Label(row_4,text="\t:\t"+str(Total_Credit),font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='W',pady=10,row=1,column=2)
            Label(row_4,text="Total Debits of All Banks ",font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=2,column=1)
            Label(row_4,text="\t:\t"+str(Total_Debit),font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='W',pady=10,row=2,column=2)
            Label(row_4,text="Total Balance of All Banks ",font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=3,column=1)
            Label(row_4,text="\t:\t"+str(Total_Balance),font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=3,column=2)
        else:
            Label(row_2_1,text="There is No records for the year: "+str(year),font=('TimeNewRoman 15 bold'),fg='#003153',background="#E6BF33").pack(anchor='center',pady=10)
            
        b1.pack_forget()
        b2.pack_forget()
        row_1.pack_forget()

#For Checking and Displaying accounting details of Particular Month in Particular Year.
class Month_Sheet:
    def Month_Sheet_Screen(index_screen,username):
        index_screen.destroy()
        month_sheet_screen=tk.Tk()
        #setting tkinter window size as maximized
        month_sheet_screen.state('zoomed')
        
        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(month_sheet_screen,"Month Wise Balance Check",'Month Wise Balance Check Sheet',username)    
       
        #Fonts
        c_font = TkFont.Font(family='Times New Roman', size = 14)
        #Getting the User Using Banks list from Server
        Banks_fields=Get_Data.For_Fields(username)
        month_List=["January","February","March","April","May","June","July","August"
                        "September","October","November","December"]
        year_List=[]
        for year in range(2000,2100):
            year_List.append(year)
        
        #Creating Year Entry Form for Balance
        row_1= tk.Frame(month_sheet_screen,background='#FFFACD')
        lab_1= tk.Label(row_1, width=15, text="Month" , anchor='w',font=c_font,background='#FFFACD')
        lab_2=  tk.Label(row_1, width=1, text=":" , anchor='w',font=c_font,background='#FFFACD')
        month_entry = ttk.Combobox(row_1,state="readonly",values=month_List,font=c_font)
        month_entry.current(month_List.index(datetime.now().strftime("%B")))
        
        lab_3= tk.Label(row_1, width=15, text="Year" , anchor='w',font=c_font,background='#FFFACD')
        lab_4=  tk.Label(row_1, width=1, text=":" , anchor='w',font=c_font,background='#FFFACD')
        year_entry = ttk.Combobox(row_1,state="readonly",values=year_List,font=c_font)
        year_entry.current((datetime.now().year)%100)
        row_1.pack(side=tk.TOP,anchor=CENTER,
                        padx=5,
                        pady=5)
        lab_1.pack(side=tk.LEFT)
        lab_2.pack(side=tk.LEFT)
        month_entry.pack(side=tk.LEFT,expand=tk.YES,fill=tk.X)
        lab_3.pack(side=tk.LEFT)
        lab_4.pack(side=tk.LEFT)      
        year_entry.pack(side=tk.LEFT,expand=tk.YES,fill=tk.X)

        #For Displaying Udated Result
        row_2=tk.Frame(month_sheet_screen,background="#FFFACD")
        row_2.pack(side=tk.TOP,
                        anchor=CENTER) 
        
        #For Submit and Exit Components 
        row3 = tk.Frame(month_sheet_screen,background='#FFFACD')
        row3.pack(anchor=CENTER)
        #Submiting the Table_Ui
        b1=tk.Button(row3,text="For Individual Transaction",font=('TimeNewRoman 13'),command=lambda e1=year_entry,e2=month_entry: Month_Sheet.Month_Sheet_Submit(e1,e2,username,Banks_fields,row_1,row_2,b1,b2,'individual',month_List))
        b1.pack(side=tk.LEFT,pady=10)
        b2=tk.Button(row3,text="For Date Wise Transaction",font=('TimeNewRoman 13'),command=lambda e1=year_entry,e2=month_entry : Month_Sheet.Month_Sheet_Submit(e1,e2,username,Banks_fields,row_1,row_2,b1,b2,'date_wise',month_List))
        b2.pack(side=tk.LEFT,padx=10,pady=10)
        b3=tk.Button(row3,text="Exit",font=('TimeNewRoman 13'), command= lambda : Exit.Exit2(username,month_sheet_screen))
        b3.pack(side=tk.LEFT,padx=50,pady=10)

        month_sheet_screen.mainloop()

    def Month_Sheet_Submit(year,month,username,Banks_fields,row_1,row_2,b1,b2,Individual_date,month_list):
        year=year.get()
        month=month.get()
        month_no=str(month_list.index(month)+1)
        if month_no=="1" or month_no=="2" or month_no=="3"or month_no=="4"or month_no=="5"or month_no=="6"or month_no=="7"or month_no=="8"or month_no=="9":
            month_no="0"+month_no

        my_canvas= Canvas(row_2,height=600,border=5,width=1000,background='#FFFACD')
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

        scrollbar = Scrollbar(row_2,orient=VERTICAL,command=my_canvas.yview)
        scrollbar.pack( side = RIGHT, fill = Y )
        
        my_canvas.configure(yscrollcommand=scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        row_2_1=Frame(my_canvas,background="#FFFACD",width=900)
        my_canvas.create_window((0,0),window=row_2_1,anchor="center")
        
        Label(row_2_1,text="Accounting Details as of Month-"+str(month)+" in the Year-"+str(year),font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
        
        row_3=tk.Frame(row_2_1,background="#FFFACD")
        row_3.pack(side=tk.TOP,
                        anchor=CENTER) 
            
        dates_Getting_Data=[]
        for bank in Banks_fields:
            if bank!="Date" and bank!="Total":
                query_for_date='select Date from '+bank+"_Table where Date like '"+year+"-"+month_no+"%' and User_Name='"+username+"' Group by Date" 
                Dates=Get_Data.Get_Balance_For_Display(query_for_date)
                for date_count in range(len(Dates)):
                    if Dates[date_count][0] not in dates_Getting_Data:
                        dates_Getting_Data.append(Dates[date_count][0])
        if dates_Getting_Data!=[]:
            row_value=1
            Label(row_3,text="Date",font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',width=15,fg='#665500',background="#FFFACD").grid(row=row_value,column=1)
            Label(row_3,text="Bank_Name",font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',width=20,fg='#665500',background="#FFFACD").grid(row=row_value,column=2)
            Label(row_3,text="Credit",font=('TimeNewRoman 14 bold'),width=10,borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
            Label(row_3,text="Debit",font=('TimeNewRoman 14 bold'),width=10,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(row=row_value,column=4)
            Label(row_3,text="Balance",font=('TimeNewRoman 14 bold'),width=10,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(row=row_value,column=5)
            row_value=row_value+1
            Total_Credit=0
            Total_Debit=0
            Total_Balance=0
            if Individual_date=="date_wise":
                for date in dates_Getting_Data:
                    Label(row_3,text=str(date),font=('TimeNewRoman 14 bold'),width=15,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky=tk.S+tk.N,row=row_value,rowspan=len(Banks_fields),column=1)
                    for bank in Banks_fields:
                        if bank!="Date" and bank!="Total":
                            query_1="select Sum(Credit),Sum(Debit) from "+bank+"_Table where Date='"+str(date)+"' and User_Name='"+username+"' Group by Date"
                            Cr_De_Balances=Get_Data.Get_Balance_For_Display(query_1)
                            query_2="select Balance from "+bank+"_Table where Date='"+str(date)+"' and User_Name='"+username+"'"
                            balance=Get_Data.Get_Balance_For_Display(query_2)
                            modified_Date=str(date)
                            while(balance==[]):
                                modified_Date=datetime.strptime(modified_Date, '%Y-%m-%d')
                                modified_Date=str(modified_Date-timedelta(1))[slice(0,10)]                   
                                query_2="select Balance from "+bank+"_Table where Date='"+str(modified_Date)+"' and User_Name='"+username+"'"
                                balance=Get_Data.Get_Balance_For_Display(query_2)
                            Label(row_3,text=bank,font=('TimeNewRoman 14 bold'),width=20,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky='W',row=row_value,column=2)
                            if(Cr_De_Balances!=[]): 
                                Label(row_3,text=str(Cr_De_Balances[-1][0]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                                Label(row_3,text=str(Cr_De_Balances[-1][1]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=4)
                                Total_Credit=round(float(Cr_De_Balances[-1][0])+Total_Credit,2)
                                Total_Debit=round(float(Cr_De_Balances[-1][1])+Total_Debit,2)
                            else:
                                Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                                Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=4)
                            Label(row_3,text=str(balance[-1][0]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=5)
                            Total_Balance=round(float(balance[-1][0])+Total_Balance,2)
                            row_value=row_value+1
          #Should See From Here
            elif Individual_date=="individual":
                for date in dates_Getting_Data:
                    for bank in Banks_fields:
                        if bank!="Date" and bank!="Total":
                            query_1="select Credit,Debit,Balance from "+bank+"_Table where Date='"+str(date)+"' and User_Name='"+username+"'"
                            Cr_De_Balances=Get_Data.Get_Balance_For_Display(query_1)
                            
                            if(Cr_De_Balances!=[]):
                                for rows in Cr_De_Balances:
                                    Label(row_3,text=str(date),font=('TimeNewRoman 14 bold'),width=15,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky="W",row=row_value,column=1)
                                    Label(row_3,text=bank,font=('TimeNewRoman 14 bold'),width=20,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky="W",row=row_value,column=2)
                                    Label(row_3,text=str(rows[0]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                                    Label(row_3,text=str(rows[1]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=4)
                                    Label(row_3,text=str(rows[2]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=5)
                                    Total_Credit=round(float(rows[0])+Total_Credit,2)
                                    Total_Debit=round(float(rows[1])+Total_Debit,2)
                                    row_value=row_value+1
                            else:
                                Label(row_3,text=str(date),font=('TimeNewRoman 14 bold'),width=15,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky="W",row=row_value,column=1)
                                Label(row_3,text=bank,font=('TimeNewRoman 14 bold'),width=20,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky="W".N,row=row_value,column=2)
                                Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                                Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=4)
                                Label(row_3,text=str(Cr_De_Balances[-1][2]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=5)
                                row_value=row_value+1

                            Total_Balance=round(float(Cr_De_Balances[-1][2])+Total_Balance,2)
                                            

            Label(row_2_1,text="Account Summary As of Month-"+str(month)+" in the Year- "+str(year),font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
            row_4=tk.Frame(row_2_1,background="#FFFACD")
            row_4.pack(side=tk.TOP,
                            anchor=CENTER) 
            Label(row_4,text="Total Credits of All Banks ",font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=1,column=1)
            Label(row_4,text="\t:\t"+str(Total_Credit),font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='W',pady=10,row=1,column=2)
            Label(row_4,text="Total Debits of All Banks ",font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=2,column=1)
            Label(row_4,text="\t:\t"+str(Total_Debit),font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='W',pady=10,row=2,column=2)
            Label(row_4,text="Total Balance of All Banks ",font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=3,column=1)
            Label(row_4,text="\t:\t"+str(Total_Balance),font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=3,column=2)
        else:
            Label(row_2_1,text="There is No records for the Month : "+str(month)+" in Year : "+str(year),font=('TimeNewRoman 15 bold'),fg='#003153',background="#E6BF33").pack(anchor='center',pady=10)
            
        b1.pack_forget()
        b2.pack_forget()
        row_1.pack_forget()

#For Checking and Displaying Balance and accounting details in Between two dates.
class Date_to_Date_Sheet:
    def Date_to_Date_Sheet_Screen(index_screen,username):
        index_screen.destroy()
        date_sheet_screen=tk.Tk()
        #setting tkinter window size as maximized
        date_sheet_screen.state('zoomed')
        scrollbar = Scrollbar(date_sheet_screen,orient="vertical")
        scrollbar.pack( side = RIGHT, fill = Y )
      

        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(date_sheet_screen,"Date to Date Balance Check",'Balance Sheet In between Two Dates',username)    
       
        #Fonts
        c_font = TkFont.Font(family='Times New Roman', size = 14)
        #Getting the User Using Banks list from Server
        Banks_fields=Get_Data.For_Fields(username)
        
        #Creating Data Entry Form for Balance
        row_1_1= tk.Frame(date_sheet_screen,background='#FFFACD')
        lab = tk.Label(row_1_1, width=15, text="Starting_Date" , anchor='w',font=c_font,background='#FFFACD')
        lab2=  tk.Label(row_1_1, width=1, text=":" , anchor='w',font=c_font,background='#FFFACD')
        date_entry_1 = DateEntry(row_1_1, width=17,font=c_font, background='darkblue',
                        foreground='white',borderwidth=2)
        row_1_1.pack(side=tk.TOP,anchor=CENTER,
                        padx=5,
                        pady=5)
        lab.pack(side=tk.LEFT)
        lab2.pack(side=tk.LEFT)
        date_entry_1.pack(side=tk.RIGHT,expand=tk.YES,fill=tk.X)

        row_1_2= tk.Frame(date_sheet_screen,background='#FFFACD')
        lab = tk.Label(row_1_2, width=15, text="End_Date" , anchor='w',font=c_font,background='#FFFACD')
        lab2=  tk.Label(row_1_2, width=1, text=":" , anchor='w',font=c_font,background='#FFFACD')
        date_entry_2 = DateEntry(row_1_2, width=17,font=c_font, background='darkblue',
                        foreground='white',borderwidth=2)
        row_1_2.pack(side=tk.TOP,anchor=CENTER,
                        padx=5,
                        pady=5)
        lab.pack(side=tk.LEFT)
        lab2.pack(side=tk.LEFT)
        date_entry_2.pack(side=tk.RIGHT,expand=tk.YES,fill=tk.X)

        #For Displaying Udated Result
        row_2=tk.Frame(date_sheet_screen,background="#FFFACD")
        row_2.pack(side=tk.TOP,
                        anchor=CENTER) 
        
        #For Submit and Exit Components 
        row3 = tk.Frame(date_sheet_screen,background='#FFFACD')
        row3.pack(anchor=CENTER)
        #Submiting the Table_Ui
        b1=tk.Button(row3,text="Individual_Transaction",font=('TimeNewRoman 13'),command=lambda e1=date_entry_1,e2=date_entry_2: Date_to_Date_Sheet.Date_to_Date_Sheet_Submit(e1,e2,username,Banks_fields,row_1_1,row_1_2,row_2,b1,b2,'individual'))
        b1.pack(side=tk.LEFT,pady=10)
        b2=tk.Button(row3,text="Bank Wise Transaction",font=('TimeNewRoman 13'),command=lambda e1=date_entry_1,e2=date_entry_2: Date_to_Date_Sheet.Date_to_Date_Sheet_Submit(e1,e2,username,Banks_fields,row_1_1,row_1_2,row_2,b1,b2,'date_wise'))
        b2.pack(side=tk.LEFT,padx=10,pady=10)
        b3=tk.Button(row3,text="Exit",font=('TimeNewRoman 13'), command= lambda : Exit.Exit2(username,date_sheet_screen))
        b3.pack(side=tk.LEFT,padx=50,pady=10)

        date_sheet_screen.mainloop()

    def Date_to_Date_Sheet_Submit(date_1,date_2,username,Banks_fields,row_1_1,row_1_2,row_2,b1,b2,print_view):
        date_1=date_1.get_date()
        date_2=date_2.get_date()

        my_canvas= Canvas(row_2,height=600,border=5,width=1000,background='#FFFACD')
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

        scrollbar = Scrollbar(row_2,orient=VERTICAL,command=my_canvas.yview)
        scrollbar.pack( side = RIGHT, fill = Y )
        
        my_canvas.configure(yscrollcommand=scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        row_2_1=Frame(my_canvas,background="#FFFACD")
        my_canvas.create_window((0,0),window=row_2_1,anchor="center")

        Label(row_2_1,text="Accounting Details In between "+str(date_1)+ " and "+str(date_2),font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
        
        row_3=tk.Frame(row_2_1,background="#FFFACD")
        row_3.pack(side=tk.TOP,
                        anchor=CENTER) 
        
        dates_Getting_Data=[]
        for bank in Banks_fields:
            if bank!="Date" and bank!="Total":
                query_for_date='select Date from '+bank+"_Table where User_Name='"+username+"' and Date between '"+str(date_1)+"' and '"+str(date_2)+"' Group by Date" 
                Dates=Get_Data.Get_Balance_For_Display(query_for_date)
                for date_count in range(len(Dates)):
                    if Dates[date_count][0] not in dates_Getting_Data:
                        dates_Getting_Data.append(Dates[date_count][0])
        if dates_Getting_Data!=[]:
            row_value=1
            Label(row_3,text="Date",font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',width=15,fg='#665500',background="#FFFACD").grid(row=row_value,column=1)
            Label(row_3,text="Bank_Name",font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',width=20,fg='#665500',background="#FFFACD").grid(row=row_value,column=2)
            Label(row_3,text="Credit",font=('TimeNewRoman 14 bold'),width=10,borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
            Label(row_3,text="Debit",font=('TimeNewRoman 14 bold'),width=10,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(row=row_value,column=4)
            Label(row_3,text="Balance",font=('TimeNewRoman 14 bold'),width=10,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(row=row_value,column=5)
            row_value=row_value+1
            Total_Credit=0
            Total_Debit=0
            Total_Balance=0
            if print_view=="date_wise":
                for date in dates_Getting_Data:
                    Label(row_3,text=str(date),font=('TimeNewRoman 14 bold'),width=15,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky=tk.S+tk.N,row=row_value,rowspan=len(Banks_fields),column=1)
                    for bank in Banks_fields:
                        if bank!="Date" and bank!="Total":
                            query_1="select Sum(Credit),Sum(Debit) from "+bank+"_Table where Date='"+str(date)+"' and User_Name='"+username+"' Group by Date"
                            Cr_De_Balances=Get_Data.Get_Balance_For_Display(query_1)
                            query_2="select Balance from "+bank+"_Table where Date='"+str(date)+"' and User_Name='"+username+"'"
                            balance=Get_Data.Get_Balance_For_Display(query_2)
                            modified_Date=str(date)
                            while(balance==[]):
                                modified_Date=datetime.strptime(modified_Date, '%Y-%m-%d')
                                modified_Date=str(modified_Date-timedelta(1))[slice(0,10)]                   
                                query_2="select Balance from "+bank+"_Table where Date='"+str(modified_Date)+"' and User_Name='"+username+"'"
                                balance=Get_Data.Get_Balance_For_Display(query_2)
                            Label(row_3,text=bank,font=('TimeNewRoman 14 bold'),width=20,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky='W',row=row_value,column=2)
                            if(Cr_De_Balances!=[]): 
                                Label(row_3,text=str(Cr_De_Balances[-1][0]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                                Label(row_3,text=str(Cr_De_Balances[-1][1]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=4)
                                Total_Credit=round(float(Cr_De_Balances[-1][0])+Total_Credit,2)
                                Total_Debit=round(float(Cr_De_Balances[-1][1])+Total_Debit,2)
                            else:
                                Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                                Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=4)
                            Label(row_3,text=str(balance[-1][0]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=5)
                            Total_Balance=round(float(balance[-1][0])+Total_Balance,2)
                            row_value=row_value+1
          #Should See From Here
            elif print_view=="individual":
                for date in dates_Getting_Data:
                    for bank in Banks_fields:
                        if bank!="Date" and bank!="Total":
                            query_1="select Credit,Debit,Balance from "+bank+"_Table where Date='"+str(date)+"' and User_Name='"+username+"'"
                            Cr_De_Balances=Get_Data.Get_Balance_For_Display(query_1)
                            
                            if(Cr_De_Balances!=[]):
                                for rows in Cr_De_Balances:
                                    Label(row_3,text=str(date),font=('TimeNewRoman 14 bold'),width=15,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky="W",row=row_value,column=1)
                                    Label(row_3,text=bank,font=('TimeNewRoman 14 bold'),width=20,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky="W",row=row_value,column=2)
                                    Label(row_3,text=str(rows[0]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                                    Label(row_3,text=str(rows[1]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=4)
                                    Label(row_3,text=str(rows[2]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=5)
                                    Total_Credit=round(float(rows[0])+Total_Credit,2)
                                    Total_Debit=round(float(rows[1])+Total_Debit,2)
                                    row_value=row_value+1
                            else:
                                Label(row_3,text=str(date),font=('TimeNewRoman 14 bold'),width=15,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky="W",row=row_value,column=1)
                                Label(row_3,text=bank,font=('TimeNewRoman 14 bold'),width=20,fg='#665500',borderwidth=2,relief='solid',background="#FFFACD").grid(sticky="W".N,row=row_value,column=2)
                                Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=3)
                                Label(row_3,text=0,width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=4)
                                Label(row_3,text=str(Cr_De_Balances[-1][2]),width=10,font=('TimeNewRoman 14 bold'),borderwidth=2,relief='solid',fg='#665500',background="#FFFACD").grid(row=row_value,column=5)
                                row_value=row_value+1

                            Total_Balance=round(float(Cr_De_Balances[-1][2])+Total_Balance,2)
                                            

            Label(row_2_1,text="Account Summary In between Dates-"+str(date_1)+" To Date- "+str(date_2),font=('TimeNewRoman 15 bold'),fg='purple2',background="#FFFACD").pack(anchor='center',pady=10)
            row_4=tk.Frame(row_2_1,background="#FFFACD")
            row_4.pack(side=tk.TOP,
                            anchor=CENTER) 
            Label(row_4,text="Total Credits of All Banks ",font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=1,column=1)
            Label(row_4,text="\t:\t"+str(Total_Credit),font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='W',pady=10,row=1,column=2)
            Label(row_4,text="Total Debits of All Banks ",font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=2,column=1)
            Label(row_4,text="\t:\t"+str(Total_Debit),font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='W',pady=10,row=2,column=2)
            Label(row_4,text="Total Balance of All Banks ",font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=3,column=1)
            Label(row_4,text="\t:\t"+str(Total_Balance),font=('TimeNewRoman 15 bold'),fg='#665500',background="#FFFACD").grid(sticky='w',pady=10,row=3,column=2)
        else:
            Label(row_2_1,text="There is No records In between these Dates : "+str(date_1)+" to "+str(date_2),font=('TimeNewRoman 15 bold'),fg='#003153',background="#E6BF33").pack(anchor='center',pady=10)
            
        b1.pack_forget()
        b2.pack_forget()
        row_1_1.pack_forget()
        row_1_2.pack_forget()
