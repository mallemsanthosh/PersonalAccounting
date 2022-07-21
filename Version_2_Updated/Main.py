#importing the Common Function Which are in  Common_code
from Common_Code import *
#Registration and Login related function Import
from Registration import Registration
from Login import Login
from Server import Building_Server

#Main Class, Application Exicution Start from Here
class Main:
    def Main():
        main=tk.Tk()
        #Windows Screen Configuration
        main.configure(background='#FFFACD')
        main.title("Welcome")
        #setting tkinter window size as maximized
        main.state("zoomed")
        main.iconbitmap('./Assests/Icons_Images/icon1.ico')

        #Creating Table for Authentication Purpose
        Building_Server.Build_Table()#For New User it will Create DataBase and New Authentication  Table

        #Fonts
        c_font = TkFont.Font(family='Times New Roman', size = 15,weight='bold')
        
        #Title Desiging
        row=tk.Frame(main,background='#FFFACD')
        row.pack(anchor='center')
        img = ImageTk.PhotoImage(Image.open("./Assests/Icons_Images/Logo.jpg"))
        Logo = Label(row, image = img)
        Logo.pack(side='left',padx='10px')
        Title=Label(row,text='WELCOME\nTO\nPERSONAL ACCOUNTING',fg='red',background='#FFFACD')
        Title['font']=TkFont.Font(family='Times New Roman', weight = 'bold', size = 25)
        Title.pack(side='right')

        #Button Layout
        #Login
        row_1=tk.Frame(main,background='#FFFACD')
        row_1.pack(pady=10,padx=20)
        reg=Button(row_1,text="LOGIN",width=10,font=c_font,foreground="navy",command= (lambda  : Login.User_Login(main) ))#Calls the Login Screen
        reg.pack(anchor='center',pady=10)
        
        #Register
        reg=Button(row_1,text="REGISTER",width=10,font=c_font,foreground="navy",command= (lambda  : Registration.Register_Screen(main)))#Calls the Registration Screen
        reg.pack(anchor='center',pady=10)

        #Exit Layout
        b2=Button(row_1,text="EXIT",width=10,font=c_font,foreground="navy",command= lambda : Exit.Exit(main))#Exit the Screen.
        b2.pack(anchor='center',pady=10)

        
        #For Opening the window.
        main.mainloop()

#Execution Starts From Here...
Main.Main()