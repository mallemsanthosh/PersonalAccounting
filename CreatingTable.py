import sqlite3 as sql
from ownenanddecode import *
from Date import *
class CreateTable:
#To Create Table
    def CreateTab(colum,name1):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        debit="create table if not Exists "+name1+"debit(Date date," +','.join(colum) + ",Total varchar(150))"
        credit="create table if not Exists "+name1+"credit(Date date," +','.join(colum)+ ",Total varchar(150))"
        balance="create table if not Exists "+name1+"balance(Date date," +','.join(colum) + ",Total varchar(150))"
        curs.execute(debit)
        curs.execute(credit)
        curs.execute(balance)      
        conn.close()
        
#To find whether the table is created or Not.
    def DummyTab():
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("create table if not Exists test(Dummy varchar(225),User_Name varchar(100) not null unique,Password varchar(225) not null,Phone_Number varchar(225),Email varchar(225),Name varchar(225) )")
        conn.close()
        
#To Store or remember our Fields
    def Remeber(tcolum,enteries):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("insert into test  values(?,?,?,?,?,?)",(tcolum,enteries['User Name'].get(),str(enteries['Password'].get()),str(enteries["Phone"].get()),enteries["Email"].get(),enteries["Name"].get()))
        conn.commit()
        conn.close()

#To Delete or Drop Table
    #def Drop():
    
    def Fields(username):
        cr_fields=[]
        de_fields=[]
        bal_fields=[]
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("select * from test where User_Name=?",(username,))
        field=curs.fetchall()
        fields=field[0][0].split(",")
        conn.close()
        for f in fields:
            if f!='Null':
                cr_fields.append('Cr_'+str(f))
                de_fields.append('Deb_'+str(f))
                bal_fields.append('Bal_'+str(f))
        return (cr_fields,de_fields,bal_fields,fields)

    def CreditEntry(cr_fields_list,fields,username):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        selectbal='select * from '+username+'balance where Date=?'
        curs.execute(selectbal,(cr_fields_list[0],))
        bal=curs.fetchall() 
        val="?"
        for i in range(1,len(cr_fields_list)):
            val=val+','+'?'
        crbr_value=[]
        babr_value=[]
        if len(bal)==0:
            selectbal='select * from '+username+'balance order by Date'
            curs.execute(selectbal)
            bal=curs.fetchall()
        for i in range (0,len(fields)):
            if i==0:
                crbr_value.append(cr_fields_list[i])
                babr_value.append(cr_fields_list[i])
            else:
                crbr_value.append(Encodess.Encodes(str(cr_fields_list[i])))
                if len(bal)==0:
                    babr_value.append(Encodess.Encodes(str(cr_fields_list[i])))
                else:
                    babr_value.append(Encodess.Encodes(str(round(float(cr_fields_list[i])+float(Decodess.Decodes(bal[-1][i])),2))))           
        try:
            insertcredit="insert into "+username+"credit values(" +val+ ")"
            insertbalance="insert into "+username+"balance values(" +val+ ")"
            curs.execute(insertcredit,crbr_value)
            curs.execute(insertbalance,babr_value)
            conn.commit()   
        except sql.IntegrityError as ei:
                pass
        finally:
            conn.close()
    
    def DebitEntry(deb_fields_list,fields,username):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        selectbal='select * from '+username+'balance where Date=?'
        curs.execute(selectbal,(deb_fields_list[0],))
        bal=curs.fetchall() 
        val="?"
        for i in range(1,len(deb_fields_list)):
            val=val+','+'?'
        debbr_value=[]
        babr_value=[]
        if len(bal)==0:
            selectbal='select * from '+username+'balance order by Date'
            curs.execute(selectbal)
            bal=curs.fetchall()
        for i in range (0,len(fields)):
            if i==0:
                debbr_value.append(deb_fields_list[i])
                babr_value.append(deb_fields_list[i])
            else:
                debbr_value.append(Encodess.Encodes(str(deb_fields_list[i])))
                if len(bal)==0:
                    babr_value.append(Encodess.Encodes(str(deb_fields_list[i])))
                else:
                    babr_value.append(Encodess.Encodes(str(round(-float(deb_fields_list[i])+float(Decodess.Decodes(bal[-1][i])),2))))           
        try:
            insertcredit="insert into "+username+"debit values(" +val+ ")"
            insertbalance="insert into "+username+"balance values(" +val+ ")"
            curs.execute(insertcredit,debbr_value)
            curs.execute(insertbalance,babr_value)
            conn.commit()   
        except sql.IntegrityError as ei:
                pass
        finally:
            conn.close()
    
    def CheckBalance(username,date):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute('select * from '+username+'balance order by Date=?',(date,))
        data=curs.fetchall()
        conn.close()
        return (data)

    def Validate(username):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute('select Dummy,User_Name,Password from test where User_Name=?',(username,))
        data=curs.fetchall()
        conn.close()
        return (data)
    
    def CheckUsername(username):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute('select User_Name from test where User_Name=?',(username,))
        data=curs.fetchall()
        conn.close()
        return (data)

#Example Test
#colum="Name varchar(225),Ram varchar(225)"    
#CreateTable.CreateTab(colum,"name10")
#print(CreateTable.Validate("SaiRam","8500155340"))

#fields=["Date","SBI","DCCB","Total"]
#cr_fields_list=["21-04-2022",'12.20','100.20',"2021.20"]
#CreateTable.CreditEntry(cr_fields_list,fields,"SaiRam")