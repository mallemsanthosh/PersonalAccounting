#importing the Common Function Which are in  Common_code
from Common_Code import *
from Index import Index
#Server side Imports
from Server import Validation_Server,Forget

class Login:
    def User_Login(screen=0):
        if screen!=0:
            screen.destroy()
        login_screen=tk.Tk()
        #setting tkinter window size as maximized
        login_screen.state('zoomed')
        
        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(login_screen,"Login Form",'Login',"")    
       
        #Fonts
        c_font = TkFont.Font(family='Times New Roman', size = 14)
       
        #For User_Login details Entry
        row=tk.Frame(login_screen,background='#FFFACD')
        row.pack(side=tk.TOP,
                fill=tk.X,
                    padx=5,
                    pady=5)
        label1=Label(row,text='\nEnter the User Name :',background="#FFFACD")
        label1['font']=c_font
        label1.pack()

        username = tk.Entry(row,width=25)
        username.insert(0, "")
        username['font']=c_font
        username.pack()
        
        label2=Label(row,text='\nEnter the Password :',background="#FFFACD")
        label2['font']=c_font
        label2.pack()

        password= tk.Entry(row,show='*',width=25)
        password.insert(0, "")
        password['font']=c_font
        password.pack()
        
        #For Alert
        label3=Label(row,text='',background="#FFFACD")
        label3['font']=c_font
        label3.pack()

        #For link to Registration
        row2=tk.Frame(login_screen,background="#FFFACD")
        row2.pack(side=tk.TOP,
                    padx=10,
                    pady=10,
                    anchor=CENTER)
        Label(row2,text="For Registration",fg='#0000cd',background="#FFFACD",width=30,font=('TimeNewRoman 13')).pack(side=LEFT)
        from Registration import Registration#For calling Registration class this Import was Done.
        reg=Button(row2,text="Register", font=('TimeNewRoman 13'),width=10,command= (lambda  : Registration.Register_Screen(login_screen) ))
        reg.pack(side=RIGHT,padx=20)
        
        #For link to Forgot Password and User_Name
        row_forget=tk.Frame(login_screen,background="#FFFACD")
        row_forget.pack(side=tk.TOP,
                    padx=10,
                    pady=10,
                    anchor=CENTER)
        Label(row_forget,text="For Forget User_Name/Password",fg='#0000cd',background="#FFFACD",width=30,font=('TimeNewRoman 13')).pack(side=LEFT)
        forget=Button(row_forget,text="Forget", font=('TimeNewRoman 13'),width=10,command= (lambda  : Forget_Password_UserName.Forget_Screen(login_screen) ))
        forget.pack(side=RIGHT,padx=20)

        #For Submit and Exit Components
        row3=tk.Frame(login_screen,background="#FFFACD")
        row3.pack(side=tk.TOP,
                    padx=50,
                    pady=20,
                    anchor=CENTER)
        b1=Button(row3,text="Login",font=c_font,command= (lambda e1=username,e2=password : Login.Login_Validation_Logic(e1,e2,label3,login_screen) ))#Calls the Validation Logic
        b1.pack(side=LEFT,padx=20)
        b2=Button(row3,text="Exit",font=c_font,command= lambda : Exit.Exit(login_screen))#Exit the Screen.
        b2.pack(side=RIGHT,padx=20)

        #For Exicuting the Screen
        login_screen.mainloop()

    def Login_Validation_Logic(username,password,error_label,login_screen):
        if username.get()=="" and password.get()=="":
            error_label['text']="Enter User Name and Password"
            error_label['fg']='red'
        elif password.get()=="":
            error_label['text']="Enter Password"
            error_label['fg']='red'
        elif username.get()=="":
            error_label['text']="Enter User Name"
            error_label['fg']='red'
        else:
            result=Validation_Server.User_Authentication_Validation(username.get())#Validate the User and Password From Database
            if result==[] or result[0][1]!=username.get():
                error_label['text']="Enter Valid User Name and Password\n or Regiester if New User"
                error_label['fg']='red'
            else:
                if result[0][2]==password.get():
                    error_label['text']="Success"
                    error_label['fg']='green'
                    Index.Index_Screen(username.get(),login_screen)#After Success FUll Validation, the Selection Page Will be Open.
                else:
                    error_label['text']="Password Wrong"
                    error_label['fg']='red'


