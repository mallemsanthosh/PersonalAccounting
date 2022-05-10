#Sql/DataBase Related Imports
import sqlite3 as sql
from sqlalchemy import null

#For Encoding and Decoding Related Import
from ownenanddecode import *


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
        
#For New Users, Creating Database and Create Authentication Table for Authentication.
    def AuthenticationTab():
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("create table if not Exists Authentication(Dummy varchar(225),User_Name varchar(100) not null unique,Password varchar(225) not null,Phone_Number varchar(225),Email varchar(225),Name varchar(225) )")
        conn.close()
        
#To Store or remember our Fields
    def Remeber(tcolum,enteries):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("insert into Authentication  values(?,?,?,?,?,?)",(tcolum,enteries['User Name'].get(),str(enteries['Password'].get()),str(enteries["Phone"].get()),enteries["Email"].get(),enteries["Name"].get()))
        conn.commit()
        conn.close()

#For Getting the User Fields for Layout Making.    
    def Fields(username):
        cr_fields=[]
        de_fields=[]
        bal_fields=[]
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("select * from Authentication where User_Name=?",(username,))
        field=curs.fetchall()
        fields=field[0][0].split(",")
        conn.close()
        for f in fields:
            if f!='Null':
                cr_fields.append('Cr_'+str(f))
                de_fields.append('Deb_'+str(f))
                bal_fields.append('Bal_'+str(f))
        return (cr_fields,de_fields,bal_fields,fields)

#For Credit Update
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

 #For Debit Update...   
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

#For Balance Update..    
    def BalanceEntry(bal_fields_list,fields,username):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        val="?"
        for i in range(1,len(bal_fields_list)):
            val=val+','+'?'
        babr_value=[]
        for i in range (0,len(fields)):
                if i==0:
                    babr_value.append(bal_fields_list[i])
                else:
                    babr_value.append(Encodess.Encodes(str(bal_fields_list[i])))
        try:
            insertbalance="insert into "+username+"balance values(" +val+ ")"
            curs.execute(insertbalance,babr_value)
            conn.commit()   
        except sql.IntegrityError as ei:
                pass
        finally:
            conn.close()

#For Checking the Balance    
    def CheckBalance(username,date):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        if date==null:
            curs.execute('select * from '+username+'balance order by Date')
            data=curs.fetchall()
            date=data[-1][0]    
        else:    
            curs.execute('select * from '+username+'balance order by Date=?',(date,))
            data=curs.fetchall()
        curs.execute('select * from '+username+'credit order by Date=?',(date,))
        cre_data=curs.fetchall()
        curs.execute('select * from '+username+'debit order by Date=?',(date,))
        deb_data=curs.fetchall()
        conn.close()
        return (data,cre_data,deb_data)

#For Deleting the User Account..   
    def DeleteAccount(username):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute('Delete From Authentication where User_Name=?',(username,))
        cr='Drop Table '+username+'credit'
        bal='Drop Table '+username+'balance'
        de='Drop Table '+username+'debit'
        curs.execute(cr)
        curs.execute(bal)
        curs.execute(de)
        conn.commit()
        conn.close()

    #For Validating the Username and Password from the DataBase.   
    def Validate(username):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute('select Dummy,User_Name,Password from Authentication where User_Name=?',(username,))
        data=curs.fetchall()
        conn.close()
        return (data)

#For Verifing Whether User Name is Exist or Not..    
    def CheckUsername(username):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute('select User_Name from Authentication where User_Name=?',(username,))
        data=curs.fetchall()
        conn.close()
        return (data)

