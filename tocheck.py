import sqlite3 as sql

from sqlalchemy import true

from ownenanddecode import *


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

        

For_Excel('Ram')