class Forget_Password_UserName:
    def Forget_Screen(login_screen):
        login_screen.destroy()
        forget_screen=tk.Tk()
        #setting tkinter window size as maximized
        forget_screen.state('zoomed')
        
        #To avoid Repitative code This Function is Used
        Commonscreen.Commonscreen(forget_screen,"Forget Password/UserName",'Forget UserName/Password',"")    

        #To retrive and hide frames.
        def invoke_hide(revoke,hide):
            revoke.pack(padx=10,pady=20)
            hide.pack_forget()
              
        #Fonts
        c_font = TkFont.Font(family='Times New Roman', size = 14)

        #For Showing the for_get_password and for_get_username
        frame1=tk.Frame(forget_screen,background="#FFFACD")
        #For Showing the Error/details Message
        frame2=tk.Frame(forget_screen,background="#FFFACD")
        
        #For Displaying the User_Name and Password
        display_label=tk.Label(frame2,text="",font=TkFont.Font(family='Times New Roman',weight="bold",size=16),width=30)
        
        #Forget Username Related Frame
        frame_forget_username=tk.Frame(frame1,background="#ECCAC1")
        tk.Label(frame_forget_username,text="Retriving User_Name",font=('TimeNewRoman 16 bold'),fg='#f80b0b',background="#ECCAC1").pack(padx=5,pady=10)
        tk.Label(frame_forget_username,text="Enter Your Email Id",font=c_font,background="#ECCAC1").pack(padx=5,pady=10)
        Email_forget=tk.Entry(frame_forget_username,width=25,font=c_font)
        Email_forget.insert(0, "")
        Email_forget.pack(padx=5)
        tk.Label(frame_forget_username,text="Enter Your Phone No.",font=c_font,background="#ECCAC1").pack()
        Phone_forget=tk.Entry(frame_forget_username,width=25,font=c_font)
        Phone_forget.insert(0,"")
        Phone_forget.pack(padx=5)
        tk.Label(frame_forget_username,text="Enter Your Name",font=c_font,background="#ECCAC1").pack(padx=5,pady=10)
        Name_forget=tk.Entry(frame_forget_username,width=25,font=c_font)
        Name_forget.insert(0,"")
        Name_forget.pack(padx=5)
        tk.Button(frame_forget_username,text="Submit",width=20,font=c_font,command= lambda: Forget_Password_UserName.Forget_Username(display_label,frame_forget_username,Email_forget,Phone_forget,Name_forget)).pack(padx=10,pady=10)

        #Forget Password Related Frame
        frame_forget_password=tk.Frame(frame1,background="#ECCAC1")
        tk.Label(frame_forget_password,text="Retriving Password",font=('TimeNewRoman 16 bold'),fg='#f80b0b',background="#ECCAC1").pack(padx=5,pady=10)
        tk.Label(frame_forget_password,text="Enter Your User_Name",font=c_font,background="#ECCAC1").pack(padx=5,pady=10)
        User_Name_forget=tk.Entry(frame_forget_password,width=25,font=c_font)
        User_Name_forget.insert(0,"")
        User_Name_forget.pack(padx=5)
        tk.Label(frame_forget_password,text="Enter Your Email Id",font=c_font,background="#ECCAC1").pack(padx=5,pady=10)
        Email_forget=tk.Entry(frame_forget_password,width=25,font=c_font)
        Email_forget.insert(0, "")
        Email_forget.pack(padx=5)
        tk.Label(frame_forget_password,text="Enter Your Phone No.",font=c_font,background="#ECCAC1").pack()
        Phone_forget=tk.Entry(frame_forget_password,width=25,font=c_font)
        Phone_forget.insert(0,"")
        Phone_forget.pack(padx=5)
        tk.Button(frame_forget_password,text="Submit",width=20,font=c_font,command= lambda: Forget_Password_UserName.Forget_Password(display_label,frame_forget_password,Email_forget,Phone_forget,User_Name_forget)).pack(padx=10,pady=10)

        #For Creating Button such as Forget user_name and Password
        frame_button=tk.Frame(forget_screen,background="#FFFACD")
        frame_button.pack(side=tk.TOP,
                    padx=10,
                    pady=10,
                    anchor=CENTER)

        username_button=tk.Button(frame_button,text="Forget User_Name",font=c_font,width=20,command=lambda :invoke_hide(frame_forget_username,frame_forget_password))
        username_button.pack(side=LEFT,padx=20)

        password_button=tk.Button(frame_button,text="Forget Password",width=20,font=c_font,command=lambda :invoke_hide(frame_forget_password,frame_forget_username))
        password_button.pack(side=RIGHT,padx=20)

        #Placing Entry frame after button frame.
        frame1.pack(side=tk.TOP,
                    anchor=CENTER)
        #Placing Error Frame after the Entry Frame.
        frame2.pack(side=tk.TOP,
                    anchor=CENTER)
        

        #For Creating Button such as Login and Registration
        frame1_button=tk.Frame(forget_screen,background="#FFFACD")
        frame1_button.pack(side=tk.TOP,
                    padx=10,
                    pady=10,
                    anchor=CENTER)
        login_button=tk.Button(frame1_button,text="For Login",font=('TimeNewRoman 14 bold'),width=20,fg="navy",background='#7CD147',command=lambda :Login.User_Login(forget_screen))
        login_button.pack(side=LEFT,padx=20)
        from Registration import Registration#For calling Registration class this Import was Done.
        registration_button=tk.Button(frame1_button,text="For Registration",width=20,font=('TimeNewRoman 14 bold'),fg="navy",background='#7CD147',command=lambda :Registration.Register_Screen(forget_screen))
        registration_button.pack(side=RIGHT,padx=20)
    

        forget_screen.mainloop()

    def Forget_Username(display_label,frame_forget_username,Email_forget,Phone_forget,Name_forget):
        user_name=Forget.Forget_User_Name(Phone_forget.get(),Email_forget.get(),Name_forget.get())
        if len(user_name)!=0:
            display_label['text']=user_name
            display_label['background']="#ECCAC1"
            display_label['fg']="#4000FF"
            frame_forget_username.pack_forget()
        else:
            display_label['background']="#999999"
            display_label['fg']="#D32821"
            display_label["text"]="User Details Not Found\nPlease Re-Check the Details or\nRegister For New UserId"
        display_label.pack(padx=10,pady=20)

    def Forget_Password(display_label,frame_forget_password,Email_forget,Phone_forget,User_Name_forget):
        user_password=Forget.Forget_Password(Phone_forget.get(),Email_forget.get(),User_Name_forget.get())
        if len(user_password)!=0:
            display_label['text']=user_password
            display_label['background']="#ECCAC1"
            display_label['fg']="#4000FF"
            frame_forget_password.pack_forget()
        else:
            display_label['background']="#999999"
            display_label['fg']="#D32821"
            display_label['width']=40
            display_label["text"]="Provided Details are Not Matching\nPlease Try Again with Correct Credintials/Details."
        display_label.pack(padx=10,pady=20)
