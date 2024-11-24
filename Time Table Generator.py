#------------------------------------------------------------------------------------------Modules Imported-----------------------------------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
from tkinter import messagebox
import pickle
import mysql.connector
import  datetime
from datetime import timedelta
import random
import sys
sys.setrecursionlimit (100000)


class time_table_generator :
    
    def __init__ (s) :

#-------------------------------------------------------------------------------------------------------window variables-------------------------------------------------------------------------------------------------

        s.start_screen = ""
        s.home_window = ""
        s.login_window = ""
        s.sign_up_window = ""
        s.create_tt_window = ""
        s.create_masters_window =""
        s.classes_window = ""
        s.class_window = ""
        s.create_teacher_window = ""
        s.linking_window = ""
        s.diplay_window = ""

#-------------------------------------------------------------------------------------------------------ID variables-------------------------------------------------------------------------------------------------------

        s.sub_id = 100
        s.teacher_id = 100
        
#------------------------------------------------------------------------------------------------------login related variables-----------------------------------------------------------------------------------------------

        s.username = ""
        s.password = ""
        s.user_dict = {}
        s.none_dict = {}
        s.sql_username = ""
        s.sql_password = ""
    
        s.Teacher_none_dict = {}
        s.class_none_dict = {}

#---------------------------------------------------------------------------------------------Linking window variables--------------------------------------------------------------------------------------------------

        #s.sections= ["A"]
        s.block = 0
        s.block2 = 0
        s.sub = 0
        s.class_aa = 0
        s.count=0

        s.Crepeat_check = 0
        s.Trepeat_check = 0
        s.Lrepeat_check = 0

        s.school_days_list = [ "Monday" , "Tuesday" , "Wednesday" , "Thursday" ]


#------------------------------------------------------------------------Checks related variables-------------------------------------------------------------------------------------------------------------------

        s.class1 = ""
        s.teacher = ""
        s.nested_slot_list = []
        s.original = []
        s.tlist=[]
        s.clist=[]
        s.c = 0
        s.checks = 0
        s.update_check = 0
        s.link_update_check = 0
        s.teachers_buttons_check = 0
        s.new_assignment =0
#----------------------------------------------------------------------------------------------------Start Screen Window------------------------------------------------------------------------------------------

    def start_screen_(s):
        
        s.start_screen = tkinter.Tk()
        s.start_screen.title ("Get to know us !")
        s.start_screen.geometry ("600x400")
        s.start_screen.configure ( bg = "white")
        s.logo_image = tkinter.PhotoImage ( file = "logo12.png")
        s.logo_label = tkinter.Label (s.start_screen , image = s.logo_image).pack( pady = 30)
        
        s.about_text_1 = tkinter.Label ( s.start_screen , text="A time table generator created by Avni Tongia and Rupal Shah, ",
                                              font=( "Times New Roman" , 14 , "italic") ,
                                              bg = "White" ,
                                              fg = "Black").pack()
        
        s.about_text_1 = tkinter.Label ( s.start_screen , text="Coders by passion",
                                              font=( "Times New Roman" , 14 , "italic") ,
                                              bg = "White" ,
                                              fg = "Black").pack( pady = 10)

        s.about_text_2 = tkinter.Label ( s.start_screen , text="Dedicated to our beloved teachers...",
                                              font=( "Times New Roman" , 15 , "italic" ) ,
                                              bg = "White" ,
                                              fg = "DodgerBlue4").pack(pady = 20)

        s.begin_button = tkinter.Button ( s.start_screen ,text = "Begin ", font = ( "Times New Roman" , 14 , "bold" ) ,
                                        fg = "white" ,
                                      bg = "black",
                                       width="20",
                                       height="1",command=s.sql_credentials_window).pack()

        s.start_screen.mainloop()


#----------------------------------------------------------------------------------------------Home Window--------------------------------------------------------------------------------------------------------
        

    def home_window_function(s):
        
        s.sql_window.withdraw()
        
        s.home_window = tkinter.Toplevel()
        s.home_window.title ("Welcome to DaySched! ")
        s.home_window.geometry ("400x400")
        s.home_window.configure ( bg = "white")

#----------------------------------------------------------------------------------------------------Logo------------------------------------------------------------------------------------------------------------------

        s.logo_image = tkinter.PhotoImage ( file = "logo12.png")
        s.logo_label = tkinter.Label (s.home_window , image = s.logo_image).grid ( column = 0 , row = 0 , columnspan = 10 , rowspan = 10 , padx = 60 , pady = 10)
        s.logo_tagline = tkinter.Label ( s.home_window ,
                                              text = "Time Tables just a click away!",
                                              font=("Times New Roman",16, "italic","bold") ,
                                              bg = "White" ,
                                              fg = "Black").grid ( column= 0 , row = 10, columnspan = 10 , padx = 60)


#-----------------------------------------------------------------------------------------------Sign Up Button---------------------------------------------------------------------------------------------------------

        s.sign_up_image = tkinter.PhotoImage ( file = "signup.png")
        s.sign_up_image_place = tkinter.Label ( s.home_window , image = s.sign_up_image).grid (column = 4 , row = 12 )
        s.sign_up_button = tkinter.Button ( s.home_window ,
                                      text = " Sign Up " ,
                                      font = ( "Times New Roman" , 14 , "bold" ) ,
                                      fg = "DodgerBlue4" ,
                                      bg = "White",
                                      command=s.sign_up)
        s.sign_up_button.grid ( column = 5 , row = 12)

#------------------------------------------------------------------------------------------------Login Button-----------------------------------------------------------------------------------------------------------

        s.login_image = tkinter.PhotoImage ( file = "login.png" )
        
        s.login_image_place = tkinter.Label ( s.home_window ,
                                                         image = s.login_image).grid ( column = 4 , row = 11, pady = 30)
        
        s.login_button = tkinter.Button ( s.home_window ,
                                                  text = " Login " ,
                                                  font = ( "Times New Roman" , 14 , "bold" ) ,
                                                  fg = "DodgerBlue4" ,
                                                  bg = "White" ,
                                                command = s.login)
        
        s.login_button.grid ( column = 5 , row = 11)


        s.home_window.mainloop()



