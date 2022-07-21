import sqlite3 as sql
from datetime import datetime, timedelta,date
from Server import *
from tkinter import *

  
conn=sql.connect("Accounting.sqlite3")
curs=conn.cursor() 
#curs.execute("select Date,Credit,Debit,Balance,'SBI' as Bank_Name from SBI_Table where User_Name=?  union select Date,Credit,Debit,Balance,'ICICI' as Bank_Name from ICICI_Table where User_Name=? order by Date",("Ram","Ram"))
#curs.execute("select Date,sum(Credit),sum(Debit),'SBI' as Bank_Name from SBI_Table where User_Name=? Group by Date union select Date,sum(Credit),sum(Debit),'ICICI' as Bank_Name from ICICI_Table where User_Name=? Group by Date Order By Date",("Ram","Ram"))
#curs.execute("select Date,Balance,'SBI' as Bank_Name from (Select Date,Balance,ROW_NUMBER() OVER(PARTITION BY Date ORDER BY Date desc) AS Rank from SBI_Table where User_Name=?) where Rank=Max(Rank) Group by Date",("Ram",))
#curs.execute("select Date from SBI_Table where User_Name='Ram'")
curs.execute("select * from SBI_Table where User_Name='Ram' and Date between '2020-06-24' and '2022-06-26'")
retrieved_fields=curs.fetchall()
conn.commit()
#retrieved_fields=list(retrieved_fields[0][0].split(","))
conn.close()

print(len(retrieved_fields),end="this is data")

query_1="select Credit,Debit,Balance from "+"SBI"+"_Table where Date='"+str('2022-06-11')+"' and User_Name='"+"Sai"+"'"
Cr_De_Balances=Get_Data.Get_Balance_For_Display(query_1)

#print(Cr_De_Balances)
for row in Cr_De_Balances:
    #print (row[1])
    pass


l=tuple(Get_Data.For_Fields("Sai"))
m=list(l)
for i in l:
    m.remove(i)
#    print(m)
#print(m)
#print("This",l)



"""root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
    mylist.insert(END, "This is line number " + str(line))

mylist.pack(  )
scrollbar.config( command = mylist.yview )

mainloop()"""

print(datetime.now().strftime("%B"))

"""# importing modules
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

# initializing variables with values
fileName = 'sample.pdf'
documentTitle = 'sample'
title = 'Technology'
subTitle = 'The largest thing now!!'
textLines = [
	'Technology makes us aware of',
	'the world around us.',
]
image = ''

# creating a pdf object
pdf = canvas.Canvas(fileName)

# setting the title of the document
pdf.setTitle(documentTitle)

# registering a external font in python
pdfmetrics.registerFont(
    TTFont('TNR', 'times.ttf')
	)

# creating the title by setting it's font
# and putting it on the canvas
pdf.setFont('TNR', 36)
pdf.drawCentredString(300, 770, title)

# creating the subtitle by setting it's font,
# colour and putting it on the canvas
pdf.setFillColorRGB(0, 0, 255)
pdf.setFont("Courier-Bold", 24)
pdf.drawCentredString(290, 720, subTitle)

# drawing a line
pdf.line(30, 710, 550, 710)

# creating a multiline text using
# textline and for loop
text = pdf.beginText(40, 680)
text.setFont("Courier", 18)
text.setFillColor(colors.red)
for line in textLines:
	text.textLine(line)
pdf.drawText(text)

# drawing a image at the
# specified (x.y) position
#pdf.drawInlineImage(image, 130, 400)

# saving the pdf
pdf.save()"""
