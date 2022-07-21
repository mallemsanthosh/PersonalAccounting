#Sql/DataBase Related Imports
import sqlite3 as sql
from Common_Code import Bank_List

#Server Class
#For Building Database templet
class Building_Server:
    #For New Users, Creating Database and Create Authentication Table for Authentication.
    def Build_Table():
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("create table if not Exists Authentication_Table(Fields_Name varchar(225),User_Name varchar(100) not null unique,Password varchar(225) not null,Phone_Number varchar(225),Email varchar(225),Name varchar(225) )")
        for bank in Bank_List:
            create_bank_table_query="create table if not Exists "+bank+"_Table(User_Name varchar(100) not null,Date date,Transaction_id varchar(100) not null unique,Credit NUMERIC(10,2),Debit NUMERIC(10,2),Balance NUMERIC(10,2),Remark varchar(225))"
            curs.execute(create_bank_table_query)
        conn.close()

#For Validation Purpose    
class Validation_Server:
    #For Verifing Whether User Name is Exist or Not..    
    def Check_Username(username):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute('select User_Name from Authentication_Table where User_Name=?',(username,))
        data=curs.fetchall()
        conn.close()
        return (data)

    #For Validating the Username and Password from the DataBase.
    def User_Authentication_Validation(username):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute('select Fields_Name,User_Name,Password from Authentication_Table where User_Name=?',(username,))
        data=curs.fetchall()
        conn.close()
        return (data)

    #For Updateing User_details collecting All details from the DataBase.
    def User_Details(username):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute('select * from Authentication_Table where User_Name=?',(username,))
        data=curs.fetchall()
        conn.close()
        return (data)

#For Updating Authentication/User details
class Update_Authentication_Server:
    #For Updating the data related the User(Authenticator)
    #To Store or remember our Fields
    def Update_Fields(tcolum,enteries):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        try:
            curs.execute("insert into Authentication_Table  values(?,?,?,?,?,?)",(tcolum,enteries['User Name'].get(),str(enteries['Password'].get()),str(enteries["Phone"].get()),enteries["Email"].get(),enteries["Name"].get()))
        except:
            conn.commit()
            curs.execute("insert into Authentication_Table  values(?,?,?,?,?,?)",(tcolum,enteries['User Name'].get(),str(enteries['Password'].get()),str(enteries["Phone"].get()),enteries["Email"].get(),enteries["Name"].get()))        
        finally:
            conn.commit()
            conn.close()
    
    #For Updating User Details
    def Update_User_Details(username,password=0,phone=0,email=0):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        try:
            if(password!=0):
                curs.execute('update Authentication_Table set Password=? where User_Name=?',(password,username))
        except:
            conn.commit()
            curs.execute('update Authentication_Table set Password=? where User_Name=?',(password,username))
        try:
            if(phone!=0):
                curs.execute('update Authentication_Table set Phone_Number=? where User_Name=?',(phone,username))
        except:
            conn.commit()
            curs.execute('update Authentication_Table set Phone_Number=? where User_Name=?',(phone,username))
        try:
            if(email!=0):
                curs.execute('update Authentication_Table set Email=? where User_Name=?',(email,username))                
        except:
            conn.commit()
            curs.execute('update Authentication_Table set Email=? where User_Name=?',(email,username))        
        finally:
            conn.commit()
            conn.close()

    #This terminate/Delete All User Related Tables From the DataBase and also Delete User Login Credintials From Authentication Table.
    def Delete_Account(username):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute('Delete From Authentication_Table where User_Name=?',(username,))
        for bank in Bank_List:
            delete_query='Delete From '+bank+'_Table where User_Name=?'
            curs.execute(delete_query,(username,))
            conn.commit()
        conn.close() 

#This Class is to retrive the User Data IF the User Forget.
class Forget:
    def Forget_User_Name(Phone,Email,Name):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute("select User_Name from Authentication_Table where Phone_Number=? and LOWER(Email)=? and LOWER(Name)=?",(Phone,Email.lower(),Name.lower()))
        retrieved_Username=curs.fetchall()
        conn.commit()
        conn.close()
        return (retrieved_Username)
    
    def Forget_Password(Phone,Email,User_Name):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute("select Password from Authentication_Table where Phone_Number=? and LOWER(Email)=? and User_Name=?",(Phone,Email.lower(),User_Name))
        retrieved_Password=curs.fetchall()
        conn.commit()
        conn.close()
        return (retrieved_Password)

#This for getting the Data from Database    
class Get_Data:
    def For_Fields(User_name):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute("select Fields_Name from Authentication_Table where User_Name=?",(User_name,))
        retrieved_fields=curs.fetchall()
        conn.commit()
        retrieved_fields=list(retrieved_fields[0][0].split(","))
        conn.close()
        return (retrieved_fields)
    
    def Retriving_Balance(User_name,Date,Bank_Name):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        query1="select Balance from "+Bank_Name+"_Table where User_Name=? and Date=?" 
        curs.execute(query1,(User_name,Date))
        retrieved_Data=curs.fetchall()
        if retrieved_Data==[]:
            query2="select Balance from "+Bank_Name+"_Table where User_Name=? order by Date"
            curs.execute(query2,(User_name,))
            retrieved_Data=curs.fetchall()
        if retrieved_Data==[]:
            retrieved_Data=[0]
        conn.commit()       
        conn.close()
        return (retrieved_Data)
    
    def Get_Balance_For_Display(query):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute(query)
        retrieved_Data=curs.fetchall()
        conn.commit()       
        conn.close()
        return (retrieved_Data)

    def Get_Name(user_name):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("select Name from Authentication_Table where User_Name=?",(user_name,))
        Name=curs.fetchall()
        conn.commit()       
        conn.close()
        return (Name)

#For Updating the Tables with data.
class Update_Bank_Tables:
    def Update_Bank_Tables(query):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        try:
            curs.execute(query)
            conn.commit()
        except:
            conn.commit()
            curs.execute(query)
            conn.commit()
        finally:
            conn.commit()
            conn.close()

#For Deleting Use-less Records
class All_delete:
    def All_Delete():
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        for bank in Bank_List:
            delete_query='Delete From '+bank+'_Table where Credit=0 and Debit=0 and Balance=0'
            curs.execute(delete_query)
            conn.commit()       
        conn.close()