#------------------------------------------------------------------------------------------SQL credentials window ------------------------------------------------------------------------------------------------------

    def sql_credentials_window ( s ) :

        s.start_screen. withdraw ()

        s.sql_window = tkinter.Toplevel()
        s.sql_window. title ( "SQL Credentials")
        s.sql_window.geometry ( "620x350" )
        s.sql_window.configure ( bg = "White")

        s.Heading = tkinter.Label ( s.sql_window , text = "Kindly fill in your SQL credentials for a user on localhost " , 
                                              font=( "Times New Roman" , 16 , "bold") ,
                                              bg = "White" ,
                                              fg = "DodgerBlue4").place ( x = 55 , y = 20 )

        s.Heading = tkinter.Label ( s.sql_window , text = " Leave the confidentiality worry to us! " , 
                                              font=( "Times New Roman" , 16 , "bold") ,
                                              bg = "White" ,
                                              fg = "DodgerBlue4"). place ( x = 155 , y = 60 )
        
        s.username_label = tkinter.Label ( s.sql_window , text = "Username : ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                fg = "black").place ( x = 100 , y = 130 )
        
        s.password_label = tkinter.Label ( s.sql_window , text = "Password : ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                fg = "black"). place ( x = 100 , y = 200 )

        s.sql_username = tkinter.StringVar()
        s.sql_password = tkinter.StringVar()

        s.username_entry = tkinter.Entry (s.sql_window ,
                                                        width="30" ,
                                                        font = ("Times New Roman" , 14) ,
                                                        textvariable = s. sql_username ,
                                                        borderwidth = 2 ,
                                                        relief = "ridge").place ( x = 230 , y = 130 )
        
        s.password_entry = tkinter.Entry ( s.sql_window ,
                                                        width="30" ,
                                                        font = ("Times New Roman" , 14) ,
                                                        textvariable = s.sql_password ,
                                                        borderwidth = 2  ,
                                                        relief = "ridge" , 
                                                        show = "*"). place (x = 230 , y = 200 )

        s.go_ahead_button = tkinter.Button ( s.sql_window ,
                                                                          text = "Go Ahead! " ,
                                                                          font = ( "Times New Roman" , 14 , "bold" ) ,
                                                                          fg = "white" ,
                                                                          bg = "black",
                                                                          width="20",
                                                                          height="1" ,
                                                                          command = s.home_window_function).place ( x = 180 , y = 280 )

        s.sql_window . mainloop()



#------------------------------------------------------------------------------------------Sign Up window--------------------------------------------------------------------------------------------------------------

    def sign_up(s):

        s.home_window.withdraw()
        
        s.sign_up_window = tkinter.Toplevel()
        s.sign_up_window. title ( "Sign Up")
        s.sign_up_window.geometry ( "500x550" )
        s.sign_up_window.configure ( bg = "White")

        #---------------------------------------------------------------------------------------Tkinter variables for entry boxes-------------------------------------------------------------------------------------------

        s.username = tkinter.StringVar()
        s.password = tkinter.StringVar()
        s.confirm_password = tkinter.StringVar()
        s.name_of_org = tkinter.StringVar()

        #---------------------------------------------------------------------------------------------------------Heading-----------------------------------------------------------------------------------------------------
        
        s.heading = tkinter.Label ( s.sign_up_window , text="We're happy to have you! sign up here...",
                                              font=( "Times New Roman" , 18 , "bold") ,
                                              bg = "White" ,
                                              fg = "DodgerBlue4").pack(pady=10)

        #-----------------------------------------------------------------------------------------------------Username-------------------------------------------------------------------------------------------------------
        
        s.username_label = tkinter.Label ( s.sign_up_window , text = "Username : ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                fg = "black") . pack ( pady = 20 )

        s.username_entry = tkinter.Entry ( s.sign_up_window ,
                                                        width="30" ,
                                                        font = ("Times New Roman" , 14) ,
                                                        textvariable = s.username ,
                                                        borderwidth = 2,
                                                        relief = "ridge").pack ()

        #-----------------------------------------------------------------------------------------------------Password-------------------------------------------------------------------------------------------------------
        
        s.password_label = tkinter.Label ( s.sign_up_window , text="Password : ",
                                                 font = ("Times New Roman",14,"bold") ,
                                                 bg = "White" ,
                                                 fg = "Black").pack ( pady =20 )

        s.password_entry = tkinter.Entry ( s.sign_up_window ,
                                                        width="30" ,
                                                        font = ("Times New Roman" , 14) ,
                                                        textvariable = s.password,
                                                        borderwidth = 2 ,
                                                         relief = "ridge"). pack ()

        #----------------------------------------------------------------------------------------------------Confirm Password-----------------------------------------------------------------------------------------------
        
        s.confirm_password_label = tkinter.Label ( s.sign_up_window , text="Confirm Password : ",
                                                             font=("Times New Roman",14,"bold") ,
                                                             bg = "White" ,
                                                             fg = "Black"). pack ( pady = 20 )

        s.confirm_password_entry = tkinter.Entry ( s.sign_up_window ,
                                                                        width="30" ,
                                                                        font = ("Times New Roman" , 14) ,
                                                                        textvariable = s.confirm_password ,
                                                                        borderwidth = 2 ,
                                                                         relief = "ridge").pack ()

        #-----------------------------------------------------------------------------------------Name of the organisation---------------------------------------------------------------------------------------------------
        
        s.name_of_org_label = tkinter.Label ( s.sign_up_window , text="Name of the organisation :",
                                                    font=("Times New Roman",14,"bold") ,
                                                    bg = "White",
                                                    fg = "Black").pack ( pady = 20 )

        s.name_of_org_entry = tkinter.Entry ( s.sign_up_window ,
                                                               width="30" ,
                                                               font = ("Times New Roman" , 14) ,
                                                               textvariable = s.name_of_org ,
                                                                borderwidth = 2 ,
                                                                relief = "ridge"). pack ()

#-----------------------------------------------------------------------------------------------------Save Button--------------------------------------------------------------------------------------------------------

        s.save_button = tkinter.Button (s.sign_up_window ,
                                                      text = "Sign Up " ,
                                                      font = ( "Times New Roman" , 14 , "bold" ) ,
                                                      fg = "white" ,
                                                      bg = "black",
                                                      width = "20",
                                                      height = "1",
                                                      command = s.save_sign_up_info). pack ( pady = 30 )
        s.sign_up_window.mainloop()
        

#---------------------------------------------------------------------------------------------------------Command for save button-----------------------------------------------------------------------------------

    def save_sign_up_info(s):
                
        s.password_info = s.password.get()
        s.confirm_password_info = s.confirm_password.get()
        s.username_info = s.username.get()

        if s.password_info != s.confirm_password_info :

            messagebox.showerror ( " Password Authentication Error " , " Password and Confirm Password fields do not match")
                    
            s.confirm_password.set("")
            s.password.set("")

        elif len(s.password_info) < 8  :

            messagebox.showerror ( " Weak Password " , " Password strength = weak ")
                    
            s.confirm_password.set("")
            s.password.set("")

        elif s.password_info == s.confirm_password_info and len ( s.password_info ) > 8 :
            
            s.sign_in_check = open ( "user_info.txt" , "ab+" )
                    
            try :
            
                while True :
                    check_user = pickle.load ( s.sign_in_check )
                
                    if s.username_info == check_user ['Username' ]:
                        messagebox.showerror ( "User Exists" , "This user already exists. Be creative !! try a different username " )
                        s.username.set("")
                        break

                    else :
                        s.username_info = s.username.get()
                        s.password_info = s.password.get()
                        s.confirm_password_info = s.confirm_password.get()
                        s.name_of_org_info = s.name_of_org.get()
                        s.user_dict['Username'] = s.username_info
                        s.user_dict['Password'] = s.password_info
                        s.user_dict['name of the organisation'] = s.name_of_org_info
                        s.sign_up_info = open("user_info.txt",'ab')
                        pickle.dump(s.user_dict , s.sign_up_info)
                        s.sign_up_info.close()

                        s.sign_up_window.withdraw()
                                
                        s.login()

            except EOFError :
                s.username_info = s.username.get()
                s.password_info = s.password.get()
                s.confirm_password_info = s.confirm_password.get()
                s.name_of_org_info = s.name_of_org.get()
                s.user_dict['Username'] = s.username_info
                s.user_dict['Password'] = s.password_info
                s.user_dict['name of the organisation'] = s.name_of_org_info
                s.sign_up_info = open("user_info.txt",'ab')
                pickle.dump(s.user_dict , s.sign_up_info)
                s.sign_up_info.close()

                s.sign_up_window.withdraw()
                        
                s.login()
                s.sign_in_check . close()
          
        else:
            s.username_info = s.username.get()
            s.password_info = s.password.get()
            s.confirm_password_info = s.confirm_password.get()
            s.name_of_org_info = s.name_of_org.get()
            s.user_dict['Username'] = s.username_info
            s.user_dict['Password'] = s.password_info
            s.user_dict['name of the organisation'] = s.name_of_org_info
            s.sign_up_info = open("user_info.txt",'ab')
            pickle.dump(s.user_dict , s.sign_up_info)
            s.sign_up_info.close()

            s.sign_up_window.withdraw()
                    
            s.login()
        
                
        
#--------------------------------------------------------------------------------------------Login Window-------------------------------------------------------------------------------------------------------------

    def login(s):
    
        s. home_window.withdraw()
        
        s.login_window = tkinter.Toplevel()
        s.login_window. title ( "Login")
        s.login_window.geometry ( "550x300" )
        s.login_window.configure ( bg = "White")

#-----------------------------------------------------------------------------------------Labels for Login Window--------------------------------------------------------------------------------------------------

        s.Heading = tkinter.Label ( s.login_window , text="Lets get started !!!",
                                              font=( "Times New Roman" , 18 , "bold") ,
                                              bg = "White" ,
                                              fg = "DodgerBlue4").grid ( column = 2 , row = 0 , columnspan = 5 , pady = 20)
        
        s.username_label = tkinter.Label ( s.login_window , text = "Username : ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                fg = "black").grid (column = 1 , row = 3 , pady = 20 , padx = 20)
        
        s.password_label = tkinter.Label ( s.login_window , text = "Password : ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                fg = "black").grid ( column = 1 , row = 4 , pady = 20 , padx = 20)

#----------------------------------------------------------------------------------Entry Boxes for Login Window-------------------------------------------------------------------------------------------------

        s.username = tkinter.StringVar()
        s.password = tkinter.StringVar()

        s.username_entry = tkinter.Entry (s.login_window ,
                                                        width="30" ,
                                                        font = ("Times New Roman" , 14) ,
                                                        textvariable = s.username ,
                                                        borderwidth = 2 ,
                                                        relief = "ridge").grid (column = 2 , row = 3 , pady = 20)
        
        s.password_entry = tkinter.Entry ( s.login_window ,
                                                        width="30" ,
                                                        font = ("Times New Roman" , 14) ,
                                                        textvariable = s.password ,
                                                        borderwidth = 2  ,
                                                        relief = "ridge" , 
                                                        show = "*").grid (column = 2 , row = 4 , pady = 20)

        s.go_ahead_button = tkinter.Button ( s.login_window ,
                                                                          text = "Go Ahead! " ,
                                                                          font = ( "Times New Roman" , 14 , "bold" ) ,
                                                                          fg = "white" ,
                                                                          bg = "black",
                                                                          width="20",
                                                                          height="1", command = s.user_pass_check).grid ( column = 2 , row = 5 , columnspan = 5 , pady = 20)

        s.login_window.mainloop()

#---------------------------------------------------------------------------------------------------creating the databases ----------------------------------------------------------------------------------------------

        
    def create_db(s):

        s.database = mysql.connector.connect( host="localhost",
                                                                            user = s.sql_username.get(),
                                                                            passwd = s.sql_password . get() )
        
        s.db = s.database.cursor()
        s.db.execute("CREATE DATABASE IF NOT EXISTS %s" %s.user['name of the organisation'])
        s.db.execute("SHOW DATABASES")
        s.database.commit()
        s.database.close()
        
#----------------------------------------------------------------------------------------------------------login check-------------------------------------------------------------------------------------------
                    
    def user_pass_check(s):

        s.username_login_info = s.username.get()
        s.password_login_info = s.password.get()
            
        s.user_info = open("user_info.txt",'rb')
        s.check=0
        
        try:
            while True:
                
                s.user = pickle.load( s.user_info)
                    
                if s.user [ "Username" ] == s.username_login_info and s.user [ "Password" ] == s.password_login_info :

                    s.check=1
                    s.create_db()

                    break
                        
        except:
            s.user_info.close()

        if s.check==0 :
                messagebox.showerror ( " Wrong Username or password " , " The Username or Password is incorrect" )
                s.username.set("")
                s.password.set("")

        elif s.check == 1 :
            s.school()


#--------------------------------------------------------------------------------------------School Inputs Window------------------------------------------------------------------------------------------------------

    def school (s ) :

        s.login_window . withdraw ()
            
        s.school_inputs_window = tkinter.Toplevel()
        s.school_inputs_window. title ( "General Inputs Regarding the Institution ")
        s.school_inputs_window. geometry ( "670x450" )
        s.school_inputs_window. configure ( bg = "White")

        s.heading = tkinter.Label ( s.school_inputs_window , text="We're keen to know more about your Institution !",
                                                  font=( "Times New Roman" , 18 , "bold") ,
                                                  bg = "White" ,
                                                  fg = "DodgerBlue4").place ( x = 80 , y = 10)

        s.starthours = tkinter.IntVar()
        s.startminutes = tkinter.IntVar()
            
        s.endhours = tkinter.IntVar()
        s.endminutes = tkinter.IntVar()

        s.lectureduration = tkinter.IntVar()

        s.sections_tkinter = tkinter . StringVar()
            
    #----------------------------------------------------------------------------------------------Start of school timings--------------------------------------------------------------------------------------------------    

        s.school_start = tkinter.Label ( s.school_inputs_window , text = "   School begins at : ",
                                                    font=("Times New Roman",14,"bold") ,
                                                    bg = "White" ,
                                                    fg = "black").place ( x = 15 , y = 70) 
            
        s.start_hours = tkinter.Spinbox ( s.school_inputs_window ,
                                                     from_ = 1 ,
                                                     to = 24 ,
                                                     font = ( "Times New Roman" , 14 ) ,
                                                     width = 5 ,
                                                      justify = "center", textvariable = s.starthours) . place (x = 60 , y =118)

        hours_label = tkinter.Label ( s.school_inputs_window , text = "hrs ",
                                                font=("Times New Roman",14 , "italic") ,
                                                bg = "White" ,
                                                 fg = "black"). place ( x = 135 , y = 118 )

        s.start_minutes = tkinter.Spinbox ( s.school_inputs_window ,
                                                         from_ = 0,
                                                         to = 60 ,
                                                         font = ( "Times New Roman" , 14 ) ,
                                                         width = 5 ,
                                                          justify = "center", textvariable = s.startminutes) . place ( x = 230 ,y = 118)

        minutes_label = tkinter.Label ( s.school_inputs_window , text = "mins ",
                                                font=("Times New Roman",14 , "italic") ,
                                                bg = "White" ,
                                                 fg = "black"). place ( x = 300 , y = 118 )
        
            
    #-------------------------------------------------------------------------------------------------End of school Timings -----------------------------------------------

        s.school_end = tkinter.Label ( s.school_inputs_window , text = "School ends at : ",
                                                    font=("Times New Roman",14,"bold") ,
                                                    bg = "White" ,
                                                     fg = "black").place (y = 163 , x = 15)

        s.end_hours = tkinter.Spinbox ( s.school_inputs_window ,
                                                     from_ = 1 ,
                                                     to = 24 ,
                                                     font = ( "Times New Roman" , 14 ) ,
                                                     width = 5 ,
                                                      justify = "center",
                                                      textvariable = s.endhours) . place (x = 60 , y = 215)

        hours_label = tkinter.Label ( s.school_inputs_window , text = "hrs ",
                                                font=("Times New Roman",14 , "italic") ,
                                                bg = "White" ,
                                                 fg = "black"). place ( x = 135 , y = 215 )

        s.end_minutes = tkinter.Spinbox ( s.school_inputs_window ,
                                                         from_ = 0,
                                                         to = 60 ,
                                                         font = ( "Times New Roman" , 14 ) ,
                                                         width = 5 ,
                                                          justify = "center",
                                                          textvariable = s.endminutes) . place (x = 230, y = 215 )

        minutes_label = tkinter.Label ( s.school_inputs_window , text = "mins ",
                                                font=("Times New Roman",14 , "italic") ,
                                                bg = "White" ,
                                                 fg = "black"). place ( x = 300 , y = 215 )

            
    #-----------------------------------------------------------------------------------------------------Per lecture duration----------------------------------------------------------------------------------------------

        s.lecture_duration = tkinter.Label ( s.school_inputs_window , text = "Every lecture is : ",
                                                                font=("Times New Roman",14,"bold") ,
                                                                bg = "White" ,
                                                                fg = "black").place(x = 410 , y = 70)
            
        s.lecture_duration_entry = tkinter.Entry ( s.school_inputs_window , 
                                                                        font=("Times New Roman",13) ,
                                                                        borderwidth = 2 ,
                                                                        relief = "ridge",
                                                                        fg = "black" ,
                                                                        textvariable = s.lectureduration ,
                                                                        width = 10).place (x = 410 , y =118)

        minutes_3_label = tkinter.Label ( s.school_inputs_window , text = "mins ",
                                                font=("Times New Roman",14 , "italic") ,
                                                bg = "White" ,
                                                 fg = "black"). place ( x = 520 , y = 118 )


    #-------------------------------------------------------------------------------------------------------School Days------------------------------------------------------------------------------------------------------

        s.days_label = tkinter.Label ( s.school_inputs_window , text = "School Days : ",
                                                                font=("Times New Roman",14,"bold") ,
                                                                bg = "White" ,
                                                                fg = "black").place (x = 410 , y = 163)

        s.monday_label = tkinter.Label ( s.school_inputs_window , text = "Monday    -  ",
                                                                font=("Times New Roman",13) ,
                                                                bg = "White" ,
                                                                fg = "black").place ( x = 375 , y = 215 )

        s.days = tkinter . StringVar ()

        s.school_days = tkinter.Spinbox (s.school_inputs_window ,
                                                                         values = ( "Friday" ,"Saturday" , "Sunday"  ) , 
                                                                         font = ( "Times New Roman" , 13 ) ,
                                                                         width = 13 ,
                                                                          justify = "center",
                                                                          textvariable = s.days ,
                                                                           increment = 5) . place ( x = 470 , y = 215 )

        s.school_sections = tkinter.Label ( s.school_inputs_window , text = "Sections:     A -  ",
                                                    font=("Times New Roman",14,"bold") ,
                                                    bg = "White" ,
                                                    fg = "black").place(x =170 , y = 290)

        s.spin_sections = tkinter.Spinbox (s.school_inputs_window ,
                                                                         values = ("B","C","D","E","F","G","H","I","J") ,
                                                                         font = ( "Times New Roman" , 13 ) ,
                                                                         width = 13 ,
                                                                          justify = "center",
                                                                          textvariable = s.sections_tkinter ,
                                                                           increment = 5) .place ( x = 330 , y = 290)


        #--------------------------------------------------------------------------------------- Create Masters Button -------------------------------------------------------------------------------------------------------

        s.create_masters_button = tkinter.Button ( s.school_inputs_window ,
                                                                      text = "Create Masters " ,
                                                                      font = ( "Times New Roman" , 14 , "bold" ) ,
                                                                      fg = "white" ,
                                                                      bg = "black",
                                                                      width="15",
                                                                      height="1" ,
                                                                       command = s.create_masters).place (x = 50 , y = 350)
        
        s.view_time_tables = tkinter.Button ( s.school_inputs_window ,
                                                                      text = "View Time Table " ,
                                                                      font = ( "Times New Roman" , 14 , "bold" ) ,
                                                                      fg = "white" ,
                                                                      bg = "black",
                                                                      width="15",
                                                                      height="1" ,
                                                                       command = s.choose_teacher_or_class).place (x = 450 , y = 350)

        s.update_masters = tkinter.Button ( s.school_inputs_window ,
                                                                      text = "Update Masters" ,
                                                                      font = ( "Times New Roman" , 14 , "bold" ) ,
                                                                      fg = "white" ,
                                                                      bg = "black",
                                                                      width="15",
                                                                      height="1" ,
                                                                       command = s.update_window).place (x = 250 , y = 350)


        s.school_inputs_window.mainloop()

        
                
#-----------------------------------------------------------------------------------------------------------creating the master tables----------------------------------------------------------------------------------
                
    def create_tables(s):
        
        s.tables = mysql.connector.connect ( host="localhost",
                                                                        user = s.sql_username .get (),
                                                                        passwd = s.sql_password . get (),
                                                                        database = s.user['name of the organisation'])

        s.table = s.tables.cursor()
        s.table.execute("CREATE TABLE IF NOT EXISTS Subjects (Subject_id VARCHAR(5) PRIMARY KEY , Subject_name VARCHAR(50))")
        s.table.execute("CREATE TABLE IF NOT EXISTS Teachers (Teacher_id VARCHAR(5) PRIMARY KEY, Teacher_name VARCHAR(255) , Arrival_time TIME NOT NULL, Departure_time TIME NOT NULL , Subject_1 VARCHAR(50) , Subject_2 VARCHAR (50) , Subject_3 VARCHAR (50) , Lunch VARCHAR (30)) ")
        s.table.execute("CREATE TABLE IF NOT EXISTS Classes ( Class INT , Arrival_time TIME NOT NULL , Departure_time TIME NOT NULL , Subject_1 VARCHAR (50) , Subject_2 VARCHAR(50) , Subject_3 VARCHAR(50) , Subject_4 VARCHAR (50) , Subject_5 VARCHAR (50) , Subject_6 VARCHAR (50) , Subject_7 VARCHAR (50) , Subject_8 VARCHAR (50), Lunch VARCHAR (30))")
        s.table.execute("CREATE TABLE IF NOT EXISTS Linking ( Class_id VARCHAR (5) , Subject_id VARCHAR (5) , Teacher_id VARCHAR (5) , Lec_per_week INT )")
        #s.table.execute ( "CREATE TABLE IF NOT EXISTS Outputs ( Class_id VARCHAR (5) , Subject_id VARCHAR (5) , Teacher_id VARCHAR (5) , Slot_id INT , Day VARCHAR (10) , Time TIME ) ")

        s.tables.commit()
        s.tables.close()
        
#----------------------------------------------------------------------------------------------------------inserting subjects in the table----------------------------------------------------------------------------------

    def insert_subject(s):
        
        try :
        
            s.add_subjects = mysql.connector.connect (host="localhost",
                                                                        user = s.sql_username .get (),
                                                                        passwd = s.sql_password . get (),
                                                                        database = s.user['name of the organisation'])
            
            s.sub_id=s.sub_id+1
            s.sub_name_info = s.sub_name.get()
            s.add_subject = s.add_subjects.cursor()
            s.temp = ("S" + str(s.sub_id) ,s.sub_name_info)
            s.add_sub =( "INSERT INTO Subjects (Subject_id, Subject_name) VALUES (%s,%s)")
            s.add_subject.execute(s.add_sub,s.temp)
            s.add_subjects.commit()
            s.add_subjects.close()
            s.sub_name.set("")

        except mysql.connector.errors.IntegrityError:
            
            s.add_subjects = mysql.connector.connect ( host="localhost",
                                                                        user = s.sql_username .get (),
                                                                        passwd = s.sql_password . get (),
                                                                        database = s.user['name of the organisation'])
            s.add_subject = s.add_subjects.cursor()
            s.add_subject . execute ( "SELECT MAX(Subject_id) FROM Subjects;")
            s.id_fetch = s.add_subject . fetchone ()
            s.max_id = s.id_fetch [0]
            
            s.add_subject . close()
            s.add_subjects.close ()

            s.add_subjects = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
            
            s.sub_id=int(s.max_id[1::])+1
            s.sub_name_info = s.sub_name.get()
            s.add_subject = s.add_subjects.cursor()
            s.temp = ("S" + str(s.sub_id) ,s.sub_name_info)
            s.add_sub =( "INSERT INTO Subjects (Subject_id, Subject_name) VALUES (%s,%s)")
            s.add_subject.execute(s.add_sub,s.temp)
            s.add_subjects.commit()
            s.add_subjects.close()
            s.sub_name.set("")

#--------------------------------------------------------------------------------------------------Create Masters Window-------------------------------------------------------------------------------------------

    def create_masters(s) :

        if s.update_check== 0 :
        
            s.create_tables()

            s.slots_for_entire_school = s.slot_creation_for_school ( s.starthours , s.startminutes , s.endhours , s.endminutes )

            slot_dictionary_school = {}

            slot_dictionary_school [ "School" ] = s.slots_for_entire_school
            
            
            s.school_inputs_window.withdraw()

        else :
            s.updates_window . withdraw()
        
        s.create_masters_window = tkinter.Toplevel()
        s.create_masters_window.title ("Master Databases")
        s.create_masters_window.geometry ("500x300")
        s.create_masters_window.configure ( bg = "white")
        
        s.heading = tkinter.Label ( s.create_masters_window , text = "1. Subjects " ,
                                                   bg = "White" ,
                                                   fg = "DodgerBlue4" ,
                                                   font = ("Times New Roman" , 18 , "bold") ). grid (column = 1 , row = 0 , columnspan = 2 , pady = 20)
        
        s.subject_name_label = tkinter.Label ( s.create_masters_window , text = "Subject Name : ",
                                                        font=("Times New Roman",14,"bold") ,
                                                        bg = "White" ,
                                                        fg = "black").grid (column = 1 , row = 3 , pady = 20 , padx = 20)
                                      
        s.sub_name = tkinter.StringVar()

        s.sub_name_entry = tkinter.Entry (s.create_masters_window ,
                                                                width="30" ,
                                                                font = ("Times New Roman" , 14) ,
                                                                textvariable = s.sub_name ,
                                                                borderwidth = 2 ,
                                                                relief = "ridge").grid (column = 2 , row = 3 , pady = 20)

        s.add_button = tkinter.Button (s.create_masters_window ,
                                                        text = "Add Subject " ,
                                                        font = ( "Times New Roman" , 14 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="20",
                                                        height="1",
                                                        command = s.insert_subject).grid ( column = 1 , row = 4 , columnspan = 20 , pady = 20)

        if s.update_check == 0 :
            
            s.done_button = tkinter.Button (s.create_masters_window ,
                                                        text = "Done " ,
                                                        font = ( "Times New Roman" , 14 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="10",
                                                        height="1" ,
                                                        command = s.classes).grid ( column = 2 , row = 5 , pady = 20 , padx = 50)

            
#---------------------------------------------------------------------------------------------Slot Creation for the school------------------------------------------------------------------------------------------------

    def slot_creation_for_school (s , from_hours , from_minutes , to_hours , to_minutes):
        
        s.start_hours_info = int(from_hours.get())
        s.start_minutes_info = int(from_minutes.get())
        
        s.end_hours_info = int(to_hours.get())
        s.end_minutes_info = int(to_minutes.get())

        s.sections = ["A"]

        s.section_variable = s.sections_tkinter . get()

        section_max_values = ("B","C","D","E","F","G","H","I","J")

        sec_index = section_max_values . index (s.section_variable)

        for sec in range (sec_index+1):
            s.sections.append(section_max_values[sec])

        #print(s.sections)

        
        
        s.lecture_duration_info = int(s.lectureduration.get())

        begin = timedelta (hours = s.start_hours_info , minutes = s.start_minutes_info)

        end = timedelta ( hours = s.end_hours_info , minutes = s.end_minutes_info )

        lecture = timedelta ( minutes = s.lecture_duration_info )

        s.days_info = s.days.get()

        #s.school_days_list = [ "Monday" , "Tuesday" , "Wednesday" , "Thursday" ]

        if s.days_info == "Friday" :
            s.school_days_list . append ( "Friday" )

        elif s.days_info == "Saturday" :
            s.school_days_list . extend ( [ "Friday" , "Saturday" ] )

        elif s.days_info == "Sunday" :
            s.school_days_list . extend ( [ "Friday" , "Saturday" , "Sunday" ] )

        no_of_lectures = (end - begin ) // lecture
        slot_id = 0
        s.time_slots = {}
        s.lunch_dropdown = []
        s. lunch_dropdown_2 = []

        for day in s.school_days_list :
            for time in range ( no_of_lectures ):
                begin_str = str (begin)
                timing = begin + lecture
                end_str = str ( timing )
                slot = begin_str + " to " + end_str + "  " + day
                lunch = begin_str + " to " + end_str + " >>>> " + str(slot_id)
                s.lunch_dropdown . append ( lunch )
                s.time_slots [ slot ] = slot_id
                slot_id +=1
                begin = timing

            s.start_hours_info = int(from_hours.get())
            s.start_minutes_info = int(from_minutes.get())
            begin = timedelta (hours = s.start_hours_info , minutes = s.start_minutes_info)

        days_file = {}

        lunch_slots = len ( s. time_slots ) // len ( s.school_days_list)

        for lunches in range (lunch_slots) :
            s.lunch_dropdown_2 .append ( s.lunch_dropdown [ lunches] )

        days_file["Organisation"] = s.user['name of the organisation']
        days_file ["School Days"] = s.school_days_list

        file = open ( "School_slot_timings.txt" , "wb" )
        pickle . dump (s.time_slots, file)
        file.close()

        file2 = open ("School_Days.txt","ab+")
        try:
            while True :
                p= pickle . load (file2)
                if p ["Organisation"] == s.user['name of the organisation'] :
                    break
                else :
                    pickle . dump ( days_file , file2)
        except EOFError :
            
            file2.close()

        return s.time_slots


#---------------------------------------------------------------------------------------------------Slot Creation For Classes----------------------------------------------------------------------------------------------

    def slot_creation_for_classes (s , from_hours , from_minutes , to_hours , to_minutes):
        
        s.start_hours_info = int(from_hours.get())
        s.start_minutes_info = int(from_minutes.get())
        
        s.end_hours_info = int(to_hours.get())
        s.end_minutes_info = int(to_minutes.get())
        
        s.lecture_duration_info = int(s.lectureduration.get())

        begin = timedelta (hours = s.start_hours_info , minutes = s.start_minutes_info)

        end = timedelta ( hours = s.end_hours_info , minutes = s.end_minutes_info )

        lecture = timedelta ( minutes = s.lecture_duration_info )

        s.days_info = s.days.get()

        school_days = [ "Monday" , "Tuesday" , "Wednesday" , "Thursday" ]

        if s.days_info == "Friday" :
            school_days . append ( "Friday" )

        elif s.days_info == "Saturday" :
            school_days . extend ( [ "Friday" , "Saturday" ] )

        elif s.days_info == "Sunday" :
            school_days . extend ( [ "Friday" , "Saturday" , "Sunday" ] )

        no_of_lectures = (end - begin ) // lecture
        time_slots_class = {}

        for day in school_days :
            for time in range ( no_of_lectures ):
                begin_str = str (begin)
                timing = begin + lecture
                end_str = str ( timing )
                slot = begin_str + " to " + end_str + "  " + day
                time_slots_class [ slot ] = s.time_slots [ slot ]
                begin = timing

            s.start_hours_info = int(from_hours.get())
            s.start_minutes_info = int(from_minutes.get())
            begin = timedelta (hours = s.start_hours_info , minutes = s.start_minutes_info)

        return time_slots_class



#------------------------------------------------------------------Slot creation for teachers--------------------------------------------------------------------------

    
    def slot_creation_for_teachers (s , Tstart_hours , Tstart_minutes , Tend_hours , Tend_minutes):
    
        arrival = timedelta (hours = Tstart_hours , minutes = Tstart_minutes)

        departure = timedelta ( hours = Tend_hours , minutes = Tend_minutes)

        lecture_duration = timedelta ( minutes = s.lecture_duration_info) 

        s.days_info = s.days.get()

        school_days = [ "Monday" , "Tuesday" , "Wednesday" , "Thursday" ]

        if s.days_info == "Friday" :
            school_days . append ( "Friday" )

        elif s.days_info == "Saturday" :
            school_days . extend ( [ "Friday" , "Saturday" ] )

        elif s.days_info == "Sunday" :
            school_days . extend ( [ "Friday" , "Saturday" , "Sunday" ] )

        no_of_Teachers_lectures = (departure - arrival ) // lecture_duration
        time_slots_teachers = {}

        for day in school_days :
            for s.time in range ( no_of_Teachers_lectures ):
                arrival_str = str (arrival)
                any_time = arrival + lecture_duration
                depart_str = str ( any_time )
                Teachers_slot = arrival_str + " to " + depart_str + "  " + day
                time_slots_teachers [ Teachers_slot ] = s.time_slots [ Teachers_slot ]
                arrival = any_time
                

            s.Teacher_start_hours_info = int(Tstart_hours)
            s.Teacher_start_minutes_info = int(Tend_hours)
            arrival = timedelta (hours = Tstart_hours , minutes = Tstart_minutes)
            
        return time_slots_teachers

    

#----------------------------------------------------------------------------------------------------Classes window----------------------------------------------------------------------------------------------------

    def classes(s):

        s.create_masters_window.withdraw()
        
        s.classes_window = tkinter.Toplevel()
        s.classes_window. title ( "Classes")
        s.classes_window. geometry ( "750x200" )
        s.classes_window. configure ( bg = "White")

        s.heading = tkinter.Label ( s.classes_window , text="2.Classes",
                                              font=( "Times New Roman" , 18 , "bold") ,
                                              bg = "White" ,
                                              fg = "DodgerBlue4").grid (column = 1 , row = 0 , columnspan = 6 , pady = 10 )

        s.class_from = tkinter.IntVar()
        s.class_to = tkinter.IntVar()

        s.class_from_label = tkinter.Label ( s.classes_window , text = "You educate from class: ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                fg = "black").grid (column = 1 , row = 1 , pady = 20 , padx = 20) 
        
        s.class_from_spin = tkinter.Spinbox ( s.classes_window ,
                                                 from_ = 1 ,
                                                 to = 12 ,
                                                 font = ( "Times New Roman" , 14 ) ,
                                                 width = 5 ,
                                                  justify = "center", textvariable = s.class_from) . grid ( column = 2 , row = 1 , padx = 20)

        s.class_to_label = tkinter.Label ( s.classes_window , text = "You educate till class: ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                fg = "black").grid (column = 3 , row = 1 , pady = 20) 
        
        s.class_to_spin = tkinter.Spinbox ( s.classes_window ,
                                                 from_ = 1 ,
                                                 to = 12 ,
                                                 font = ( "Times New Roman" , 14 ) ,
                                                 width = 5 ,
                                                  justify = "center", textvariable = s.class_to) . grid ( column = 4 , row = 1 , padx = 30)

        s.go_ahead_button = tkinter.Button (s.classes_window ,
                                                                      text = "Go Ahead! " ,
                                                                      font = ( "Times New Roman" , 14 , "bold" ) ,
                                                                      fg = "white" ,
                                                                      bg = "black",
                                                                      width="20",
                                                                      height="1", command = s.add_classes).grid ( column = 1 , row = 2 , columnspan = 5 , pady = 20)

        s.classes_window.mainloop()
    

#------------------------------------------------------------------------------------------------------------Classes Inputs--------------------------------------------------------------------------------------------
    
    def add_classes(s):

        if s.update_check == 0 :

            s.classes_window.withdraw()
            
            s.class_from_info = s.class_from.get()
            s.class_to_info = s.class_to.get()
            s.count = s.class_from_info -1
            s.classes = int(s.class_from_info)
            s.classes_list = []
            for classlis in range ( s.class_from_info , s.class_to_info +1 ):
                s.classes_list.append(classlis)

        else:
            s.classes_update_window . withdraw ()
            s.classes = int(s.class_update_variable . get ())
            s.display_subjects = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
            cursor = s.display_subjects . cursor ()
            cursor . execute ("SELECT MAX(Class),MIN(class) FROM Classes")
            fetch = cursor . fetchone ()
            s.class_from_info= fetch[1]
            s.class_to_info = fetch [0]
            s.slots_for_entire_school = s.slot_creation_for_school ( s.starthours , s.startminutes , s.endhours , s.endminutes )
  
        
        s.class_window = tkinter.Toplevel()
        s.class_window. title ( "Classes")
        s.class_window.geometry ("600x700")
        s.class_window. configure ( bg = "White")


        
        if s.classes >= int(s.class_from_info) and s.classes <= int(s.class_to_info):

            s.class_var = "Class   " + str(s.classes)
            
            s.class_label = tkinter.Label ( s.class_window , text = s.class_var , 
                                                font=("Times New Roman", 18 ,"bold") ,
                                                bg = "black" ,
                                                fg = "white").grid (column = 1 , row = 2 , columnspan = 6 , pady = 20 , ipadx = 30 , ipady = 5)

#------------------------------------------------------------------------------------------Class arrival timings----------------------------------------------------------------------------------------------------

            s.starthours = tkinter.IntVar()
            s.startminutes = tkinter.IntVar()
            
            
            s.class_start = tkinter.Label ( s.class_window , text = "Arrives at : ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 1 , row = 5 , pady = 20)

            s.class_start_hours = tkinter.Spinbox ( s.class_window ,
                                                 from_ = 1 ,
                                                 to = 24 ,
                                                 font = ( "Times New Roman" , 14 ) ,
                                                 width = 5 ,
                                                  justify = "center",
                                                  textvariable = s.starthours) . grid ( column = 1 , row = 6 )

            hours_label = tkinter.Label ( s.class_window , text = "hrs ",
                                                font=("Times New Roman",14 , "italic" , "bold" ) ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 2 , row = 6)

            s.class_start_minutes = tkinter.Spinbox ( s.class_window ,
                                                     from_ = 0,
                                                     to = 60 ,
                                                     font = ( "Times New Roman" , 14 ) ,
                                                     width = 5 ,
                                                      justify = "center",
                                                      textvariable = s.startminutes ,
                                                      increment = 5) . grid ( column = 3 , row = 6 )

            minutes_label = tkinter.Label ( s.class_window , text = "mins ",
                                                font=("Times New Roman",14 , "italic" , "bold") ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 4 , row = 6)
    
#---------------------------------------------------------------------------------------------------Class departure timings---------------------------------------------------------------------------------------

            s.endhours = tkinter.IntVar()
            s.endminutes = tkinter.IntVar()
            
            
            s.class_end = tkinter.Label ( s.class_window , text = "Departs at : ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 1 , row = 7 , pady = 20)

            s.class_end_hours = tkinter.Spinbox ( s.class_window ,
                                                 from_ = 1 ,
                                                 to = 24 ,
                                                 font = ( "Times New Roman" , 14 ) ,
                                                 width = 5 ,
                                                  justify = "center",
                                                  textvariable = s.endhours) . grid ( column = 1 , row = 8 )

            hours_2_label = tkinter.Label ( s.class_window , text = "hrs ",
                                                font=("Times New Roman",14 , "italic" , "bold") ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 2 , row = 8)

            s.class_end_minutes = tkinter.Spinbox ( s.class_window ,
                                                     from_ = 0,
                                                     to = 60 ,
                                                     font = ( "Times New Roman" , 14 ) ,
                                                     width = 5 ,
                                                      justify = "center",
                                                      textvariable = s.endminutes ,
                                                    increment = 5) . grid ( column = 3 , row = 8 )

            minutes_2_label = tkinter.Label ( s.class_window , text = "mins ",
                                                font=("Times New Roman",14 , "italic" , "bold") ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 4 , row = 8)

            
            s.sub_selection_label = tkinter.Label ( s.class_window , text = "Subjects studied: ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 1 , row = 9 , pady = 20 , padx = 10)


            s.displaying_subjects()

#------------------------------------------------------------------------------------------------Displaying subjects in dropdown menus------------------------------------------------------------------------------

    def displaying_subjects (s) :
            
        s.display_subjects = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
                
        s.cursor = s.display_subjects . cursor()
        s.cursor.execute ( "SELECT * FROM Subjects")
        s.rows = s.cursor.fetchall ()
        s.subjects = ["None"]
        
        for s.subject in s.rows :
            s.subjects.append ( s.subject [ 1 ] )

        s.subject_1_variable = tkinter.StringVar()
        s.subject_2_variable = tkinter.StringVar()
        s.subject_3_variable = tkinter.StringVar()
        s.subject_4_variable = tkinter.StringVar()
        s.subject_5_variable = tkinter.StringVar()
        s.subject_6_variable = tkinter.StringVar()
        s.subject_7_variable = tkinter.StringVar()
        s.subject_8_variable = tkinter.StringVar()

#-----------------------------------------------------------------------------------------------Subject 1 for class --------------------------------------------------------------------------------------------------

        subject_1_label = tkinter.Label ( s.class_window , text = "Subject 1 ",
                                                font=("Times New Roman",12) ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 1 , row = 10 , padx = 5 , pady = 12)

        subject_1= ttk.Combobox ( s.class_window ,
                                                          width = 12 ,
                                                           textvariable = s.subject_1_variable ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        subject_1 [ 'values' ] = tuple ( s.subjects )
        subject_1.grid ( column = 2 , row =10 , pady = 12)
        subject_1.current(0)
        
#-----------------------------------------------------------------------------------------------Subject 2 for class--------------------------------------------------------------------------------------------------

        subject_2_label = tkinter.Label ( s.class_window , text = "Subject 2 ",
                                                font=("Times New Roman",12) ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 3 , row = 10 , padx = 10 , pady = 12)

        subject_2= ttk.Combobox ( s.class_window ,
                                                          width = 12 ,
                                                           textvariable = s.subject_2_variable ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        subject_2 [ 'values' ] = tuple (s. subjects )
        subject_2.grid ( column = 4 , row =10 , pady = 12 , padx = 10)
        subject_2.current(0)

#-----------------------------------------------------------------------------------------------Subject 3 for class--------------------------------------------------------------------------------------------------

        subject_3_label = tkinter.Label ( s.class_window , text = "Subject 3 ",
                                                font=("Times New Roman",12) ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 1 , row = 11 , padx = 5 , pady = 12)

        subject_3 = ttk.Combobox ( s.class_window ,
                                                          width = 12 ,
                                                           textvariable = s.subject_3_variable ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        subject_3 [ 'values' ] = tuple ( s.subjects )
        subject_3.grid ( column = 2 , row =11 , pady = 12)
        subject_3.current(0)

#-----------------------------------------------------------------------------------------------Subject 4 for class--------------------------------------------------------------------------------------------------

        subject_4_label = tkinter.Label ( s.class_window , text = "Subject 4 ",
                                                font=("Times New Roman",12) ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 3 , row = 11, padx = 10 , pady = 12)

        subject_4 = ttk.Combobox ( s.class_window ,
                                                          width = 12 ,
                                                           textvariable = s.subject_4_variable ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        subject_4 [ 'values' ] = tuple ( s.subjects )
        subject_4.grid ( column = 4 , row =11 , pady = 12 , padx = 10)
        subject_4.current(0)

#-----------------------------------------------------------------------------------------------Subject 5 for class--------------------------------------------------------------------------------------------------

        subject_5_label = tkinter.Label ( s.class_window , text = "Subject 5 ",
                                                font=("Times New Roman",12) ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 1 , row = 12, padx = 5 , pady = 12)

        subject_5 = ttk.Combobox ( s.class_window ,
                                                          width = 12 ,
                                                           textvariable = s.subject_5_variable ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        subject_5 [ 'values' ] = tuple ( s.subjects )
        subject_5.grid ( column = 2 , row =12 , pady = 12)
        subject_5.current(0)

#-----------------------------------------------------------------------------------------------Subject 6 for class--------------------------------------------------------------------------------------------------

        subject_6_label = tkinter.Label ( s.class_window , text = "Subject 6 ",
                                                font=("Times New Roman",12) ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 3 , row = 12, padx = 10 , pady = 12 )

        subject_6 = ttk.Combobox ( s.class_window ,
                                                          width = 12 ,
                                                           textvariable = s.subject_6_variable ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        subject_6 [ 'values' ] = tuple ( s.subjects )
        subject_6.grid ( column = 4 , row =12 , pady = 12 , padx = 10)
        subject_6.current(0)

        #-----------------------------------------------------------------------------------------------Subject 7 for class--------------------------------------------------------------------------------------------------

        subject_7_label = tkinter.Label ( s.class_window , text = "Subject 7 ",
                                                font=("Times New Roman",12) ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 1, row = 13, padx = 5 , pady = 12)

        subject_7 = ttk.Combobox ( s.class_window ,
                                                          width = 12 ,
                                                           textvariable = s.subject_7_variable ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        subject_7 [ 'values' ] = tuple ( s.subjects )
        subject_7.grid ( column = 2, row =13 , pady = 12)
        subject_7.current(0)

#-----------------------------------------------------------------------------------------------Subject 8 for class--------------------------------------------------------------------------------------------------

        subject_8_label = tkinter.Label ( s.class_window , text = "Subject 8 ",
                                                font=("Times New Roman",12) ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 3 , row = 13, padx = 10 , pady = 12)

        subject_8 = ttk.Combobox ( s.class_window ,
                                                          width = 12 ,
                                                           textvariable = s.subject_8_variable ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        subject_8 [ 'values' ] = tuple ( s.subjects )
        subject_8.grid ( column = 4 , row =13 , pady = 12 , padx = 10)
        subject_8.current(0)

#-----------------------------------------------------------------------------------------------------Lunch-----------------------------------------------------------------------------------------------------------------

        lunch_label = tkinter.Label ( s.class_window , text = "Lunch at : ",
                                                font=("Times New Roman",14 , "bold") ,
                                                bg = "White" ,
                                                 fg = "black"). place ( x = 150 , y = 585 )

        s.lunch_info = tkinter.StringVar()

        lunch = ttk.Combobox ( s.class_window ,
                                                          width = 25 ,
                                                           textvariable = s.lunch_info ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        lunch [ 'values' ] = tuple ( s.lunch_dropdown_2 )
        lunch.place (x = 260 , y= 585 )


        if s.update_check != 0 :

            s.store_class = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
            cursor = s.store_class . cursor ()
            cursor . execute ("SELECT * FROM Classes WHERE Class = %s" %(s.classes,))
            fetch = cursor . fetchone ()
            #print("Fetched",str(fetch[1]))
            s.starthours. set (str(fetch[1])[0])
            s.startminutes . set (str(fetch[1])[2:4])
            s.endhours. set (str(fetch[2])[:2])
            s.endminutes . set (str(fetch[2])[3:5])
            s.subject_1_variable.set(fetch[3])
            s.subject_2_variable.set(fetch[4])
            s.subject_3_variable.set(fetch[5])
            s.subject_4_variable.set(fetch[6])
            s.subject_5_variable.set(fetch[7])
            s.subject_6_variable.set(fetch[8])
            s.subject_7_variable.set(fetch[9])
            s.subject_8_variable.set(fetch[10])
            s.lunch_info . set (fetch[11])
            

        
#-------------------------------------------------------------------------------------------------Go Ahead Button--------------------------------------------------------------------------------------------------------
        
        s.add_class_button = tkinter.Button (s.class_window ,
                                                                      text = "Add Class " ,
                                                                      font = ( "Times New Roman" , 14 , "bold" ) ,
                                                                      fg = "white" ,
                                                                      bg = "black",
                                                                      width="10",
                                                                      height="1", command = s.store_classes).place ( x = 250 , y = 650 )
        if s.update_check == 0 :
            
            s.done_button = tkinter.Button (s.class_window ,
                                                        text = "Done " ,
                                                        font = ( "Times New Roman" , 14 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="10",
                                                        height="1" ,
                                                        command = s.teachers_window).place (x = 460 , y = 655)
#---------------------------------------------------------------------------------------------------Storing Classes--------------------------------------------------------------------------------------------------------        

    def store_classes(s):

        s.Crepeat_check +=1

        s.class_info = s.classes

        class_section_updation_list = []

        if s.update_check != 0 :
            for section in s.sections :
                class_section_updation_list . append ( str(s.class_info) + section)

            for class_and_section in class_section_updation_list :
                s.store_class = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
                cursor = s.store_class . cursor ()
                cursor.execute ( "DELETE FROM class_assignment WHERE Class_id = '%s'"%(class_and_section,))
                s.store_class.commit()
                cursor.close()
                s.store_class.close()
                
            s.store_class = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
            cursor = s.store_class . cursor ()
            cursor . execute ( "DELETE FROM Classes WHERE Class = '%s' " % (s.class_info,))
            s.store_class . commit ()
            cursor.close()
            s.store_class.close()
            
                        
        s.store_class = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
           
        

        s.start_hours_info = s.starthours.get()
        s.start_minutes_info = s.startminutes.get()

        s.end_hours_info = s.endhours.get()
        s.end_minutes_info = s.startminutes.get()

        s.class_lunch_info = s.lunch_info.get()
            
        s.arrival_time_info = str(s.start_hours_info) + ":" + str(s.start_minutes_info) 
        s.depart_time_info = str(s.end_hours_info) + ":" + str(s.end_minutes_info)

        slots = s.slot_creation_for_classes ( s.starthours , s.startminutes , s.endhours , s.endminutes )

        check_redundant_subjects = [s.subject_1_variable.get() , s.subject_2_variable.get() , s.subject_3_variable.get() , s.subject_4_variable.get() , s.subject_5_variable.get() , s.subject_6_variable.get() , s.subject_7_variable.get() , s.subject_8_variable.get() ]

        okay_subjects = []
        check = 0
        
        for element in check_redundant_subjects :
            if element != "None" and element not in okay_subjects :
                okay_subjects.append ( element )
            elif element != "None" and element in okay_subjects :
                messagebox.showerror ( "Redundant Subjects" , "Two subjects can not be the same, kindly change one of them." )
                check = 1

        if check != 1 :
        
            s.cursor = s.store_class.cursor()
            s.command = ( "INSERT INTO Classes VALUES (%s , %s , %s  , %s , %s , %s , %s , %s , %s , %s , %s , %s )")
            s.data = (s.class_info , s.arrival_time_info , s.depart_time_info , s.subject_1_variable.get() , s.subject_2_variable.get() , s.subject_3_variable.get() , s.subject_4_variable.get() , s.subject_5_variable.get() , s.subject_6_variable.get() , s.subject_7_variable.get() , s.subject_8_variable.get() , s.class_lunch_info )
            s.cursor.execute(s.command , s.data)
            s.store_class.commit()
            s.cursor.close()
            s.store_class.close()
            s.reset()
#--------------------------------------------------------------------creating none_dict_for classes------------------------------------------------------------------
            
        slots_for_entire_school = s.slots_for_entire_school.values()

        #print (s.Crepeat_check)
#-----------------------------------------------------------------class database-----------------------------------------------------------------------------------
        if s.Crepeat_check == 1 :

            if s.update_check == 0 :

                class1_list = mysql . connector . connect ( host = "localhost" ,
                                                           user = s.sql_username . get (),
                                                            passwd = s.sql_password . get () ,
                                                            database = s.user['name of the organisation'])
                cursor1 = class1_list . cursor ()

                cursor1.execute ("CREATE TABLE IF NOT EXISTS Class_Assignment ( Class_id VARCHAR (5) )")
                for i in range (len(slots_for_entire_school)) :
                    x= "`" +str(i) +"`"
                    cursor1.execute ("ALTER TABLE Class_Assignment ADD ( %s VARCHAR (7))" % (x,))
                cursor1.close()

            #----------------------------------------------------------- inserting values of class id in table -----------------------------------------------------------

            slot_values = slots.values()
            print(slot_values)
            x = int(s.class_lunch_info [-1])
            y = len(slots_for_entire_school)//len(s.school_days_list) 
            g=0
            for section_value in range (len(s.sections)) :
                none_list = []
                for i in range (len (slots_for_entire_school)) :
                    if i in slot_values :
                        none_list . insert (i , "N" )
                    else:
                        none_list . insert (i , "B")
                #print(none_list)
                for z in range (len(s.school_days_list)) :
                    none_list [x] = "Lunch"
                    x +=y
                #print(x,y)
                
                none_list.insert (0,str (s.class_info) + s.sections [section_value] )
                #print(none_list)
                #print(none_list)
                x = int(s.class_lunch_info [-1])
                #print(x)

                m = none_list[0]

                class2_list = mysql . connector . connect ( host = "localhost" ,
                                                       user = s.sql_username . get (),
                                                        passwd = s.sql_password . get () ,
                                                        database = s.user['name of the organisation'])

                cursor2 = class2_list . cursor ()
                
                cursor2.execute ("INSERT INTO Class_Assignment (class_id) VALUES ('%s')" % (m,))
                class2_list.commit()

                k = none_list . pop (0)
               
                for j in range (len(none_list)) :
                    g = none_list[j]
                    yz= "`" +str(j) +"`"
                    cursor2.execute("UPDATE Class_Assignment SET %s = '%s' WHERE class_id = '%s'"%(yz,g,k))
                class2_list.commit()  
                cursor2. close()

        elif s.Crepeat_check >1 :

            slot_values = slots.values()
            print(slot_values)
            x = int(s.class_lunch_info [-1])
            y = len(slots_for_entire_school)//len(s.school_days_list)
            g=0
            for section_value in range (len(s.sections)) :
                none_list = []
                for i in range (len (slots_for_entire_school)) :
                    if i in slot_values :
                        none_list . insert (i , "N" )
                    else:
                        none_list . insert (i , "B")
                for z in range (len(s.school_days_list)) :
                    none_list [x] = "Lunch"
                    x +=y
                    #print(x , y)
                
                none_list.insert (0,str (s.class_info) + s.sections [section_value] )
                #print(none_list)
                x = int(s.class_lunch_info [-1])
                #print(x)
                

                m = none_list[0]

                class2_list = mysql . connector . connect ( host = "localhost" ,
                                                           user = s.sql_username . get (),
                                                            passwd = s.sql_password . get () ,
                                                            database = s.user['name of the organisation'])

                cursor2 = class2_list . cursor ()
                    
                cursor2.execute ("INSERT INTO Class_Assignment (class_id) VALUES ('%s')" % (m,))
                class2_list.commit()

                k = none_list . pop (0)
                   
                for j in range (len(none_list)) :
                    g = none_list[j]
                    yz= "`" +str(j) +"`"
                    cursor2.execute("UPDATE Class_Assignment SET %s = '%s' WHERE class_id = '%s'"%(yz,g,k))
                class2_list.commit()  
                cursor2. close()


    #---------------------------------------------------------------------------------------------------Resetting for next clas input---------------------------------------------------------------------------------------

    def reset (s) :

        s.classes+=1
        
        if s.classes >= int(s.class_from_info) and s.classes <= int(s.class_to_info) and s.update_check == 0:

            s.class_var = "Class   " + str(s.classes)
            
            s.class_label = tkinter.Label ( s.class_window , text = s.class_var , 
                                                font=("Times New Roman", 18 ,"bold") ,
                                                bg = "black" ,
                                                fg = "white").grid (column = 1 , row = 2 , columnspan = 6 , pady = 30 , ipadx = 30 , ipady = 5)
            
            
            s.starthours.set(1)
            s.startminutes.set(0)

            s.endhours.set(1)
            s.endminutes.set(0)
            
            s.subject_1_variable.set("None")
            s.subject_2_variable.set("None")
            s.subject_3_variable.set("None")
            s.subject_4_variable.set("None")
            s.subject_5_variable.set("None")
            s.subject_6_variable.set("None")
            s.subject_7_variable.set("None")
            s.subject_8_variable.set("None")

            s.lunch_info . set ("") 
            
#-------------------------------------------------------------------------------done button------------------------------------------------------------------------------------
            
        if s.classes > int(s.class_to_info) and s.update_check ==0:
                
                s.cdone_button =  tkinter.Button (s.class_window ,
                                                                          text = "Done" ,
                                                                          font = ( "Times New Roman" , 14 , "bold" ) ,
                                                                          fg = "white" ,
                                                                          bg = "black",
                                                                          width="10",
                                                                          height="1" , command = s.teachers_window). place (x = 240 , y = 650 )

    #-------------------------------------------------------------------------------- Teachers Window ---------------------------------------------------------------------------------------------------------------------

    def teachers_window(s):

        if s.update_check == 0 :
            s.class_window.withdraw()
            s.create_masters_window.withdraw()
            

        elif s.teachers_buttons_check == 1 :
            s.teachers_buttons_window . withdraw ()
            
            s.teacher_name_for_updates = s.teacher_variable . get ()
            s.slots_for_entire_school = s.slot_creation_for_school ( s.starthours , s.startminutes , s.endhours , s.endminutes )

        else :
            s.updates_window.withdraw ()
            s.slots_for_entire_school = s.slot_creation_for_school ( s.starthours , s.startminutes , s.endhours , s.endminutes )
            
        
        s.create_teacher_window = tkinter.Toplevel()
        s.create_teacher_window.title ("Master Databases")
        s.create_teacher_window.geometry ("650x620")
        s.create_teacher_window.configure ( bg = "white")
        
        s.heading = tkinter.Label ( s.create_teacher_window , text = " 3. Teachers " ,
                                                   bg = "White" ,
                                                   fg = "DodgerBlue4" ,
                                                   font = ("Times New Roman" , 18 , "bold") ). grid (column = 0 , row = 0 , columnspan = 6 , pady = 20)
        if s.update_check == 0 :
            
            s.teacher_name = tkinter.Label ( s.create_teacher_window , text = "Teacher's name : ",
                                                        font=("Times New Roman",14,"bold") ,
                                                        bg = "White" ,
                                                        fg = "black").grid (column = 1 , row = 3 , pady = 20 , padx = 20)
            s.teacher_name = tkinter.StringVar()

            s.teacher_name_entry = tkinter.Entry (s.create_teacher_window ,
                                                                width="30" ,
                                                                font = ("Times New Roman" , 14) ,
                                                                textvariable = s.teacher_name ,
                                                                borderwidth = 2 ,
                                                                relief = "ridge").grid (column = 2 , row = 3 , pady = 20)
        if  s.teachers_buttons_check == 1:
            s.teacher_name = tkinter.Label ( s.create_teacher_window , text = "Teacher's name : ",
                                                        font=("Times New Roman",14,"bold") ,
                                                        bg = "White" ,
                                                        fg = "black").grid (column = 1 , row = 3 , pady = 20 , padx = 20)
            
            s.teacher_name = tkinter.StringVar()

            s.teacher_name_entry = tkinter.Entry (s.create_teacher_window ,
                                                                width="30" ,
                                                                font = ("Times New Roman" , 14) ,
                                                                textvariable = s.teacher_name ,
                                                                borderwidth = 2 ,
                                                                relief = "ridge").grid (column = 2 , row = 3 , pady = 20)
            s.teacher_name.set(s.teacher_name_for_updates)

        else :

            s.teacher_name = tkinter.Label ( s.create_teacher_window , text = "Teacher's name : ",
                                                        font=("Times New Roman",14,"bold") ,
                                                        bg = "White" ,
                                                        fg = "black").grid (column = 1 , row = 3 , pady = 20 , padx = 20)
            s.teacher_name = tkinter.StringVar()

            s.teacher_name_entry = tkinter.Entry (s.create_teacher_window ,
                                                                width="30" ,
                                                                font = ("Times New Roman" , 14) ,
                                                                textvariable = s.teacher_name ,
                                                                borderwidth = 2 ,
                                                                relief = "ridge").grid (column = 2 , row = 3 , pady = 20)
        

    #------------------------------------------------------------------------------------------teacher arrival timings-------------------------------------------------------------------------------------------------------

        s.Tstarthours = tkinter.IntVar()
        s.Tstartminutes = tkinter.IntVar()
        
            
        s.teacher_start = tkinter.Label ( s.create_teacher_window, text = "Arrives at : ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 1 , row = 5 , pady = 20)
        
        s.teacher_start_hours = tkinter.Spinbox (s.create_teacher_window,
                                                 from_ = 1 ,
                                                 to = 24 ,
                                                 font = ( "Times New Roman" , 14 ) ,
                                                 width = 5 ,
                                                  justify = "center",
                                                  textvariable = s.Tstarthours) . grid ( column = 1 , row = 6 )

        hours_label = tkinter.Label ( s.create_teacher_window , text = "hrs ",
                                                font=("Times New Roman",14 , "italic" , "bold") ,
                                                bg = "White" ,
                                                 fg = "black").place(x=155 , y= 205 )

        s.teacher_start_minutes = tkinter.Spinbox (s.create_teacher_window ,
                                                     from_ = 0,
                                                     to = 60 ,
                                                     font = ( "Times New Roman" , 14 ) ,
                                                     width = 5 ,
                                                      justify = "center",
                                                      textvariable = s.Tstartminutes ,
                                                       increment = 5) . place (x = 250 , y = 208)
        
        minutes_label = tkinter.Label ( s.create_teacher_window , text = "mins ",
                                                font=("Times New Roman",14 , "italic" , "bold") ,
                                                bg = "White" ,
                                                 fg = "black").place ( x = 340,  y = 205)
        
    #---------------------------------------------------------------------------------------------------teacher departure timings------------------------------------------------------------------------------------------

        s.Tendhours = tkinter.IntVar()
        s.Tendminutes = tkinter.IntVar()
            
            
        s.teacher_end = tkinter.Label ( s.create_teacher_window , text = "Departs at : ",
                                            font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 1 , row = 7,pady = 20 )
        
        s.teacher_end_hours = tkinter.Spinbox ( s.create_teacher_window ,
                                                 from_ = 1 ,
                                                 to = 24 ,
                                                 font = ( "Times New Roman" , 14 ) ,
                                                 width = 5 ,
                                                  justify = "center",
                                                  textvariable = s.Tendhours) . grid ( column = 1 , row = 8 )

        hours_2_label = tkinter.Label ( s.create_teacher_window , text = "hrs ",
                                                font=("Times New Roman",14 , "italic" , "bold") ,
                                                bg = "White" ,
                                                 fg = "black").place ( x =155 , y = 300 )

        s.teacher_end_minutes = tkinter.Spinbox ( s.create_teacher_window ,
                                                     from_ = 0,
                                                     to = 60 ,
                                                     font = ( "Times New Roman" , 14 ) ,
                                                     width = 5 ,
                                                      justify = "center",
                                                      textvariable = s.Tendminutes ,
                                                      increment = 5) . place ( x = 250 , y = 300 )

        minutes_label = tkinter.Label ( s.create_teacher_window , text = "mins ",
                                                font=("Times New Roman",14 , "italic" , "bold") ,
                                                bg = "White" ,
                                                 fg = "black"). place ( x = 340 , y = 300 )
        
        s.add_Tsubjects()

   #------------------------------------------------------------------------------------------------Subjects taught by the teacher-----------------------------------------------------------------------------------------
        
    def add_Tsubjects(s):
        
        s.display_Tsubjects = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
                
        s.Tcursor = s.display_Tsubjects . cursor()
        s.Tcursor.execute ( "SELECT * FROM Subjects")
        s.Trows = s.Tcursor.fetchall ()
        s.Tsubjects = ["None"]

        s.Tsubject_1_variable = tkinter.StringVar()
        s.Tsubject_2_variable = tkinter.StringVar()
        s.Tsubject_3_variable = tkinter.StringVar()
        
    #----------------------------------------------------------------------------------------Teacher Subject 1 Input---------------------------------------------------------------------------------------------------------
        
        for s.Tsubject in s.Trows :
            s.Tsubjects.append ( s.Tsubject [ 1 ] )

        Tsubject_1_label = tkinter.Label ( s.create_teacher_window, text = "Subject 1 ",
                                                font=("Times New Roman",14,"bold"),
                                                bg = "White" ,
                                                 fg = "black").grid (column = 1 , row = 10 , pady = 20 )

        Tsubject_1= ttk.Combobox ( s.create_teacher_window ,
                                                          width = 12 ,
                                                           textvariable = s.Tsubject_1_variable ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        Tsubject_1 [ 'values' ] = tuple ( s.Tsubjects )
        Tsubject_1.grid ( column = 1 , row =11 , pady = 12)
        Tsubject_1.current(0)
        
    #--------------------------------------------------------------------------------------------Teacher Subject 2 Input---------------------------------------------------------------------------------------------------
        
        Tsubject_2_label = tkinter.Label ( s.create_teacher_window , text = "Subject 2 ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 2 , row = 10 , pady = 20 )

        Tsubject_2= ttk.Combobox ( s.create_teacher_window ,
                                                          width = 12 ,
                                                           textvariable = s.Tsubject_2_variable ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        Tsubject_2 [ 'values' ] = tuple (s. Tsubjects )
        Tsubject_2.grid ( column = 2 , row =11 )
        Tsubject_2.current(0)
        
#------------------------------------------------------------------------------------------------Teacher Subject 3 Input--------------------------------------------------------------------------------------------------
        
        Tsubject_3_label = tkinter.Label ( s.create_teacher_window , text = "Subject 3 ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                 fg = "black").grid (column = 3 , row = 10 , padx = 10 , pady = 20)

        Tsubject_3= ttk.Combobox ( s.create_teacher_window ,
                                                          width = 12 ,
                                                           textvariable = s.Tsubject_3_variable ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        Tsubject_3 [ 'values' ] = tuple (s. Tsubjects )
        Tsubject_3.grid ( column = 3 , row =11)
        Tsubject_3.current(0)


#-----------------------------------------------------------------------------------------------------Lunch-----------------------------------------------------------------------------------------------------------------

        lunch_label = tkinter.Label ( s.create_teacher_window , text = "Lunch at : ",
                                                font=("Times New Roman",14 , "bold") ,
                                                bg = "White" ,
                                                 fg = "black"). place ( x = 150 , y = 480 )

        s.Tlunch_info = tkinter.StringVar()

        lunch = ttk.Combobox ( s.create_teacher_window ,
                                                          width = 25 ,
                                                           textvariable = s.Tlunch_info ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        lunch [ 'values' ] = tuple ( s.lunch_dropdown_2 )
        lunch.place (x = 260 , y = 480 )

        if s.teachers_buttons_check == 1:

            s.store_class = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
            cursor = s.store_class . cursor ()
            cursor . execute ("SELECT * FROM Teachers WHERE Teacher_name = '%s'" %(s.teacher_name_for_updates,))
            fetch = cursor . fetchone ()
            #print("Fetched",str(fetch[1]))
            s.Tstarthours. set (str(fetch[2])[0])
            s.Tstartminutes . set (str(fetch[2])[2:4])
            s.Tendhours. set (str(fetch[3])[:2])
            s.Tendminutes . set (str(fetch[3])[3:5])
            s.Tsubject_1_variable.set(fetch[4])
            s.Tsubject_2_variable.set(fetch[5])
            s.Tsubject_3_variable.set(fetch[6])
            s.Tlunch_info . set (fetch[7])
        

        s.add_teacher_button = tkinter.Button ( s.create_teacher_window,
                                                                      text = "Add Teacher " ,
                                                                      font = ( "Times New Roman" , 12 , "bold" ) ,
                                                                      fg = "white" ,
                                                                      bg = "black",
                                                                      width="15",
                                                                      height="1", command = s.store_teacher). place ( x = 260 , y = 540 )
        if s.update_check == 0:
            
            s.Tdone_button = tkinter.Button ( s.create_teacher_window,
                                                                      text = "Done" ,
                                                                      font = ( "Times New Roman" , 12 , "bold" ) ,
                                                                      fg = "white" ,
                                                                      bg = "black",
                                                                      width="10",
                                                                      height="1" ,
                                                                      command = s.link_window). place ( x = 500 , y = 580 )
        

#----------------------------------------------------------------------------------------------------Storing Teacher Data---------------------------------------------------------------------------------------------
        
    def store_teacher(s):

        try :

            if s.update_check != 0 and s.teachers_buttons_check != 0:

                s.store_updated_link = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
                cursor1 = s.store_updated_link. cursor ()

                cursor1. execute ( "SELECT Teacher_name , Teacher_id FROM Teachers WHERE Teacher_name = '%s' " %(s.teacher_name_for_updates , ) )

                row = cursor1.fetchone ()
                #print(row)
                s.update_teacher_id =  row [1]
                cursor1.close()
                s.store_updated_link.close()

                s.store_class = mysql.connector.connect ( host="localhost",
                                                                                        user = s.sql_username . get (),
                                                                                        passwd = s.sql_password . get () ,
                                                                                        database = s.user['name of the organisation'])
                cursor = s.store_class . cursor ()
                cursor.execute ( "DELETE FROM teacher_assignment WHERE teacher_id = '%s'"%(s.update_teacher_id,))
                s.store_class.commit()
                cursor.close()
                s.store_class.close()

                s.store_class = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
                cursor = s.store_class . cursor ()
                cursor . execute ( "DELETE FROM teachers WHERE teacher_id = '%s' " % (s.update_teacher_id,))
                s.store_class . commit ()
                cursor.close()
                s.store_class.close()

            

            s.Trepeat_check += 1
            
            s.store_teachers = mysql.connector.connect ( host="localhost",
                                                                                        user = s.sql_username . get (),
                                                                                        passwd = s.sql_password . get () ,
                                                                                        database = s.user['name of the organisation'])
            
            s.Tstart_hours_info = s.Tstarthours.get()
            s.Tstart_minutes_info = s.Tstartminutes.get()
            

            s.Tend_hours_info = s.Tendhours.get()
            s.Tend_minutes_info = s.Tstartminutes.get()

            s.teacher_lunch_info = s.Tlunch_info . get()
            
            s.teacher_id=s.teacher_id+1
            
            s.Tarrival_time_info = str(s.Tstart_hours_info) + ":" + str(s.Tstart_minutes_info) 
            s.Tdepart_time_info = str(s.Tend_hours_info) + ":" + str(s.Tend_minutes_info)

            check_redundant_subjects = [s.Tsubject_1_variable.get() , s.Tsubject_2_variable.get() , s.Tsubject_3_variable.get()  ]

            okay_subjects = []
            check = 0
            
            for element in check_redundant_subjects :
                
                if element != "None" and element not in okay_subjects :
                    
                    okay_subjects . append ( element )
                    
                elif element != "None" and element in okay_subjects :
                    
                    messagebox.showerror ( "Redundant Subjects" , "Two subjects can not be the same, kindly change one of them." )
                    check = 1

            if check != 1 :
            
                s.Tcursor = s.store_teachers.cursor()
                s.Tcommand = ( "INSERT INTO Teachers VALUES (%s , %s , %s , %s  , %s , %s , %s , %s )")
                s.Tdata = ("T" + str(s.teacher_id), s.teacher_name.get() , s.Tarrival_time_info , s.Tdepart_time_info , s.Tsubject_1_variable.get() , s.Tsubject_2_variable.get() , s.Tsubject_3_variable.get() , s.teacher_lunch_info)
                s.Tcursor.execute(s.Tcommand,s.Tdata)
          
                s.store_teachers.commit()
                
                s.Tcursor.close()
                s.store_teachers.close()
                s.reset_teacher()

            s.teacher_slots = s.slot_creation_for_teachers ( s.Tstart_hours_info , s.Tstart_minutes_info , s.Tend_hours_info , s.Tend_minutes_info )
            

    #-------------------------------------------------------------creating none variables for teachers---------------------------------------------------------------------
            
            slots_for_entire_school = s.slots_for_entire_school . values ()
            slot_values = s.teacher_slots .values ()
            x = int(s.teacher_lunch_info[-1])
            y = len(slots_for_entire_school)//len ( s.school_days_list )
            g=0
            none_list = []
            for i in range (len (slots_for_entire_school)) :
                if i in slot_values :
                    none_list . insert (i , "N" )
                else:
                    none_list . insert (i , "B")
            for z in range (len ( s.school_days_list )) :
                none_list [x] = "Lunch"
                x +=y

            x = int ( s.teacher_lunch_info [-1] )
            none_list . insert ( 0 , "T" + str(s.teacher_id) )

            
             
            if s.Trepeat_check == 1 :

                if s.update_check == 0:
                
                    teacher1_list = mysql.connector.connect ( host = "localhost" ,
                                                               user = s.sql_username . get (),
                                                                passwd = s.sql_password . get () ,
                                                                database = s.user['name of the organisation'])


                    cursor1 = teacher1_list . cursor ()

                    cursor1.execute ("CREATE TABLE IF NOT EXISTS Teacher_Assignment ( Teacher_id VARCHAR (5) )")
                
                    for i in range (len(s.slots_for_entire_school)) :
                        x= "`" +str(i) +"`"
                        cursor1.execute ("ALTER TABLE Teacher_Assignment ADD ( %s VARCHAR (7))" % (x,))

                    cursor1.close()
                    teacher1_list.close()

                    #----------------------------------------------------------- inserting values of teacher id in table -----------------------------------------------------------
                teacher1_list = mysql.connector.connect ( host = "localhost" ,
                                                               user = s.sql_username . get (),
                                                                passwd = s.sql_password . get () ,
                                                                database = s.user['name of the organisation'])
                cursor1 = teacher1_list . cursor ()
                n= none_list[0]
                    
                cursor1.execute ("INSERT INTO Teacher_Assignment (Teacher_id) VALUES ('%s')" % (n,))   
                teacher1_list.commit()

                l= none_list.pop(0)
                    
                for a in range (len(none_list)) :
                    n = none_list[a]
                    e= "`" +str(a) +"`"
                        #print(n,e)
                    cursor1.execute("UPDATE Teacher_Assignment SET %s = '%s' WHERE Teacher_id = '%s'"%(e,n,l))
                        
                            
                teacher1_list.commit()  
                cursor1. close()
                
            else:

                teacher1_list = mysql.connector.connect ( host = "localhost" ,
                                                           user = s.sql_username . get (),
                                                            passwd = s.sql_password . get () ,
                                                            database = s.user['name of the organisation'])


                cursor1 = teacher1_list . cursor ()

                n= none_list[0]
                
                cursor1.execute ("INSERT INTO Teacher_Assignment (Teacher_id) VALUES ('%s')" % (n,))   
                teacher1_list.commit()

                l= none_list.pop(0)
                
                for a in range (len(none_list)) :
                    n = none_list[a]
                    e= "`" +str(a) +"`"
                    #print(n,e)
                    cursor1.execute("UPDATE Teacher_Assignment SET %s = '%s' WHERE Teacher_id = '%s'"%(e,n,l))
                    
                        
                teacher1_list.commit()  
                cursor1. close()

        except mysql.connector.errors.IntegrityError:

            
            
            s.add_teachers = mysql.connector.connect ( host="localhost",
                                                                        user = s.sql_username .get (),
                                                                        passwd = s.sql_password . get (),
                                                                        database = s.user['name of the organisation'])
            s.add_teacher = s.add_teachers.cursor()
            s.add_teacher . execute ( "SELECT MAX(teacher_id) FROM teachers;")
            s.id_fetch = s.add_teacher . fetchone ()
            s.max_id = s.id_fetch [0]
            
            s.add_teacher . close()
            s.add_teachers.close ()

            s.add_subjects = mysql.connector.connect (host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
            
            s.teacher_id = int(s.max_id[1::])+1

            s.Trepeat_check += 1
            
            s.store_teachers = mysql.connector.connect ( host="localhost",
                                                                                        user = s.sql_username . get (),
                                                                                        passwd = s.sql_password . get () ,
                                                                                        database = s.user['name of the organisation'])
            
            s.Tstart_hours_info = s.Tstarthours.get()
            s.Tstart_minutes_info = s.Tstartminutes.get()
            

            s.Tend_hours_info = s.Tendhours.get()
            s.Tend_minutes_info = s.Tstartminutes.get()

            s.teacher_lunch_info = s.Tlunch_info . get()
            
            
            s.Tarrival_time_info = str(s.Tstart_hours_info) + ":" + str(s.Tstart_minutes_info) 
            s.Tdepart_time_info = str(s.Tend_hours_info) + ":" + str(s.Tend_minutes_info)

            check_redundant_subjects = [s.Tsubject_1_variable.get() , s.Tsubject_2_variable.get() , s.Tsubject_3_variable.get()  ]

            okay_subjects = []
            check = 0
            
            for element in check_redundant_subjects :
                
                if element != "None" and element not in okay_subjects :
                    
                    okay_subjects . append ( element )
                    
                elif element != "None" and element in okay_subjects :
                    
                    messagebox.showerror ( "Redundant Subjects" , "Two subjects can not be the same, kindly change one of them." )
                    check = 1

            if check != 1 :
            
                s.Tcursor = s.store_teachers.cursor()
                s.Tcommand = ( "INSERT INTO Teachers VALUES (%s , %s , %s , %s  , %s , %s , %s , %s )")
                s.Tdata = ("T" + str(s.teacher_id), s.teacher_name.get() , s.Tarrival_time_info , s.Tdepart_time_info , s.Tsubject_1_variable.get() , s.Tsubject_2_variable.get() , s.Tsubject_3_variable.get() , s.teacher_lunch_info)
                s.Tcursor.execute(s.Tcommand,s.Tdata)
          
                s.store_teachers.commit()
                
                s.Tcursor.close()
                s.store_teachers.close()
                s.reset_teacher()

            s.teacher_slots = s.slot_creation_for_teachers ( s.Tstart_hours_info , s.Tstart_minutes_info , s.Tend_hours_info , s.Tend_minutes_info )
            

    #-------------------------------------------------------------creating none variables for teachers---------------------------------------------------------------------
            
            slots_for_entire_school = s.slots_for_entire_school . values ()
            slot_values = s.teacher_slots .values ()
            x = int(s.teacher_lunch_info[-1])
            y = len(slots_for_entire_school)//len ( s.school_days_list )
            g=0
            none_list = []
            for i in range (len (slots_for_entire_school)) :
                if i in slot_values :
                    none_list . insert (i , "N" )
                else:
                    none_list . insert (i , "B")
            for z in range (len ( s.school_days_list )) :
                none_list [x] = "Lunch"
                x +=y

            x = int ( s.teacher_lunch_info [-1] )
            none_list . insert ( 0 , "T" + str(s.teacher_id) )

            
             
            if s.Trepeat_check == 1 :
                
                teacher1_list = mysql.connector.connect ( host = "localhost" ,
                                                           user = s.sql_username . get (),
                                                            passwd = s.sql_password . get () ,
                                                            database = s.user['name of the organisation'])


                cursor1 = teacher1_list . cursor ()

                cursor1.execute ("CREATE TABLE IF NOT EXISTS Teacher_Assignment ( Teacher_id VARCHAR (5) )")
            
                for i in range (len(s.slots_for_entire_school)) :
                    x= "`" +str(i) +"`"
                    cursor1.execute ("ALTER TABLE Teacher_Assignment ADD ( %s VARCHAR (7))" % (x,))

                #----------------------------------------------------------- inserting values of teacher id in table -----------------------------------------------------------

                n= none_list[0]
                
                cursor1.execute ("INSERT INTO Teacher_Assignment (Teacher_id) VALUES ('%s')" % (n,))   
                teacher1_list.commit()

                l= none_list.pop(0)
                
                for a in range (len(none_list)) :
                    n = none_list[a]
                    e= "`" +str(a) +"`"
                    #print(n,e)
                    cursor1.execute("UPDATE Teacher_Assignment SET %s = '%s' WHERE Teacher_id = '%s'"%(e,n,l))
                    
                        
                teacher1_list.commit()  
                cursor1. close()
                
            else:

                teacher1_list = mysql.connector.connect ( host = "localhost" ,
                                                           user = s.sql_username . get (),
                                                            passwd = s.sql_password . get () ,
                                                            database = s.user['name of the organisation'])


                cursor1 = teacher1_list . cursor ()

                n= none_list[0]
                
                cursor1.execute ("INSERT INTO Teacher_Assignment (Teacher_id) VALUES ('%s')" % (n,))   
                teacher1_list.commit()

                l= none_list.pop(0)
                
                for a in range (len(none_list)) :
                    n = none_list[a]
                    e= "`" +str(a) +"`"
                    #print(n,e)
                    cursor1.execute("UPDATE Teacher_Assignment SET %s = '%s' WHERE Teacher_id = '%s'"%(e,n,l))
                    
                        
                teacher1_list.commit()  
                cursor1. close()
            

    #---------------------------------------------------------------------------------------------Resetting for next Teacher Input----------------------------------------------------------------------------------------
        
    def reset_teacher(s):

        s.Tstarthours.set(1)
        s.Tstartminutes.set(0)
        
        s.Tendhours.set(1)
        s.Tendminutes.set(0)
        
        s.Tsubject_1_variable.set("None")
        s.Tsubject_2_variable.set("None")
        s.Tsubject_3_variable.set("None")
        
        s.teacher_name.set("")

        s.Tlunch_info . set ("")

    #-----------------------------------------------------------------------------------------------Linking Window---------------------------------------------------------------------------------------------------------
        
    def link_window(s):

        s.create_teacher_window .withdraw()

        s.Lrepeat_check +=1
        
        
        s.linking_window = tkinter.Toplevel()
        s.linking_window. title ( "Subject - Teacher - Class Linking")
        s.linking_window.geometry ("380x370")
        s.linking_window. configure ( bg = "White")
        s.class_label123()
        
   #---------------------------------------------------------------------------------------------------The class Label------------------------------------------------------------------------------------------------------
        
    def class_label123(s):
   
        if s.class_aa < len (s.classes_list) :

            s.class_label = tkinter.Label ( s.linking_window , text = "Class " + str(s.classes_list[s.class_aa]) , 
                                                    font=("Times New Roman", 18 ,"bold") ,
                                                    bg = "black" ,
                                                    fg = "white" 
                                                ).grid (column = 0 , row = 0 , columnspan = 3 , pady = 30 , ipadx = 30 , ipady = 5)
 
        if s.class_aa == 0:
            s.teacher_extraction()
        else:
            s.subject_extraction()
            
    #---------------------------------------------------------------------------------------Extracting Teachers that teach perticular subjects---------------------------------------------------------------------------
            
    def teacher_extraction (s) :
        
        s.linking = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])

        s.extract_teacher = s.linking.cursor ()
        s.extract_teacher.execute ( "SELECT Teacher_name , Subject_1 , Subject_2 , Subject_3 FROM Teachers ")
        s.teachers = s.extract_teacher.fetchall()

        s.extract_teacher.close()
        s.subject_extraction()
        
    #-----------------------------------------------------------------------------------Extracting Subjects that the particular class studies-----------------------------------------------------------------------------
        
    def subject_extraction(s):
        
        s.linking1 = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
        
        #s.count = s.class_from_info -1
        s.count +=1
        #change this count to class_from variable till class to variable
        s.extract_subjects = s.linking1.cursor()
     
        
        s.extract_subjects.execute("SELECT Subject_1,Subject_2,Subject_3,Subject_4,Subject_5,Subject_6,Subject_7,Subject_8 FROM Classes WHERE Class = %s "%(s.count,) )
        
        s.extract_class_subjects = s.extract_subjects.fetchone()
        
        s.class_subjects = []
        
        for sub in s.extract_class_subjects:
            if sub != "None":
                s.class_subjects.append(sub)


        s.linking1.close()

        s.variables = []

        for s.variable in range (len(s.class_subjects)) :
            s.var = "Variable" + str (s.variable)
            s.variables.append (s.var)

        s.d = {}
        teachers =[]

        for sub in s.class_subjects :
            for teacher in s.teachers:
                if teacher [1] == sub:
                    teachers.append (teacher[0])
                elif teacher[2] == sub :
                    teachers .append (teacher[0])
                elif teacher [3] ==sub :
                    teachers.append (teacher[0])

            s.d[sub] = tuple(teachers )
                
            teachers.clear()


        s.link_graphics()

    #---------------------------------------------------------------------------------------------Graphics for the linking window----------------------------------------------------------------------------------------

    def link_graphics (s) :
                                            
        if s.block < len(s.sections) and s.sub < len(s.class_subjects):

            s.class_id = str(s.classes_list[s.class_aa]) + s.sections[s.block]

            s.class_id_label = tkinter.Label ( s.linking_window , text = s.class_id,
                                                            font=("Times New Roman",18,"bold" , "underline") ,
                                                            bg = "White" ,
                                                            fg = "black" ,
                                                            width = 20).grid (column = 1 , row = 1 , pady = 10 ,  padx = 20 , columnspan = 2)


            if s.sub < len (s.class_subjects) :
     

                s.subject_1 = s.class_subjects [s.sub]

                s.blank_label = tkinter.Label ( s.linking_window , text = "wejkk",
                                                            font=("Times New Roman",14) ,
                                                            bg = "White" ,
                                                            fg = "White" ,
                                                            width = 17).grid (column = 1 , row = 2 , pady = 10 ,  padx = 20)

                s.sub_label = tkinter.Label ( s.linking_window , text = s.subject_1,
                                                            font=("Times New Roman",14) ,
                                                            bg = "White" ,
                                                            fg = "black").grid (column = 1 , row = 2 , pady = 10 ,  padx = 20)
            

                s.combo = str(s.variables[s.block2]) 
                    
                s.combo = tkinter.StringVar ()

                subject_1= ttk.Combobox ( s.linking_window ,
                                                                  width = 12 ,
                                                                   textvariable = s.combo ,
                                                                    font = ( "Times New Roman" , 12 ) ,
                                                                    justify = "center" )
                
                subject_1 [ 'values' ] = s.d[s.class_subjects[s.block2]]
                subject_1.grid ( column = 2 , row = 2 , pady = 10)

                s.entry = "Entry" + str(s.variables[s.block2])

                s.entry = tkinter.StringVar ()

                lecture_label = tkinter.Label ( s.linking_window, text = "Lectures per week: ",
                                                                font=("Times New Roman", 14) ,
                                                                bg = "White" ,
                                                                fg = "black").grid (column = 1 , row = 3,  padx = 20 , pady = 10)

                lecture_entry = tkinter.Entry ( s.linking_window ,
                                                                width="10" ,
                                                                font = ("Times New Roman" , 12) ,
                                                                textvariable = s.entry ,
                                                                borderwidth = 2 ,
                                                                relief = "ridge").grid (column = 2 , row = 3 , pady =10)


                #------------------------------------------------------------Button for changing subject when input for all the sections has been taken-------------------------------------------------------------------

                if s.block == len(s.sections) -1:

                    s.save_button = tkinter.Button (s.linking_window ,
                                                        text = "Save Data" ,
                                                        font = ( "Times New Roman" , 12 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="10",
                                                        height="1" ,
                                                        command = s.change_subject).grid ( column = 1 , row = 4, pady = 10 , padx = 50 , columnspan = 2)
                    
               #----------------------------------------------------------------------------------Button for storing data in SQL tables--------------------------------------------------------------------------------------
                    
                else:

                    s.save_button = tkinter.Button (s.linking_window ,
                                                        text = "Save Data" ,
                                                        font = ( "Times New Roman" , 12 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="10",
                                                        height="1" ,
                                                        command = s.store_data).grid ( column = 1 , row = 4, pady = 10 , padx = 50 , columnspan = 2)
                   

         #-----------------------------------------------------Button for changing class when inputs for all sections and subjects has been taken---------------------------------------------------------------------
                    
                    
        if s.sub == len(s.class_subjects)-1 and s.block == len(s.sections)-1:
            s.save_button = tkinter.Button (s.linking_window ,
                                                        text = "Save Data" ,
                                                        font = ( "Times New Roman" , 12 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="10",
                                                        height="1" ,
                                                        command = s.change_class).grid ( column = 1 , row = 4, pady = 10 , padx = 50 , columnspan = 2)

        if s.sub == len(s.class_subjects)-1 and s.block == len(s.sections)-1 and s.class_aa == len (s.classes_list )-1:
            
            #print("Done")

            s.Done_button = tkinter.Button (s.linking_window ,
                                                        text = "Done" ,
                                                        font = ( "Times New Roman" , 12 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="10",
                                                        height="1" ,
                                                        command = s.shift_to_checks).grid ( column = 1 , row = 4, pady = 10 , padx = 50 , columnspan = 2)
            
    #------------------------------------------------------------------------------------------Storing data function----------------------------------------------------------------------------------------------------
            
    def store_data (s) :

        s.add_data = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
        
        s.subject_cursor = s.add_data.cursor()
        s.subject_cursor.execute("SELECT * FROM Subjects")
        s.subject_ids = s.subject_cursor.fetchall()
        s.subject_cursor.close()

        s.teacher_cursor = s.add_data.cursor()
        s.teacher_cursor.execute ( "SELECT Teacher_name , Teacher_id FROM Teachers")
        s.teacher_ids = s.teacher_cursor.fetchall ()
        s.teacher_cursor.close()
            
        subject = s.subject_1

        #----------------------------------------------------------------------------------------------Finding Subject ID of the subject-----------------------------------------------------------------------------------
        
        for s_id in s.subject_ids :
            if s_id [1] == subject :
                sub_id = s_id[0]
                break

        #----------------------------------------------------------------------------------------------Finding Teacher ID for the Teacher-----------------------------------------------------------------------------
                
        s.teacher = s.combo.get()
            
        for t_id in s.teacher_ids :
            if t_id [0] == s.teacher :
                s.teachers_id = t_id [1]
                break
                
        lec_per_week = s.entry.get()
  
        data = (s.class_id , sub_id , s.teachers_id , lec_per_week )

        data_101 = (s.class_id , sub_id , s.teachers_id )

        s.add_to_link_table_1 = s.add_data.cursor()
        s.command_1 = ( "INSERT INTO Linking VALUES ( %s , %s , %s , %s ) ")
        s.add_to_link_table_1 . execute ( s.command_1 , data)
        s.add_data . commit ()
        s.add_to_link_table_1 . close()
        
                        

        s.block += 1
        s.link_graphics()

    #---------------------------------------------------------------------------------------------Subject Changing Function---------------------------------------------------------------------------------------------

    def change_subject (s) :

        s.add_data = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
        
        s.subject_cursor = s.add_data.cursor()
        s.subject_cursor.execute("SELECT * FROM Subjects")
        s.subject_ids = s.subject_cursor.fetchall()
        s.subject_cursor.close()

        s.teacher_cursor = s.add_data.cursor()
        s.teacher_cursor.execute ( "SELECT Teacher_name , Teacher_id FROM Teachers")
        s.teacher_ids = s.teacher_cursor.fetchall ()
        s.teacher_cursor.close()
            
        subject = s.subject_1
        
        for s_id in s.subject_ids :
            if s_id [1] == subject :
                sub_id = s_id[0]
                break
                
        s.teacher = s.combo.get()
            
        for t_id in s.teacher_ids :
            if t_id [0] == s.teacher :
                s.teachers_id = t_id [1]
                break
                
        lec_per_week = s.entry.get()
  
        data = (s.class_id , sub_id , s.teachers_id , lec_per_week )

        data_202 = (s.class_id , sub_id , s.teachers_id )
        
        s.add_to_link_table_2 = s.add_data.cursor()
        s.command_2 = ( "INSERT INTO Linking VALUES ( %s , %s , %s , %s ) ")
        s.add_to_link_table_2 . execute ( s.command_2 , data)
        s.add_data . commit ()
        s.add_to_link_table_2 . close()


        #-------------------------------------------------------------------Above code for saving info below code for actucally changing subject----------------------------------------------------------------------

        s.sub +=1
        s.block2 +=1
        s.block = 0
        s.link_graphics()

    #-----------------------------------------------------------------------------------------------Class changing funtion-----------------------------------------------------------------------------------------------

    def change_class (s) :

        s.add_data = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
        
        s.subject_cursor = s.add_data.cursor()
        s.subject_cursor.execute("SELECT * FROM Subjects")
        s.subject_ids = s.subject_cursor.fetchall()
        s.subject_cursor.close()

        s.teacher_cursor = s.add_data.cursor()
        s.teacher_cursor.execute ( "SELECT Teacher_name , Teacher_id FROM Teachers")
        s.teacher_ids = s.teacher_cursor.fetchall ()
        s.teacher_cursor.close()
        
        subject = s.subject_1
        
        for s_id in s.subject_ids :
            if s_id [1] == subject :
                sub_id = s_id[0]
                break
                
        s.teacher = s.combo.get()
            
        for t_id in s.teacher_ids :
            if t_id [0] == s.teacher :
                s.teachers_id = t_id [1]
                break
                
        lec_per_week = s.entry.get()
  
        data = (s.class_id , sub_id , s.teachers_id , lec_per_week )

        data_303 = (s.class_id , sub_id , s.teachers_id )
        
        s.add_to_link_table_3 = s.add_data.cursor()
        s.command_3 = ( "INSERT INTO Linking VALUES ( %s , %s , %s , %s ) ")
        s.add_to_link_table_3 . execute ( s.command_3 , data)
        s.add_data . commit ()
        s.add_to_link_table_3 . close()
        
        #------------------------------------------------------------Above code for saving info below code for actually changing the class----------------------------------------------------------------------------
        
        s.class_aa +=1
        s.block = 0
        s.block2 = 0
        s.sub = 0
        s.class_label123()


    def shift_to_checks (s):

        s.add_data = mysql.connector.connect ( host="localhost",
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
        
        s.subject_cursor = s.add_data.cursor()
        s.subject_cursor.execute("SELECT * FROM Subjects")
        s.subject_ids = s.subject_cursor.fetchall()
        s.subject_cursor.close()

        s.teacher_cursor = s.add_data.cursor()
        s.teacher_cursor.execute ( "SELECT Teacher_name , Teacher_id FROM Teachers")
        s.teacher_ids = s.teacher_cursor.fetchall ()
        s.teacher_cursor.close()
        
        subject = s.subject_1
        
        for s_id in s.subject_ids :
            if s_id [1] == subject :
                sub_id = s_id[0]
                break
                
        s.teacher = s.combo.get()
            
        for t_id in s.teacher_ids :
            if t_id [0] == s.teacher :
                s.teachers_id = t_id [1]
                break
                
        lec_per_week = s.entry.get()
  
        data = (s.class_id , sub_id , s.teachers_id , lec_per_week )

        data_303 = (s.class_id , sub_id , s.teachers_id )
        
        s.add_to_link_table_3 = s.add_data.cursor()
        s.command_3 = ( "INSERT INTO Linking VALUES ( %s , %s , %s , %s ) ")
        s.add_to_link_table_3 . execute ( s.command_3 , data)
        s.add_data . commit ()
        s.add_to_link_table_3 . close()



        s. fetching_linking_data ()
        s.choose_teacher_or_class()

#-----------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------Lecture assignment----------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
    def sql_class_updation (s,changed_list , class_id):
        class1_list = mysql.connector.connect ( host="localhost",
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
        cursor1 = class1_list . cursor ()
        m= changed_list[0]
        k= class_id 
       
        for j in range (len(changed_list)) :
            g = changed_list[j]
            y= "`" +str(j) +"`"
            cursor1.execute("UPDATE Class_Assignment SET %s = '%s' WHERE class_id = '%s'"%(y,g,k))
        class1_list.commit()
        
        cursor1. close()
        class1_list.close()
#--------------------------------------------------------- teacher updation -------------------------------------------------------------------------------------------------    
    def sql_teacher_updation (s,changed_list , teacher_id):
        
        class1_list = mysql.connector.connect ( host="localhost",
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
        cursor1 = class1_list.cursor ()
        m= changed_list[0]
        k= teacher_id 
        for j in range (len(changed_list)) :
            g = changed_list[j]
            y= "`" +str(j) +"`"
            cursor1.execute("UPDATE teacher_Assignment SET %s = '%s' WHERE teacher_id = '%s'"%(y,g,k))
        class1_list.commit()
        
        cursor1. close()
        class1_list.close()

    def fetching_linking_data(s):
        s.class1_list = mysql . connector . connect ( host="localhost",
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
       
        cursor2 = s.class1_list.cursor()
        cursor2.execute ( "SELECT Class_id FROM class_assignment")
        s.class_checks_list = []
        class_checks_fetch = cursor2.fetchall()
        cursor2.close()
        s.class1_list.close()
        for class_checks_id in class_checks_fetch :
            s.class_checks_list . append (class_checks_id)
        s.actual_assignment()

    def actual_assignment (s) :
       
        if 0<= s.checks < len (s.class_checks_list):
            #print("Came here")
            s.class1_list = mysql . connector . connect ( host="localhost",
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
            cursor1 = s.class1_list.cursor()
            #print("Class ID",class_checks_list[s.checks][0])
            cursor1.execute("SELECT * FROM Linking WHERE Class_id = '%s'" %(s.class_checks_list[s.checks][0],))
            
            s.l_rows = cursor1.fetchall()
            
            if 0<=s.c < len(s.l_rows):
                print("s.l_rows[s.c]" ,s.l_rows[s.c])
                
                s.class1 = s.l_rows[s.c][0]
                s.teacher1 = s.l_rows[s.c][2] 
                s.subject1 = s.l_rows[s.c][1] 
                s.lec_no = s.l_rows[s.c][3]
                
                s.class1_list.commit()
                cursor1.close()
                s.class1_list.close()
                
                s.fetching_class_data()
                
            else :
                
                s.checks +=1
                s.c = 0
                s.actual_assignment()
                
                
        else:
            print("over1")
            
            
            
        
    
#-----------------------------------fetching class slots from class assignment table------------------------------------------------------------
    def fetching_class_data(s):
        class2_list = mysql . connector . connect ( host="localhost",
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
        cursor2 = class2_list.cursor()
        cursor2.execute("SELECT * FROM class_assignment WHERE Class_id = '%s'" %s.class1)
        s.c_rows = cursor2.fetchall()
        class2_list.close()
        for s.c_row in s.c_rows:
            s.clist = list (s.c_row[1::])
        print(s.clist)
        cursor2.close()
        s.fetching_teacher_data()
        

#-----------------------------------fetching teacher slots from teacher assignment table------------------------------------------------------------
    def fetching_teacher_data(s):
        class3_list = mysql . connector . connect( host="localhost",
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
        cursor3 = class3_list.cursor()
        cursor3.execute("SELECT * FROM teacher_assignment WHERE teacher_id = '%s'" %s.teacher1)
        s.t_rows = cursor3.fetchall()
        class3_list.close()
        for s.t_row in s.t_rows:
            s.tlist = list (s.t_row[1::])
        print(s.tlist)
        cursor3.close()
        s.create_nested_day_list()
        
#---------------------------------------------creating nested list -----------------------------------------------------------------------------------

    def create_nested_day_list(s):
        counter = 0
        
        s.nested_slot_list =[]
        
        s.no_of_lectures_per_day = (len(s.clist)) // len(s.school_days_list)
        for i in range(len(s.school_days_list)):
            a=[]
            for j in range(s.no_of_lectures_per_day ):
                a.append(counter)
                
                counter+=1
            s.nested_slot_list.append(a)
        s.teacher_conversion = list(s.nested_slot_list)
       
        
        s.lecture_assignment()

    
    def normal_to_nested (s, slot_list ) :  
        a = 0
        b = 0
        list_nest = []
        for i in s.teacher_conversion :
            
            nest = []
            for j in i :
              
                nest . insert (a, slot_list[j])
                a +=1
            list_nest . insert (b,nest)
            b+=1
            a = 0
        return list_nest
    
    def nested_to_normal(s, slot_list  ):
        s.original = []
        for x in slot_list :
            for y in x :
                s.original . append (y)
        return s.original

  

#-------------------------------------------------------------------lecture assignment -----------------------------------------------------------------------------
    def lecture_assignment(s) :


        if 0 < s.lec_no > len(s.nested_slot_list):
            
            s.random_no = random . choice (s.nested_to_normal(s.nested_slot_list))
            print("printing the nested slot list here" , s.nested_slot_list)
            
            
            if s.random_no == len (s.clist) -1 :
                if  (s.clist [ s.random_no ] == "N" and s.clist [ s.random_no - 1 ] == "N"  and s.tlist [ s.random_no ] == "N" and s.tlist [ s.random_no -1 ] == "N"):
                    s.check_block_backward ()
            elif s.random_no == 0:
                if (s.clist [ s.random_no ] == "N" and s.clist [ s.random_no + 1 ] == "N"  and s.tlist [ s.random_no ] == "N" and s.tlist [ s.random_no +1 ] == "N"):
                    s.check_block_forward()
            else :
                if (s.clist [ s.random_no ] == "N" and s.clist [ s.random_no + 1 ] == "N"  and s.tlist [ s.random_no ] == "N" and s.tlist [ s.random_no +1 ] == "N"):
                    s.check_block_forward()

                elif  (s.clist [ s.random_no ] == "N" and s.clist [ s.random_no - 1 ] == "N"  and s.tlist [ s.random_no ] == "N" and s.tlist [ s.random_no -1 ] == "N"):
                    s.check_block_forward ()
                else:
                    
                    s.lecture_assignment()
                    
        if 0< s.lec_no <= len(s.nested_slot_list) :
            
            s.random_no = random . choice (s.nested_to_normal(s.nested_slot_list))
            
            
            if s.clist [ s.random_no ] == "N" and s.tlist [ s.random_no ] == "N" :
                s.check_day ()
            else:
                
                s.lecture_assignment ()
                
        if s.lec_no == 0 :
            s.sql_class_updation (s.clist , s.class1)
            s.sql_teacher_updation (s.tlist ,s.teacher1)
            s.c+=1
            
            s.actual_assignment()
            print("over2")
#-----------------------------------------------------------------check day------------------------------------------------------------------------------------

    def check_day (s) :
        
        for day in s.nested_slot_list :
            if s.random_no in day  :
                s.random_no_index = day.index (s.random_no)
                s.day_index = s.nested_slot_list.index (day)
                
                s.clist [ s.random_no ] = s.subject1
                s.tlist [ s.random_no ] = s.class1
                y = s.consecutive_teachers_check ()
                if y == 1 :
                    
                    s.nested_slot_list . remove ( day )
                    s.lec_no-=1
                   
                    s.lecture_assignment ()
        
                elif y == -1 :
                    s.clist [ s.random_no ] = "N"
                    s.tlist [ s.random_no ] = "N"
                    
                    s.lecture_assignment ()
                  
                break
        else:
            
            s.lecture_assignment ()
       
            
    def check_block_forward (s):
        
        for day in s.nested_slot_list :
            if s.random_no in day and s.random_no+1 in day :
                s.random_no_index = day.index (s.random_no)
                s.day_index = s.nested_slot_list.index(day)
                
                s.clist [ s.random_no ] , s.clist [ s.random_no +1 ] = s.subject1,s.subject1
                s.tlist [ s.random_no ] , s.tlist [ s.random_no +1 ] = s.class1, s.class1
                
            
                
                y = s.consecutive_teachers_check ()
                if y == 1 :
                    
                    s.nested_slot_list . remove ( day )
                    
                    
                    s.lec_no -= 2
                    
                    s.lecture_assignment ()
                    break
                elif y == -1 :
                    
                    s.clist [ s.random_no ] , s.clist [ s.random_no +1 ] = "N","N"
                    s.tlist [ s.random_no ] , s.tlist [ s.random_no +1 ] = "N","N"
                    
                    s.lecture_assignment ()
                    
                    break
        else:
            
            s.lecture_assignment ()
                      
        
    def check_block_backward (s):
        
        for day in s.nested_slot_list :
            if (s.random_no and s.random_no-1) in day :
                s.random_no_index = day.index (s.random_no )
                s.day_index = s.nested_slot_list.index(day)
                
                s.clist [ s.random_no ] , s.clist [ s.random_no -1 ] = s.subject1 , s.subject1
                s.tlist [ s.random_no ] , s.tlist [ s.random_no -1 ] = s.class1, s.class1
                
                
                y = s.consecutive_teachers_check ()
                if y == 1 :
                    
                    s.nested_slot_list . remove ( day )
                    
                    
                    s.lec_no -= 2
                    
                    s.lecture_assignment ()
                elif y == -1 :
                    s.clist [ s.random_no ] , s.clist [ s.random_no +1 ] = "N","N"
                    s.tlist [ s.random_no ] , s.tlist [ s.random_no +1 ] = "N","N"
                    
                    s.lecture_assignment ()
                break
                
        else:
            
            s.lecture_assignment ()
        
        
       
#-----------------------------------------------------------------consecutive teachers -------------------------------------------------------------------------------
    def lunch_to_none(s,somelist):
        l=[]
        for i in somelist:
            if i == "Lunch":
                l.append("N")
            else:
                l.append(i)
        return l

    def consecutive_teachers_check (s) :
        s.check_list = s.lunch_to_none(s.tlist)
        s.teachers_converted = s.normal_to_nested (s.check_list)
        count = 0
        for y in range ( len (s.teachers_converted[0]) - 3) : 
            if  s.teachers_converted  [ s.day_index ] [ y ] != "N" and s.teachers_converted  [ s.day_index ] [ y+1 ] != "N" and s.teachers_converted [ s.day_index ] [ y+2 ] != "N" and  s.teachers_converted [ s.day_index ] [ y+3 ] == "N" :
                count = -1
                break
            else:
                count = 1
          
        return count
#------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------Time Table Display-----------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------

    
    def choose_teacher_or_class (s) :
        
        #s.view

        if s.new_assignment == 1:
            s.updates_window.withdraw ()

        if s.Lrepeat_check == 0:
            #s.school_days_list = []
            s.school_inputs_window . withdraw()
            f = open ("School_Days.txt","rb")
            try:
                while True :
                    p = pickle . load (f)
                    if p["Organisation"] == s.user['name of the organisation']:
                        s.school_days_list = p["School Days"]
            except EOFError :
                f.close()

        else:
            s.linking_window.withdraw()

        s.choose_window = tkinter.Toplevel()
        s.choose_window.title (" Choose! ")
        s.choose_window . geometry ("480x250")
        s.choose_window.configure ( bg = "white")

        s.heading  = tkinter.Label ( s.choose_window ,
                                        text = "Which Time Tables would you like to view ?",
                                        font=("Times New Roman",18 , "bold") ,
                                        bg = "White" ,
                                        fg = "DodgerBlue4").pack(pady = 10)

        s.class_button = tkinter.Button ( s.choose_window ,
                                          text = "Classes" ,
                                          font = ( "Times New Roman" , 14 , "bold" ) ,
                                          fg = "white" ,
                                          bg = "black",
                                          width="20",
                                          height="1" ,
                                          command = s.classes_buttons). pack(pady = 20)
        
        s.Teacher_button = tkinter.Button ( s.choose_window ,
                                          text = "Teachers" ,
                                          font = ( "Times New Roman" , 14 , "bold" ) ,
                                          fg = "white" ,
                                          bg = "black",
                                          width="20",
                                          height="1" ,
                                          command = s.teachers_buttons). pack(pady = 10) 


    def classes_buttons (s) :

        #s.choose_window.withdraw()

        s.classes_buttons_window = tkinter.Toplevel()
        s.classes_buttons_window.title ("Choose your class.")
        s.classes_buttons_window.configure ( bg = "white")
        
        row = 0
        column = 0

        s.heading  = tkinter.Label ( s.classes_buttons_window ,
                                        text = "Which class' Time Table would you like to view ?",
                                        font=("Times New Roman",18 , "bold") ,
                                        bg = "White" ,
                                        fg = "DodgerBlue4"). grid (  column = 0 , row = 0 , columnspan = 2 , pady = 10 , padx = 20 )

        display_sql = mysql.connector.connect ( host = "localhost" ,
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
        cursor1 = display_sql . cursor ()

        cursor1. execute ("SELECT Class_id FROM Class_Assignment")

        rows = cursor1.fetchall ()

        classes_and_sections_list = []

        for row1 in rows :
            classes_and_sections_list . append (row1)


        s.class_heading  = tkinter.Label ( s.classes_buttons_window ,
                                            text = "Select Class : ",
                                            font=("Times New Roman",16 , "bold") ,
                                            bg = "White" ,
                                            fg = "Black"). grid ( column = 0 , row = 1 , padx = 10 , pady = 15 )

        s.class_variable = tkinter.StringVar ()

        classes = ttk.Combobox ( s.classes_buttons_window ,
                                        width = 25 ,
                                        textvariable = s.class_variable ,
                                        font = ( "Times New Roman" , 12 ) ,
                                        justify = "center" )
            
        classes[ 'values' ] = tuple ( classes_and_sections_list )
        classes.grid ( column = 1 , row = 1 , pady = 15 , padx = 10)

        s.done_button = tkinter.Button ( s.classes_buttons_window ,
                                              text = "Done",
                                              font = ( "Times New Roman" , 14 , "bold" ) ,
                                              fg = "white" ,
                                              bg = "black",
                                              width="10",
                                              height="1" ,
                                              command = s.class_time_table). grid ( column = 0 , row = 2  , padx = 10 , pady =10 , columnspan = 2)
                

    def class_time_table (s) :

        CID = s.class_variable.get()
        s. display_window_classes (CID)
       

    def teachers_buttons (s):

        s.teachers_buttons_check += 1

        s.teachers_buttons_window = tkinter.Toplevel()
        s.teachers_buttons_window.title ("Choose a Teacher.")
        s.teachers_buttons_window.configure ( bg = "white")
        s.teachers_buttons_window . geometry ("600x200")

        

        if s.update_check != 0:
            s.updates_window . withdraw ()
            s.heading  = tkinter.Label ( s.teachers_buttons_window ,
                                            text = "Which Teacher's Record would you like to update?",
                                            font=("Times New Roman",18 , "bold") ,
                                            bg = "White" ,
                                            fg = "DodgerBlue4"). grid ( column = 0 , row = 0 , columnspan = 2 , pady = 10 , padx = 20 )

            
        else:
            #s.choose_window.withdraw()

            s.heading  = tkinter.Label ( s.teachers_buttons_window ,
                                            text = "Which Teacher's Time Table would you like to view ?",
                                            font=("Times New Roman",18 , "bold") ,
                                            bg = "White" ,
                                            fg = "DodgerBlue4"). grid ( column = 0 , row = 0 , columnspan = 2 , pady = 10 , padx = 20 )

        display_sql = mysql.connector.connect (host = "localhost" ,
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
        cursor1 = display_sql . cursor ()

        cursor1 . execute ( "SELECT Teacher_name FROM Teachers ")

        rows = cursor1.fetchall()

        teachers_names_list = []


        for teacher in rows :

            teachers_names_list . append (teacher[0])

        s.teacher_heading  = tkinter.Label ( s.teachers_buttons_window ,
                                        text = "Select Teacher : ",
                                        font=("Times New Roman",16 , "bold") ,
                                        bg = "White" ,
                                        fg = "Black"). grid ( column = 0 , row = 1 , padx = 10 , pady = 15 )

        s.teacher_variable = tkinter . StringVar ()

        teacher = ttk.Combobox ( s.teachers_buttons_window ,
                                    width = 25 ,
                                    textvariable = s.teacher_variable ,
                                    font = ( "Times New Roman" , 12 ) ,
                                    justify = "center" )
        
        teacher[ 'values' ] = tuple ( teachers_names_list )
        teacher.grid ( column = 1 , row = 1 , pady = 15 , padx = 10)

        if s.update_check == 0 :

            s.done_button = tkinter.Button ( s.teachers_buttons_window ,
                                          text = "Done",
                                          font = ( "Times New Roman" , 14 , "bold" ) ,
                                          fg = "white" ,
                                          bg = "black",
                                          width="10",
                                          height="1" ,
                                          command = s.teacher_time_table). grid ( column = 0 , row = 2  , padx = 10 , pady =10 , columnspan = 2)
        elif s.new_assignment == 1 :
            s.done_button = tkinter.Button ( s.teachers_buttons_window ,
                                          text = "Done",
                                          font = ( "Times New Roman" , 14 , "bold" ) ,
                                          fg = "white" ,
                                          bg = "black",
                                          width="10",
                                          height="1" ,
                                          command = s.teacher_time_table). grid ( column = 0 , row = 2  , padx = 10 , pady =10 , columnspan = 2)

        elif s. update_check == 0 and s.teachers_buttons_check == 1:
            
            s.done_button = tkinter.Button ( s.teachers_buttons_window ,
                                          text = "Done",
                                          font = ( "Times New Roman" , 14 , "bold" ) ,
                                          fg = "white" ,
                                          bg = "black",
                                          width="10",
                                          height="1" ,
                                          command = s.teacher_time_table). grid ( column = 0 , row = 2  , padx = 10 , pady =10 , columnspan = 2)
            
            
        else :
            s.done_button = tkinter.Button ( s.teachers_buttons_window ,
                                          text = "Done",
                                          font = ( "Times New Roman" , 14 , "bold" ) ,
                                          fg = "white" ,
                                          bg = "black",
                                          width="10",
                                          height="1" ,
                                          command = s.teachers_window). grid ( column = 0 , row = 2  , padx = 10 , pady =10 , columnspan = 2)
            
    def teacher_time_table ( s ) :

        s.teacher_selected = s.teacher_variable . get ()

        display_sql = mysql.connector.connect ( host = "localhost" ,
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
        cursor1 = display_sql . cursor ()

        cursor1 . execute( "SELECT Teacher_id , Teacher_name FROM Teachers WHERE Teacher_name = '%s' " % (s.teacher_selected , ) )

        row = cursor1.fetchone ()

        s . display_window_teachers (row[0])


    def display_window_classes (s , CID) :

        s.classes_buttons_window.withdraw()
        
        s.display_window = tkinter.Tk()
        s.display_window.title (" Your Time Table is ready ! ")
        s.display_window.configure ( bg = "white")

        display_sql = mysql.connector.connect ( host = "localhost" ,
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
        cursor1 = display_sql . cursor ()

        cursor1.execute ( "SELECT * FROM Class_Assignment WHERE Class_id = '%s' " % (CID, ))
        rows = cursor1.fetchone ()
        s.class_list = rows [1::]
        s.class_id_display = rows[0]
        
        no_school_days= len(s.school_days_list)
        
        s.create_nested_day_list_display()

    def create_nested_day_list_display(s):
        counter = 0
        s.nested_slot_list =[]
        s.no_of_lectures_per_day = (len(s.class_list)+1) // len(s.school_days_list)
        for i in range(len(s.school_days_list)):
            a=[]
            for j in range(s.no_of_lectures_per_day ):
                a.append(counter)
                counter+=1
            s.nested_slot_list.append(a)
        s.class_conversion = list(s.nested_slot_list)
        s.ready_to_display = s.normal_to_nested_classes(s.class_list)

        s.time_table_classes()

    def subject_code_to_subject_name (s ,Sub_id) :

        display_sql = mysql.connector.connect ( host = "localhost" ,
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
        cursor1 = display_sql . cursor ()

        cursor1. execute ( "SELECT * FROM Subjects WHERE Subject_id = '%s' " %(Sub_id , ) )

        row = cursor1.fetchone ()
        return row [1]
        

    
    def normal_to_nested_classes (s, slot_list ) :
        a = 0
        b = 0
        list_nest = []
        for i in s.class_conversion :
            nest = []
            for j in i :
                nest . insert (a, slot_list[j])
                a +=1
            list_nest . insert (b,nest)
            b+=1
            a = 0
            
        return list_nest

    def lecture_timings (s) :

        f = open ( "School_slot_timings.txt" , "rb" )
        s.timings_list = []
        try :
            while True :
                p = pickle . load (f)
                for element in p :
                    if p[element] in s.nested_slot_list [0]:
                        s.timings_list . append ( element [:20] )
                                                
        except EOFError :
            f.close()


        return s.timings_list

    def time_table_classes (s) :

        row = 1
        column = 1

        s.class_label = tkinter.Label ( s.display_window ,
                                        text = s.class_id_display,
                                        font=("Times New Roman",35,"bold") ,
                                        bg = "black" ,
                                        fg = "white" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column , row = row , rowspan = 2 , ipadx = 20 , ipady =20)

        for day in s.school_days_list:

            s.day_label = tkinter.Label ( s.display_window ,
                                        text = day,
                                        font=("Times New Roman",16,"bold") ,
                                        bg = "black" ,
                                        fg = "white" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column , row = row +2  , ipadx = 20 , ipady =15, padx = 10 , pady = 10)
            row +=1

        row = 1

        for lecture_no in s.nested_slot_list [0] :

            s.lecture_label = tkinter.Label ( s.display_window ,
                                        text = lecture_no,
                                        font=("Times New Roman",16,"bold") ,
                                        bg = "black" ,
                                        fg = "white" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column +1 , row = row , ipadx = 30 , ipady =10 , pady = 10 , padx = 10)
            
            column += 1

        row = 1
        column = 1

        s.timings_list = s.lecture_timings()

        for lecture_time in s.timings_list :

            s.lecture_label = tkinter.Label ( s.display_window ,
                                        text = lecture_time,
                                        font=("Times New Roman",12 , "bold") ,
                                        bg = "black" ,
                                        fg = "white" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column +1 , row = row +1 , ipadx = 2, ipady = 5 , pady = 10 , padx = 10)
            column +=1
            
        row = 2
        column = 1
       
        for day in s.ready_to_display :
            for lecture in day :

                if lecture == "B" :
                    s.lecture_label = tkinter.Label ( s.display_window ,
                                        text = "----",
                                        font=("Times New Roman",16) ,
                                        bg = "White" ,
                                        fg = "Black" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column +1  , row = row+1 , ipadx = 40 , ipady =15 , pady = 8 , padx = 10)
                    column += 1

                elif lecture == "N" :
                    s.lecture_label = tkinter.Label ( s.display_window ,
                                        text = "----",
                                        font=("Times New Roman",16) ,
                                        bg = "White" ,
                                        fg = "Black" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column +1  , row = row+1 , ipadx = 40 , ipady =15 , pady = 8 , padx = 10)
                    column += 1

                elif lecture == "Lunch" :
                    s.lecture_label = tkinter.Label ( s.display_window ,
                                        text = "Lunch",
                                        font=("Times New Roman",16) ,
                                        bg = "White" ,
                                        fg = "Black" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column +1  , row = row+1 , ipadx = 40 , ipady =15 , pady = 8 , padx = 10)
                    column += 1
                else:
                    
                    s.lecture_label = tkinter.Label ( s.display_window ,
                                        text = s.subject_code_to_subject_name (lecture),
                                        font=("Times New Roman",16) ,
                                        bg = "White" ,
                                        fg = "Black" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column +1  , row = row+1 , ipadx = 40 , ipady =15 , pady = 8 , padx = 10)
                    column += 1
            row += 1
            column = 1


    def display_window_teachers (s , TID) :

        s.teachers_buttons_window.withdraw()
        
        s.display_window = tkinter.Tk()
        s.display_window.title (" Your Time Table is ready ! ")
        s.display_window.configure ( bg = "white")

        display_sql = mysql.connector.connect ( host = "localhost" ,
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
        cursor1 = display_sql . cursor ()

        cursor1.execute ( "SELECT * FROM Teacher_Assignment WHERE Teacher_id = '%s' " %(TID,))
        rows = cursor1.fetchone ()
        s.teachers_list_display = rows [1::]
        s.Teacher_id = rows[0]
        
        no_school_days= len(s.school_days_list)
        
        s.create_nested_day_list_teachers()

    def create_nested_day_list_teachers(s):
        counter = 0
        s.nested_slot_list =[]
        s.no_of_lectures_per_day = (len(s.teachers_list_display)+1) // len(s.school_days_list)
        for i in range(len(s.school_days_list)):
            a=[]
            for j in range(s.no_of_lectures_per_day ):
                a.append(counter)
                counter+=1
            s.nested_slot_list.append(a)
        s.teacher_conversion = list(s.nested_slot_list)
        s.ready_to_display = s.normal_to_nested_teachers(s.teachers_list_display)

        s.time_table_teachers()

    def Teacher_code_to_Teacher_name (s ,Teacher_id) :

        display_sql = mysql.connector.connect ( host = "localhost" ,
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
        cursor1 = display_sql . cursor ()

        cursor1. execute ( "SELECT * FROM Teachers WHERE Teacher_id = '%s' " %(Teacher_id , ) )

        row = cursor1.fetchone ()
        #print(row)
        return row [1]
        

    
    def normal_to_nested_teachers (s, slot_list ) :  #days llist variable
        a = 0
        b = 0
        list_nest = []
        for i in s.teacher_conversion :
            nest = []
            for j in i :
                nest . insert (a, slot_list[j])
                a +=1
            list_nest . insert (b,nest)
            b+=1
            a = 0
            
        return list_nest

    def lecture_timings (s) :

        f = open ( "School_slot_timings.txt" , "rb" )
        s.timings_list = []
        try :
            while True :
                p = pickle . load (f)
                for element in p :
                    if p[element] in s.nested_slot_list [0]:
                        s.timings_list . append ( element [:20] )
                                                
        except EOFError :
            f.close()


        return s.timings_list

    def time_table_teachers (s) :

        row = 1
        column = 1

        s.Teacher_label = tkinter.Label ( s.display_window ,
                                        text = s.Teacher_code_to_Teacher_name(s.Teacher_id),
                                        font=("Times New Roman",10,"bold") ,
                                        bg = "black" ,
                                        fg = "white" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column , row = row , rowspan = 2 , ipadx = 20 , ipady =20, padx = 5)

        for day in s.school_days_list:

            s.day_label = tkinter.Label ( s.display_window ,
                                        text = day,
                                        font=("Times New Roman",16,"bold") ,
                                        bg = "black" ,
                                        fg = "white" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column , row = row +2  , ipadx = 20 , ipady =15, padx = 10 , pady = 10)
            row +=1

        row = 1

        for lecture_no in s.nested_slot_list [0] :

            s.lecture_label = tkinter.Label ( s.display_window ,
                                        text = lecture_no,
                                        font=("Times New Roman",16,"bold") ,
                                        bg = "black" ,
                                        fg = "white" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column +1 , row = row , ipadx = 30 , ipady =10 , pady = 10 , padx = 10)
            
            column += 1

        row = 1
        column = 1

        s.timings_list = s.lecture_timings()

        for lecture_time in s.timings_list :

            s.lecture_label = tkinter.Label ( s.display_window ,
                                        text = lecture_time,
                                        font=("Times New Roman",12 , "bold") ,
                                        bg = "black" ,
                                        fg = "white" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column +1 , row = row +1 , ipadx = 2, ipady = 5 , pady = 10 , padx = 10)
            column +=1
            
        row = 2
        column = 1
       
        for day in s.ready_to_display :
            for lecture in day :

                if lecture == "B" :
                    s.lecture_label = tkinter.Label ( s.display_window ,
                                        text = "----",
                                        font=("Times New Roman",16) ,
                                        bg = "White" ,
                                        fg = "Black" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column +1  , row = row+1 , ipadx = 40 , ipady =15 , pady = 8 , padx = 10)
                    column += 1

                elif lecture == "N" :
                    s.lecture_label = tkinter.Label ( s.display_window ,
                                        text = "----",
                                        font=("Times New Roman",16) ,
                                        bg = "White" ,
                                        fg = "Black" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column +1  , row = row+1 , ipadx = 40 , ipady =15 , pady = 8 , padx = 10)
                    column += 1

                elif lecture == "Lunch" :
                    s.lecture_label = tkinter.Label ( s.display_window ,
                                        text = "Lunch",
                                        font=("Times New Roman",16) ,
                                        bg = "White" ,
                                        fg = "Black" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column +1  , row = row+1 , ipadx = 40 , ipady =15 , pady = 8 , padx = 10)
                    column += 1
                else:
                    
                    s.lecture_label = tkinter.Label ( s.display_window ,
                                        text = lecture,
                                        font=("Times New Roman",16) ,
                                        bg = "White" ,
                                        fg = "Black" ,
                                        borderwidth = 2, relief = "solid").grid ( column = column +1  , row = row+1 , ipadx = 40 , ipady =15 , pady = 8 , padx = 10)
                    column += 1
            row += 1
            column = 1



    def update_window (s) :

        s.update_check += 1

        if s.link_update_check != 0 :
            s.linking_updation_window . withdraw ()
            
        s.school_inputs_window . withdraw ()

        s.updates_window = tkinter.Toplevel()
        s.updates_window. title ( "Updations")
        s.updates_window.geometry ("400x550")
        s.updates_window. configure ( bg = "White")

        s.heading = tkinter.Label ( s.updates_window , text = "Select What You Want To Update" ,
                                                   bg = "White" ,
                                                   fg = "DodgerBlue4" ,
                                                   font = ("Times New Roman" , 18 , "bold") ). grid (column = 1 , row = 0 , columnspan = 2 , pady = 20 , padx = 20)

        
        s.add_button = tkinter.Button (s.updates_window ,
                                                        text = "Add Subject " ,
                                                        font = ( "Times New Roman" , 14 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="20",
                                                        height="1",
                                                        command = s.create_masters).grid ( column = 1 , row = 1 , columnspan = 20 , pady = 20 , padx = 20)

        s.add_button = tkinter.Button (s.updates_window ,
                                                        text = "Update Classes" ,
                                                        font = ( "Times New Roman" , 14 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="20",
                                                        height="1" ,
                                                        command = s.update_classes).grid ( column = 1 , row = 2 , columnspan = 20 , pady = 20 , padx = 20)

        s.add_button = tkinter.Button (s.updates_window ,
                                                        text = "Update Linking" ,
                                                        font = ( "Times New Roman" , 14 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="20",
                                                        height="1" ,
                                                        command = s.linking_updation).grid ( column = 1 , row = 5 , columnspan = 20 , pady = 20 , padx = 20)
        s.add_button = tkinter.Button (s.updates_window ,
                                                        text = "Add Teacher" ,
                                                        font = ( "Times New Roman" , 14 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="20",
                                                        height="1" ,
                                                        command = s.teachers_window).grid ( column = 1 , row = 3 , columnspan = 20 , pady = 20 , padx = 20)
        s.add_button = tkinter.Button (s.updates_window ,
                                                        text = "Update Teacher" ,
                                                        font = ( "Times New Roman" , 14 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="20",
                                                        height="1",
                                                        command = s.teachers_buttons).grid ( column = 1 , row = 4 , columnspan = 20 , pady = 20 , padx = 20)
        s.add_button = tkinter.Button (s.updates_window ,
                                                        text = "Assign Lectures" ,
                                                        font = ( "Times New Roman" , 14 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="20",
                                                        height="1" ,
                                                        command = s.class_none).grid ( column = 1 , row = 6 , columnspan = 20 , pady = 20 , padx = 20)

    def linking_updation (s) :

        s.link_update_check +=1

        s.updates_window . withdraw ()

        s.linking_updation_window = tkinter.Toplevel()
        s.linking_updation_window.title ("Update who teaches what and to whom!")
        s.linking_updation_window.geometry ("700x280")
        s.linking_updation_window.configure ( bg = "white")

        s.heading = tkinter.Label ( s.linking_updation_window , text="Update your Linking Table !",
                                              font=( "Times New Roman" , 18 , "bold") ,
                                              bg = "White" ,
                                              fg = "DodgerBlue4").place ( x = 180 , y = 10 )
        
        s.Class_id_label = tkinter.Label ( s.linking_updation_window , text = "Select Class:  ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                fg = "black") . grid ( column = 0 , row = 1 , pady =45 , padx = 10)

        s.display_classes = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])

        cursor= s.display_classes . cursor ()
        cursor . execute ( "SELECT Class_id FROM Class_Assignment ")
        fetch = cursor. fetchall ()
        class_id_list = []
        for i in fetch :
            class_id_list . append (i[0])

        s.class_id_variable = tkinter . StringVar ()

        class_id_linking_updation = ttk.Combobox ( s.linking_updation_window ,
                                                          width = 12 ,
                                                           textvariable = s.class_id_variable ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        class_id_linking_updation [ 'values' ] = tuple ( class_id_list) 
        class_id_linking_updation.grid ( column = 0 , row = 2, padx = 10)

        go_ahead_button = tkinter.Button (s.linking_updation_window ,
                                                        text = "Go Ahead" ,
                                                        font = ( "Times New Roman" , 14 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="10",
                                                        height="1" ,
                                                        command = s.linking_subject_updation).grid ( column = 0 , row= 3 , pady = 15 , padx = 10)

    def linking_subject_updation (s) :

        s.linking_class_id = s.class_id_variable . get ()

        s.linking_class = s.linking_class_id [0]

        s.display_subjects = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
        cursor = s.display_subjects . cursor ()

        cursor . execute ( "SELECT Subject_1, Subject_2, Subject_3, Subject_4, Subject_5, Subject_6, Subject_7,Subject_8 FROM Classes WHERE Class = %s " % (int(s.linking_class),)) 
        fetch = cursor . fetchone ()

        s. linking_subjects = []

        for subject in fetch :

           if subject != "None":

               s.linking_subjects . append ( subject )

        s.subject_label = tkinter.Label ( s.linking_updation_window , text = "Select Subject:  ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                fg = "black") . grid ( column = 1 , row = 1 , padx = 10)

        s.subject_variable = tkinter . StringVar ()

        subject_linking_updation = ttk.Combobox ( s.linking_updation_window ,
                                                          width = 12 ,
                                                           textvariable = s.subject_variable ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        subject_linking_updation [ 'values' ] = tuple ( s.linking_subjects) 
        subject_linking_updation.grid ( column = 1 , row = 2 , padx = 10)

        go_ahead_button = tkinter.Button (s.linking_updation_window ,
                                                        text = "Go Ahead " ,
                                                        font = ( "Times New Roman" , 14 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="10",
                                                        height="1",
                                                        command = s.linking_teacher_updation).grid ( column = 1 , row= 3 , padx = 10)


    def linking_teacher_updation (s) :

        s.link_subject = s.subject_variable . get()

        s.display_teachers = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])

        cursor = s.display_teachers .cursor ()

        cursor. execute ( "SELECT Teacher_name FROM Teachers WHERE Subject_1 = '%s' OR Subject_2 = '%s' OR Subject_3 = '%s' " % (s.link_subject,s.link_subject , s.link_subject))
        
        fetch = cursor . fetchall ()

        s.linking_teachers = []

        for teacher in fetch :

            s.linking_teachers . append (teacher[0])


        s.teacher_label = tkinter.Label ( s.linking_updation_window , text = "Select Teacher:  ",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                fg = "black") . grid ( column = 2 , row = 1 , padx = 10)

        s.teacher_variable = tkinter . StringVar ()

        subject_linking_updation = ttk.Combobox ( s.linking_updation_window ,
                                                          width = 12 ,
                                                           textvariable = s.teacher_variable ,
                                                            font = ( "Times New Roman" , 12 ) ,
                                                            justify = "center" )
        
        subject_linking_updation [ 'values' ] = tuple ( s.linking_teachers) 
        subject_linking_updation.grid ( column = 2 , row = 2,padx = 10)

        go_ahead_button = tkinter.Button (s.linking_updation_window ,
                                                        text = "Go Ahead " ,
                                                        font = ( "Times New Roman" , 14 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="10",
                                                        height="1" ,
                                                        command = s.updated_link_store).grid ( column = 3 , row= 3 , padx = 10)

        s.lec_per_week_label = tkinter.Label ( s.linking_updation_window , text = "No. of lectures a week:",
                                                font=("Times New Roman",14,"bold") ,
                                                bg = "White" ,
                                                fg = "black") . grid ( column = 3 , row = 1 , padx = 10)
        
        s.linking_lectures = tkinter . StringVar ()

        s.lec_per_week_entry = tkinter.Entry (s.linking_updation_window ,
                                                                width="10" ,
                                                                font = ("Times New Roman" , 14) ,
                                                                textvariable = s.linking_lectures ,
                                                                borderwidth = 2 ,
                                                                relief = "ridge").grid (column = 3 , row = 2 )

        done_button = tkinter.Button (s.linking_updation_window ,
                                                        text = "Done" ,
                                                        font = ( "Times New Roman" , 14 , "bold" ) ,
                                                        fg = "white" ,
                                                        bg = "black",
                                                        width="10",
                                                        height="1" ,
                                                        command = s.updates_window).place (x = 570 , y = 230 )

    def teacher_name_to_teacher_code (s) :

        s.link_teacher_name = s.teacher_variable . get ()

        s.store_updated_link = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
        cursor1 = s.store_updated_link. cursor ()

        cursor1. execute ( "SELECT Teacher_name , Teacher_id FROM Teachers WHERE Teacher_name = '%s' " %(s.link_teacher_name , ) )

        row = cursor1.fetchone ()
        #print(row)
        return row [1]

    def subject_name_to_subject_code (s) :

        s.link_subject_name = s.subject_variable . get ()

        s.store_updated_link = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
        cursor1 = s.store_updated_link. cursor ()

        cursor1. execute ( "SELECT Subject_name , Subject_id FROM Subjects WHERE Subject_name = '%s' " %(s.link_subject_name , ) )

        row = cursor1.fetchone ()
        #print(row)
        return row [1]

    def updated_link_store (s) :

        s.link_class_id = s.linking_class_id
        s.link_sub_id = s.subject_name_to_subject_code ()
        s.link_teacher_id = s.teacher_name_to_teacher_code ()
        s.link_lec_per_week = s.linking_lectures . get ()

        s.store_updated_link = mysql.connector.connect ( host="localhost",
                                                                                    user = s.sql_username . get (),
                                                                                    passwd = s.sql_password . get () ,
                                                                                    database = s.user['name of the organisation'])
        cursor = s.store_updated_link . cursor ()
        cursor . execute ("UPDATE Linking SET Teacher_id = '%s' WHERE Class_id = '%s' and Subject_id = '%s' " % (s.link_teacher_id , s.link_class_id , s.link_sub_id))

        cursor . execute ("UPDATE Linking SET lec_per_week = '%s' WHERE Class_id = '%s' and Subject_id = '%s' " % (s.link_lec_per_week , s.link_class_id , s.link_sub_id))
        
        s.store_updated_link . commit ()
        cursor . close()
        s.store_updated_link . close()

        s.class_id_variable.set ("")
        s.subject_variable.set ("")
        s.teacher_variable.set ("")
        s.linking_lectures.set ("")


    def update_classes (s):

        s.updates_window . withdraw ()

        s.classes_update_window = tkinter.Toplevel()
        s.classes_update_window.title ("Choose your class.")
        s.classes_update_window.configure ( bg = "white")

        s.heading  = tkinter.Label ( s.classes_update_window ,
                                        text = "Which Class do you want to Update ?",
                                        font=("Times New Roman",18 , "bold") ,
                                        bg = "White" ,
                                        fg = "DodgerBlue4"). grid (  column = 0 , row = 0 , columnspan = 2 , pady = 10 , padx = 20 )

        display_sql = mysql.connector.connect ( host = "localhost" ,
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
        cursor1 = display_sql . cursor ()

        cursor1. execute ("SELECT Class FROM Classes")

        fetch = cursor1.fetchall ()

        update_classes = []

        for row in fetch :
            update_classes .append (row[0])

        s.class_update_heading  = tkinter.Label ( s.classes_update_window ,
                                        text = "Select Class : ",
                                        font=("Times New Roman",16 , "bold") ,
                                        bg = "White" ,
                                        fg = "Black"). grid ( column = 0 , row = 1 , padx = 10 , pady = 15 )

        s.class_update_variable = tkinter . StringVar ()

        class_updations = ttk.Combobox ( s.classes_update_window ,
                                    width = 25 ,
                                    textvariable = s.class_update_variable ,
                                    font = ( "Times New Roman" , 12 ) ,
                                    justify = "center" )
        
        class_updations[ 'values' ] = tuple ( update_classes )
        class_updations.grid ( column = 1 , row = 1 , pady = 15 , padx = 10)

        s.done_button = tkinter.Button ( s.classes_update_window ,
                                          text = "Done",
                                          font = ( "Times New Roman" , 14 , "bold" ) ,
                                          fg = "white" ,
                                          bg = "black",
                                          width="10",
                                          height="1" ,
                                          command = s.add_classes). grid ( column = 0 , row = 2  , padx = 10 , pady =10 , columnspan = 2)

        
    def teacher_none(s):
        
        change_to_none = mysql.connector.connect(host = "localhost" ,
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
        change_to_none_cursor = change_to_none.cursor()
        change_to_none_cursor.execute("SELECT * FROM Teacher_assignment")
        s.fetch_no_of_columns = change_to_none_cursor.fetchall()
        s.no_of_columns = len(s.fetch_no_of_columns[0]) - 1
        for i in range(s.no_of_columns):
            column_no = "`" + str(i) + "`"
            change_to_none_cursor.execute("UPDATE teacher_assignment SET %s = 'N' WHERE %s != 'B' AND %s != 'Lunch';"%(column_no,column_no,column_no))
            change_to_none.commit()
        change_to_none.close()
        
    def class_none(s):

        #s.update_window ()

        s.new_assignment += 1

        change_to_none = mysql.connector.connect(host = "localhost" ,
                                                user = s.sql_username . get (),
                                                passwd = s.sql_password . get () ,
                                                database = s.user['name of the organisation'])
        change_to_none_cursor = change_to_none.cursor()
        change_to_none_cursor.execute("SELECT * FROM class_assignment")
        s.fetch_no_of_columns = change_to_none_cursor.fetchall()
        s.no_of_columns = len(s.fetch_no_of_columns[0]) - 1
        for i in range(s.no_of_columns):
            column_no = "`" + str(i) + "`"
            change_to_none_cursor.execute("UPDATE class_assignment SET %s = 'N' WHERE %s != 'B' AND %s != 'Lunch';"%(column_no,column_no,column_no))
            change_to_none.commit()        
        change_to_none.close()
        s.teacher_none ()
        s. fetching_linking_data ()
        s.choose_teacher_or_class()




        

                
                    
                

        
        
        
#----------------------------------------------------------------------------------------------------------Mains----------------------------------------------------------------------------------------------------------

time_table_generator1 = time_table_generator()
time_table_generator1.start_screen_()
