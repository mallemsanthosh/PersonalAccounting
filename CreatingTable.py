import sqlite3 as sql
class createtable:
    def createtab(colum):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("create table account(" + ', '.join(colum) + ")")
        conn.close()
        print("Table is created")

    def dummytab():
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("create table test('dummy float')")
        conn.close()
        print("Table is Created")    
#createtable.createtab()    