#For creating Excel collecting data..
    def For_Excel(username):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor() 
        curs.execute('select Date from '+username+'balance Group by Date')
        dates=curs.fetchall()
        allbal=[]
        cr=[]
        deb=[]
        for i in dates:
            curs.execute('select * from '+username+'balance where Date=?',(i[0],))
            bal=curs.fetchall()
            allbal.append(bal[-1])
            curs.execute('select * from '+username+'credit where Date=?',(i[0],))
            crdum=curs.fetchall()
            if crdum!=[]:
                if len(crdum)==1:
                    cr.append(crdum[-1])
                else:
                    for l in crdum:
                        cr.append(l)
            else:
                cr.append([i[0]])
            curs.execute('select * from '+username+'debit where Date=?',(i[0],))
            debdum=curs.fetchall()
            if debdum!=[]:
                if len(debdum)==1:
                    deb.append(debdum[-1])
                else:
                    for l in debdum:
                        deb.append(l)
            else:
                deb.append([i[0]])
        conn.close()
        bal1=[]
        cr1=[]
        deb1=[]
        for i in range (0,len(allbal)):
            bal1.append([])
            for j in range (0,len(allbal[i])):
                if j!=0:
                    bal1[i].append(Decodess.Decodes(str(allbal[i][j])))
                else:
                    bal1[i].append(allbal[i][j])
        
        for i in range (0,len(cr)):
            cr1.append([])
            for j in range (0,len(cr[i])):
                if len(cr1)==1:
                    if j!=0:
                        cr1[i].append(Decodess.Decodes(str(cr[i][j])))
                    else:
                        cr1[i].append(cr[i][j])
                else:
                    if j!=0:
                        m=0
                        for l in range(len(cr1)):
                            if len(cr1[l])!=0:
                                if cr1[l][0]==cr[i][0]:
                                    if len(cr1[l])==len(cr1[0]):
                                        cr1[l][j]=float(cr1[l][j])+float(Decodess.Decodes(str(cr[i][j])))
                                    else:
                                        cr1[i].append(Decodess.Decodes(str(cr[i][j])))
                    else:
                        m=0
                        for l in range(len(cr1)):
                            if len(cr1[l])!=0:
                                if cr1[l][0]==cr[i][0]:
                                    m=1
                        if m==0:
                                cr1[i].append(cr[i][j])
        for s in cr1:
            if s==[]:
                cr1.remove(s)
        
        for i in range (0,len(deb)):
            deb1.append([])
            for j in range (0,len(deb[i])):
                if len(deb1)==1:
                    if j!=0:
                        deb1[i].append(Decodess.Decodes(str(deb[i][j])))
                    else:
                        deb1[i].append(deb[i][j])
                else:
                    if j!=0:
                        m=0
                        for l in range(len(deb1)):
                            if len(deb1[l])!=0:
                                if deb1[l][0]==deb[i][0]:
                                    if len(deb1[l])==len(cr1[0]):
                                        deb1[l][j]=float(deb1[l][j])+float(Decodess.Decodes(str(deb[i][j])))
                                    else:
                                        deb1[i].append(Decodess.Decodes(str(deb[i][j])))
                    else:
                        m=0
                        for l in range(len(deb1)):
                            if len(deb1[l])!=0:
                                if deb1[l][0]==deb[i][0]:
                                    m=1
                        if m==0:
                                deb1[i].append(deb[i][j])
        for s in deb1:
            if s==[]:
                deb1.remove(s)
        return bal1,cr1,deb1

 #For Collecting the data for Showing Year wise records   
    def For_YearBalance(username,year):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        baleq="select Date from "+username+"balance where Date like '"+year+"%' and strftime(Date) Group by Date order by Date"
        curs.execute(baleq)
        dates=curs.fetchall()
        allbal=[]
        cr=[]
        deb=[]    
        if dates!=[]:
            for i in dates:
                curs.execute('select * from '+username+'balance where Date=?',(i[0],))
                bal=curs.fetchall()
                allbal.append(bal[-1])
                curs.execute('select * from '+username+'credit where Date=?',(i[0],))
                crdum=curs.fetchall()
                if crdum!=[]:
                    if len(crdum)==1:
                        cr.append(crdum[-1])
                    else:
                        for l in crdum:
                            cr.append(l)
                else:
                    cr.append([i[0]])
                curs.execute('select * from '+username+'debit where Date=?',(i[0],))
                debdum=curs.fetchall()
                if debdum!=[]:
                    if len(debdum)==1:
                        deb.append(debdum[-1])
                    else:
                        for l in debdum:
                            deb.append(l)
                else:
                    deb.append([i[0]])
            conn.close()
            bal1=[]
            cr1=0
            deb1=0
            for i in range (0,len(allbal)):
                bal1.append([])
                for j in range (0,len(allbal[i])):
                    if j!=0:
                        bal1[i].append(Decodess.Decodes(str(allbal[i][j])))
                    else:
                        bal1[i].append(allbal[i][j])
            
            for c in cr:
                if len(c)!=1:
                    cr1=cr1+float(Decodess.Decodes(str(c[-1])))

            for d in deb:
                if len(d)!=1:
                    deb1=deb1+float(Decodess.Decodes(str(d[-1])))
            return bal1,cr1,deb1
        else:
            return allbal,cr,deb

#For Collecting the data for Showing Month wise records
    def For_MonthBalance(username,month,year):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        baleq="select Date from "+username+"balance where Date like '"+year+"-"+month+"-__' and strftime(Date) Group by Date order by Date"
        curs.execute(baleq)
        dates=curs.fetchall()
        allbal=[]
        cr=[]
        deb=[]    
        if dates!=[]:
            for i in dates:
                curs.execute('select * from '+username+'balance where Date=?',(i[0],))
                bal=curs.fetchall()
                allbal.append(bal[-1])
                curs.execute('select * from '+username+'credit where Date=?',(i[0],))
                crdum=curs.fetchall()
                if crdum!=[]:
                    if len(crdum)==1:
                        cr.append(crdum[-1])
                    else:
                        for l in crdum:
                            cr.append(l)
                else:
                    cr.append([i[0]])
                curs.execute('select * from '+username+'debit where Date=?',(i[0],))
                debdum=curs.fetchall()
                if debdum!=[]:
                    if len(debdum)==1:
                        deb.append(debdum[-1])
                    else:
                        for l in debdum:
                            deb.append(l)
                else:
                    deb.append([i[0]])
            conn.close()
            bal1=[]
            cr1=0
            deb1=0
            for i in range (0,len(allbal)):
                bal1.append([])
                for j in range (0,len(allbal[i])):
                    if j!=0:
                        bal1[i].append(Decodess.Decodes(str(allbal[i][j])))
                    else:
                        bal1[i].append(allbal[i][j])
            
            for c in cr:
                if len(c)!=1:
                    cr1=cr1+float(Decodess.Decodes(str(c[-1])))

            for d in deb:
                if len(d)!=1:
                    deb1=deb1+float(Decodess.Decodes(str(d[-1])))
            return bal1,cr1,deb1
        else:
            return allbal,cr,deb

#-------------------------------------------------------
#Example Test
#colum="Name varchar(225),Ram varchar(225)"    
#CreateTable.CreateTab(colum,"name10")
#print(CreateTable.Validate("SaiRam","8500155340"))

#fields=["Date","SBI","DCCB","Total"]
#cr_fields_list=["21-04-2022",'12.20','100.20',"2021.20"]
#CreateTable.CreditEntry(cr_fields_list,fields,"SaiRam")

#CreateTable.CreateTab('Sai')

#CreateTable.For_Excel('Ram')

#CreateTable.For_YearBalance('Ram',"2021")