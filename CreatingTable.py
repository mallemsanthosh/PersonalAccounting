import sqlite3 as sql
class CreateTable:
#To Create Table
    def CreateTab(colum):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("create table accountdebit(Date date," + ','.join(colum) + ",Total float)")
        curs.execute("create table accountcredit(Date date," + ','.join(colum) + ",Total float)")
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
    
#createtable.dummytab()
