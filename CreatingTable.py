import sqlite3 as sql
class createtable:
    def createtab(colum):
        conn=sql.connect("Accounting.sqlite3")
        curs=conn.cursor()
        curs.execute("create table account(" + ', '.join(colum) + ")")
        conn.close()
        print("Table is created")

#createtable.createtab()    