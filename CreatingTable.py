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
        curs.execute("create table test(Dummy varchar(225),User_Name varchar(100) not null unique,Password varchar(225) not null,Phone_Number varchar(225),Email varchar(225),Name varchar(225) )")
        conn.close()
        
#To Store or remember our Fields
    def Remeber(tcolum,enteries):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("insert into test  values(?,?,?,?,?,?)",(tcolum,enteries['User Name'].get(),str(enteries['Password'].get()),str(enteries["Phone"].get()),enteries["Email"].get(),enteries["Name"].get()))
        conn.commit()
        conn.close()

#To Delete or Drop Table
    def Drop():
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("drop table if Exists test")
        conn.commit()
        conn.close()
    
    def Fields():
        cr_fields=[]
        de_fields=[]
        bal_fields=[]
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("select * from test")
        field=curs.fetchall()
        fields=field[0][0].split(",")
        conn.close()
        for f in fields:
            if f!='Null':
                cr_fields.append('Cr_'+str(f))
                de_fields.append('Deb_'+str(f))
                bal_fields.append('Bal_'+str(f))
        return (cr_fields,de_fields,bal_fields,fields)

    def CreditEntry(cr_fields,cr_fields_list,fields):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute('select * from accountbalance where Date=?',(cr_fields_list[0],))
        bal=curs.fetchall() 
        val="?"
        for i in range(1,len(cr_fields_list)):
            val=val+','+'?'
            print (val)
        crbr_value=[]
        babr_value=[]
        for i in range (0,len(fields)):
            if i==0:
                crbr_value.append(cr_fields_list[i])
            else:
                crbr_value.append(Encodess.Encodes(str(cr_fields_list[i])))
            if len(bal)==0:
                babr_value.append(Encodess.Encodes(str(cr_fields_list[i])))
            else:
                if i==0:
                    babr_value.append(cr_fields_list[i])
                else:
                    babr_value.append(Encodess.Encodes(str(float(cr_fields_list[i])+float(Decodess.Decodes(bal[-1][i])))))           
        try:
            curs.execute("insert into accountcredit values(" +val+ ")",crbr_value)
            curs.execute("insert into accountbalance values(" +val+ ")",crbr_value)
            conn.commit()   
        except sql.IntegrityError as ei:
                pass
        finally:
            conn.close()

    def Validate(username,password):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute('select Dummy,User_Name,Password from test where User_Name=? or Password=?',(username,password))
        data=curs.fetchall()
        conn.close()
        return (data)


#Example Test
#colum="Name varchar(225),Ram varchar(225)"    
#CreateTable.CreateTab(colum,"name10")
#CreateTable.Validate("SaiRam","99490638")