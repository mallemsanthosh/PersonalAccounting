import sqlite3 as sql
class createtable:
#To Create Table
    def createtab(colum):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("create table accountdebit(" + ', '.join(colum) + ")")
        curs.execute("create table accountcredit(" + ', '.join(colum) + ")")
        curs.execute("create table accountbalance(" + ', '.join(colum) + ")")      
        conn.close()
        
#To find whether the table is created or Not.
    def dummytab():
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("create table test(dummy varchar(225))")
        conn.close()
        
#To Store or remember our Fields
    def remeber(tcolum):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("insert into test  values(?)",(tcolum,))
        conn.commit()
        conn.close()
        
#createtable.dummytab()
