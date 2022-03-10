import sqlite3 as sql
class CreateTable:
#To Create Table
    def CreateTab(colum):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("drop table if Exists accountdebit")
        curs.execute("create table accountdebit(Date date," + ','.join(colum) + ",Total float)")
        curs.execute("drop table if Exists accountcredit")
        curs.execute("create table accountcredit(Date date," + ','.join(colum) + ",Total float)")
        curs.execute("drop table if Exists accountbalance")
        curs.execute("create table accountbalance(Date date," + ','.join(colum) + ",Total float)")      
        conn.close()
        
#To find whether the table is created or Not.
    def DummyTab():
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("create table test(dummy varchar(225))")
        conn.close()
        
#To Store or remember our Fields
    def Remeber(tcolum):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("insert into test  values(?)",(tcolum,))
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
                de_fields.append('Del_'+str(f))
                bal_fields.append('Bal_'+str(f))
        return (cr_fields,de_fields,bal_fields)
    
#print(CreateTable.Fields())